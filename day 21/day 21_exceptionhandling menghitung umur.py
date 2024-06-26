def convert_to_int(string):
    try:
        result = int(string)
        return  result
    except ValueError:
        raise ValueError("Input harus berupa angka!")

try:
    umur = input('Masukkan umur kamu: ')
    umur_dalam_tahun = convert_to_int(umur)
    umur_5_tahun_lagi = umur_dalam_tahun + 5
    print(f"Umur kamu 5 tahun lagi adalah {umur_5_tahun_lagi}")
except ValueError as e:
    print(e)