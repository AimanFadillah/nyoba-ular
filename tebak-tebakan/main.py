import random

lobang_kosong = ["[]"] * 4

print(f'''
================================
TIKUS BERSEMBUNYI DILOBANG MANA?
================================
        {"".join(lobang_kosong)}
================================
''')

tebakan = random.randint(1,4)
lobang = lobang_kosong.copy()
lobang[tebakan - 1] = "[$_$]"
pilihan = int(input("Lubang :"))

if tebakan == pilihan :
    print(f''' 
================================
        {"".join(lobang)}
================================
BERIKAN DIA HUKUMAN MATI
================================
    ''')
elif pilihan > 4 or pilihan < 1:
    print(''' 
================================
ADUUH LUBANG YANG MANA
================================
    ''')
else :
    print(f'''
================================
        {"".join(lobang)}
================================
YAHHH KAMU SALAH LUBANG
================================
    ''')
