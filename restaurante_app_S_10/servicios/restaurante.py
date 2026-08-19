from typing import List, Optional
from modelos.producto import Producto


class Restaurante:
    def __init__(self):
        self.__productos: List[Producto] = []

    def agregar_producto(self, producto: Producto) -> bool:
        if self.buscar_por_codigo(producto.codigo) is not None:
            print(f"⚠️ Ya existe un producto con código {producto.codigo}")
            return False
        self.__productos.append(producto)
        return True

    def buscar_por_codigo(self, codigo: str) -> Optional[Producto]:
        for prod in self.__productos:
            if prod.codigo == codigo:
                return prod
        return None

    def listar_productos(self) -> List[Producto]:
        return list(self.__productos)

    def actualizar_producto(self, codigo: str, nuevo_titulo: str, nuevo_precio: float) -> bool:
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        # Validaciones antes de actualizar
        if not nuevo_titulo or nuevo_titulo.strip() == "":
            raise ValueError("El título no puede quedar vacío")
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo")
        producto.titulo = nuevo_titulo.strip()
        producto.precio = nuevo_precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self.__productos.remove(producto)
        return True