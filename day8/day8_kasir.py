#memita user memasukkan inputan belanja
jumlah_baju = int(input('Maukkan jumlah baju: '))
harga_baju = int(input('Masukkan harga baju: '))
total_harga = jumlah_baju * harga_baju

file = open('invoice.txt', 'w')
file.write('==========RINCIAN==========\n')
file.write(f'Jumlah Baju: {jumlah_baju}\n')
file.write(f'Harga Baju: Rp.{harga_baju}\n')
file.write('===========================\n')
file.write(f'TOTAL: Rp.{total_harga}\n')
file.close()

print()
print('==========RINCIAN=========')
print(f'jumlah Baju: {jumlah_baju}')
print(f'harga Baju: Rp.{harga_baju}')
print('==========================')
print(f'TOTAL: Rp.{total_harga}')
