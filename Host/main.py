import asyncio

import control
import pinger
import bot


def main():
    state_event = pinger.ChangeState()
    ping = pinger.Pinger(state_event)
    ping.start()

    client = bot.Bot(asyncio.new_event_loop(), state_event)

    control_thread = control.ControlThread(state_event, client)
    control_thread.start()

    client.run(client.secret)


if __name__ == "__main__":
    main()
