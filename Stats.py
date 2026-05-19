#-------------------------------------Un juego basado en Star Wars mientras aprendo Python---------------------------------
print("May the force of code be with you")
Stats = {
"Vida_jugador" : 100,
"Vigor" : 0,
"Agilidad" : 0,
"Fuerza_SW" : 0,
"Armas" : 0,
}
Inventario = ["Comida en lata"]
PuntosExp = 2
Personaje = False
#-----------------------------------------Creación del personaje------------------------------------------------
while Personaje == False:
    Personaje = input("""Elige un personaje para tu aventura
                Jedi / Sith / Bounty Hunter :
                """).lower()
    match Personaje:
        case "jedi":
            Nombre_jugador = "Cal Kestis"
            Stats["Vigor"]=5
            Stats["Agilidad"]=5
            Stats["Fuerza_SW"]=50
            Clase = "Jedi"
            Personaje = True
            print(f"Joven {Nombre_jugador}, restaura la orden Jedi")
        case "sith":
            Nombre_jugador = "Darth Maul"
            Stats["Vigor"]=6
            Stats["Agilidad"]=6
            Stats["Fuerza_SW"]=60
            Clase = "Sith"
            Personaje = True
            print(f"Venga a tus hermanos caídos {Nombre_jugador}, mata a Obi-Wan Kenobi")
        case "bounty hunter":
            Nombre_jugador = "Boba Fett"
            Stats["Vigor"]=5
            Stats["Agilidad"]=7
            Stats["Armas"]=80
            Inventario.append("Rifle blaster")
            Clase = "Bounty hunter"
            Personaje = True
            print("Solo te importa el dinero, caza jedis para conseguirlo")
        case _:
            print("Esa clase no existe en esta galaxia")
            Personaje = False
while PuntosExp > 0 and Personaje == True:
    print(f"Tienes {PuntosExp} puntos de mejora disponibles.")
    Elección = input ("""Que quieres mejorar? Fuerza / Agilidad :
                      """).lower()
    match Elección:
        case "fuerza":
            Stats["Vigor"]+=1
            PuntosExp-=1
            print(f"Level Up! Tu fuerza a aumentado, {Nombre_jugador}")
        case "agilidad":
            Stats["Agilidad"]+=1
            PuntosExp-=1
            print("Level Up! Eres agil como el maestro Yoda")
        case _:
            Stats["Vida_jugador"]-=10
            PuntosExp-=2
            print("""Esa arrogancia fue la que condujo al lado oscuro
            al joven Anakin""")
if Nombre_jugador == "Cal Kestis":
    sable_de_luz = input("""Elige el color de tu sable joven Padawan
                            Azul / Verde / Morado:
                            """).lower()
    match sable_de_luz:
        case "azul":
            Stats["Vigor"]+=1
            Stats["Fuerza_SW"]-=10
            Inventario.append("Sabledeluz")
            print("""Eres un buen guerrero joven Padawan pero en el
                    camino de la fuerza, la violencia no lo es todo""")
            print("""Vigor ha aumentado!
                Conexión con la fuerza a disminuido!""")
        case "verde":
            Stats["Fuerza_SW"]+=10
            Stats["Vigor"]-=1
            Inventario.append("Sabledeluz")
            print("""Eres sabio como el maestro Qui-Gon Jinn pero así
                    como el, los duelos no son lo tuyo""")
            print("""Conexión con la fuerza ha aumentado!
                    Vigor ha disminuido!""")
        case "morado":
            Stats["Vigor"]+=1
            Stats["Fuerza_SW"]+=10
            Stats["Vida_jugador"]-=10
            Inventario.append("Sabledeluz")
            print("""Pocos tienen el coraje para caminar entre
                    ambos lados de la fuerza. Cuidado joven Padawan""")
            print("""Conexión con la fuerza ha aumentado!
                    Vigor ha aumentado!
                    Vida ha disminuido!""")
        case _:
            print("Ese sable no pertenece a ha orden Jedi")
            print("""El Padawan perdió su sable de luz al sobrevivir
                    a la orden 66""")
            print("Haz perdido mejoras disponibles")
elif Nombre_jugador == "Darth Maul":
    sable_de_luz = input("""Como haz conseguido tu sable de luz?
                            Sangrando / Robandolo:
                         """).lower()
    match sable_de_luz:
        case "sangrando":
            Stats["Fuerza_SW"]+=20
            Stats["Vigor"]+=2
            Stats["Vida_jugador"]-=10
            Inventario.append("Sabledeluz")
            print("Tu odio ha hecho sangrar tu cristal Kyber")
            print("""Vigor ha aumentado!
                    Vida ha disminuido!""")
        case "robandolo":
            Stats["Vigor"]+=1
            Stats["Vida_jugador"]-=10
            Inventario.append("Sabledeluz")
            print("""Te haz enfrentado a otro usuario de la fuerza
                    haz salido victorioso pero herido""")
            print("""Vigor ha aumentado!
                    Vida ha disminuido!""")
        case _:
            print("Opción no válida, suponemos que perdiste tu sable de luz")
            print("Un sith débil es una deshonra, perdiste mejoras disponibles")
#------------------------------------------------Stats terminadas-----------------------------------------               
print(f"""Tus stats son:
        Nombre: {Nombre_jugador}
        Vida:{Stats["Vida_jugador"]}
        Fuerza:{Stats["Vigor"]}
        Agilidad:{Stats["Agilidad"]}
        Clase:{Clase}""")
if Clase == "Bounty hunter":
    print(f"Especial (Armas):{Stats["Armas"]}")
else:
    print(f"Especial (La Fuerza):{Stats["Fuerza_SW"]}")
print(f"Inventario:{Inventario}")
input("Presiona Enter para finalizar:")