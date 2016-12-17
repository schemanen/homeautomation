"""
Created by Kim Myhrman
Last updated: 2016-12-17
"""
import os

class Tellstick:
	"""
	Class to handle on/off for devices controlled
	by the tellstick duo device
	"""
	def __init__(self):
		pass

	def turnOnDevice(self, device = None):
		command = "tdtool --on " + str(device)
		os.system(command)

	def turnOffDevice(self, device = None):
		command = "tdtool --off " + str(device)
		os.system(command)