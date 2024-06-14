# Buat kelas Mobil
class Mobil:
  def __init__(self, merk, tahun, harga):
    self.merk = merk
    self.tahun = tahun
    self.harga = harga

# Buat kelas PenjualanMobil
class PenjualanMobil:
  def __init__(self):
    # Inisialisasi list mobil
    self.list_mobil = []
  
  # Method untuk menambah mobil ke list
  def tambah_mobil(self, mobil):
    self.list_mobil.append(mobil)
  
  # Method untuk menampilkan detail mobil yang tersedia
  def lihat_mobil(self):
    for mobil in self.list_mobil:
      print(f"Merk: {mobil.merk} | Tahun: {mobil.tahun} | Harga: {mobil.harga}")
  
  # Method untuk mencari mobil berdasarkan merk
  def cari_mobil(self, merk):
    hasil = []
    for mobil in self.list_mobil:
      if mobil.merk.lower() == merk.lower():
        hasil.append(mobil)
    return hasil

# Buat objek PenjualanMobil
penjualan = PenjualanMobil()

# Tambahkan beberapa mobil ke list
penjualan.tambah_mobil(Mobil("Toyota", 2020, 100000000))
penjualan.tambah_mobil(Mobil("Honda", 2019, 80000000))
penjualan.tambah_mobil(Mobil("Suzuki", 2018, 60000000))

# Tampilkan detail mobil yang tersedia
print("Daftar mobil yang tersedia:")
penjualan.lihat_mobil()

# Cari mobil berdasarkan merk
merk_cari = input("\nMasukkan merk mobil yang ingin dicari: ")
print(f"\nHasil pencarian mobil dengan merk {merk_cari.capitalize()}:")
hasil_cari = penjualan.cari_mobil(merk_cari)
for mobil in hasil_cari:
  print(f"Merk: {mobil.merk} | Tahun: {mobil.tahun} | Harga: {mobil.harga}")