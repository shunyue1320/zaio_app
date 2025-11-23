
from typing import Dict, Any, List
from llm.client import LLMClient
import json


class StateUpdateTrigger:
    """
    用户 state_snapshot 属性更新触发器。
    由 LLM 根据最近输入与历史，给出需要更新的字段。
    role = trigger_state_update
    """

    ROLE = "trigger_state_update"

    def __init__(self, llm_client: LLMClient):
        self.llm = llm_client

    def infer_updates(self, user_text: str, history: List[Dict[str, Any]], snapshot: Dict[str, Any]) -> Dict[str, Any]:
        payload = {
            "user_text": user_text,
            "history": history,
            "snapshot": snapshot,
        }
        raw = self.llm.call_llm(self.ROLE, payload, temperature=0.4)
        if not raw:
            return {}
        try:
            data = json.loads(raw)
            if isinstance(data, dict):
                return data
        except Exception:
            pass
        return {}
