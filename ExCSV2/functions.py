import csv

def file_check(fname):
  try:
    f = open(fname, "r")
    return True
  except FileNotFoundError:
    return False

def file_header(fname):
  with open(fname, 'a', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['Any', 'Nom', 'Personalitat o Entitat', 'Sexe', 'Descripció', 'A títol pòstum', 'Decret', 'URL']
    writeCSV = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writeCSV.writeheader()

def file_write(fname, creus):
  with open(fname, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['Any', 'Nom', 'Personalitat o Entitat', 'Sexe', 'Descripció', 'A títol pòstum', 'Decret', 'URL']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writerow({'Any': creus['year'], 'Nom': creus['Nom'], 'Personalitat o Entitat': creus['Personalitat'], 'Sexe': creus['Sexe'], 'Descripció': creus['Description'], 'A títol pòstum': creus['title'], 'Decret': creus['decret'], 'URL': creus['url']})