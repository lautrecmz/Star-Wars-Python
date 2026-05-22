class Personaje:
    def __init__(self, nombre, clase, stats):
        self.nombre = nombre
        self.clase = clase
        self.vida = 100
        self.vigor = stats.get("vigor", 0)
        self.agilidad = stats.get("agilidad", 0)
        self.fuerza_sw = stats.get("fuerza_sw", 0)
        self.armas = stats.get("armas", 0)
        self.exp_actual = 0
        self.exp_siguiente = 50
        self.nivel = 1
        self.inventario = ["Comida en lata"]
        self.puntos_habilidad = 2

    def mejorar_stats(self):
        while self.puntos_habilidad > 0:
            print(f"Tienes {self.puntos_habilidad} puntos de mejora disponibles.")
            eleccion = input("Que quieres mejorar? Fuerza / Agilidad: ").lower()
            if eleccion == "fuerza":
                self.vigor += 1
                self.puntos_habilidad -= 1
                print(f"Level Up! Tu fuerza ha aumentado, {self.nombre}")
            elif eleccion == "agilidad":
                self.agilidad += 1
                self.puntos_habilidad -= 1
                print("Level Up! Eres agil como el maestro Yoda")
            else:
                self.vida -= 10
                self.puntos_habilidad -= 2
                print("Esa arrogancia fue la que condujo al lado oscuro al joven Anakin")

    def elegir_arma(self):
        pass

    def mostrar_stats(self):
        print(f"""
Nombre: {self.nombre}
Vida: {self.vida}
Fuerza: {self.vigor}
Agilidad: {self.agilidad}
Clase: {self.clase}""")
        if self.clase == "Bounty Hunter":
            print(f"Especial (Armas): {self.armas}")
        else:
            print(f"Especial (La Fuerza): {self.fuerza_sw}")
        print(f"Inventario: {self.inventario}")


class Jedi(Personaje):
    def __init__(self):
        super().__init__("Cal Kestis", "Jedi", {"vigor": 5, "agilidad": 5, "fuerza_sw": 50})
        print(f"Joven {self.nombre}, restaura la orden Jedi")

    def elegir_arma(self):
        color = input("Elige el color de tu sable joven Padawan\nAzul / Verde / Morado: ").lower()
        if color == "azul":
            self.vigor += 1
            self.fuerza_sw -= 10
            self.inventario.append("Sabledeluz")
            print("Eres un buen guerrero joven Padawan pero en el camino de la fuerza, la violencia no lo es todo")
            print("Vigor ha aumentado!\nConexion con la fuerza a disminuido!")
        elif color == "verde":
            self.fuerza_sw += 10
            self.vigor -= 1
            self.inventario.append("Sabledeluz")
            print("Eres sabio como el maestro Qui-Gon Jinn pero asi como el, los duelos no son lo tuyo")
            print("Conexion con la fuerza ha aumentado!\nVigor ha disminuido!")
        elif color == "morado":
            self.vigor += 1
            self.fuerza_sw += 10
            self.vida -= 10
            self.inventario.append("Sabledeluz")
            print("Pocos tienen el coraje para caminar entre ambos lados de la fuerza. Cuidado joven Padawan")
            print("Conexion con la fuerza ha aumentado!\nVigor ha aumentado!\nVida ha disminuido!")
        else:
            print("Ese sable no pertenece a la orden Jedi")
            print("El Padawan perdio su sable de luz al sobrevivir a la orden 66")


class Sith(Personaje):
    def __init__(self):
        super().__init__("Darth Maul", "Sith", {"vigor": 6, "agilidad": 6, "fuerza_sw": 60})
        print(f"Venga a tus hermanos caidos {self.nombre}, mata a Obi-Wan Kenobi")

    def elegir_arma(self):
        metodo = input("Como haz conseguido tu sable de luz?\nSangrando / Robandolo: ").lower()
        if metodo == "sangrando":
            self.fuerza_sw += 20
            self.vigor += 2
            self.vida -= 10
            self.inventario.append("Sabledeluz")
            print("Tu odio ha hecho sangrar tu cristal Kyber")
            print("Vigor ha aumentado!\nVida ha disminuido!")
        elif metodo == "robandolo":
            self.vigor += 1
            self.vida -= 10
            self.inventario.append("Sabledeluz")
            print("Te haz enfrentado a otro usuario de la fuerza, haz salido victorioso pero herido")
            print("Vigor ha aumentado!\nVida ha disminuido!")
        else:
            print("Opcion no valida, suponemos que perdiste tu sable de luz")
            print("Un sith debil es una deshonra, perdiste mejoras disponibles")


class BountyHunter(Personaje):
    def __init__(self):
        super().__init__("Boba Fett", "Bounty Hunter", {"vigor": 5, "agilidad": 7, "armas": 80})
        self.inventario.append("Rifle blaster")
        print("Solo te importa el dinero, caza jedis para conseguirlo")


if __name__ == "__main__":
    print("May the force of code be with you")

    fabrica = {
        "jedi": Jedi,
        "sith": Sith,
        "bounty hunter": BountyHunter,
    }

    while True:
        eleccion = input("""Elige un personaje para tu aventura
                Jedi / Sith / Bounty Hunter: """).lower()
        if eleccion in fabrica:
            personaje = fabrica[eleccion]()
            break
        print("Esa clase no existe en esta galaxia")

    personaje.mejorar_stats()
    personaje.elegir_arma()
    personaje.mostrar_stats()
    input("Presiona Enter para finalizar:")
