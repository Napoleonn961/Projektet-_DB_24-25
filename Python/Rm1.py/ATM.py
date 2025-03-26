balanca = 10000

while True:
    try:
        opsionet = int(input("Zgjidh nje nga opsione e meposhtme \n------- ATM -------"
                             "\n1.Trego Balancen "
                             "\n2.Terhiq para "
                             "\n3.Depozito  "
                             "\n4.exit "))

        if opsionet == 1:
            print(f"Shuma juaj e mbetur eshte: {balanca:,}")

        elif opsionet == 2:
            terhiq = float(input("Zgjidh shumen qe deshironi te terhiqni: "))
            if terhiq > balanca:
                print("Nuk keni mjaftueshem fonde!")
            else:
                balanca -= terhiq
                print(f"Ju lutem terhiqni parat!  Shuma juaj e mbetur eshte: {balanca:,}")

        elif opsionet == 3:
            depozito = float(input("Vendos shumen qe do te depozitosh: "))
            balanca += depozito
            print(f"Shuma juaj e re eshte: {balanca:,}")

        elif opsionet == 4:
            break

        else:
            print(opsionet)

    except ValueError:
        print("Ju lutem, shenoni nje numer te vlefshem. Programi do te ndaloje.")
        break



