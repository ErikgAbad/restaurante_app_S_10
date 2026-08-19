import json
from typing import List, Optional
from modelos.producto import Producto


class ArchivoServicio:
    RUTA_ARCHIVO = "datos/productos.json"

    def guardar_productos(self, productos: List[Producto]) -> bool:
        """Guarda la lista de productos en el archivo JSON"""
        try:
            # Convertir objetos a diccionarios
            datos_a_guardar = [producto.to_dict() for producto in productos]

            with open(self.RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
            return True

        except PermissionError:
            print("⚠️ No tienes permisos para escribir en el archivo.")
        except Exception as e:
            print(f"❌ Error al guardar: {e}")
        return False

    def cargar_productos(self) -> List[Producto]:
        """Carga productos desde JSON y los convierte en objetos Producto"""
        productos: List[Producto] = []

        try:
            with open(self.RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
                registros = json.load(archivo)

            if not isinstance(registros, list):
                print("⚠️ El formato del archivo no es una lista. Se iniciará vacío.")
                return productos

            for registro in registros:
                try:
                    producto = Producto.from_dict(registro)
                    productos.append(producto)
                except KeyError as e:
                    print(f"⚠️ Registro incompleto omitido: falta clave {e}")
                except ValueError as e:
                    print(f"⚠️ Registro con datos inválidos omitido: {e}")

        except FileNotFoundError:
            # Primera ejecución: archivo no existe → lista vacía
            print("ℹ️ Archivo de productos no encontrado. Se iniciará con lista vacía.")
        except json.JSONDecodeError:
            print("⚠️ El archivo JSON está corrupto. Se iniciará con lista vacía.")
        except PermissionError:
            print("⚠️ No tienes permisos para leer el archivo. Se iniciará con lista vacía.")

        return productos