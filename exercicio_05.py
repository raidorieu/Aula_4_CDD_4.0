numero=0
soma=0
numeropositivo=0
for x in range(0, 10, 1):
    negativo=int(input("Que números? "))
    if negativo<0:
        print(negativo, "é negativo")
        numero= numero + 1
        soma= soma + negativo
    else:
        numeropositivo= numeropositivo +1
print(f"a soma dos números é {soma}")
print(numero, f"números negativos")
print(numeropositivo, "numero positivos")
