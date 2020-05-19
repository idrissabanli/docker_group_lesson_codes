product_name = input("Mehsulun adini daxil edin: ")
price = input("Mehsulun qiymetini daxil edin: ")
weigth = input("Mehsulun cekisini daxil edin: ")
discount_persent = input("Endirim %-ini daxil edin: ")

# and || exit

if price.isdigit():
    price = int(price)
    if weigth.isdigit():
        weigth = int(weigth)
        if discount_persent.isdigit():
            discount_persent = int(discount_persent)

            summary = price * weigth * (100-discount_persent)/100

            print(product_name, " ucun ", summary, " manat demelisiniz")
        else:
            print('endirimi reqem kimi daxil ede bilersiniz')
    else:
        print('cekini yalniz reqem daxil ede bilersiniz')
else:
    print('price-i yalniz reqem daxil ede bilersiniz')