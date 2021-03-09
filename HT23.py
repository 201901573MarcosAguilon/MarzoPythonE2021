print("Ingrese el número a comprobar")
n=int(input())
x=2
cont=4
if n==1:
    print("Ha ingresado la unidad")
if n== 0:
    print("No se puede determinar si es primo o sino lo es")
if n==2:
     print("El número ingresado es primo")
elif n!=2: 
     while x<n :
        if n%x==0:
             cont=0
             break
        elif n%x!=0:
            cont=1
        x=x+1
                                 
if cont==1:
    print("Es un número primo")
elif cont==0:
    print("No es un número primo")



           



