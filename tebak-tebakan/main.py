import random

lobang_kosong = ["[]"] * 4

print(lobang_kosong.join())
exit()

print(f'''
================================
TIKUS BERSEMBUNYI DILOBANG MANA?
================================
    {lobang_kosong}
================================
''')

tebakan = random.randint(1,4)
lobang = lobang_kosong.copy()
lobang[tebakan - 1] = "[$_$]"
pilihan = int(input("Lubang :"))

if tebakan == pilihan :
    print(f''' 
================================
  {lobang}
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
  {lobang}
================================
YAHHH KAMU SALAH LUBANG
================================
    ''')
