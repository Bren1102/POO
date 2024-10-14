class Documento:
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return "Documento(id={self.id}, contenido={self.contenido})"
    


class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}
    
    def añadir_documento(self, documento):
        self.documentos[documento.id] =  documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return "Coleccion {self.nombre} con {len(self.documentos)} documentos"

class BaseDeDatosDocumental:
    def __init__(self):
        self.colecciones = {}

    def crear_coleccion(self, nombre_coleccion):
        if nombre_coleccion not in self.colecciones:
            self.colecciones[nombre_coleccion] = Coleccion(nombre_coleccion)

    def eliminar_coleccion(self, nombre_coleccion):
        if nombre_coleccion in self.colecciones:
            del self.colecciones[nombre_coleccion]

    def obtener_coleccion(self, nombre_coleccion):
        return self.colecciones.get(nombre_coleccion, None)
    
    def __str__(self):
        return "Base de datos documental con {len(self.colecciones)}"
    



schema = 'Nombre,Apellido,Edad,Mail'
row = 'Brenda,Morrone,36,bmorrone@hotmail.com'

class Str2Dic():
    def __init__(self, schema, separator=','):
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self, row)
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            return d

            
        