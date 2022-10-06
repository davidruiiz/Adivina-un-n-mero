import random 

numero = random.randint(0,100)
print(numero)
i=0

intento=int(input("Introduce un número:\n"))

while True:
    while intento<0 or intento>100:
        intento=int(input("Introduce un número:\n"))

    if intento==numero:
        print("¡Ha acertado el número!")
        break
    elif intento>numero:
        print("El numero es menor")
    else:
        print("El número es mayor")

    i+=1
    intento=101

print("Se han necesitado",i,"intentos")