def run_length_encoding(message): #Defino la función para aplicar el algoritmo run-lenght
    sequence = ''
    previous_char = ''
    cont = 1
    for char in message: #Para cada elemento del array introducito por el user
        if char != previous_char: #si el elemento actual es diferente al anterior
            if previous_char: #añadimos el elemento y el numero de veces que está repetido a nuestra sequencia de salida
                sequence = sequence + previous_char + str(cont)
            cont = 1 #retrocedemos contador a 1
            previous_char = char #actualizamos variable previous_char
        else: #si el elemento actual es igual al anterior actualizamos contador
            cont += 1
    else:
        sequence = sequence + previous_char + str(cont) #final del array input
        return sequence

while True: #Creo un menú para interectuar con el user
    try:
        message_to_encode = input("Enter a string of characters to be encoded by Run-Length: ")
        result = run_length_encoding(message_to_encode)
        print(result)
    except ValueError:
        print("Error.")
        continue




