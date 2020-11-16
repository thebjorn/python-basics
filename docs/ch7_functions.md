# Funksjoner

Vi har allerede sett eksempler på en del funksjoner:

    len(range(5))
    print("hello world")
    linspace(-3, 3, 5)

Funksjoner er en måte å strukturere et program på, slik at man ikke trenger
å skrive all koden for å gjøre noe hver gang.

F.eks. be brukeren om å taste inn et tall mellom 0 og 100:

    tall = -1
    while tall < 0 or tall > 100:
        tall = int(input("tast inn et tall mellom 0 og 100:"))
        
hva gjør vi hvis vi skal be brukeren om å taste inn 3 tall mellom 0 og 100?
Enn om vi kunne skrive:

    a = tall_mellom(0, 100)        
    b = tall_mellom(0, 100)        
    c = tall_mellom(0, 100)        

vi kan legge koden vår inn i en funksjon:

    def tall_mellom(lo, hi):
        tall = lo - 1
        while tall < lo or tall > hi:
            tall = int(input(f"tast inn et tall mellom {lo} og {hi}:"))
        return tall

## turtles..

Skilpadde-grafikk har en lang historie (Logo/'67).

Vi kan skrive ut en firkant:

    from turtle import *
    
    shape('turtle')
    shapesize(2)
    bgcolor('darkblue')
    color('yellow')
    speed(4)
    
    # tegn en firkant
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    
    done()
    
det er litt mye repetisjon, la oss lage en funksjon:

    from turtle import *
    
    shape('turtle')
    shapesize(2)
    bgcolor('darkblue')
    color('yellow')
    speed(4)
    
    def firkant():
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)
        right(90)
        forward(100)

    firkant()
    done()    

kan vi skrive ut flere firkanter?

    for i in range(12):
        firkant()
        right(360 / 12)
        
kan vi skrive en kortere versjon av `firkant()`?

    def firkant():
        for i in range(4):
            right(90)
            forward(100)

enn hvis vi vil lage en større firkant?

    def firkant(size):
        for i in range(4):
            right(90)
            forward(size)

hva er sammenhengen mellom tallene 4 og 90?  Kan vi skrive en funksjon som tegner en 
femkant?

    def femkant(size):
        for i in range(5):
            right(360 / 5)
            forward(size)

Hvordan skriver vi en funksjon som kan lage en n-kant?

    def n_kant(n, size):
        for i in range(n):
            right(360 / n)
            forward(size)
            
prøv selv:

    for i in range(3, 12):
        n_kant(i, 150)
            
