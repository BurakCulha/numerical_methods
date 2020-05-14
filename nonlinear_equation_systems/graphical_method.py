import math as mt

def graphical():


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
    start = float(input("araligin ilk degerini giriniz\n"))
    stop = float(input("araligin ikinci degerini giriniz\n"))
    delta = float(input("delta giriniz\n"))

    f_start = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, start)
    f_stop = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, stop)

    i = 0


    if f_start*f_stop <= 0:
        print "aralikta kok vardir"

        while (abs(f_start-f_stop) > eps) and (i < 1000):
            step = start + delta
            f_step = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, step)

            if f_step * f_stop < 0:
                start = step
                f_start = f_step
            elif f_step * f_stop > 0:
                stop = step
                f_stop = f_step
                step -= delta
                f_step = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, step)
                delta /= 4
            else:
                start = stop = step
                f_start = f_stop = f_step
            i = i + 1

        print "returning value = ", step
        return step



    else:
        print "aralikta kok bulunmuyor."
        pass


def f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, value):

    y = 0

    for i in range(pol_num):

        y += pol_terimler[i][0]*pow(value,pol_terimler[i][1])

    for i in range(ln_num):
        print "in fx polinom",ln_terimler[i][0],"*ln",ln_terimler[i][1],"*",value
        y += ln_terimler[i][0]*mt.log(ln_terimler[i][1]*value)
        print "i degeri = ",i


    for i in range(trig_num):
        temp = 0

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

graphical()
