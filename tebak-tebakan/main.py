import random
from pesan import pesan

lobang_kosong = ["[]"] * 4

pesan("TIKUS BERSEMBUNYI DILOBANG MANA?")
print(f'''{"".join(lobang_kosong)}
================================
''')

tebakan = random.randint(1,4)
lobang = lobang_kosong.copy()
lobang[tebakan - 1] = "[$_$]"
pilihan = int(input("Lubang :"))

if tebakan == pilihan :
    print(f''' 
================================
{"  ".join(lobang)}
    ''')
    pesan("BERIKAN DIA HUKUMAN MATI")
elif pilihan > 4 or pilihan < 1:
    pesan("ADUHH LUBANG YANG MANA")
else :
    print(f'''
================================
    {"  ".join(lobang)}
    ''')
    pesan("YAHH KAMU SALAH LOBANG")
