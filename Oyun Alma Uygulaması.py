yazi = ' OYUN DÜNYASINA HOŞGELDİNİZ'
print(yazi.center(50, '*'))
while True:
    def butce_Karsilastirma(butce):
        import re
        if len(butce) > 2:
            raise Exception('Bütçe en fazla 99 TL olmalı')
        elif not re.search("[0-9]", butce):
            raise Exception('Sayı gerekli')
        elif re.search("[A-Z]", butce):
            raise Exception('Harf olmamalı')
        elif re.search("[a-z]", butce):
            raise Exception('Harf olmamalı')
        elif re.search("[_@$]", butce):
            raise Exception('Alfa numara olmamalı')
        elif re.search("\s", butce):
            raise Exception('Boşluk olmamalı')
        else:
            print(f'Bütçeniz: {butce} TL')


    butce = input('Bütçenizi Giriniz: ')
    try:
        butce_Karsilastirma(butce)
        break
    except Exception as ex:
        print(ex)


def oyunlar(butce):
    while True:

        oyun_Ad = {
            '1-) COUNTER STRİKE': 30,
            '2-) FİFA 2022': 50,
            '3-) GTA V': 40,
            '4-) ÇIKIŞ': 0
        }
        for i in oyun_Ad:
            print(i, '=>', oyun_Ad[i])
        if int(butce) > 0:
            oyun_Secimi = input('Hangi oyunu almak istersiniz? ')
            if oyun_Secimi == '1':
                butce = int(butce) - oyun_Ad['1-) COUNTER STRİKE']
                if butce < 0:
                    print('Bütçe yetersiz')
                else:
                    print(f'Kalan para: {butce} TL')
                break
            elif oyun_Secimi == '2':
                butce = int(butce) - oyun_Ad['2-) FİFA 2022']
                if butce < 0:
                    print('Bütçe yetersiz')
                else:
                    print(f'Kalan para: {butce} TL')
                break
            elif oyun_Secimi == '3':
                butce = int(butce) - oyun_Ad['3-) GTA V']
                if butce < 0:
                    print('Bütçe yetersiz')
                else:
                    print(f'Kalan para: {butce} TL')
                break
            elif oyun_Secimi == '4':
                break
            else:
                print('Yanlış işlem')
                break

        


oyunlar(int(butce))