__all__ = ("logger_setup",)


import sys
from typing import Any, Literal, TextIO

from loguru import logger


def logger_setup(
        sink: TextIO | str = sys.stderr,
        level: Literal[
                   "TRACE",
                   "DEBUG",
                   "INFO",
                   "SUCCESS",
                   "WARNING",
                   "ERROR",
                   "CRITICAL"
               ] | int = "INFO",
        colorize: bool = True,
        backtrace: bool = False,
        diagnose: bool = False,
        **kwargs: Any
) -> None:
    """
    Remove loguru default logger and configure own logger.
    Look https://loguru.readthedocs.io/en/stable/api/logger.html#loguru._logger.Logger.add for more details.
    """

    logger.remove()

    logger.add(
        sink,
        level=level,
        format="<green>{time:YYYY/DD/MM HH:mm:ss}</green> | "
               "<bold><level>{level: <6}</level></bold> | "
               "<cyan>{name}</cyan>:<cyan>{line}</cyan> - "
               "<level>{message}</level>",
        colorize=colorize,
        backtrace=backtrace,
        diagnose=diagnose,
        **kwargs
    )
