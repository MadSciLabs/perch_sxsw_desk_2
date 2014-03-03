import math, random, Perch

try:
	if len(cardLocations) > 0:
	 	pass;
except Exception:
	cardLocations = {
	'1' : '76,50|150,150|228,100|152,300',
	'2' : '228,50|158,150|76,100|152,300',
	'3' : '76,150|150,50|228,100|152,300',
	'4' : '228,150|158,50|76,100|152,300',
	'5' : '76,250|150,350|228,300|152,100',
	'6' : '228,250|158,350|76,300|152,100',
	'7' : '76,350|150,250|228,300|152,100',
	'8' : '228,350|158,250|76,300|152,100'
	}

try:
	if len(cardLocationsU) > 0:
	 	pass;

except Exception:
	cardLocationsU = {
	'1' : '76,50|150,150|228,100|152,300',
	'2' : '228,50|158,150|76,100|152,300',
	'3' : '76,150|150,50|228,100|152,300',
	'4' : '228,150|158,50|76,100|152,300',
	'5' : '76,250|150,350|228,300|152,100',
	'6' : '228,250|158,350|76,300|152,100',
	'7' : '76,350|150,250|228,300|152,100',
	'8' : '228,350|158,250|76,300|152,100'
	}

try:
	if len(hashMen) > 0:
	 	pass;
except Exception:
	hashMen = {}

try:
	if len(blinkOn) > 0:
	 	pass;
except Exception:
	blinkOn = [];

try:
	if len(blinkOff) > 0:
	 	pass;
except Exception:
	blinkOff = []

try:
	if len(arrTeleport) > 0:
	 	pass;
except Exception:
	arrTeleport = []; 

try:
	if len(hashMenIndex) > 0:
	 	pass;
except Exception:

	# LOM CONFIG 

	#LEFT SIDE
	hashMenIndex={
	'1' : '26',
	'2' : '27',
	'3' : '28',
	'4' : '29',
	'5' : '31',
	'6' : '32',
	'7' : '33',
	'8' : '34',
	'9' : '35',
	'10' : '36',
	'11' : '39',
	'12' : '40',
	'13' : '41',
	'14' : '44',
	'15' : '45',
	'16' : '49',
	'17' : '51',
	'18' : '53',
	'19' : '54',
	'20' : '55',
	'21' : '56',
	'22' : '64',
	'23' : '65',
	'24' : '67',
	'25' : '68',
	'26' : '71',
	'27' : '72',
	'28' : '73',
	'29' : '77',
	'30' : '78',
	'31' : '79',
	'32' : '80'
	}
	"""

	#RIGHT SIDE
	hashMenIndex={
	'15' : '26',
	'16' : '27',
	'17' : '28',
	'18' : '29',
	'19' : '31',
	'20' : '32',
	'21' : '33',
	'22' : '34',
	'23' : '35',
	'24' : '36',
	'25' : '39',
	'26' : '40',
	'27' : '41',
	'28' : '44',
	'29' : '45',
	'30' : '49',
	'31' : '51',
	'32' : '53',
	'1' : '54',
	'2' : '55',
	'3' : '56',
	'4' : '64',
	'5' : '65',
	'6' : '67',
	'7' : '68',
	'8' : '71',
	'9' : '72',
	'10' : '73',
	'11' : '77',
	'12' : '78',
	'13' : '79',
	'14' : '80'
	}
	"""

def masterBlink(obj,kwargs):

    global blinkOn
    global blinkOff
    global arrTeleport

    blinkOff = blinkOn
    blinkOn = []
    arrSample = []
    arrTeleport = []

    for (i, item) in enumerate(hashMen):
      arrSample.append( str(item))

    arrSample = list(set(arrSample) - set(blinkOff))
    random.shuffle(arrSample)

    for i in range(0, 3):
      blinkOn.append( str( arrSample[int(i)]) )

    arrSample = list(set(arrSample) - set(blinkOn))
    random.shuffle(arrSample)

    arrTeleport.append(arrSample[0])
    arrTeleport.append(arrSample[1])

    #Switch dudes
    t = hashMen[arrSample[0]]
    hashMen[arrSample[0]] = hashMen[arrSample[1]]
    hashMen[arrSample[1]] = t

def blink(obj,kwargs):

    global blinkOn
    global blinkOff

    arr = str(kwargs[0]).split('|')
    imgIndex = arr[1]

    if str(imgIndex) in blinkOff:
      obj.show()

    if str(imgIndex) in blinkOn:
      obj.hide()

    obj.run = False;

def teleport(obj,kwargs):

    global arrTeleport

    arr = str(kwargs[0]).split('|')
    orientation = arr[0]
    imgIndex = arr[1]
    size = arr[2]

    if imgIndex in arrTeleport :
      obj.hide()
      obj.run = False;

      i = hashMen[str(imgIndex)] 
      imgPath = 'assets/images/' + str(orientation) + "/" + str(size) + '/' + hashMenIndex[str(i)] + ".png"
      obj.updateImage(obj , imgPath )

      obj.show()
      obj.run = False;

def showObj(obj,kwargs):
    arr = str(kwargs[0]).split('|')
    imgIndex = arr[1]

    if imgIndex not in blinkOn:
      obj.show();

    #print 'attempting show'
    obj.run = False;

def hideObj(obj,arg):
    obj.hide();
    print 'attempting hide'
    obj.run = False;

def initLocation(obj, kwargs):

    #arr = str(kwargs[0]).split('|')
    #imgIndex = arr[0]
    #size = arr[1]
    '''
    obj.position.x=100 * int(imgIndex)
    obj.position.y=100 * int(imgIndex)
    '''
    obj.position.x = 640;
    obj.position.y = 400;
    obj.run = False;

def initBlack(obj, kwargs):

    arr = str(kwargs[0]).split('|')
    orientation = str(arr[0])
    size = arr[2]
    
    imgPath = 'assets/images/' + orientation + "/" + str(size) + '/black.png'

    obj.updateImage(obj , imgPath )
    obj.run = False;

def initMan(obj, kwargs):

    arr = str(kwargs[0]).split('|')
    orientation = str(arr[0])
    imgIndex = arr[1]
    size = arr[2]

    i = len(hashMen) + 1

    print "START I"
    print i

    if i > 32:
      i = i - 32

    print "END I"
    print i

    hashMen[str(imgIndex)] = str(i)
    imgPath = 'assets/images/' + orientation + '/' + str(size) + '/' + hashMenIndex[str(i)] + '.png'

    obj.updateImage(obj , imgPath )
    obj.run = False;

def disableSensor(obj, kwargs):

    print "SENSOR DISABLED"
    obj.position.x = 1000
    obj.position.y = 1000

    obj.run = False

def initCardName(obj, kwargs):

    initCardAsset(obj, kwargs, "/cards/names-right/", 1)

def initCardNumber(obj, kwargs):

    initCardAsset(obj, kwargs, "/cards/numbers/", 0)

def initCardImg(obj, kwargs):

    initCardAsset(obj, kwargs, "/m/", 2)

def initCardQuote(obj, kwargs):

    initCardAsset(obj, kwargs, "/cards/quotes/", 3)

def initCardAsset(obj, kwargs, imgRoot, positionIndex):

    arr = str(kwargs[0]).split('|')

    orientation = str(arr[0])
    imgIndex = arr[1]
    pos = int(arr[2])
   
    #print "CARD : o "
    #print orientation
    #print " positionindex "
    #print positionIndex
    #print " index "
    #print imgIndex
    #print " pos "
    #print pos

    #SET CORRECT NAME
    if int(positionIndex) == 1:

      if str(orientation) == "r":
        if (int(pos) in [2, 4, 6, 8]):
          imgRoot = "/cards/names-left/"

      else:
        if (int(pos) in [1, 3, 5, 7]):
          imgRoot = "/cards/names-left/"


    print imgRoot

    menIndex = hashMen[str(imgIndex)]
    imgIndex = hashMenIndex[str(menIndex)]

    imgPath = "assets/images/" + orientation + imgRoot + str(imgIndex) + ".png"

    obj.updateImage(obj , imgPath )
   
    #SET IMAGE FROM CARD LOCATIONS STRING
    if str(orientation) == "u":

      #print "ORIENTATION"
      locationString = cardLocationsU[str(pos)] 
    else: 
      locationString = cardLocations[str(pos)] 

    arrAllLoc = locationString.split("|")
    arrPosition = arrAllLoc[positionIndex].split(",")

    obj.position.x = int(arrPosition[0])
    obj.position.y = int(arrPosition[1])

    #print " values "
    #print arrPosition[0]
    #print ","
    #print arrPosition[1]

    obj.run = False;

def debug(obj,kwargs):

    print kwargs[0]
