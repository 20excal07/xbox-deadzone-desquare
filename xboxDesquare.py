import math

def circle(x, y):
	return (x * math.sqrt(1 - 0.5 * math.pow(y, 2)))

if starting:
	pollingRate = 160	# Hz; default is 160
	system.setThreadTiming(TimingTypes.HighresSystemTimer)
	system.threadExecutionInterval = 1000 / pollingRate
	vv = vJoy[0]
	vvAxisMax = vv.axisMax
	x360 = xbox360[0]

x = x360.leftStickX
y = -x360.leftStickY
rx = x360.rightStickX
ry = -x360.rightStickY

vv.x = circle(x, y) * vvAxisMax
vv.y = circle(y, x) * vvAxisMax
vv.rx = circle(rx, ry) * vvAxisMax
vv.ry = circle(ry, rx) * vvAxisMax
vv.z = (x360.leftTrigger * 2 - 1) * vvAxisMax
vv.rz = (x360.rightTrigger * 2 - 1) * vvAxisMax

vv.setButton(0, x360.a)
vv.setButton(1, x360.b)
vv.setButton(2, x360.x)
vv.setButton(3, x360.y)
vv.setButton(4, x360.leftShoulder)
vv.setButton(5, x360.rightShoulder)
vv.setButton(6, x360.back)
vv.setButton(7, x360.start)
vv.setButton(8, x360.leftThumb)
vv.setButton(9, x360.rightThumb)

if x360.up is True and x360.right is True:
 	vv.setAnalogPov(0,4500)
elif x360.right is True and x360.down is True: 
	vv.setAnalogPov(0,13500)
elif x360.down is True and x360.left is True: 
	vv.setAnalogPov(0,22500)
elif x360.left is True and x360.up is True: 
	vv.setAnalogPov(0,31500)
elif x360.up is True: 
	vv.setAnalogPov(0,0)
elif x360.right is True: 
	vv.setAnalogPov(0,9000)
elif x360.down is True: 
	vv.setAnalogPov(0,18000)
elif x360.left is True: 
	vv.setAnalogPov(0,27000)
else:
	vv.setAnalogPov(0,-1)
