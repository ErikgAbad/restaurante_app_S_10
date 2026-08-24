# ✨ Restaurante App — Semana 10: Persistencia en JSON

## 👤 Estudiante
ERIKG CRISTOFER ABAD ABAD

## 📋 Descripción del sistema
Sistema de administración de productos para un restaurante que permite registrar, buscar, listar, actualizar y eliminar productos. Incorpora **persistencia mediante archivo JSON**, por lo que los productos se conservan aunque se cierre y vuelva a abrir la aplicación. La información de usuarios se mantiene en memoria esta semana.

## 📁 Estructura del proyecto
restaurante_app/

├── datos/

│ └── productos.json ← Almacena los productos automáticamente

├── modelos/

│ ├── init.py

│ ├── producto.py ← Clase Producto con conversión a diccionario

│ └── usuario.py ← Clase Usuario (en memoria)

├── servicios/

│ ├── init.py

│ ├── archivo_servicio.py ← Responsable de leer y escribir el JSON

│ └── restaurante.py ← Lógica de negocio y administración

├── main.py ← Menú, interacción y coordinación

└── README.md

## 💾 ¿Cómo funciona la persistencia?

### 📥 Al iniciar la aplicación (carga)
1. Se crea el servicio de archivos.
2. Se intenta leer `datos/productos.json` utilizando `json.load()`.
3. Cada registro se valida y reconstruye como objeto `Producto`.
4. Los objetos cargados se entregan al servicio Restaurante para trabajar normalmente.

### 📤 Al guardar
1. Cuando se registra, actualiza o elimina un producto → se modifica la colección en memoria.
2. Cada objeto `Producto` se convierte a diccionario mediante el método `to_dict()`.
3. Se escribe el archivo con `json.dump()` usando codificación **UTF-8**.

## ⚠️ Excepciones controladas
| Excepción | Situación | Comportamiento |
|---|---|---|
| `FileNotFoundError` | El archivo aún no existe | Inicia con lista vacía sin detener el programa |
| `json.JSONDecodeError` | El archivo existe pero tiene formato corrupto | Muestra mensaje y inicia con lista vacía |
| `PermissionError` | Sin permisos de lectura o escritura | Muestra advertencia y continúa |
| `KeyError` | Falta algún campo obligatorio en un registro | Omite el registro defectuoso y avisa |
| `ValueError` | Datos inválidos al reconstruir un producto | Rechaza el registro y muestra información |

## ✅ Comprobación de persistencia realizada
Se probó el flujo completo de la siguiente manera:

1. ✅ Se ejecutó `main.py` por primera vez
2. ✅ Se registraron varios productos desde el menú
3. ✅ Se verificó que se creó y escribió el archivo `datos/productos.json`
4. ✅ Se cerró completamente la aplicación
5. ✅ Se volvió a ejecutar `main.py`
6. ✅ Al listar y buscar, los productos aparecieron tal como se dejaron
7. ✅ Se modificó y eliminó un producto
8. ✅ Se reinició la aplicación nuevamente
9. ✅ Los cambios también se conservaron correctamente

> **Conclusión:** Los productos se guardan en JSON, se reconstruyen como objetos al iniciar, y el archivo se actualiza automáticamente después de cada operación. El programa continúa trabajando con objetos durante toda la ejecución — los diccionarios se usan únicamente para guardar y cargar.

## 🚀 Cómo ejecutar el programa
1. Asegúrate de que exista la carpeta `datos/` junto a `main.py`.
2. Ejecuta en la terminal:
```bash
python main.py


---

## ✅ PASO A PASO PARA ACTUALIZARLO EN GITHUB

1. Entra a tu repositorio: **https://github.com/ErikgAbad/restaurante_app_S_10**
2. Haz clic en el archivo **README.md**
3. Botón **✏️ Editar**
4. **Borra todo** el contenido que tenga
5. **Pega el texto completo de arriba**
6. Baja hasta el final → botón verde **Commit changes** ✅

---

## 📋 RESUMEN DE LO QUE TIENE ESTE README:

| Requisito del profesor | ¿Está incluido? |
|---|---|
| Nombre del estudiante | ✅ Sí |
| Descripción del sistema | ✅ Sí |
| Estructura de carpetas | ✅ Sí |
| Flujo de carga (al iniciar) | ✅ Sí |
| Flujo de guardado (al modificar) | ✅ Sí |
| Lista de excepciones controladas | ✅ Sí |
| Prueba de persistencia paso a paso | ✅ Sí |
| Instrucciones para ejecutar | ✅ Sí |
