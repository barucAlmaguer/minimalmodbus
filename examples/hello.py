import minimalmodbus
import time

instr = minimalmodbus.Instrument('COM19',2)
instr.serial.baudrate = 9600

#def print():
#    instr

def blink(pin, count, s):
    for i in range(0,count):
        instr.write_bit(pin,1)
        time.sleep(s)
        instr.write_bit(pin,0)
        time.sleep(s)