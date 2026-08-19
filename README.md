# Restaurante App — Semana 10: Persistencia en JSON

## Estudiante
ERIKG CRISTOFER ABAD ABAD 

## Descripción del sistema
Sistema de administración de productos para un restaurante que permite registrar, buscar, listar, actualizar y eliminar productos. Ahora incorpora **persistencia mediante archivo JSON**, por lo que los productos se conservan aunque se cierre y vuelva a abrir la aplicación.

## Estructura del proyecto
restaurante_app/

├── datos/

│ └── productos.json ← Almacena los productos automáticamente

├── modelos/

│ ├── init.py

│ ├── producto.py ← Clase Producto con validaciones y conversión a diccionario

│ └── usuario.py ← Clase Usuario (en memoria esta semana)

├── servicios/

│ ├── init.py

│ ├── archivo_servicio.py ← Responsable de leer y escribir el JSON

│ └── restaurante.py ← Lógica de negocio y administración de productos

├── main.py ← Menú, interacción con usuario y coordinación

└── README.md


## ¿Cómo funciona la persistencia?

### 📥 Al iniciar (carga)
1. Al ejecutar `main.py`, se crea el servicio de archivos.
2. Se intenta leer `datos/productos.json` con `json.load()`.
3. Cada registro se valida y reconstruye como objeto `Producto`.
4. Los objetos se cargan al servicio Restaurante para trabajar normalmente.

### 📤 Al guardar
1. Cuando se registra, actualiza o elimina un producto → se modifica la colección en memoria.
2. Se convierte cada `Producto` a diccionario con el método `to_dict()`.
3. Se escribe el archivo con `json.dump()` usando codificación UTF-8.

## Excepciones controladas
- **`FileNotFoundError`**: Si el archivo aún no existe → se inicia con lista vacía sin detener el programa.
- **`JSONDecodeError`**: Si el archivo existe pero tiene formato corrupto → se avisa y se inicia vacío.
- **`PermissionError`**: Si no hay permisos de lectura o escritura → se avisa y continúa.
- **`KeyError`**: Si un registro guardado le falta algún campo obligatorio → se omite y se avisa.
- **`ValueError`**: Si los datos de un producto son inválidos → se rechaza y se informa.

## Cómo ejecutar el programa
1. Asegúrate de crear la carpeta `datos/` junto a `main.py`.
2. Ejecuta en la terminal:
   ```bash
   python main.py

Usa el menú para registrar, buscar, listar, actualizar o eliminar productos.

1. Comprobación de persistencia

2. Registra uno o más productos.

3. Cierra la aplicación con la opción Salir.

4. Vuelve a ejecutar main.py.

5. Al listar o buscar, los productos aparecen tal como los dejaste. 

✅Modifica o elimina un producto, cierra y vuelve a abrir: los cambios también se conservan.

✅ Persistencia real: los productos se guardan en productos.json.

✅ Al iniciar, los datos se reconstruyen como objetos Producto.

✅ El archivo se actualiza automáticamente después de cada cambio.

✅ Manejo controlado de errores de archivo y formato JSON.

✅ La lógica de negocio no cambia: se sigue trabajando con objetos.
