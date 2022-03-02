import csv
#MSG_True= "El fitxer existeix"
#MSG_False= "El fitxer no existeix"

def file_header(archivo):
  with open(archivo, 'a', encoding='utf-8', newline='') as csv_file:
    fieldnames = ['ID', 'Nom', 'Cognom1', 'Edat', 'Tecnologia']
    writeCSV = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writeCSV.writeheader()

def file_write(archivo, ID, nom, edat, cognom, tecno):
  with open(archivo, 'a', encoding='utf-8') as csv_file:
    fieldnames = ['ID', 'Nom', 'Cognom1', 'Edat', 'Tecnologia']
    writeCSV= csv.DictWriter(csv_file, fieldnames=fieldnames)
    writeCSV.writerow({'ID': ID, 'Nom': nom, 'Cognom1': cognom, 'Edat': edat, 'Tecnologia': tecno})
