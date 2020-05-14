import math as mt

def simple_iteration():


    print "polinom ifadenin terim sayisini giriniz"
    pol_num = int(input())

    print " fonksiyonun logritmik terim sayisini giriniz"
    ln_num = int(input())

    print "trigonomoterik terim sayisini giriniz"
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
        print "logaritmik fonksiyonun icindeki  katsayisini giriniz"
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
        print "trigonometrik fonksiyonun icindeki  katsayisini giriniz"
        kuvvet = float(input())
        ic.append(kuvvet)
        trig_terimler.append(ic)

    eps = float(input("hata miktarini giriniz\n"))
    x_i = float(input("baslangic degerini giriniz\n"))
    x_next = f_x_plus_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i)
    g_prime = f_prime_x_plus_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i)

    if abs(g_prime)<1:

        iterator = 0
        while (abs((x_next-x_i)/x_next)*100 > eps) and iterator<1000:
            x_i = x_next
            x_next = f_x_plus_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i)
            iterator+=1

        print x_i
        return x_i

    else:
        print abs(g_prime)
        print "koke yakinsamiyor"


def f_x_plus_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, value):

    y = 0

    for i in range(pol_num):

        y += pol_terimler[i][0]*pow(value,pol_terimler[i][1])

    for i in range(ln_num):
        print "in fx polinom",ln_terimler[i][0],"*ln",ln_terimler[i][1],"*",value
        y += ln_terimler[i][0]*mt.log(ln_terimler[i][1]*value)
        print "i degeri = ",i


    for i in range(trig_num):
        temp=0

        if trig_terimler[i][1] == "sin":
            temp = trig_terimler[i][0]*mt.sin(trig_terimler[i][2] * value * mt.pi/180)

        elif trig_terimler[i][1] == "cos":
            temp = trig_terimler[i][0] * mt.cos(trig_terimler[i][2] * value * mt.pi/180)

        elif trig_terimler[i][1] == "tan":
            temp = trig_terimler[i][0] * mt.tan(trig_terimler[i][2] * value * mt.pi/180)

        else:
            temp = trig_terimler[i][0] * mt.cot(trig_terimler[i][2] * value * mt.pi/180)

        y += temp

    return y+value   # +x value



def f_prime_x_plus_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, value):
    print "#_________inside f_prime__________#"

    y = 0
    y += 1   #    x' = 1

    for i in range(pol_num):
        y += (pol_terimler[i][0] * pol_terimler[i][1]) * pow(value, pol_terimler[i][1]-1)

    for i in range(ln_num):
        temp = 0
        temp += ln_terimler[i][0]*ln_terimler[i][1]/value
        # print "temp = ", temp, " katsayi = ", ln_terimler[i][1], "payda = ", value
        y += temp

        # print "i = ",i
        # y += ln_terimler[i][0] * mt.log(ln_terimler[i][1] * value)

    for i in range(trig_num):
        temp = 0

        if trig_terimler[i][1] == "sin":
            temp = trig_terimler[i][2] * trig_terimler[i][0] * mt.cos(trig_terimler[i][2] * value * mt.pi/180)

        elif trig_terimler[i][1] == "cos":
            temp = -trig_terimler[i][2] * trig_terimler[i][0] * mt.sin(trig_terimler[i][2] * value * mt.pi/180)

        elif trig_terimler[i][1] == "tan":
            # temp = trig_terimler[i][2] * trig_terimler[i][0] * mt.tan(trig_terimler[i][2] * value)
            temp = trig_terimler[i][2] / pow(mt.cos(trig_terimler[i][2] * value * mt.pi/180),2)

        else:
            # temp = trig_terimler[i][0] * mt.cot(trig_terimler[i][2] * value)
            temp = -trig_terimler[i][2] / pow(mt.sin(trig_terimler[i][2] * value * mt.pi/180), 2)


        y += temp

    # print "temp = ", temp
    print "#_________exit from f_prime__________#"
    return y



simple_iteration()
