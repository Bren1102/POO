class Coleccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.documentos = {}

    def añadir_documentos(self, documento):
        self.documentos[documento.id] = documento

    def eliminar_documento(self, id_documento):
        if id_documento in self.documentos:
            del self.documentos[id_documento]

    def buscar_documento(self, id_documento):
        return self.documentos.get(id_documento, None)
    
    def __str__(self):
        return ("Coleccion {self.nombre} con {len(self.documentos)} documentos")