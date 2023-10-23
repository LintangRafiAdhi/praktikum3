def hitung_luas(jari_jari):
    return (22/7) * jari_jari**2

def hitung_keliling(jari_jari):
    return 2 * (22/7) * jari_jari

# Input jari-jari dari pengguna
jari_jari = float(input("Masukkan jari-jari lingkaran: "))

# Hitung luas dan keliling
luas = hitung_luas(jari_jari)
keliling = hitung_keliling(jari_jari)

# Tampilkan hasil
print(f"Luas lingkaran: {luas}")
print(f"Keliling lingkaran: {keliling}")
