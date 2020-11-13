# python som kalkulator

Python promptet (`>>>`) kan brukes som en kalkulator:

    >>> 1 + 2
    3
    >>> 5 - 3
    2
    >>> 5 * 5
    25
    >>> 5 ** 2
    25
    >>> 5 * 5 * 5
    125
    >>> 5 ** 3
    125
    >>> 10 ** 100
    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    >>> 2 + 3 * 4
    14
    >>> (2 + 3) * 4
    20
 
heltall (over) har å begrensninger i Python.
 
(nb: vi skriver `(2 + 3) * 4` og ikke `(2+3)*4` slik at det blir enklere for mennesker å lese).
 
Python bruker flyttall (float) for å representere reelle tall (dvs. tall i R). I mange tilfeller 
vil dette være "usynlig":
 
    >>> 1/10
    0.1
    >>> 1/10 + 0.5
    0.6
    >>> 1 / 3
    0.3333333333333333

vær obs på at enkelte flyttall ikke har en eksakt verdi. Python prøver å skjule detaljene så mye som 
mulig, men enkelte ganger vil du kunne oppdage at verdien som er lagret kun er en tilnærming
av verdien du har skrevet:

    >>> 0.1 + 0.1 + 0.1
    0.30000000000000004
 
oftest dukker slike problemer når du forsøker å sammenligne en flyttallsutregning med en verdi:
 
    >>> 0.1 + 0.1 + 0.1 == 0.3
    False
