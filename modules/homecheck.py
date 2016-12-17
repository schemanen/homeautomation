"""
Created by Kim Myhrman
Last updated: 2016-12-17
"""
import os

class Homecheck:
	"""
	Class that check if a IP address is in the network or not
	"""
	def __init__(self):
		pass

	def checkIP(self, ip = None):
		"""
		Check the ip with ping
		"""
		return os.system("ping -c 1 -w2 " + ip + " > /dev/null 2>&1") == 0
