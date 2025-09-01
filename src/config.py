from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    WEB_BASE_URL: str = os.getenv("WEB_BASE_URL", "https://s4e.io")
    APP_BASE_URL: str = os.getenv("APP_BASE_URL", "https://app.s4e.io")
    HEADLESS: bool = os.getenv("HEADLESS", "1") == "1"
    TIMEOUT_MS: int = int(os.getenv("TIMEOUT_MS", "10000"))
    RUN_AI_TEST: bool = os.getenv("RUN_AI_TEST", "0") == "1"

    @classmethod
    def load(cls) -> "Settings":
        return cls()
