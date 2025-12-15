import sys
import time
from threading import Thread, Event


class Spinner:
    def __init__(self, message="Processing"):
        self.message = message
        self.frames = ["|", "/", "-", "\\"]
        self.stop_event = Event()
        self.thread = Thread(target=self._spin)

    def _spin(self):
        i = 0
        while not self.stop_event.is_set():
            frame = self.frames[i % len(self.frames)]
            print(f"\r{self.message} {frame}", end="")
            sys.stdout.flush()
            time.sleep(0.1)
            i += 1

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_event.set()
        self.thread.join()
        print(f"\r✔ {self.message} done.     ")
