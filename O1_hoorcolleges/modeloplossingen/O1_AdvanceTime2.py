# Advance the current time with one second.
#   The program reads the current time in European
#   format, and prints out the advanced time.

hours   = int(input("Enter the hours   : "))
minutes = int(input("Enter the minutes : "))
seconds = int(input("Enter the seconds : "))

if hours == 23 and minutes == 59 and seconds == 59:
  hours = 0
  minutes = 0
  seconds = 0
elif minutes == 59 and seconds == 59:  # hours < 23
  hours += 1
  minutes = 0
  seconds = 0
elif seconds == 59:  # minutes < 59
  minutes += 1
  seconds = 0
else:  # seconds < 59
  seconds += 1

print(hours, ":", minutes, ":", seconds)
