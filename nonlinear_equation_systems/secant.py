import math as mt

def secant():


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

    x_i = float(input("kiris icin ilk degerini giriniz\n"))
    x_i_past = float(input("kiris icin ikinci degerini giriniz\n"))

    f_x_i = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i)
    f_x_i_past = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i_past)

    '''
    formula we should think f' as ( f_xpast - f_xi)/( xpast - xi )

    and we should put f' into newton raphson formula
    '''
    x_next = x_i - ((f_x_i) * (x_i_past - x_i)) / (f_x_i_past - f_x_i)
    f_x_next = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_next)

    iteration_stopper = 0
    while (abs(f_x_next - f_x_i) > eps) and iteration_stopper < 1000:
        x_i_past = x_i
        # f_x_i_past = func(a, b, c, d, e, k, j, x_i_past)
        f_x_i_past = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i_past)
        x_i = x_next
        # f_x_i = func(a, b, c, d, e, k, j, x_i)
        f_x_i = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_i)
        x_next = x_i - ((f_x_i) * (x_i_past - x_i)) / (f_x_i_past - f_x_i)
        f_x_next = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, x_next)

        iteration_stopper += 1

    print x_i
    return x_i

def f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, value):

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

    return y


secant()
