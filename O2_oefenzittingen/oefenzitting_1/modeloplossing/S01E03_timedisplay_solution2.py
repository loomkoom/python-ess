"""
A program that reads a number of seconds, and displays it as a number of
hours, a number of minutes and a number of seconds.

* Input may not be negative
* Output is of the format: hours:minutes:seconds
* Output hours will range between 0 and 23

Some example outputs for given inputs:
12457   3 : 27 : 37
0       0 : 0 : 0
86399   23 : 59 : 59
86400   0 : 0 : 0
1000000 13 : 46 : 40
"""

total_seconds = int(input("Enter a number of seconds: "))

seconds = total_seconds%60
total_minutes = total_seconds // 60
minutes = total_minutes % 60
total_hours = total_minutes // 60
hours = total_hours % 24

print(hours, ":", minutes, ":", seconds)
