"""
Calculate the distance of lightning when given the delay between 
the lightning strike and the thunder. If the storm is too close, 
within 1 km, the program should warn you to unplug all appliances.

 * The time is given in seconds, and should be a decimal number
 * The speed of sound is 343 m/s
 * Print the distance in kilometer and meter
 * Print an optional warning message if the storm is too close
 * Make sure the time is positive

Verify your program:
 t = 1          | 0 km and 343 meter + [Warning message]
 t = -1         | [Error message]
 t = 10         | 3 km and 430 meter
 t = 2.9        | 0 km and 994 meter + [Warning message]
 t = 3          | 1 km and 29 meter
"""

time = float(input("Enter the time difference between lighting and thunder: "))

SPEED_OF_SOUND = 343.0

if time < 0:
	print("Enter a positive time")
else:
	distance = int(SPEED_OF_SOUND*time)
	distance_km = distance // 1000
	distance_m = distance - (distance_km*1000)
	print("The storm is at", distance_km, "km and", distance_m, "m")

	if distance < 1000:
		print("WARNING: The storm is too close, please unplug all appliances!")



