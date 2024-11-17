import csv

from bd import Coleccion
from bd import Documento
from bd import Str2Dic

class ColeccionNueva(Coleccion):
   def __init__(self, nombre, id_inicial=0):
      super().__init__(nombre)
      self.id_documento = id_inicial

   def import_collection(self, nombre_archivo):
      with open(nombre_archivo, 'r') as f:
         schema = f.readline().rstrip()
         diccionario_schema = Str2Dic(schema)
         linea = f.readline().strip()
         while linea != "":
            d = diccionario_schema.convert(linea)
            doc = Documento(self.id_documento, d)
            self.añadir_documento(doc) 
            self.id_documento = self.id_documento + 1
            #leer de vuelta al final
            linea = f.readline().strip()

c = ColeccionNueva('pruebaDatos', 1)
c.import_collection('datos_personales.csv')

# Verfico que se han añadido los documentos
for doc_id, doc in c.documentos.items():
   print(doc_id)


