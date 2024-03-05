import random

print('''
================================
TIKUS BERSEMBUNYI DILOBANG MANA?
================================
           [] [] [] []
================================
''')

tebakan = random.randint(1,4)
pilihan = int(input("Lubang :"))

if tebakan == pilihan :
    print(''' 
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
    print('''
================================
YAHHH KAMU SALAH LUBANG
================================
    ''')


