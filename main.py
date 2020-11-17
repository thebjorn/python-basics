# ---------------------------------------------------------------------
# x = input('skriv inn verdi for x:')
# print(f"du skrev inn {x} som er av type {type(x)}")
# ---------------------------------------------------------------------

# a = {1, 2, 3, 4, 5}
# størst = max(a)
# print("største element i", a, "er", max(a))
# print(f"største element i {a} er {max(a)}")
# print(f"største element i {a} er {størst}")
#
# b = {3, 4, 5, 6, 7}
# print("største element i", b, "er", max(b))
#
# print("største element i", a & b, "er", max(a & b))

# ---------------------------------------------------------------------

# a = input("a:")
# b = input("b:")
#
# if a > b:
#     print("a er større enn b")
# else:
#     print("b er større enn a")

# ---------------------------------------------------------------------

# from pylab import *
# x = linspace(-3, 3, 5)
# y = []
# for xval in x:
#     y.append(xval ** 2)
# plot(x, y)
# show()

# ---------------------------------------------------------------------

# from pylab import *
# x = linspace(-3, 3, 30)
# y = x**2
# plot(x, y)
# show()

# ---------------------------------------------------------------------

# from pylab import *         # importerer pylab
#
# pop = zeros(21)             # definerer tom array for populasjon
# tid = linspace(0, 20, 21)   # definerer array med årstall fra 0-20
#
# pop[0] = 300                # populasjonen starter på 300, så populasjonen
# # ved år 0 er 300.
#
# for i in range(1, 21):      # løkken starter med i=1 fordi vi har pop[0]
#     # ny pop = gammel pop + vekst
#     pop[i] = pop[i-1] + 0.10 * pop[i-1] * (1 - (pop[i-1]/200))
#
# plot(tid, pop)      # plotter tid langs x-aksen og pop langs y-aksen
# show()              # husk å skrive show() for å få frem plottet

# ---------------------------------------------------------------------
# from turtle import *
#
# shape('turtle')
# shapesize(2)
# bgcolor('darkblue')
# color('yellow')
# speed(10)
#
# penup()
# left(90)
# forward(200)
# pendown()
#
# def firkant(size):
#     for i in range(4):
#         right(90)
#         forward(size)
#
# def femkant(size):
#     for i in range(5):
#         right(360 / 5)
#         forward(size)
#
# def n_kant(n, size):
#     for i in range(n):
#         right(360 / n)
#         forward(size)
#
# # firkant(200)
# # femkant(200)
#
# # for i in range(10):
# #     n_kant(45, 10)
# #     right(5)
#
# for i in range(3, 13):
#     n_kant(i, 150)
#
# # for i in range(12):
# #     firkant()
# #     right(360 / 12)
#
# done()
