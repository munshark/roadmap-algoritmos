import random

las_manitos = ["piedra", "papel", "tijera"]
jugador = input("Ingresa tu opción: (piedra, papel o tijera)").lower()
maquinola = random.choice(las_manitos)

print(f"Jugador : {jugador}  vs CPU : {maquinola}")

if (jugador == "piedra" and maquinola == "tijera") or(jugador == "tijera" and maquinola == "papel") or  (jugador == "papel" and maquinola == "piedra"):
    print("Ganaste")
elif jugador == maquinola:
    print("Empataron")
else:
    print("Perdiste")
