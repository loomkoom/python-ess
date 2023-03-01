# Advance the current time with one second.
#   The program reads the current time in European
#   format, and prints out the advanced time.

hours   = int(input("Enter the hours   : "))
minutes = int(input("Enter the minutes : "))
seconds = int(input("Enter the seconds : "))

if seconds < 59:
  seconds += 1
else:
  seconds = 0
  if minutes < 59:
    minutes += 1
  else:
    minutes = 0
    if hours < 23:
      hours += 1
    else:
      hours = 0

print(hours, ":", minutes, ":", seconds)
