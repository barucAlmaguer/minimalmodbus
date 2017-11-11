
import minimalmodbus
import time
import serial
import serial.tools.list_ports as listPorts

def portNames(i):
	pnames = []
	for port in listPorts.comports():
		pnames.append(port[0])
	return pnames[i]

def initArduino(name, id, baud):
    instr = minimalmodbus.Instrument(name,id)
    instr.serial.baudrate = baud
    return instr

def print():
    instr

def blink(pin, count, s):
    for i in range(0,count):
        instr.write_bit(pin,1)
        time.sleep(s)
        instr.write_bit(pin,0)
        time.sleep(s)

def readJoystick(ins):
    return ins.read_registers(0,3,4)