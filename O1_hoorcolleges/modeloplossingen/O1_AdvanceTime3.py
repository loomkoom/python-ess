# Advance the current time with one second.
#   The program reads the current time in European
#   format, and prints out the advanced time.

hours   = int(input("Enter the hours   : "))
minutes = int(input("Enter the minutes : "))
seconds = int(input("Enter the seconds : "))

if seconds < 59:
  seconds += 1
elif minutes < 59:  # seconds == 59
  minutes += 1
  seconds = 0
elif hours < 23:  # minutes == 59, seconds == 59
  hours += 1
  minutes = 0
  seconds = 0
else:  # hours == 23, minutes == 59, seconds == 59
  hours = 0
  minutes = 0
  seconds = 0

print(hours, minutes, seconds, sep=":")
