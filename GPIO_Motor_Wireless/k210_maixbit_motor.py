import time
from Maix import GPIO
from fpioa_manager import fm
from board import board_info


fm.register(7,fm.fpioa.GPIO0, force=True)
fm.register(6,fm.fpioa.GPIO1, force=True)
ctrla = GPIO(GPIO.GPIO0, GPIO.OUT)
ctrla.value(1)
ctrlb = GPIO(GPIO.GPIO1, GPIO.OUT)
ctrlb.value(1)


def stop():
    print("Stop:set both to 1 ")
    ctrla.value(1)
    ctrlb.value(1)


def up():
    print("up:ctrla=1,ctrlb=0  ")
    ctrla.value(1)
    ctrlb.value(0)


def down():
    print("down:ctrla=0,ctrlb=1  ")
    ctrla.value(0)
    ctrlb.value(1)

def flush():
    down()
    time.sleep(0.25)
    stop()
    time.sleep(5)
    up()
    time.sleep(0.25)
    stop()



time.sleep(5)
for i in range(10):
    print("i=%d"%i)
    flush()
    time.sleep(15)

print("End........")

fm.unregister(6)
fm.unregister(7)


