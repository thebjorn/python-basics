# "programmering"

Vi skal nå gå bort fra å skrive kode i Python Console og i stedet skrive 
kode (program) i en fil.

# Kode kjøres i rekkefølge (sekvens)

    x = 1
    print(x)
    x = 2 
    print(x)
    x = 3
    print(x)

Lag, eller åpne filen `main.py` (programfiler må ha extension .py) og legg inn
følgende kode:

    a = {1, 2, 3, 4, 5}
    størst = max(a)
    print("største element i", a, "er", størst)
    print(f"største element i {a} er {størst}")
    
    b = {3, 4, 5, 6, 7}
    print("største element i", b, "er", max(b))
    
    print(f"største element i {a & b} er {max(a & b)}")

- [ ] verdier skrives ikke automatisk ut (slik de gjorde i Python Console), så 
      du må bruke `print` funksjonen brukes til å skrive til "terminalen"...


# seleksjon (if) (2/3)

Hvis `_A_` så `_B_`.
Hvis det er mørkt så slå på lyset.
Hvis x er større enn 5 så skriv ut x.

I python skrives det slik:

    if _A_:
        _B_
   
- [ ] legg merke til kolon
- [ ] legg merke til innrykk



    if is_dark():
        turn_light_on()
        
    if x > 5:
        print(f"{x} er større enn fem")


programmet fortsetter etter if-setningen:

    if x > 5:
        print('hello')
        print('world')
    print('goodbye')
    print('world')
        

## hvis `_A_` så `_B_` ellers så `_C_`  (if/else)

Hvis x er større enn 5 skriv "stor" ellers så skriv "liten".

    if x > 5:
        print('stor')
    else:
        print('liten')


    a = 3
    b = 4
    
    if a > b:
        print("a er større enn b")
    else:
        print("a er ikke større enn b")    


# input

`input(prompt)` er en funksjon som skriver ut `prompt` og ber brukeren om å taste inn 
en verdi:

    x = input("skriv inn verdi for x:")
    print(f"du skrev {x} som har type {type(x)}")

Hvis du kjører programmet over et par ganger, så ser du at `input(..)` funksjonen alltid
returnerer en string:
    
    skriv inn verdi for x:>? 3
    du skrev inn 3 som er av type <class 'str'>

    skriv inn verdi for x:>? 3.141
    du skrev inn 3.141 som er av type <class 'str'>

Hvis brukerinput skal brukes som int/float så må verdien konverteres først:

    x = int(input("skriv inn verdi for x:"))

    x = float(input("skriv inn verdi for x:"))

## if/elif/else

    a = int(input("skriv inn verdi for a:"))
    b = int(input("skriv inn verdi for b:"))
    
    if a > b + 10:
        print("a er mye større enn b")
    elif a > b:
        print("a er større enn b")
    elif b > a + 10:
        print("b er mye større enn a")
    elif b > a:
        print("b er større enn a")
    else:
        print("a og b er like store")    
