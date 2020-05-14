import math as mt

def simpson():
    print "polinom ifadenin terim sayisini giriniz"
    pol_num = int(input())

    print " fonksiyonun logaritmik terim sayisini giriniz"
    ln_num = int(input())

    print "trigonometrik terim sayisini giriniz"
    trig_num = int(input())

    pol_terimler = []
    for i in range(pol_num):
        ic = []
        print "polinomun ", i + 1, ". teriminin katsayisini giriniz"
        katsayi = float(input())
        ic.append(katsayi)
        print "polinomun ", i + 1, ". teriminin kuvvetini giriniz"
        kuvvet = float(input())
        ic.append(kuvvet)
        pol_terimler.append(ic)

    ln_terimler = []
    for i in range(ln_num):
        ic = []
        print i + 1, ". e tabanindaki logaritmik fonksiyonun katsayisini giriniz"
        katsayi = float(input())
        ic.append(katsayi)
        print "logaritmik fonksiyonun icindeki degiskenin katsayisini giriniz"
        kuvvet = float(input())
        ic.append(kuvvet)
        ln_terimler.append(ic)

    trig_terimler = []
    for i in range(trig_num):
        ic = []
        print i + 1, ". trigonometrik fonksiyonun katsayisini giriniz"
        katsayi = float(input())
        ic.append(katsayi)
        print "trigonometrik fonksiyonun adini yazin"
        print "ornek = cos, ornek = sin , ornek = tan, ornek = cot"
        # tip = str(input())
        tip = raw_input()
        ic.append(tip)
        print "trigonometrik fonksiyonun icindeki degiskenin katsayisini giriniz"
        kuvvet = float(input())
        ic.append(kuvvet)
        trig_terimler.append(ic)

    baslangic = float(input("integral alinacak bolgenin baslangic degerini girin\n"))

    son = float(input("integral alinacak bolgenin son degerini girin\n"))

    parca_num = int(input(" 4k-1 parca miktarini giriniz\n"))
    while parca_num %4 != 3:
        parca_num = int(input("4 un kati -1 sayida sayida parca miktarini giriniz"))

    sonuc = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, baslangic, son, parca_num)
    print sonuc, " = bulunan deger"


def f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, baslangic, bitis, parca_num):
    height = bitis - baslangic
    step_size = height / parca_num
    start = baslangic
    stop = bitis
    sonuc = 0
    print step_size, "= step size"


    for x in range(parca_num):
        ara_toplam = 0
        ara_toplam = eval_f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, start)
        # print "ara_toplam = ", ara_toplam
        if x%3 == 0:
            ara_toplam *= 2
        else:
            ara_toplam *= 3

        sonuc += ara_toplam

        start += step_size


        print "sonuc = ", sonuc
        # start += step_size
    # sonuc *= 2

    cikar1 = eval_f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, baslangic)
    cikar2 = eval_f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, bitis)
    # print "cikar2=", cikar2

    sonuc -= (cikar1 + cikar2)
    print "bolmededn once sonuc = ",sonuc
    sonuc = sonuc * 3 * (height / parca_num) / 8
    print "bolmededn sonra sonuc = ", sonuc
    # -------------------------------------------------

    return sonuc



def eval_f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, value):
    y = 0

    for i in range(pol_num):
        # print "iter val=",i
        # print "polinomda x = ", value
        # print "polinomda degeri = ", pol_terimler[i][0] * pow(value, pol_terimler[i][1])
        # print "polinomda katsayi = ", pol_terimler[i][0]

        y += pol_terimler[i][0] * pow(value, pol_terimler[i][1])

    for i in range(ln_num):
        print "in fx polinom", ln_terimler[i][0], "*ln", ln_terimler[i][1], "*", value
        y += ln_terimler[i][0] * mt.log(ln_terimler[i][1] * value)
        # print "i degeri = ", i

    for i in range(trig_num):
        temp = 0
        # print "i degeri = ", i
        # print "y degeri = ", y
        if trig_terimler[i][1] == "sin":
            temp = trig_terimler[i][0] * mt.sin(trig_terimler[i][2] * value * mt.pi / 180)
            print "in sin temp_val = ", temp

        elif trig_terimler[i][1] == "cos":
            temp = trig_terimler[i][0] * mt.cos(trig_terimler[i][2] * value * mt.pi / 180)
            print "in cos temp_val = ", temp

        elif trig_terimler[i][1] == "tan":
            temp = trig_terimler[i][0] * mt.tan(trig_terimler[i][2] * value * mt.pi / 180)

        else:
            temp = trig_terimler[i][0] * mt.cot(trig_terimler[i][2] * value * mt.pi / 180)

        y += temp

    return y



simpson()
