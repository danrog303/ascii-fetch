import signal


def keyboard_interrupt_handler(sig, frame):
    import sys
    print("Keyboard interrupt caught. Exiting...", file=sys.stderr)
    exit(2)


signal.signal(signal.SIGINT, keyboard_interrupt_handler)
