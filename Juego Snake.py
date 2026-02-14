ancho = 10
alto = 10

serpiente = [[5, 5], [4, 5], [3, 5]]
direccion = "s"
comida = [7, 2]

def dibujar():
    print("\n" * 3)
    for y in range(alto):
        for x in range(ancho):
            if [y, x] == serpiente[0]:
                print("O", end=" ")
            elif [y, x] in serpiente:
                print("o", end=" ")
            elif [y, x] == comida:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
    print("Mover: w=arriba s=abajo a=izq d=der")

while True:
    dibujar()

    tecla = input("Movimiento: ").lower()

    if tecla in ["w", "a", "s", "d"]:
        direccion = tecla

    cabeza = serpiente[0][:]

    if direccion == "w":
        nueva = [cabeza[0] - 1, cabeza[1]]
    elif direccion == "s":
        nueva = [cabeza[0] + 1, cabeza[1]]
    elif direccion == "a":
        nueva = [cabeza[0], cabeza[1] - 1]
    elif direccion == "d":
        nueva = [cabeza[0], cabeza[1] + 1]

    if 0 <= nueva[0] < alto and 0 <= nueva[1] < ancho:
        serpiente.insert(0, nueva)
        serpiente.pop()