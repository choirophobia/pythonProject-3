# from main import mainMenu
def interface_kubus():
    while True:
        s = float(input("Masukkan sisi : "))
        if s > 0:
            print(f"Luas kubus adalah : {calculate_kubus(s)}")
            break
        else:
            print("input yang dimasukkan tidak sesuai")
        ValueError("Masukan input dalam angka")


def interface_balok():
    while True:
        p = float(input("Masukkan panjang balok : "))
        l = float(input("Masukkan lebar balok : "))
        t = float(input("Masukkan tinggi balok : "))

        if p > 0 and l > 0 and t > 0:
            print(f"Luas balok adalah {calculate_balok(p, l, t)}")
            break
        else:
            print("input yang dimasukkan3 tidak sesuai")
        ValueError("Masukan input dalam angka")


def interface_tabung():
    while True:
        r = float(input("Masukkan Jari -jari : "))
        t = float(input("Masukkan tinggi tabung : "))

        if r > 0 and t > 0:
            print(f"Luas tabung adalah {calculate_tabung(r, t)}")
            break
        else:
            print("input yang dimasukkan tidak sesuai")
        ValueError("Masukan input dalam angka")


def interface_karucut():
    while True:
        r = float(input("Masukkan Jari -jari : "))
        t = float(input("Masukkan tinggi tabung : "))

        if r > 0 and t > 0:
            print(f"Luas kerucut adalah {calculate_kerucut(r, t)}")
            break
        else:
            print("input yang dimasukkan tidak sesuai")
        ValueError("Masukan input dalam angka")


def calculate_kubus(s):
    luas_kubus = s ** 3
    return (luas_kubus)


def calculate_balok(p, l, t):
    luas_balok = p * l * t
    return (luas_balok)


def calculate_tabung(r, t):
    v = 3.14
    luas_tabung = v * r * r * t
    return (luas_tabung)


def calculate_kerucut(r, t):
    v = 3.14
    a = 1 / 3
    luas_kerucut = a * v * r * r * t
    return (luas_kerucut)


def bangunDatar():
    pass


def operasiAritmatika():
    pass
