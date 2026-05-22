class Jedi:
    def __init__(self, nombre: str):
        # Atributos de identificación
        self.nombre = nombre
        self.rango = "Iniciado Jedi"  # Rango inicial
        
        # Estadísticas principales (Stats)
        self.vida_max = 100
        self.vida_actual = 100
        self.fuerza_max = 50
        self.fuerza_actual = 50
        
        # Habilidades que irá aprendiendo
        self.habilidades = []

    def mostrar_ficha(self):
        """Muestra en pantalla el estado actual del avatar."""
        print("\n" + "="*30)
        print(f"   FICHA DE AVATAR JEDI")
        print("="*30)
        print(f"Nombre:  {self.nombre}")
        print(f"Rango:   {self.rango}")
        print(f"Vida:    {self.vida_actual}/{self.vida_max}")
        print(f"Fuerza:  {self.fuerza_actual}/{self.fuerza_max}")
        print("="*30)


# --- Flujo de creación del jugador ---
print("""Te separaste por accidente de tu maestro Jedi durante una misión.
Ahora debes sobrevivir en un planeta desconocido y encontrar a tu maestro.
Buena suerte, Jedi.""")
nombre_elegido = input("Introduce el nombre de tu avatar Jedi: ")

# Instanciamos (creamos) el objeto usando la clase
jugador = Jedi(nombre_elegido)

# Verificamos que se haya creado correctamente mostrando sus datos
jugador.mostrar_ficha()