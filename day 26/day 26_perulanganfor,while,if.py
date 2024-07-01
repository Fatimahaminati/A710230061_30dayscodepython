# Fungsi untuk memeriksa apakah sebuah angka adalah bilangan prima
def is_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Fungsi untuk mengumpulkan bilangan prima dalam rentang tertentu
def kumpulkan_prima(start, end):
    bilangan_prima = []
    for num in range(start, end + 1):
        if is_prima(num):
            bilangan_prima.append(num)
    return bilangan_prima

# Menggunakan perulangan while untuk meminta input pengguna sampai input valid
while True:
    try:
        mulai = int(input("Masukkan angka awal: "))
        akhir = int(input("Masukkan angka akhir: "))
        if mulai >= akhir:
            print("Angka awal harus lebih kecil dari angka akhir. Coba lagi.")
            continue
        break
    except ValueError:
        print("Masukkan angka yang valid. Coba lagi.")

# Menggunakan perulangan for untuk mencetak bilangan prima dalam rentang yang ditentukan
bilangan_prima = kumpulkan_prima(mulai, akhir)
print("Bilangan prima antara", mulai, "dan", akhir, "adalah:")
for prima in bilangan_prima:
    print(prima)

# Menggunakan perulangan while untuk menghitung jumlah bilangan prima
total_prima = 0
index = 0
while index < len(bilangan_prima):
    total_prima += 1
    index += 1

print("Jumlah bilangan prima:", total_prima)
