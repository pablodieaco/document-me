import argparse
import os
import time
from collections import deque

from loguru import logger
from watchdog.events import FileCreatedEvent, FileModifiedEvent, FileSystemEventHandler
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
    parser.add_argument(
        "--input_folder",
        type=str,
        default="scripts/",
        help="Folder to be watching (default: scripts/)",
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="documented_scripts/",
        help="Folder to write the documented files (default: documented_scripts/)",
    )
    return parser.parse_args()


class ScriptModifiedHandler(FileSystemEventHandler):
    def __init__(
        self,
        model_name: str = "llama3",
        input_folder: str = "scripts/",
        output_folder: str = "documented_scripts/",
        cache_duration: int = 10,
    ):
        self.model_name = model_name
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.cache_duration = cache_duration
        self.recently_modified_files = deque()

    def on_modified(self, event):
        current_time = time.time()

        if self.is_recently_modified(event.src_path, current_time):
            return

        if event.src_path.endswith(".py"):
            logger.info(f"[Watcher] file modified detected in: {event.src_path}")
            document_script_flow(
                event.src_path, self.model_name, self.input_folder, self.output_folder
            )

            self.add_to_recent_cache(event.src_path, current_time)

    def is_recently_modified(self, file_path, current_time):
        while (
            self.recently_modified_files
            and self.recently_modified_files[0][1] < current_time - self.cache_duration
        ):
            self.recently_modified_files.popleft()

        for file, timestamp in self.recently_modified_files:
            if file == file_path:
                return True
        return False

    def add_to_recent_cache(self, file_path, current_time):
        self.recently_modified_files.append((file_path, current_time))


if __name__ == "__main__":
    args = parse_arguments()
    model_name = args.model_name
    input_folder = args.input_folder
    output_folder = args.output_folder

    observer = Observer(timeout=1)
    observer.schedule(
        ScriptModifiedHandler(model_name, input_folder, output_folder),
        path=f"{BASE_PATH}/{input_folder}/",
        recursive=False,
        event_filter=[FileModifiedEvent, FileCreatedEvent],
    )
    observer.start()

    logger.info("[Watcher] Initializing watcher...")

    try:
        logger.info(f"[Watcher] Watching folder: {BASE_PATH}/{input_folder}/")
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
