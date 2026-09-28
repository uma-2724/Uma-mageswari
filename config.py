import os
from functools import lru_cache

from dotenv import load_dotenv


# Load variables from .env
load_dotenv()


class Settings:

    APP_NAME: str = os.getenv(
        "APP_NAME",
        "EduGenie"
    )

    GEMINI_API_KEY: str = os.getenv(
        "GEMINI_API_KEY",
        ""
    )

    GEMINI_MODEL: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.5-flash"
    )

    LOCAL_EXPLANATION_ENABLED: bool = (
        os.getenv(
            "LOCAL_EXPLANATION_ENABLED",
            "false"
        ).lower()
        in {"1", "true", "yes", "on"}
    )

    LOCAL_EXPLANATION_MODEL: str = os.getenv(
        "LOCAL_EXPLANATION_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    MAX_INPUT_CHARS: int = int(
        os.getenv(
            "MAX_INPUT_CHARS",
            "12000"
        )
    )


@lru_cache
def get_settings() -> Settings:

    return Settings()