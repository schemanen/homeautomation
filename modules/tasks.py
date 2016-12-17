"""
Created by Kim Myhrman
Last modified: 2016-12-17
"""
import modules.tellstick as tellstick
import time

class Tasks:
	"""
	Class that defines tasks performed on tellstick duo
	connected devices
	"""
	__tellstick = None

	def __init__(self):
		self.__tellstick = tellstick.Tellstick()


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

