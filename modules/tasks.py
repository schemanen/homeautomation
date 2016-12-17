"""
Created by Kim Myhrman
Last modified: 2016-12-17
"""
import modules.tellstick as tellstick
import modules.homecheck as homecheck
import time

class Tasks:
	"""
	Class that defines tasks performed on tellstick duo
	connected devices
	"""
	__tellstick = None
	__home = None

	def __init__(self):
		self.__tellstick = tellstick.Tellstick()
		self.__home = homecheck.Homecheck()


	def turnOnDevice(self, device = None):
		"""
		Turn on a device using Tellstick DUO
		"""
		self.__tellstick.turnOnDevice(device)

	def turnOffDevice(self, device = None):
		"""
		Turn off a device using Tellstick DUO
		"""
		self.__tellstick.turnOffDevice(device)

	def blinkDevice(self, device = None, timer = 0):
		"""
		Blink the device for time seconds
		"""
		count = 0
		while (count < timer):
			self.__tellstick.turnOnDevice(device)
			time.sleep(1)
			self.__tellstick.turnOffDevice(device)
			time.sleep(1)
			count = count + 2

	def turnOnIfHome(self, device = None, ip = None):
		if(self.__home.checkIP(ip)):
			self.__tellstick.turnOnDevice(device)
		else:
			self.__tellstick.turnOffDevice(device)
			print("Device " + ip + " is not home. Turning of device.")


