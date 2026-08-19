class Producto:
    def __init__(self, codigo: str, titulo: str, precio: float):
        # Validaciones
        if not codigo or codigo.strip() == "":
            raise ValueError("El código no puede estar vacío")
        if not titulo or titulo.strip() == "":
            raise ValueError("El título no puede estar vacío")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        self.codigo = codigo.strip()
        self.titulo = titulo.strip()
        self.precio = precio

    def __str__(self) -> str:
        return f"{self.codigo} | {self.titulo} | ${self.precio:.2f}"

    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario para guardar en JSON"""
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, datos: dict):
        """Crea un Producto desde un diccionario recuperado de JSON"""
        # Validar que existan todas las claves
        claves_requeridas = ["codigo", "titulo", "precio"]
        for clave in claves_requeridas:
            if clave not in datos:
                raise KeyError(f"Falta el campo: {clave}")
        return cls(
            codigo=datos["codigo"],
            titulo=datos["titulo"],
            precio=float(datos["precio"])
        )