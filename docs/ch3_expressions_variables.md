# variabler i Python

Variabler er navn vi setter på verdier:

    >>> pi = 3.14
    >>> radius = 2
    >>> volum = 4/3 * pi * radius ** 3 
    >>> print(volum)

for å skrive ut verdien til en variabel kan vi kalle `print(...)` funksjonen:

    >>> print(volum)
    33.49333333333333

- [ ] funksjoner _gjør_ noe

vi så tidligere eksempel på funksjoner som fant kardinaliteten ("lengden")
på et `set`: 

    >>> a = {1, 2, 3, 4, 5}
    >>> len(a)
    5

- [ ] funksjoner kan _returnere_ verdier

NB: variabler i Python er ikke det samme som variabler i matematikk.
Standardeksemplet er:

    x = x + 1

For å forstå hva som skjer her må vi vite litt om hvordan koden vår kjører.
