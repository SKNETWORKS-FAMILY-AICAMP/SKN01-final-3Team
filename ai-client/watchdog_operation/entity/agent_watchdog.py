from abc import abstractmethod
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
from chatdev.logger import Logger
import os


class WatchdogHandler(FileSystemEventHandler):
    def __init__(self, observe_path):
        os.makedirs(observe_path, exist_ok=True)
        self.modify_logger = Logger(f'{observe_path}/modified.log', 'modified').get_logger()
        self.created_logger = Logger(f'{observe_path}/created.log', 'created').get_logger()
        self.deleted_logger = Logger(f'{observe_path}/deleted.log', 'deleted').get_logger()
    
    def on_modified(self, event):
        if not event.is_directory:
            self.modify_logger.info(msg=f"File modified: {event.src_path}")

    def on_created(self, event):
        self.created_logger.info(msg=f"File created: {event.src_path}")

    def on_deleted(self, event):
        self.deleted_logger.info(msg=f"File deleted: {event.src_path}")


class Watchdog:
    def __init__(self, observe_path):
        self.observer = self.get_observer(observe_path)
        
    def get_observer(self, observe_path):
        observer = Observer()
        event_handler = WatchdogHandler(observe_path)
        observer.schedule(event_handler, observe_path, recursive=True)
        return observer

    def run(self):
        self.observer.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.stop()
        self.observer.join()


if __name__ == "__main__":
    path = "."
    watchdog = Watchdog(path)
    watchdog.run()