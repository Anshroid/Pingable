import pystray
import threading
from PIL import Image


class TrayconThread(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(TrayconThread, self).__init__(*args, **kwargs)
        self.traycon = None
        self.stopped = False

    def run(self):
        menu = pystray.Menu(pystray.MenuItem("Exit", action=self.stop))

        icon = Image.open("favicon.ico")
        self.traycon = pystray.Icon("bot", icon=icon, menu=menu, title="Pingable Discord Bot")
        self.traycon.run()

    def stop(self):
        self.traycon.stop()
        self.stopped = True
        exit(0)
