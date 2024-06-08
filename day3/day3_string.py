#mengambil inputan nama depan dan nama belakang , nim, fakultas
nama_depan = input ('masukkan nama depan :')
nama_belakang = input('masukkan nama belakang :')
nim = input('masukkan nim :')
fakultas = input('masukkan nama fakultas :')

#gabungkan nama depan dan nama belakang
nama_lengkap = nama_depan + nama_belakang

#tulis jurusan dan universitas
jurusan = 'Pendidikan Teknik Informatika'
universitas = 'Universitas Muhammadiyah Surakarta'
kapital = universitas.upper()

print('nama lengkap :', nama_lengkap)
print()
print(jurusan.center(50))
print()
print('Nama :[{}]'.format(nama_lengkap))
print('NIM :[{}]'.format(nim))
print(fakultas)
print()
print(kapital.center(50))