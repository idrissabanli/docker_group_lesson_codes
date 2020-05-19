product_name = input("Mehsulun adini daxil edin: ")
price = input("Mehsulun qiymetini daxil edin: ")
weigth = input("Mehsulun cekisini daxil edin: ")
discount_persent = input("Endirim %-ini daxil edin: ")

price = float(price)
weigth = float(weigth)
discount_persent = int(discount_persent)

# print(type(price), type(weigth), type(discount_persent))

summary = price * weigth * (100-discount_persent)/100

print(product_name, " ucun ", summary, " manat demelisiniz")