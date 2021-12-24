import requests
import threading
import time


class ChangeState(threading.Event):
    def __init__(self):
        super(ChangeState, self).__init__()
        self.new_state = None

    def set_state(self, new_state):
        self.new_state = new_state
        self.set()


class Pinger(threading.Thread):
    def __init__(self, event: ChangeState, *args, **kwargs):
        super(Pinger, self).__init__(*args, **kwargs)
        self.is_off = False
        self.stopped = False
        self.event = event

    def get_off(self) -> str:
        return "Off" if self.is_off else "On "

    def set_off(self, value: bool) -> None:
        if self.is_off != value:
            self.is_off = value
            self.event.set_state(self.get_off())

    def run(self) -> None:
        while not self.stopped:
            time.sleep(5)
            try:
                print("request")
                requests.get("http://localhost:3050")
            except requests.exceptions.ConnectionError:
                self.set_off(True)
                print("off")
                continue
            self.set_off(False)
            print("on")

    def stop(self):
        self.stopped = True

