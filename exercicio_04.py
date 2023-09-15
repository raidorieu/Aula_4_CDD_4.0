#contador
n=int(input("Até que número vamos contar? "))
if n<=0:
    print("Não podemos contar até 0 e nem números abaixo dele.")
for x in range(1, n+1, 1):
    print(x)
