import matplotlib.pyplot as plt

#Save secuency to .txt
def saveToTxt(data):
    f = open('values.txt','w')
    f.write(data)
    f.close()

def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))

#Generate histogram
def drawHistogram(values):
    plt.hist(values, bins=10, color='orange', ec='black')
    plt.title('Histograma LGC by Andrus')
    plt.xticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
    plt.show()

#Generate pseudo random secuency
# Xi = (a * Xi+1 + c) mod m | a, c y Xo < m
def pseudoRandomSecuency(a, seed, b, m, n, period):

    x = seed
    values= []

    for i in range(n):
        x = (a*x + b) % m
        zeroToOneRange = x/m
        values.append(truncate(zeroToOneRange, period))
        saveToTxt(str(values))

    drawHistogram(values)


a  = int(input('Ingresa el valor de A: '))
x  = int(input('Ingresa el valor de Xo: '))
b  = int(input('Ingresa el valor de B: '))
m  = int(input('Ingresa el valor de M: '))
n  = int(input('Ingresa la cantidad de números a generar: '))
p  = int(input('Ingresa el periodo: '))

pseudoRandomSecuency(a, x, b, m, n, p)