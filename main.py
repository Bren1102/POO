import csv

from bd import Coleccion
from bd import Documento
from bd import Str2Dic


def import_collection(self, nombre_archivo):
    coleccion = Coleccion()

    with open(Documento, 'r') as f:
        schema = f.readline().rstrip()
        diccionario_schema = Str2Dic(schema)
        linea = coleccion.readline().split()
        while linea != "":
           d = diccionario_schema.convert(linea)
           doc = Documento(self.id_documento, d)
           self.add_document(doc) 
           self.id_documento = self.id_documento + 1
        #leer de vuelta al final
           linea = coleccion.readline

c = Coleccion()
c.import_collection('datos_personales.csv')

   
   

    