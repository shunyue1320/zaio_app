from typing import Dict, Any, List
from llm.client import LLMClient
import json


class PerspectiveMoveTrigger:
    """
    T 引擎观点树节点变化触发器。
    由 LLM 决定是否推进观点树及推进目标。
    role = trigger_perspective_move
    """

    ROLE = "trigger_perspective_move"

    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def decide_move(
        self,
        current_node: Dict[str, Any],
        user_text: str,
        ai_text: str,
        snapshot: Dict[str, Any],
        talk_history: List[Dict[str, Any]],
        full_tree: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        使用 LLM 判断：
        - 是否前进观点树（move）
        - 前进到哪个节点（next_node_id）
        - 是否需要生成新观点树（need_new_tree）
        """

        # ---- 上一节点 ----
        previous_node_id = current_node.get("_previous_node_id")
        nodes: Dict[str, Any] = {}
        if isinstance(full_tree, dict):
            nodes = full_tree.get("nodes") or {}
            if not isinstance(nodes, dict):
                nodes = {}

        previous_node = None
        if previous_node_id:
            previous_node = nodes.get(previous_node_id, {"id": previous_node_id})

        # ---- 下一节点列表 ----
        next_ids = current_node.get("children") or []
        if not isinstance(next_ids, list):
            next_ids = []

        next_nodes: List[Dict[str, Any]] = []
        for nid in next_ids:
            if isinstance(nid, str):
                next_nodes.append(nodes.get(nid, {"id": nid}))

        # ---- 构造 payload，严格对齐 system prompt ----
        payload = {
            "current_node": current_node,
            "previous_node": previous_node,
            "next_nodes": next_nodes,
            "user_text": user_text,
            "ai_text": ai_text,
            "snapshot": snapshot,
            "talk_history": talk_history,
            "full_tree": full_tree,
        }

        raw = self.llm.call_llm(self.ROLE, payload, temperature=0.3)
        if not raw:
            return {
                "move": False,
                "next_node_id": None,
                "need_new_tree": False,
                "reason": "",
            }

        try:
            data = json.loads(raw)
            move = bool(data.get("move", False))
            next_node_id = data.get("next_node_id")
            if not isinstance(next_node_id, str):
                next_node_id = None
            need_new_tree = bool(data.get("need_new_tree", False))
            reason = data.get("reason", "")

            return {
                "move": move,
                "next_node_id": next_node_id,
                "need_new_tree": need_new_tree,
                "reason": reason,
            }
        except Exception:
            return {
                "move": False,
                "next_node_id": None,
                "need_new_tree": False,
                "reason": "",
            }
