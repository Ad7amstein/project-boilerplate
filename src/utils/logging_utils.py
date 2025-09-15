"""Logging Utility Module."""

import os
import sys
import logging
from typing import Literal


def setup_logger(
    log_file: str,
    log_dir: str = "logs",
    log_to_console: bool = True,
    file_mode: Literal["a", "w"] = "a",
) -> logging.Logger:
    """Set up a logger with file and optional console handlers.

    Args:
        log_file (str): The path to the log file where messages will be saved.
        log_dir (str, optional): Directory where log files will be created. Defaults to "logs".
        log_to_console (bool, optional): Whether to also log messages to the
            console (stdout). Defaults to True.
        file_mode (str, optional): File open mode for the log file: "a" to append
            (default) or "w" to overwrite.

    Returns:
        logging.Logger: Configured logger instance.
    """
    if file_mode not in {"a", "w"}:
        raise ValueError("file_mode must be 'a' (append) or 'w' (write).")

    log_file = os.path.join(
        log_dir, f"{os.path.splitext(os.path.basename(log_file))[0]}.log"
    )
    log_dir = os.path.dirname(log_file)
    if log_dir:
        os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger(log_file)
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    formatter = logging.Formatter(
        "[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s]: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = logging.FileHandler(log_file, mode=file_mode)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    file_handler_all_logs = logging.FileHandler("logs/all_logs.log", mode="a")
    file_handler_all_logs.setLevel(logging.DEBUG)
    file_handler_all_logs.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(file_handler_all_logs)

    if log_to_console:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger


def main():
    """Entry point for the program."""

    print(f"Welcome from `{os.path.basename(__file__).split('.')[0]}` Module.")

    logger = setup_logger("logs/logging_utils.log", log_to_console=False, file_mode="a")

    logger.debug("This is a debug message (saved in file).")
    logger.info("This is an info message (shown in file & console).")
    logger.error("This is an error message (shown in file & console).")
    logger.warning("This is a warning message (shown in file & console).")


if __name__ == "__main__":
    main()
