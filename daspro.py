menu_makanan = ["nasi goreng","mie goreng","ayam geprek"]
menu_minuman = ["es teh", "air mineral", "jus alpukat", "susu"]
pesanan = input("masukan nama makanan yang diinginkan: ")

if pesanan in menu_makanan or pesanan in menu_minuman:
    print("menu tersedia")

else:
    print("menu tidak tersedia")
