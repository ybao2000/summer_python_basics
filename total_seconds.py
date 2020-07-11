# convert hours, minutes and seconds into total seconds
def total_seconds(hours, minutes, seconds):
  return hours * 3600 + minutes * 60 + seconds

print(total_seconds(2, 3, 5))