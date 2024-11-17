from bd import BaseDeDatosDocumental
import json

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
    bd = BaseDeDatosDocumental("MiBaseDeDatos")

    while true:
        opcion = mostrar_menu()

        if opcion == "1": 
            nombre_coleccion = input("Ingrese el nombre de la coleccion")
            bd.crear_coleccion(nombre_coleccion)
            print(f"Colección '{nombre_coleccion}' creada")

        elif opcion == 2: 
            nombre_coleccion = input    


