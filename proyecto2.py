N = int(input("ingrese la cantidad maxima de contenedores que se pueden apilar: "))
M = int(input("ingrese la cantidad maxima de pilas que se pueden hacer: "))
print()

N+=1
contenedores = 0

matriz = []

for i in range(N):
    matriz.append([])
    for j in range (M):
        matriz[i].append(None) 

for i in range(N):
    for j in range (M):
        print("[", matriz[i][j], "]", end=" ")
    print()
print()

menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

while menu !=4:
    if menu == 1:
        if contenedores == 0:
            print()
            print("no hay contenedores en el puerto")  
            print()
            menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
        else:
            numerocontenedora=int(input("Ingrese numero del contenedor a ubicar:"))
            empresa = input("Ingrese empresa:")
            contenedor = numerocontenedora, empresa
            for i in range(N):
                for j in range (M):
                        if contenedor == matriz [i][j]:
                            print("se encuentra fila", j+1, "altura", N-i)
                            print()
                            
                            for i in range(N):
                                for j in range (M):
                                    print("[", matriz[i][j], "]", end=" ")
                                print()
            continuar = True
            consulta = input("¿desea seguir?(y/n): ")
            while continuar:
                    if consulta == "y" or consulta == "Y":
                        numerocontenedora=int(input("Ingrese numero del contenedor a ubicar:"))
                        empresa = input("Ing-rese empresa:")
                    
                        contenedor = numerocontenedora, empresa
                        for i in range(N):
                            for j in range (M):
                                if contenedor == matriz [i][j]:
                                    print("se encuentra fila", j+1, "altura", N-i)
                                print()
                                
                                for i in range(N):
                                    for j in range (M):
                                        print("[", matriz[i][j], "]", end=" ")
                                    print()
                        consulta = input("¿desea seguir?(y/n): ")
                    else:
                        continuar = False
                        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:
        h = ((N-1)*M)-(N-2)
        if h == contenedores:
            print("ya no se puede apilar mas contenedores, el puerto esta lleno") 
            menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
       
        else:
            x = 1
            y = 1
            numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
            empresa = input("Ingrese empresa:")
            
            for i in range(N):
                # N controla la altura
                for j in range (M):
                    # M controla la fila
                    matriz[N-y][M-x] = numerocontenedora, empresa
            y +=1
            if y == N:
                y = 1
            if y == 1:
                x +=1
            contenedores += 1

            for i in range(N):
                for j in range (M):
                    print("[", matriz[i][j], "]", end=" ")
                print()
            
            continuar = True
            consulta = input("¿desea seguir?(y/n): ")
            while continuar:

                if consulta == "y" or consulta == "Y":
                    h = (N-1)*M
                    h -=(N-2)
                    if h == contenedores:
                        print("ya no se puede apilar mas contenedores, el puerto esta lleno") 
                        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
                    else:
                        numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
                        empresa = input("Ingrese empresa:")
                        for i in range(N):
                        # N controla la altura
                            for j in range (M):
                                # M controla la fila
                                matriz[N-y][M-x] = numerocontenedora, empresa
                        y +=1
                        if y == N:
                            y = 1
                        if y == 1:
                            x +=1
                        contenedores += 1

                        for i in range(N):
                            for j in range (M):
                                print("[", matriz[i][j], "]", end=" ")
                            print()
                        consulta = input("¿desea seguir?(y/n): ")
                else:
                    continuar = False
                    menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 3:
        if contenedores == 0:
            print()
            print("no hay contenedores en el puerto")  
            print()
            menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))
        else:
            numerocontenedora=int(input("Ingrese numero del contenedor a retirar:"))
            empresa = input("Ingrese empresa:")
            contenedor = numerocontenedora, empresa

            for i in range(N):
                for j in range (M):
                    if contenedor == matriz[i][j]:

                        if matriz[i-1][j] == None:
                            
                            terminar = True
                            mov1 = 0
                            mov2 = 0

                            while terminar:
                                temp = matriz [i-mov1][j]
                                matriz[i-mov1][j] = temp

                                matriz [i-mov1][j] = None
                                mov1 +=1
                                matriz[i-mov1][j] = temp
                                
                                for i in range(N):
                                    for j in range (M):
                                        print("[", matriz[i][j], "]", end=" ")
                                    print()
                                print()
                                
                                if i-mov1 <= 0:
                                    matriz [i-mov1][j] = None
                                    terminar = False
                                    print("el contenedor se ha retirado")
                                    contenedores -=1
                                    y -=1

                        if matriz[i-1][j] != None:
                             
                            terminar = True
                            while terminar:
                                print()
