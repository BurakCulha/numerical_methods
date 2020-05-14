import numpy as np

def det(matris, default_mul = 1):
    '''0. satir ile laplace acilimi'''
    boyut = len(matris)
    if boyut == 1:
        return (default_mul * matris[0][0])
    else:
        sign = -1
        total = 0
        for i in range(boyut):
            m = []
            for j in range(1, boyut):
                buff = []
                for k in range(boyut):
                    if k != i:
                        buff.append(matris[j][k])
                m.append(buff)
            sign *= -1
            total += default_mul * det(m, sign * matris[0][i])
        return total


def Cramer(matris, boyut):
    n = boyut
    print n," = len of matris"
    # Augmented = matris
    # print "deneme matrisi", deneme

    deAugmented = np.empty((n, n))
    for i in range(n):
        for j in range(n):
            deAugmented[i,j] = matris[i,j]
    deAugmented_Det = det(deAugmented)
    cozum_matrisi = np.empty((n,1))

    if deAugmented_Det != 0:
        for k in range(n):
            hesap_matrisi = np.empty((n,n))
            for i in range(n):
                for j in range(n):
                    if j == k:
                        hesap_matrisi[i, j] = matris[i, n]
                    else:
                        hesap_matrisi[i, j] = matris[i, j]
            #     print 'i = ',i,'  j = ',j
            #     print 'hm[i,j] =', hesap_matrisi[i, j] , '   matris[i,j] = ', matris[i,j]
                cozum_matrisi[k,0] = det(hesap_matrisi) / deAugmented_Det
            print 'hesap_matrisi\n', hesap_matrisi
        print "cozum soyledir = \n",cozum_matrisi
        print "son"

    else:
        print "cozum bulunmamaktadir"

def take_input():
    print "bilinmeyen sayisini giriniz"
    n = int(input())
    A_in = np.empty((n, n))
    b_in = np.empty((n,1))
    augmented = np.empty((n,n+1))
    print 'A matrisinin elemanlarini giriniz'

    for i in range(n):
        for j in range(n):
            print "A matirisin ", i + 1, ". satirinda ve ", j + 1, ". sutunundaki elemani girin"
            A_in[i, j] = float(input())
            augmented[i, j] = A_in[i, j]

    print "b matrisini doldurunuz"

    for i in range(n):
        print "b matirisin ", i + 1, ". elemani girin"
        b_in[i,0] = float(input())
        augmented[i, n] = b_in[i, 0]

    print "girilen matris soyledir"
    print augmented
    boyut = n
    Cramer(augmented, boyut)


take_input()
