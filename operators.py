

# penjumlahan
def penjumlahan():
    angka1 = int(input("masukan angka: "))
    angka2 = int(input("masukan angka: "))
    hasil = angka1 + angka2
    print(f"hasil nya adalah: {hasil}")
    return hasil

# pengurangan
def pengurangan(angka1, angka2):
    hasil = angka1 - angka2
    print(hasil)
    return hasil

# perkalian
def perkalian(a,b):
    return print(a * b) 

# pembagian
def pembagian(x,y):
    x = float(x)
    y = float(y)
    hasil = x / y
    print(hasil)
    return hasil

# pembagian sisa atau modulus
def modulus():
    a = int(input("masukan angka: "))
    hasil = a % 2
    if hasil == 1:
        print("bilangan ganjil")
    else:
        print("bilangan genap")

