import argparse
import os
import time

from loguru import logger
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from document_me.flows import document_script_flow

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def parse_arguments():
    parser = argparse.ArgumentParser(description="Watcher for script modification.")
    parser.add_argument(
        "--model_name",
        type=str,
        default="llama3",
        help="Name of the model (default: llama3)",
    )
    return parser.parse_args()


class ScriptModifiedHandler(FileSystemEventHandler):
    def __init__(self, model_name: str = "llama3"):
        self.model_name = model_name

    def on_modified(self, event):
        if (
            event.src_path.endswith(".py")
            and "documented_scripts" not in event.src_path
        ):
            logger.info(f"[Watcher] file modified detected in: {event.src_path}")
            document_script_flow(event.src_path, self.model_name)


if __name__ == "__main__":
    args = parse_arguments()
    model_name = args.model_name

    observer = Observer()
    observer.schedule(
        ScriptModifiedHandler(model_name), path=f"{BASE_PATH}/scripts/", recursive=False
    )
    observer.start()

    logger.info("[Watcher] Initializing watcher...")

    try:
        logger.info(f"[Watcher] Watching folder: {BASE_PATH}/scripts/")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
