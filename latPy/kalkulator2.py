print("Masukan angka anda")

def add(x, y):
   return x + y

angka1 = int(input("silahkan masukan angka pertama : "))
angka2 = int(input("silahkan masukan angka kedua : "))
operator= input("silahkan masukan penjumlahan:")


if operator == '+':
    print('{} + {} = ', add(angka1, angka2))
    print()

elif operator == "-":
        print('{} - {} = '.format(angka1, angka2))
        print(angka1 - angka2)

elif operator == f("*"):
        print('{} * {} = '.format(angka1, angka2))
        print(angka1 * angka2)

elif operator == f("/"):
        print('{} / {} = '.format(angka1, angka2))
        print(angka1 / angka2)
else:
        print('You have not typed a valid operator, please run the program again.')



# calculate()