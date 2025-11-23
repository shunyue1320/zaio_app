import json
import os
import datetime
from llm.client import LLMClient


class PerspectiveGenerateEngine:
    ROLE = "perspective_generate_engine"

    def __init__(self, llm_client: LLMClient, base_dir: str):
        self.llm = llm_client
        self.base_dir = base_dir
        self.tree_dir = os.path.join(base_dir, "data", "perspective_trees")
        os.makedirs(self.tree_dir, exist_ok=True)

    def generate_tree(self, user_text: str, snapshot: dict, talk_history: list) -> dict:
        """
        调用 LLM 生成一棵新的观点树，并写入 data/perspective_trees 目录。
        """

        payload = {
            "user_text": user_text or "",
            "snapshot": snapshot or {},
            "talk_history": talk_history or [],
        }

        # 调用 LLM（角色：perspective_generate_engine）
        raw = self.llm.call_llm(self.ROLE, payload, temperature=0.4)
        if not raw:
            print("[PerspectiveGenerateEngine] LLM 返回为空，放弃生成新树")
            return {}

        raw = raw.strip()

        # ======== ① 去掉 Markdown 包裹的 ```json ========
        if raw.startswith("```"):
            lines = raw.splitlines()
            # 去掉第一行（```json）
            if lines[0].startswith("```"):
                lines = lines[1:]
            # 去掉最后一行（```）
            if lines[-1].startswith("```"):
                lines = lines[:-1]
            raw = "\n".join(lines).strip()

        # ======== ② 从第一个 { 到最后一个 } 截取纯 JSON（最稳妥） ========
        start = raw.find("{")
        end = raw.rfind("}")
        if start == -1 or end == -1:
            print("[PerspectiveGenerateEngine] 无法找到 JSON 边界")
            print("[RAW]:", raw[:200])
            return {}

        json_str = raw[start:end + 1]

        # ======== ③ 尝试解析 ========
        try:
            tree = json.loads(json_str)
        except Exception as e:
            print("[PerspectiveGenerateEngine] JSON 解析失败:", e)
            print("[JSON_STR]:", json_str[:200])
            return {}

        # ======== ④ 补充 tree_id / 时间戳 ========
        ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        tree_id = tree.get("tree_id") or f"tree_{ts}"
        tree["tree_id"] = tree_id
        tree["generated_at"] = ts

        # ======== ⑤ 保存到 data/perspective_trees ========
        try:
            os.makedirs(self.tree_dir, exist_ok=True)
            path = os.path.join(self.tree_dir, f"{tree_id}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(tree, f, indent=2, ensure_ascii=False)
            print("[PerspectiveGenerateEngine] 已保存观点树:", path)
        except Exception as e:
            print("[PerspectiveGenerateEngine] 保存失败:", e)

        return tree

    def save_tree_to_file(self, tree: dict) -> str:
        """
        将一棵观点树写入 data/perspective_trees 目录，用于：
          - 默认初见树（非 LLM 生成）
          - 固定模板树
          - 人工加工的树
        返回生成的文件路径。
        """

        try:
            # 确保目录存在
            os.makedirs(self.tree_dir, exist_ok=True)

            # 生成或读取 tree_id
            ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            tree_id = tree.get("tree_id") or f"default_tree_{ts}"

            # 补齐元数据
            tree["tree_id"] = tree_id
            tree["generated_at"] = ts

            # 写入文件
            path = os.path.join(self.tree_dir, f"{tree_id}.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump(tree, f, indent=2, ensure_ascii=False)

            print("[PerspectiveGenerateEngine] 已保存自定义观点树:", path)
            return path

        except Exception as e:
            print("[PerspectiveGenerateEngine] 保存自定义观点树失败:", e)
            return ""

