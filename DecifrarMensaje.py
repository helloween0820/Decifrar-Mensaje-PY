print("Ingresa el mensaje cifrado")
mensaje = input()
print("Cuántas veces quieres devolver la letra")
veces = int(input())

mensajeDecifrado = ""

for i in range(0, len(mensaje), 1):
    letra = mensaje[i]
    minuscula = (letra >= 'a' and letra <= 'z')
    mayuscula = (letra >= 'A' and letra <= 'Z')
    if not(minuscula or mayuscula):
        mensajeDecifrado += letra
    else:
        ascii = ord(letra)
        baseAscii = ord('a')
        if mayuscula:
            baseAscii = ord('A')
        nuevoAscii = (ascii - baseAscii - veces) % 26 + baseAscii
        nuevaLetra = chr(nuevoAscii)
        mensajeDecifrado += nuevaLetra

print(mensajeDecifrado)