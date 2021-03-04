print("Ingrese su peso en Kg")
peso=float(input())
print("Ingrese su estatura en centimetros")
estatura=float(input())
a=estatura/100
imc=(peso)/(a*a)
imc= round(imc,2)
print("Su índice de masa corporal es: ", imc)