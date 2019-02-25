import RoboPiLib as RPL
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)

pin = 0
freq = 3000

RPL.pinMode(0, RPL.PWM)
RPL.pwmWrite(0, freq, 3000)
