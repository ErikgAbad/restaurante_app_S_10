# ✨ Restaurante App — Semana 9

**👤 Estudiante:** ERIKG CRISTOFER ABAD ABAD

## 📋 Descripción del sistema
Sistema de administración de productos y usuarios para un restaurante. Permite registrar, buscar, actualizar, eliminar y listar productos; así como registrar y listar usuarios. También muestra las categorías únicas de los productos. Toda la información se maneja **en memoria**.

## 📁 Estructura del proyecto
restaurante_app/

├── modelos/

│ ├── init.py

│ ├── producto.py

│ └── usuario.py

├── servicios/

│ ├── init.py

│ └── restaurante.py

├── main.py

└── README.md


## 📚 Uso justificado de estructuras de datos

### 📖 Lista (`list`)
**¿Dónde?** En `servicios/restaurante.py`: `self._productos` y `self._usuarios`
**¿Para qué?** Almacenar colecciones dinámicas de objetos que se agregan, modifican y eliminan durante la ejecución.

### 📘 Tupla (`tuple`)
**¿Dónde?** En `main.py`: `OPCIONES_MENU`
**¿Para qué?** Almacenar las opciones del menú, que son información fija y **no debe modificarse**.

### 📕 Diccionario (`dict`)
**¿Dónde?** En `main.py`: diccionario `acciones`
**¿Para qué?** Relacionar cada número de opción con su función correspondiente (`clave → valor`), evitando cadenas largas de `if/elif`.

### ✍️ Conjunto (`set`)
**¿Dónde?** En `servicios/restaurante.py`: método `obtener_categorias_unicas()`
**¿Para qué?** Obtener categorías **sin duplicados automáticamente**.

## 🚀 Ejecución
```bash
python main.py

💡 ReflexiónCada estructura tiene un propósito: lista para colecciones que cambian, tupla para datos fijos, diccionario para relaciones clave-valor, y conjunto para valores únicos. Elegir bien reduce errores y hace el código más limpio y mantenible.

