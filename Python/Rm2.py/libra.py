def regjistro_liber(librat):
    titulli = input("Titulli i librit: ")
    autori = input("Autori: ")
    viti = input("Viti i publikimit: ")
    kopjet = int(input("Numri i kopjeve: "))
    librat.append({"titulli": titulli, "autori": autori, "viti": viti, "kopjet": kopjet})
    print("Libri u shtua me sukses!\n")


def shfaq_librat(librat):
    print("\nLista e librave në inventar:")
    for liber in librat:
        if liber["kopjet"] > 0:
            print(
                f"Titulli: {liber['titulli']}, Autori: {liber['autori']}, Viti: {liber['viti']}, Kopje: {liber['kopjet']}")
    print("")


def kerko_liber(librat):
    kriter = input("Kërko sipas titullit ose autorit: ").lower()
    gjetur = False
    for liber in librat:
        if liber["kopjet"] > 0 and (kriter in liber["titulli"].lower() or kriter in liber["autori"].lower()):
            print(
                f"Titulli: {liber['titulli']}, Autori: {liber['autori']}, Viti: {liber['viti']}, Kopje: {liber['kopjet']}")
            gjetur = True
    if not gjetur:
        print("Nuk u gjet asnjë libër me këtë kriter!\n")


def menu():
    librat = []
    while True:
        print("\nMenaxhimi i Inventarit të Librarisë")
        print("1. Regjistro një libër")
        print("2. Shfaq librat")
        print("3. Kërko një libër")
        print("4. Dil")
        zgjedhja = input("Zgjidh një opsion: ")

        if zgjedhja == "1":
            regjistro_liber(librat)
        elif zgjedhja == "2":
            shfaq_librat(librat)
        elif zgjedhja == "3":
            kerko_liber(librat)
        elif zgjedhja == "4":
            print("Dalje nga programi!")
            break
        else:
            print("Opsion i pavlefshëm, provo përsëri!\n")


if __name__ == "__main__":
    menu()
