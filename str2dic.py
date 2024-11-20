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