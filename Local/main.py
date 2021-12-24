import server
import widget

server_thread = server.ServerThread()
widget_thread = widget.TrayconThread()

server_thread.start()
widget_thread.start()

while not widget_thread.stopped:
    pass

server_thread.stop()
exit(0)
