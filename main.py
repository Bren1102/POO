import csv

from bd import Coleccion
from bd import Documento
from bd import Str2Dic
from bd import BaseDeDatosDocumental
from bd import ColeccionNueva

#Creo una nueva coleccion
c = ColeccionNueva('pruebaDatos', 1)
c.import_collection('datos_personales.csv')


# Verfico que se han añadido los documentos
for doc_id, doc in c.documentos.items():
   print(doc)



def mostrar_menu():
    print("\n--- Base de Datos Documental ---")
    print("1. Crear colección")
    print("2. Importar CSV a colección")
    print("3. Consultar documento en colección")
    print("4. Eliminar documento de colección")
    print("5. Listar todos los documentos en colección")
    print("6. Salir")
    return input("Seleccione una opción: ")


def main():
    bd = BaseDeDatosDocumental("MiBaseDeDatos", 1)

    while True:
         opcion = mostrar_menu()
         #Crear colección
         if opcion == "1": 
            nombre_coleccion = input("Ingrese el nombre de la coleccion: ")
            bd.crear_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada")
         
         #Importar datos
         elif opcion == "2":
            nombre_coleccion = input("Ingrese el nombre de la coleccion a importar: ")
            Coleccion = bd.obtener_coleccion(nombre_coleccion)
            if Coleccion: 
               nombre_archivo = input("Ingrese el nombre del archivo CSV a importar: ")
               Coleccion.import_collection(nombre_archivo)
               print(f"Datos importados '{nombre_coleccion}' exitosamente")
            else: 
               print(f"La coleccion '{nombre_coleccion}' no existe")
         
         #Consultar documento
         elif opcion == "3":
            nombre_coleccion = input("Ingrese el nombre de la colección a consultar: ")
            coleccion = bd.obtener_coleccion(nombre_coleccion)
            if coleccion:
               print("IDs disponibles en la coleccion: ", coleccion.documentos.keys())
               id_documento = int(input("Ingrese el id del documento a consultar: "))
               documento = coleccion.buscar_documento(id_documento)
               if documento:
                  print(documento)
               else: 
                  print(f"El documento con ID '{id_documento}' no fue encontrado")
            else: 
               print(f"La coleccion '{nombre_coleccion}' no existe")
         
         #Eliminar documento
         elif opcion == "4":
            nombre_coleccion = input("Ingrese el nombre de la colección a eliminar: ")
            Coleccion = bd.obtener_coleccion(nombre_coleccion)
            if Coleccion:
               id_documento = input("Ingrese el id del documento a eliminar: ")
               Coleccion.eliminar_documento(id_documento)
               print(f"Documento con ID '{id_documento}' eliminado")
            else:
               print(f"La coleccion '{nombre_coleccion}' no existe")
         
         #Listar documentos
         elif opcion == "5":
            nombre_coleccion = input("Ingrese el nombre de la coleccion a mostrar: ")
            Coleccion = bd.obtener_coleccion(nombre_coleccion)
            if Coleccion:
               if Coleccion.documentos:
                  print("Documentos en la colección")
                  for documento in Coleccion.documentos.values():
                     print(documento)
               else: 
                  print(f"La colección '{nombre_coleccion}' está vacía")
            else:
               print(f"La colección '{nombre_coleccion}' no existe")
         
         elif opcion == "6":
            print("Saliendo del programa")
            break

         else:
            print("Opción no válida. Por favor, ingrese otra opción.")

if __name__ == "__main__":
   main()



