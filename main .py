import math

a = float(input("Adja meg a háromszög egyik oldalát: "))
b = float(input("Adja meg a háromszög egyik oldalát: "))
c = float(input("Adja meg a háromszög egyik oldalát: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("A háromszög létezhet!")
else:
    print("A háromszög nem jöhet létre!")

a = float(input("A téglalap egyik oldala: "))
b = float(input("A téglalap másik oldala: "))

print(f"A téglalap területe: {round(a*b, 2)} cm^2")
print(f"A téglalap kerülete: {round(2*(a+b), 2)} cm")


sugar = float(input("A kör sugara: "))

terulet = (sugar ** 2)*math.pi

print("A kör területe: ", round(terulet, 2))