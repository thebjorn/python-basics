# while-loops "gjenta så lenge som ... er sant"

En while-loop kjører en blokk med kode så lenge en test er sann

    while test:
        kode

F.eks. skriv ut tallene som er mindre enn 5:

    n = 0
    while n < 5:
        print(n)
        n = n + 1

skriv ut tallene fra 5 til 0:

    n = 5
    while n >= 0:
        print(n)
        n -= 1


# for-loops 

En for-loop gjentar en blokk med kode for hvert element i en liste

    for n in [0, 1, 2, 3]:
        print(n)

her er det mye vanskeligere å komme inn i en uendelig-loop. 

    words = ['mange', 'små', 'ord']
    
    for word in words:
        print(word)

for-loops og `range` funkjsonen passer godt sammen, f.eks. skriv ut alle tall 
som er mindre enn 5:

    for i in range(5):
        print(i)

en funksjon fra matplotlib/pylab som er nyttig når man skal lage grafer
er `linspace(fra, til, antall)` som returnerer en liste med antall 
verdier, jevnt fordelt mellom `fra` og `til`:

    from pylab import *
    for n in linspace(-3, 3, 5):
        print(n)

nb: I mange tilfeller jobber matte og plotte-bibliotekene med hele vektorer
(array) i stedet for å loope over lister.

F.eks. for å finne lage en graf av funkjsonen `y = x ** 2`, så kunne vi gjøre:

    from pylab import *
    x = linspace(-3, 3, 5)
    y = []
    for xval in x:
        y.append(xval ** 2)
    plot(x, y)
    show()

men dette kan gjøres enklere ved:
        
    from pylab import *
    x = linspace(-3, 3, 30)
    y = x**2
    plot(x, y)
    show()
