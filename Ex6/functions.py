import csv

def file_header(fname):
  with open(fname, 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writeheader()

def file_write(fname, book):
  with open('files/books.csv', 'a', encoding='utf-8', newline='') as csvfile:
    fieldnames = ['isbn', 'title', 'author', 'editorial', 'pub_date']
    writeCSV = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writeCSV.writerow({'isbn': book['isbn'], 'title': book['title'], 'author': book['author'], 'editorial': book['editorial'], 'pub_date': book['pub_date']})