import OPi.GPIO as GPIO
from time import sleep
GPIO.setboard(GPIO.ZERO)
GPIO.setmode(GPIO.BOARD)

pin = 26
GPIO.setup(pin, GPIO.OUT)


def take_shot(ir_pin):
    """
    Nikon's remote ir controller code
    2.0ms on
    27.8ms off
    0.5ms on
    1.5ms off
    0.5ms on
    3.5ms off
    0.5 ms on
    """
    GPIO.output(ir_pin, 0)

    codes = [
        (0.002, 1),
        (0.0278, 0),
        (0.0005, 1),
        (0.0015, 0),
        (0.0005, 1),
        (0.0035, 0),
        (0.0005, 1),
    ]

    for code in codes:
        time, value = code
        GPIO.output(ir_pin, value)
        sleep(time)

    GPIO.output(ir_pin, 0)


take_shot(pin)
