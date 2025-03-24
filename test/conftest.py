import logging
import pytest
import colorlog


def pytest_configure():
    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
        )
    )
    logging.basicConfig(level=logging.INFO, handlers=[handler])


@pytest.fixture(autouse=True)
def setup_logging(caplog):
    caplog.set_level(logging.INFO)
