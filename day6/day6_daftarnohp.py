#memasukkan nama dan no handphone teman user
kontak = {}
for i in range(1, 6):
    nama = input('Maukkan nama teman {}: '.format(i))
    no_hp = input('Masukkan no HP teman {}: '.format(i))
    kontak[nama] = no_hp

#beri judul
judul = 'Phone Book'

#menampilkan hasil
print()
print(judul.center(50))
print()
for no, nama in enumerate(kontak, start=1):
    print('{}. [{}] = [{}]'.format(no, nama, kontak[nama]))