import json

class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_text(self):
        try:
            with open(self.file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("Error: El archivo {self.file_path} no fue encontrado.")
        except Exception as e:
            print("Error al leer el archivo: {e}")
    
    def write_text(self, content):
        try: 
            with open(self.file_path, 'w') as file:
                file.write(content)
            print("Archivo {self.file_path} escrito correctamente.")
        except Exception as e:
            print("Error al escribir el arvhio: {e}")
    
    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            print("Error: El archivo {silf.file_path} no fue encontrado.")
        except json.JSONDecodeError: 
            print("Error al decodificar el archivo JSON")
        except Exception as e:
            print("Error general: {e}") 
    
    def write_json(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print("Archivo JSON {self.file_path} escrito correctamente")
        except Exception as e:
            print("Error al escribir el archivo JSON: {e}")