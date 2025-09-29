a = float(input("Adja meg a háromszög egyik oldalát: "))
b = float(input("Adja meg a háromszög egyik oldalát: "))
c = float(input("Adja meg a háromszög egyik oldalát: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("A háromszög létezhet!")
else:
    print("A háromszög nem jöhet létre!")