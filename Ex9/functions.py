import csv
MSG= "Hi han"
MSG2= "projectes"

def file_header(fname):
  with open(fname, 'a', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['ID', 'Grup', 'Nom', 'Data', 'Visites']
    writeCSV = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writeCSV.writeheader()

def file_write(fname, video, ID, data):
  with open(fname, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['ID', 'Grup', 'Nom', 'Data', 'Visites']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writerow({'ID': ID, 'Grup': video['grup'], 'Nom': video['nom'], 'Data': data, 'Visites': video['views']})

def file_read(fname):
  with open(fname) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
      print(' '.join(row))
