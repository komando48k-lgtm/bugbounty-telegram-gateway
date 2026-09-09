import os
from dataclasses import dataclass


def _ids(value: str) -> frozenset[int]:
    return frozenset(int(x.strip()) for x in value.split(",") if x.strip())


@dataclass(frozen=True)
class Settings:
    telegram_bot_token: str
    allowed_user_ids: frozenset[int]
    database_path: str
    llm_base_url: str | None
    llm_api_key: str | None
    llm_model: str | None

    @classmethod
    def from_env(cls) -> "Settings":
        token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
        if not token:
            raise RuntimeError("TELEGRAM_BOT_TOKEN is required")
        return cls(token, _ids(os.getenv("TELEGRAM_ALLOWED_USER_IDS", "")), os.getenv("DATABASE_PATH", "data/gateway.db"), os.getenv("LLM_BASE_URL") or None, os.getenv("LLM_API_KEY") or None, os.getenv("LLM_MODEL") or None)
