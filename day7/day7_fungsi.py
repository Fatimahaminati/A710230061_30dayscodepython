def apakah_prima(angka):
    if angka > 1:
        for i in range(2, int(angka**0.5) + 1):
            if (angka % i) == 0:
                print('Bukan bilangan prima')
                break
        else:
            print('Bilangan prima')
    else:
        print('Bukan bilangan prima')

#cetak hasil
angka_input = int(input('Masukkan angka: '))
apakah_prima(angka_input)