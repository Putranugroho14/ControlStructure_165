#Soal No 1
percentage = float(input("Masukan nilai: ")) 
if percentage >= 90:
    print ("Excellent performance")
elif percentage >= 80:
    print ("Very Good performance")
elif percentage >= 70:
    print ("Good performance")
elif percentage >= 60:
    print ("Average performance")
else:
    print ("Poor performance")



#Soal No 2
num1 = float(input("Masukan angka pertama: "))
num2 = float(input("Masukan angka kedua: "))
num3 = float(input("Masukan angka ketiga: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("angka yang terbesar adalah:", largest)

#Soal No 3
n = int(input("Masukan angka: "))

a, b = 0, 1
print("Deret fibonacci hingga", n, ":")

while a <= n:
    print(a, end=" ")
    a, b = b, a + b

print()


#Soal No 4
n = int(input("Masukkan sebuah angka: ")) #menginput nilai n

print("Angka ganjil hingga", n, ":") #mencetak angka ganjil
for angka in range(1, n + 1):  # Loop dari 1 hingga n
    if angka % 2 == 1:  # Memeriksa jika num adalah ganjil
        print(angka)  # Mencetak angka ganjil

print()

#Soal No 5
n = int(input("Masukkan nilai n: "))  # Meminta pengguna untuk memasukkan nilai n

for a in range(1, n + 1):  # Loop dari 1 hingga n
    for b in range(a):  # Loop untuk mencetak angka a sebanyak a kali
        print(a, end=" ")  # Mencetak angka a
    print()  # Menampilkan output
