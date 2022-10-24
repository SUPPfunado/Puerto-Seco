from re import X


N = int(input("ingrese la cantidad maxima de contenedores que se pueden apilar: "))
M = int(input("ingrese la cantidad maxima de pilas que se pueden hacer: "))
print()
contenedores = 0
matriz = []
consulta = ""
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
x = 1
z = 1
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
                    
                        for i in range(N):
                            for j in range (M):
                                if numerocontenedora == matriz[i][j] and empresa == matriz [i][j]:
                                    print("se encuentra fila", j+1, "altura", N-i)
                                    for i in range(N):
                                        for j in range (M):
                                            print("[", matriz[i][j], "]", end=" ")
                                        print()
                        consulta = input("¿desea seguir?(y/n): ")
                    else:
                        continuar = False
            
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:
        
        numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
        empresa = input("Ingrese empresa:")
        
        for i in range(N):
            # N controla la altura
            for j in range (M):
                # M controla la fila
                matriz[N-x][M-z] = numerocontenedora, empresa
        x +=1
        if x == M:
            x = 1
        if x == 1:
            z +=1
        contenedores += 1

        for i in range(N):
            for j in range (M):
                print("[", matriz[i][j], "]", end=" ")
            print()
        
        consulta = input("¿desea seguir?(y/n): ")
        continuar = True
        while continuar:
            if consulta == "y" or consulta == "Y":
                numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
                empresa = input("Ingrese empresa:")
                for i in range(N):
                    for j in range (M):
                        matriz[N-x][M-z] = numerocontenedora, empresa
                x +=1
                if x == M:
                    x = 1
                if x == 1:
                    z +=1
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
            for i in range(N):
                for j in range (M):
                    print("[", matriz[i][j], "]", end=" ")
                print()
            numerocontenedora=int(input("Ingrese numero del contenedor a retirar:"))
            empresa = input("Ingrese empresa:")
            ubicacionc= int(input("fila:"))
            ubicaciona= int(input("columna:"))
            
            if matriz[ubicacionc-1][ubicaciona] == None and numerocontenedora == matriz[ubicacionc][ubicaciona] and empresa ==matriz[ubicacionc][ubicaciona]:
                matriz[ubicacionc][ubicaciona] = None
                print("el contenedor a sido retirado")
                contenedores -= 1
                for i in range(N):
                    for j in range (M):
                        print("[", matriz[i][j], "]", end=" ")
                    print()

                consulta = input("¿desea seguir?(y/n): ")
            else:
                if matriz[ubicacionc-1][ubicaciona] != None:
                    print("hay un contenedor arriba")
                    consulta = input("¿desea seguir?(y/n): ")
                else:
                    if numerocontenedora != matriz[ubicacionc][ubicaciona] and empresa != matriz[ubicacionc][ubicaciona]:
                        print("el contenedor no se encuentra en esa ubicacion")
                        consulta = input("¿desea seguir?(y/n): ")
                    else:
                        if numerocontenedora != matriz[ubicacionc][ubicaciona]:
                            print("el numero de ese contenedor no se encuentra en esa posicion")
                            consulta = input("¿desea seguir?(y/n): ")
                        else:
                            if empresa != matriz[ubicacionc][ubicaciona]:
                                print("el contenedor de esa empresa no se encuentra en esa posicion")
                                consulta = input("¿desea seguir?(y/n): ")
            consulta = input("¿desea seguir?(y/n): ")
            while consulta == "y" or consulta == "Y":
                for i in range(N):
                    for j in range (M):
                        print("[", matriz[i][j], "]", end=" ")
                    print()

                numerocontenedora=int(input("Ingrese numero del contenedor a retirar:"))
                empresa = input("Ingrese empresa:")
                ubicacionc= int(input("fila:"))
                ubicaciona= int(input("columna:"))

                if matriz[ubicacionc-1][ubicaciona] == None and numerocontenedora == matriz[ubicacionc][ubicaciona] and empresa ==matriz[ubicacionc][ubicaciona]:
                    matriz[ubicacionc][ubicaciona] = None
                    print("el contenedor a sido retirado")
                    contenedores -= 1
                    for i in range(N):
                        for j in range (M):
                            print("[", matriz[i][j], "]", end=" ")
                        print()

                    consulta = input("¿desea seguir?(y/n): ")
                else:      
                    if matriz[ubicacionc-1][ubicaciona] != None:
                        print("hay un contenedor arriba")
                        consulta = input("¿desea seguir?(y/n): ")
                    else:
                        if numerocontenedora != matriz[ubicacionc][ubicaciona] and empresa != matriz[ubicacionc][ubicaciona]:
                            print("el contenedor no se encuentra en esa ubicacion")
                            consulta = input("¿desea seguir?(y/n): ")
                        else:
                            if numerocontenedora != matriz[ubicacionc][ubicaciona]:
                                print("el numero de ese contenedor no se encuentra en esa posicion")
                                consulta = input("¿desea seguir?(y/n): ")
                            else:
                                if empresa != matriz[ubicacionc][ubicaciona]:
                                    ("el contenedor de esa empresa no se encuentra en esa posicion")
                                    consulta = input("¿desea seguir?(y/n): ")
                consulta = input("¿desea seguir?(y/n): ")
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

