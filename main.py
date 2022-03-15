import csv

with open('data.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0

  data = {}
  for row in csv_reader:
    if line_count == 0:
      print(f'column names are {", ".join(row)}')
      line_count +=1
    else:
      print(row[11])
      line_count += 1
  print(f'Process {line_count} lines.')    