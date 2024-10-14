from bd import Coleccion
from bd import Documento
from bd import Str2Dic

def import_collection(nombre_archivo):
    Coleccion = Coleccion()

    with open(Documento, 'r') as f:
        schema = f.readline().rstrip()
        diccionario_schema = Str2Dic(schema)


    
class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
   
   

    