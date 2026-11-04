menu = ["nasi goreng", "mie goreng","ayam geprek"]
pesanan = input("masukan nama makanan yang diinginkan: ")

if pesanan in menu:
    print("menu tersedia")
else:
    print("menu tidak tersedia")
