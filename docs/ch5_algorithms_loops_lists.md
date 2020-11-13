# loops

## list datatype

Kanskje den mest brukte datatypen i Python er datatypen `list`.

    >>> [1, 2, 3, 2]
    [1, 2, 3, 2]

en liste har en rekkefølge, og kan ha dupliserte verdier 
(i motsetning til `set`).

Man kan hente ut ett element fra en liste ved å bruke en indeks:

    >>> a = [1, 2, 3, 2]  
    >>> a[0]
    1
    >>> a[1]
    2
    >>> a[2]
    3
    >>> a[-1]
    2
    
Man kan også hente ut flere sammenhengende elementer (`slice`):

    >>> a[0:2]
    [1, 2]
    >>> a[2:4]
    [3, 2]
    
    >>> a[:2]
    >>> a[2:]
    >>> a[1:-1]

`list(..)` funksjonen kan konvertere til liste:

    >>> list('hello')
    ['h', 'e', 'l', 'l', 'o']
    >>> list({1, 2, 3})
    [1, 2, 3]

`range(lo, hi)` lager et halv-åpent interval (fra-og-med `lo` til-men-ikke-inkludert `hi`):

    >>> list(range(0, 5))
    [0, 1, 2, 3, 4]
    
dersom `lo == 0` kan den sløyfes:

    >>> list(range(5))
    [0, 1, 2, 3, 4]    

spesielle slice operasjoner:

    >>> a = list(range(10))
    >>> a[:]
    >>> a[::2]
    >>> a[4::2]
    >>> a[:4:2]
    >>> a[::-1]
