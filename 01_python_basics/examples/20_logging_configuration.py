"""Lesson 20: safe logging and configuration from environment variables."""

import logging
import math
import os


def required_setting(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Set the {name} environment variable before running.")
    return value


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger("beam_monitor")

project_name = os.getenv("PROJECT_NAME", "local-beam-study")
logger.info("Starting project %s", project_name)

try:
    api_token = required_setting("DEMO_API_TOKEN")
except RuntimeError:
    logger.warning("DEMO_API_TOKEN is absent; external upload is disabled.")
else:
    logger.info("A token was supplied (%d characters); token value is hidden.", len(api_token))

def check_load(load_kn: float, limit_kn: float) -> None:
    if not math.isfinite(load_kn) or not math.isfinite(limit_kn):
        raise ValueError("Load and limit must be finite numbers.")
    if limit_kn <= 0:
        raise ValueError("Limit must be greater than zero.")
    ratio = load_kn / limit_kn
    if ratio > 1:
        logger.error("Load %.1f kN exceeds limit %.1f kN.", load_kn, limit_kn)
    else:
        logger.info("Load ratio is %.0f%%.", ratio * 100)


check_load(42.0, 50.0)
