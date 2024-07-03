# Data siswa yang terdiri dari nama, umur, dan nilai dalam berbagai mata pelajaran
# Menggunakan List untuk menyimpan beberapa siswa
siswa_list = [
    {"nama": "Amfa", "umur": 17, "nilai": {"matematika": 85, "bahasa": 90, "sains": 92}},
    {"nama": "Silvy", "umur": 18, "nilai": {"matematika": 90, "bahasa": 88, "sains": 85}},
    {"nama": "Dila", "umur": 18, "nilai": {"matematika": 75, "bahasa": 95, "sains": 80}},
]

# Menggunakan Tuple untuk menyimpan informasi kelas
kelas_tuple = ("11A", "11B", "11C")

# Menggunakan Set untuk menyimpan ekstrakurikuler yang diikuti siswa
ekstrakurikuler_set = {"badminton", "musik", "teater"}

# Menggunakan Dictionary untuk menyimpan nilai rata-rata setiap siswa
nilai_rata_rata_dict = {}

# Menghitung nilai rata-rata setiap siswa
for siswa in siswa_list:
    nama = siswa["nama"]
    nilai = siswa["nilai"]
    rata_rata = sum(nilai.values()) / len(nilai)
    nilai_rata_rata_dict[nama] = rata_rata

# Menampilkan informasi siswa
print("=== Informasi Siswa ===")
for siswa in siswa_list:
    print(f"Nama: {siswa['nama']}, Umur: {siswa['umur']}, Nilai: {siswa['nilai']}")

# Menampilkan informasi kelas
print("\n=== Informasi Kelas ===")
print("Kelas yang tersedia:", kelas_tuple)

# Menampilkan informasi ekstrakurikuler
print("\n=== Informasi Ekstrakurikuler ===")
print("Ekstrakurikuler yang tersedia:", ekstrakurikuler_set)

# Menampilkan nilai rata-rata siswa
print("\n=== Nilai Rata-rata Siswa ===")
for nama, rata_rata in nilai_rata_rata_dict.items():
    print(f"Nama: {nama}, Nilai Rata-rata: {rata_rata}")

# Menambahkan siswa baru dan mengupdate informasi
siswa_baru = {"nama": "Dina", "umur": 18, "nilai": {"matematika": 88, "bahasa": 75, "sains": 85}}
siswa_list.append(siswa_baru)

# Mengupdate nilai rata-rata siswa baru
nama_baru = siswa_baru["nama"]
nilai_baru = siswa_baru["nilai"]
rata_rata_baru = sum(nilai_baru.values()) / len(nilai_baru)
nilai_rata_rata_dict[nama_baru] = rata_rata_baru

# Menampilkan informasi yang diperbarui
print("\n=== Informasi Siswa (Diperbarui) ===")
for siswa in siswa_list:
    print(f"Nama: {siswa['nama']}, Umur: {siswa['umur']}, Nilai: {siswa['nilai']}")

print("\n=== Nilai Rata-rata Siswa (Diperbarui) ===")
for nama, rata_rata in nilai_rata_rata_dict.items():
    print(f"Nama: {nama}, Nilai Rata-rata: {rata_rata}")
