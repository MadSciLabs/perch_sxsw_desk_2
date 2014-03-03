import math, random, Perch

try:
	if sparkleOn:
		pass;
except Exception:
	sparkleOn = 1

try:
	if sparkleIndex:
		pass;
except Exception:
	sparkleIndex = 1

try:
	if sparkleOff:
		pass;
except Exception:
	sparkleOff = 1

try:
	if arrStatus:
		pass;
except Exception:
	arrStatus = {
	'0' : 0,
	'1' : 0,
	'2' : 0,
	'3' : 0,
	'4' : 0
	}

try:
	if arrSketchStatus:
		pass;
except Exception:
	arrSketchStatus = {
	'0' : 0,
	'1' : 0,
	'2' : 0,
	'3' : 0,
	'4' : 0
	}

def freeSpot(obj,kwargs):

    global lock

    lock = 0

def lockSpot(obj,kwargs):

    global sparkleOn
    global sparkleIndex
    global lock

    lock = 1
    sparkleOn = 1
    sparkleIndex = int(kwargs[0])

    obj.run = False;

def masterSparkle(obj,kwargs):

    global sparkleOn
    global sparkleIndex

    #print "master sparkle"
    #print "is on"
    #print sparkleOn
    #print str(sparkleIndex)

    if int(sparkleOn) == 1:
      sparkleIndex = sparkleIndex + 1

      if int(sparkleIndex) > 3:
        sparkleIndex = 0

      sparkleOn = 0

    else:
      sparkleOn = 1


def sparkle(obj,kwargs):

    global sparkleOn
    global sparkleIndex
    global arrStatus
    #global sparkleOff

    #arr = str(kwargs[0]).split('|')
    #imgIndex = arr[1]
    imgIndex = kwargs[0]

    if int(imgIndex) == int(sparkleIndex) and int(sparkleOn) == 1:
      if int(arrStatus[str(imgIndex)]) == 0:
        arrStatus[str(imgIndex)] = 1
        obj.show()

    else:
      if int(arrStatus[str(imgIndex)]) == 1:
        arrStatus[str(imgIndex)] = 0
        obj.hide()

    #print "sparkle"
    #print imgIndex
    obj.run = False;

def sketch(obj,kwargs):

    global sparkleOn
    global sparkleIndex
    global arrSketchStatus

    imgIndex = kwargs[0]

    if int(imgIndex) == int(sparkleIndex) and int(sparkleOn) == 1:
      if int(arrSketchStatus[str(imgIndex)]) == 0:
        arrSketchStatus[str(imgIndex)] = 1
        print "hide sketch "
        print imgIndex
        obj.show()

    else:
      if int(arrSketchStatus[str(imgIndex)]) == 1:
        arrSketchStatus[str(imgIndex)] = 0
        print "show sketch "
        print imgIndex
        obj.hide()

    obj.run = False;

def debug(obj,kwargs):

    print kwargs[0]
