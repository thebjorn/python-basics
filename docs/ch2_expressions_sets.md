# andre datatyper: set (mengde?)

I tillegg til heltall (int) og flyttall (float), har Python en del andre 
innebygde datatyper, f.eks. set. Et sett som inneholder tallene 
1 til og med 5:

    >>> {1, 2, 3, 4, 5}
    {1, 2, 3, 4, 5}
    
intersection (norsk? - snitt) - "hvilke elementer er med i settet på venstre _og_ (`&`) 
settet på høyre side":

    >>> {1, 2, 3, 4, 5} & {3, 4, 5, 6, 7}
    {3, 4, 5}

for å gjøre det mer oversiktlig kan vi bruke variabler:

    >>> a = {1, 2, 3, 4, 5}
    >>> b = {3, 4, 5, 6, 7}
    >>> a & b
    {3, 4, 5}

Historisk har tegnet `|` blitt brukt i mange programmeringsspråk for å indikere
_eller_, så union av to sett - "hvilke elementer som er med i `a` eller `b`" skrives:

    >>> a | b
    {1, 2, 3, 4, 5, 6, 7}

andre operasjoner på `set`:

    >>> a ^ b
    >>> 3 in a
    >>> 3 in a ^ b
    >>> a - b
    >>> len(a)
    >>> max(a)
    >>> min(b - a)

# andre datatyper: str (string)

Tekst er av typen `str` og skrives innenfor "fnutter". Alle disse er tillatt:

    >>> "hei"
    >>> 'hei'
    >>> """hei"""
    >>> '''hei'''

- [ ] multiline strings

og man kan f.eks. legge sammen to strings:

    >>> "hello-" + "world"
    hello-world

man kan spørre hvor mange bokstaver (lengden) på en string:

    >>> len("hello")
    5

og man kan sammenligne 2 strings alfabetisk:

    >>> "abbor" < "brosme"
    True

vær obs på at tallet `20` og strengen `"20"` er forskjellig!
Her sammenlignes heltallsverdiene:

    >>> 10 < 2
    False
    
Her "sorteres" strengene alfabetisk:

    >>> "10" < "2"
    True
    
`int(..)` funksjonen kan konvertere fra string til int:

    >>> "20"
    '20'
    >>> int("20")
    20
    
