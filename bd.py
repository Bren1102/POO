class Documento:
    def __init__(self, id_documento, contenido=None):
        self.id_documento = id_documento
        self.contenido = contenido if contenido is not None else {}

    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return f"Documento id: {self.id_documento}, contenido: {self.contenido}"
    


class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
    
    def añadir_documento(self, documento):
        self.documentos[documento.id_documento] =  documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return f"Coleccion {self.nombre} con {len(self.documentos)} documentos"

class BaseDeDatosDocumental:
    def __init__(self, nombre=None, id_inicial=0):
        self.colecciones = {}

    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = ColeccionNueva(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return "Base de datos documental con {len(self.colecciones)}"
    



schema = 'Nombre,Apellido,Edad,Mail'
row = 'Brenda,Morrone,36,bmorrone@hotmail.com'


class SchemaError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class Str2Dic():
    def __init__(self, schema, separator=','):
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            return d
        else:
            raise SchemaError("Los campos de la fila no concuerdan con el schema")


class ColeccionNueva(Coleccion):
   def __init__(self, nombre, id_inicial=0):
      super().__init__(nombre)
      self.id_inicial = id_inicial
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
   
   def consultar_documento_por_id(self, id):
       for doc in self.documentos:
           if doc.id_documento == id:
               return doc
       return None
    