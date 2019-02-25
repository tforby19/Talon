import RoboPiLib as RPL
RPL.RoboPiInit(device = "/dev/ttyAMA0", bps = 115200)



def pwmWrite():
  RPL.pinMode(0, RPL.PWM)
  RPL.pwmWrite(0, 3000, 3000)
