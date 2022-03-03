import csv

def file_header(fname):
  try:
    with open(fname, 'a', encoding='utf-8', newline='') as csvfile:
      fieldnames = ['Data', 'Nom', 'Localització', 'Espècie', 'Mida', 'Característiques']
      writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
  except:
    writeCSV.writeheader()

def file_write(fname, bio):
  with open(fname, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['Data', 'Nom', 'Localització', 'Espècie', 'Mida', 'Característiques']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writerow({'Data': bio['Data'], 'Nom': bio['Nom'], 'Localització': bio['Localització'], 'Espècie': bio['Espècie'], 'Mida': bio['Mida'], 'Característiques': bio['Característiques']})

def file_read(fname):
  with open(fname) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
      print(', '.join(row))