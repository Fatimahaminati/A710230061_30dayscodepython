class Tiket:
    def __init__(self, jumlah_tiket):
        self.jumlah_tiket = jumlah_tiket

    def hitung_total_harga(self):
        pass 

class TiketBiasa(Tiket):
    def hitung_total_harga(self):
        harga_per_tiket = 50000
        total_harga = harga_per_tiket * self.jumlah_tiket
        return total_harga
    
class TiketVIP(Tiket):
    def hitung_total_harga(self):
        harga_per_tiket = 75000
        total_harga = harga_per_tiket * self.jumlah_tiket
        return total_harga
    
class TiketGold(Tiket):
    def hitung_total_harga(self):
        harga_per_tiket = 100000
        total_harga = harga_per_tiket * self.jumlah_tiket
        return total_harga
    
# program utama
jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold): ").lower()
jumlah_tiket = int(input("Masukkan jumlah tiket: "))

if jenis_tiket == 'biasa':
    tiket = TiketBiasa(jumlah_tiket)
elif jenis_tiket == 'vip':
    tiket = TiketVIP(jumlah_tiket)
elif jenis_tiket == 'gold':
    tiket = TiketGold(jumlah_tiket)
else:
    print("Jenis tiket tidak valid!")
    exit()

total_harga = tiket.hitung_total_harga()
print("Total Harga Tiket : Rp", total_harga)
