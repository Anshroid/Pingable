import asyncio
import threading

import control
import pinger
import bot
import keepalive


def main():
    state_event = pinger.ChangeState()
    ping = pinger.Pinger(state_event)
    ping.start()

    client = bot.Bot(asyncio.new_event_loop(), state_event)

    control_thread = control.ControlThread(state_event, client)
    control_thread.start()

    keepalive_thread = threading.Thread(target=keepalive.app.run, kwargs={"host": "0.0.0.0", "port":3051})
    keepalive_thread.start()

    client.run(client.secret)


if __name__ == "__main__":
    main()
