import  math as mt
def bisection():


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


    f_start = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, start)
    f_stop = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, stop)

    i = 0


    if f_start*f_stop <= 0:
        print "aralikta kok vardir"

        while (abs(f_start-f_stop) > eps) and (i < 1000):
            mid = (start + stop) / 2
            f_mid = f_x(pol_terimler, pol_num, ln_terimler, ln_num, trig_terimler, trig_num, mid)

            if f_mid * f_stop < 0:
                start = mid
                f_start = f_mid
            elif f_mid * f_start < 0:
                stop = mid
                f_stop = f_mid
            else:
                start = stop = mid
                f_start = f_stop = f_mid
            i = i + 1

        print "returning value = ", mid
        return mid



    else:
        print "aralikta kok bulunmuyor."
        pass




#-------------------

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

#_______________________
bisection()
