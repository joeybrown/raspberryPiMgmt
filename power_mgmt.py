import RPIO
from power_utils import reboot, halt

try:
    HALT_CTRL_PIN = 23
    REBOOT_CTRL_PIN = 24

    def init():
        RPIO.setup(HALT_CTRL_PIN, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)
        RPIO.setup(REBOOT_CTRL_PIN, RPIO.IN, pull_up_down=RPIO.PUD_DOWN)       

    def add_interrupts():
        RPIO.add_interrupt_callback(REBOOT_CTRL_PIN, reboot(), edge='rising')
        RPIO.add_interrupt_callback(HALT_CTRL_PIN, halt(), edge='rising')

    def wait_for_interrupts():
        RPIO.wait_for_interrupts()

    init()
    add_interrupts()
    wait_for_interrupts()
    
except:
    GPIO.cleanup()
