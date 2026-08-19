from modelos.producto import Producto
from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio


def mostrar_menu():
    print("\n===== SISTEMA DE ADMINISTRACIÓN — RESTAURANTE =====")
    print("1. Registrar producto")
    print("2. Buscar producto por código")
    print("3. Listar todos los productos")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================================")


def main():
    # Inicializar servicios
    archivo_servicio = ArchivoServicio()
    restaurante = Restaurante()

    # Cargar productos guardados al iniciar
    print("🔄 Cargando productos...")
    productos_guardados = archivo_servicio.cargar_productos()
    for prod in productos_guardados:
        restaurante.agregar_producto(prod)
    print(f"✅ {len(productos_guardados)} productos cargados.\n")

    # Bucle principal
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo = input("Código: ").strip()
            titulo = input("Nombre/Título: ").strip()
            try:
                precio = float(input("Precio: ").strip())
                producto = Producto(codigo, titulo, precio)
                if restaurante.agregar_producto(producto):
                    archivo_servicio.guardar_productos(restaurante.listar_productos())
                    print("✅ Producto registrado y guardado.")
            except ValueError as e:
                print(f"❌ Datos inválidos: {e}")

        elif opcion == "2":
            print("\n--- Buscar Producto ---")
            codigo = input("Código a buscar: ").strip()
            producto = restaurante.buscar_por_codigo(codigo)
            if producto:
                print(f"📋 {producto}")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "3":
            print("\n--- Lista de Productos ---")
            productos = restaurante.listar_productos()
            if not productos:
                print("ℹ️ No hay productos registrados.")
            else:
                for p in productos:
                    print(p)

        elif opcion == "4":
            print("\n--- Actualizar Producto ---")
            codigo = input("Código del producto a actualizar: ").strip()
            producto = restaurante.buscar_por_codigo(codigo)
            if not producto:
                print("❌ Producto no encontrado.")
                continue
            print(f"Actual: {producto}")
            nuevo_titulo = input(f"Nuevo título (dejar vacío = mantener '{producto.titulo}'): ").strip()
            if not nuevo_titulo:
                nuevo_titulo = producto.titulo
            try:
                precio_texto = input(f"Nuevo precio (actual ${producto.precio:.2f}): ").strip()
                nuevo_precio = producto.precio if not precio_texto else float(precio_texto)
                if restaurante.actualizar_producto(codigo, nuevo_titulo, nuevo_precio):
                    archivo_servicio.guardar_productos(restaurante.listar_productos())
                    print("✅ Producto actualizado y guardado.")
            except ValueError as e:
                print(f"❌ Error: {e}")

        elif opcion == "5":
            print("\n--- Eliminar Producto ---")
            codigo = input("Código del producto a eliminar: ").strip()
            if restaurante.eliminar_producto(codigo):
                archivo_servicio.guardar_productos(restaurante.listar_productos())
                print("✅ Producto eliminado y cambios guardados.")
            else:
                print("❌ Producto no encontrado.")

        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()