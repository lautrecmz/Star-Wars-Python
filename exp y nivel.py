# ----------------------------------------------Comportamiento de exp y subida de nivel----------------------------------------
import Personaje
# ----------------------------------------------Funcion para subir de nivel--------------------------------------------------
def subir_nivel():
    if Personaje.Stats["exp_actual"] >= Personaje.Stats["exp_siguiente_nivel"]:
        Personaje.Stats["nivel"] += 1
        Personaje.Stats["exp_actual"] -= Personaje.Stats["exp_siguiente_nivel"]
        Personaje.Stats["exp_siguiente_nivel"] = int(Personaje.Stats["exp_siguiente_nivel"] * 1.5)
        if Personaje.Stats["nivel"] % 2 == 0:
            Personaje.Puntos_habilidad += 1
        print(f"¡Felicidades {Personaje.Nombre_jugador}! Has subido al nivel {Personaje.Stats['nivel']}")
