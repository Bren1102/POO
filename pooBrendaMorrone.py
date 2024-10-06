#Como leo un archivo linea a linea en python

from main import Str2Dic

f = open("csv_files/username.csv", "rt")

schema = f.readline().replace("\n", "")
parser = Str2Dic(schema)
row1 = f.readline().replace("\n", "")
row2 = f.readline().replace("\n", "")
print(parser.convert(row1))
print(parser.convert(row2))
print(schema)
print(row1)