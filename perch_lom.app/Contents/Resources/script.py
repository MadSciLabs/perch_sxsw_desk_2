import Perch

try:
	type(i)
except Exception:
	i=0

def test(obj,kwargs):
	print "calling test"
	obj.position.x = 100
	obj.run = False

def hideObject(obj , kwargs):
	obj.hide();
	print 'hide'
	obj.run = False;

def showObject(obj , kwargs):
	obj.show();
	print 'show'
	obj.run = False;

def toggleObject(obj , kwargs):
	global i;
	print 'got function call --toggleObject--'
	i+=1;
	#obj.rotation +=i
	if i %4 == 0:
		print 'PY :: DBG -- hide'
		obj.hide()
	else:
		print 'PY :: DBG -- show'		
		obj.show()
	i%=360
	print str(i)+ ' is current toggle state'
	#obj.run = False;
