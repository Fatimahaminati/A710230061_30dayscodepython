# Definisikan kelas AnggotaKeluarga
class AnggotaKeluarga:
    def __init__(self, nama, tanggal_lahir, hubungan):
        self.nama = nama
        self.tanggal_lahir = tanggal_lahir
        self.hubungan = hubungan

    def __repr__(self):
        return f"{self.nama} ({self.hubungan}), Lahir: {self.tanggal_lahir}"

# Definisikan kelas KartuKeluarga
class KartuKeluarga:
    def __init__(self, nomor_kk, alamat):
        self.nomor_kk = nomor_kk
        self.alamat = alamat
        self.anggota_keluarga = []

    def tambah_anggota(self, anggota: AnggotaKeluarga):
        self.anggota_keluarga.append(anggota)

    def tampilkan_kartu(self):
        print(f"Kartu Keluarga")
        print(f"=================")
        print(f"Nomor KK   : {self.nomor_kk}")
        print(f"Alamat     : {self.alamat}")
        print(f"=================")
        print(f"Anggota Keluarga:")
        for anggota in self.anggota_keluarga:
            print(f" - {anggota}")
        print(f"=================\n")

# Membuat objek KartuKeluarga
kartu_keluarga = KartuKeluarga("1234567890", "Jl. Merdeka No. 10")

# Membuat dan menambahkan anggota keluarga
kartu_keluarga.tambah_anggota(AnggotaKeluarga("Aldino", "01-01-1970", "Kepala Keluarga"))
kartu_keluarga.tambah_anggota(AnggotaKeluarga("Reva", "02-02-1971", "Istri"))
kartu_keluarga.tambah_anggota(AnggotaKeluarga("Saka", "03-03-2000", "Anak"))
kartu_keluarga.tambah_anggota(AnggotaKeluarga("Reynay", "04-04-2004", "Anak"))

# Menampilkan kartu keluarga
kartu_keluarga.tampilkan_kartu()

# Menyimpan data kartu keluarga ke dalam dictionary
data_kartu_keluarga = {
    kartu_keluarga.nomor_kk: kartu_keluarga
}

# Fungsi untuk mencari kartu keluarga berdasarkan nomor KK
def cari_kartu_keluarga(nomor_kk):
    if nomor_kk in data_kartu_keluarga:
        kartu_keluarga = data_kartu_keluarga[nomor_kk]
        kartu_keluarga.tampilkan_kartu()
    else:
        print(f"Kartu Keluarga dengan nomor KK {nomor_kk} tidak ditemukan.\n")

# Mencari kartu keluarga
cari_kartu_keluarga("1234567890")
cari_kartu_keluarga("1111111111")  # Contoh nomor KK yang tidak ada
