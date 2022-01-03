import signal


def keyboard_interrupt_handler(sig, frame):
    print("Keyboard interrupt caught. Exiting...")
    exit(2)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)
