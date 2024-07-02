nilai_ujian = int(input("Masukkan nilai kamu: "))

if nilai_ujian >= 80:
    hasil = "A"
elif nilai_ujian >= 70:
    hasil = "B"
elif nilai_ujian >= 60:
    hasil = "C"
else:
    hasil = "D"

if hasil == "D":
    print(f"Nilai kamu {hasil}! Kamu wajib mengulang matkul.")
else:
    print(f"Nilai kamu {hasil}!")