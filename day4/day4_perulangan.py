#masukkan tahun lahir penumpang
tahun_lahir = int(input('Masukkan tahun lahir: '))
tahun_sekarang = 2024

#hitung usia penumpang
usia = tahun_sekarang - tahun_lahir

#masukkan harga tiket kereta api
harga_tiket = int(input('Masukkan harga tiket kereta api: '))

#tentukan diskon berdasarkan usia
if usia >= 0 and usia <= 4:
    diskon = 1.0 #diskon 100%
elif usia >= 5 and usia <= 11:
    diskon = 0.5 #diskon 50%
else:
    diskon = 0.0 #tidak ada diskon

#hitung harga setelah diskon
harga_setelah_diskon = harga_tiket * (1- diskon)

#tampilkan hasil
print(f'Usia penumpang: {usia} tahun')
print('Diskon:', int(diskon * 100),'%')
print('Harga tiket setelah diskon: Rp.', int(harga_setelah_diskon))
