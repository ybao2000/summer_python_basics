def save_month_lines(indent, number):
  lines = []
  line = '   ' * indent
  for i in range(1, number+1):
    line += f"{i:2d} "
    if (i+indent) % 7 == 0:
      lines.append(line)
      line = ''
  if line:   # simplified of len(line) > 0 
    line = line + ' ' * (21-len(line))   # to make line as a full line (21 characters)
    lines.append(line)

  return lines

jan_lines = save_month_lines(3, 31)
indent_feb = (3+31) % 7
feb_lines = save_month_lines(indent_feb, 29)
indent_mar = (indent_feb + 29) % 7
mar_lines = save_month_lines(indent_mar, 31)

for i in range(5):
  print(jan_lines[i], feb_lines[i], mar_lines[i])