# "programmering"

Vi skal nå gå bort fra å skrive kode i Python Console og i stedet skrive 
kode (program) i en fil.

Lag, eller åpne filen `main.py` (programfiler må ha extension .py) og legg inn
følgende kode:

    a = {1, 2, 3, 4, 5}
    print("største element i", a, "er", max(a))
    
    b = {3, 4, 5, 6, 7}
    print("største element i", b, "er", max(b))
    
    print("største element i", a & b, "er", max(a & b))

- [ ] verdier skrives ikke automatisk ut (slik de gjorde i Python Console), så 
      du må bruke `print` funksjonen brukes til å skrive til "terminalen"...
- [ ] koden kjøres i rekkefølge... (`b = ...` må kjøre før kode som bruker `b`
      kan kjøre). (1/3)


# if/else (2/3)

- [ ] type of input
- [ ] incomplete cases


    a = input("a:")
    b = input("b:")
    
    if a > b:
        print("a er større enn b")
    else:
        print("b er større enn a")    

output (hva er feilen?)

    a: 10
    b: 2
    b er større enn a

## konverter input

    a = int(input("a:"))
    b = int(input("b:"))
    
    if a > b:
        print("a er større enn b")
    else:
        print("b er større enn a")    
        
## add missing case (a==b)        

    if a > b:
        print("a er større enn b")
    elif b < a:
        print("b er større enn a")
    else:
        print("a og b er like store")    
