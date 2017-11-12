import time
import minimalmodbus
import serial.tools.list_ports as listPorts

def portNames(i):
	pnames = []
	for port in listPorts.comports():
		pnames.append(port[0])
	return pnames[i]

def initArduino(name, id, baud):
    instr = minimalmodbus.Instrument(name,id)
    instr.serial.baudrate = baud
    instr.serial.timeout = 0.5
    return instr

def infiniteTest(id, baud, delay):
    ins = initArduino(portNames(0), id, baud)
    i = 0
    while True:
        print("{}: {}".format(i, readJoystick(ins)))
        i += 1
        time.sleep(delay)

def doubleTest(baud, delay):
    ins = initArduino(portNames(0), 1, baud)
    ins2 = initArduino(portNames(0), 2, baud)
    i = 0
    errors = 0
    while True:
        try:
            print("{}: i1={}, i2={}".format(i, readJoystick(ins), readJoystick(ins2)))
            i+=1
            time.sleep(delay)
        except IOError:
            errors += 1
            print("ERROR".format())
        except KeyboardInterrupt:
            print("{} errors found".format(errors))
            raise KeyboardInterrupt

def blink(ins, pin, count, s):
    for i in range(0,count):
        ins.write_bit(pin,1)
        time.sleep(s)
        ins.write_bit(pin,0)
        time.sleep(s)

def readJoystick(ins):
    return ins.read_registers(0,3,4)