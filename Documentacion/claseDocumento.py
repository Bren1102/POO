class Documento: 
    def __init__(self, id, contenido=None):
        self.id = id
        self.contenido = contenido if contenido is not None else {}

    
    def obtener_valor(self, clave):
        return self.contenido.get(clave, None)
    
    def modificar_valor(self, clave, valor):
        self.contenido[clave] = valor

    def __str__(self):
        return ("Documento(id={self.id}, contenido={self.contenido})")
    

d = Documento(1)
if not d.obtener_valor('direccion'):
    d.modificar_valor('direccion', 'Calle 12')
print(d.obtener_valor('direccion'))