"""
Created by Kim Myhrman
Last updated: 2016-12-17
"""

import modules.tasks as tasks
import schedule
import time

# Create the handeler for Tellstick DUO
taskHandeler = tasks.Tasks()

"""
Schedules
"""
schedule.every().day.at("07:15").do(taskHandeler.turnOnDevice, "tv")
schedule.every().day.at("07:15").do(taskHandeler.blinkDevice, "christmastree", 10)
schedule.every(1).minutes.do(taskHandeler.turnOnIfHome, "christmastree", "192.168.1.13")

"""
Engine
"""
while True:
	schedule.run_pending()
	time.sleep(1)