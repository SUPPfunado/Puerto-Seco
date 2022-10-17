N = int(input("ingrese la cantidad maxima de contenedores que se pueden apilar: "))
M = int(input("ingrese la cantidad maxima de pilas que se pueden hacer: "))
print()

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

while menu !=4:
    if menu == 1:
        numerocontenedora=int(input("Ingrese numero del contenedor a ubicar:"))
        empresa = input("Ingrese empresa:")
        contenedor = numerocontenedora, empresa
        for i in range(N):
            for j in range (M):
                    if contenedor == matriz [i][j]:
                        print("se encuentra en la posicion", i, j)
                        for i in range(N):
                            for j in range (M):
                                print("[", matriz[i][j], "]", end=" ")
        print()
        consulta = input("¿desea seguir?(y/n): ")
        while consulta == "y" or consulta == "Y":
            numerocontenedora=int(input("Ingrese numero del contenedor a ubicar:"))
            empresa = input("Ingrese empresa:")
         
            for i in range(N):
                for j in range (M):
                    if numerocontenedora == matriz[i][j] and empresa == matriz [i][j]:
                        print("se encuentra en la posicion", i, j)
                        for i in range(N):
                            for j in range (M):
                                print("[", matriz[i][j], "]", end=" ")
                
        consulta = input("¿desea seguir?(y/n): ")
            
        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 2:
        
        numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
        empresa = input("Ingrese empresa:")
        ubicacionc= int(input("fila:"))
        ubicaciona= int(input("columna:"))

        matriz[ubicacionc][ubicaciona] = numerocontenedora, empresa

       
        for i in range(N):
            for j in range (M):
                print("[", matriz[i][j], "]", end=" ")
            print()
        
        consulta = input("¿desea seguir?(y/n): ")
        while consulta == "y" or consulta == "Y":
            numerocontenedora=int(input("Ingrese numero del contenedor a añadir:"))
            empresa = input("Ingrese empresa:")
            ubicacionc= int(input("fila:"))
            ubicaciona= int(input("columna:"))

            matriz[ubicacionc][ubicaciona] = numerocontenedora, empresa

        
            for i in range(N):
                for j in range (M):
                    print("[", matriz[i][j], "]", end=" ")
                print()
            consulta = input("¿desea seguir?(y/n): ")

        menu = int(input("1 para ubicar un contenedor \n2 para ingresar un contenedor \n3 para retirar un contenedor  \n4 para terminar la jornada \neleccion:"))

    if menu == 3:
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
