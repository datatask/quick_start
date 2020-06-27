import sys

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

nb_terms=int(sys.argv[1])

for i in range(1,nb_terms+1):
    print("Terme {} de la suite de fibonacci : {}".format(i,fibonacci(i)))