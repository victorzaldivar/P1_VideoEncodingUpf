def rgb2yuv(R,G,B): #Defino la función para pasar de RGB a YUV con la formula de la teoría
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128
    return print("The conversion is: Y =",Y,"U =",U,"V =",V)

def yuv2rgb(Y,U,V): #Defino la función para pasar de YUV a RGB con la formula de la teoría
    B = 1.164 * (Y - 16) + 2.018 * (U - 128)
    G = 1.164 * (Y - 16) - 0.819 * (V - 128) - 0.391 * (U - 128)
    R = 1.164 * (Y - 16) + 1.596 * (V - 128)
    return print("The conversion is: R =",R,"G =",G,"B =",B)


while True: #Creo un menú para interactuar con el user
    try:
        result = int(input("Choose the method of conversion '1' or '2' (0 to exit of the program): \n"
                           "1. RGB->YUV\n"
                            "2. YUV->RGB\n"))
    except ValueError:
        print("You must to enter a number.")
        continue
    if result == 1:
        print("Introduce values between 0 to 255")
        R = float(input("R: "))
        G = float(input("G: "))
        B = float(input("B: "))

        if (0<=R<=255 and 0<=G<=255 and 0<=B<=255): #Aplico la resticción de que no pueden haber valores de RGB negativos ni por encima de 255
            rgb2yuv(R, G, B);
            continue
        else:
            print("Error: You must enter values between 0 to 255")
            continue

    elif result == 2:
        print("Introduce values between 0 to 255\n")
        Y = float(input("Y: "))
        U = float(input("U: "))
        V = float(input("V: "))

        if (0<=Y<=255 and 0<=U<=255 and 0<=V<=255): #Aplico la resticción de que no pueden haber valores de YUV negativos ni por encima de 255
            yuv2rgb(Y, U, V);
            continue
        else:
            print("Error: You must enter values between 0 to 255")
            continue

        continue
    elif result == 0: #Para salir del programa
        break
    elif result != 1 and result !=2:
        print("You must enter '1' or '2'.")
        continue







