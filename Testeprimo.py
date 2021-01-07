def éPrimo(x):
        fator = 2
        while x % fator != 0 and x/2 > fator:
                fator = fator + 1
        if x % fator == 0:
                return False
        else:
                return True
        
n = int(input("digite um número inteiro para ferificar se é primo: "))

while n > 0:
        if éPrimo(n):
                print(n, "é um número primo.")
        else:
                print(n, "não é um número primo.")
        n = int(input("digite um número inteiro para ferificar se é primo: "))

                
