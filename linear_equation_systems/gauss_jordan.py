import numpy as np

def gauss_jordan():
    print "lineer denklem sistemini cozmeye yarar\n"
    print " sistem  [A] * {x} = {b} seklindedir"
    print " [A] matrisi kare olmak zorundadir"
    A_sat = int(input("A matrisinin satir sayisini girin\n"))
    A_sut = int(input("A matrisinin sutun sayisini girin\n"))
    A_in = np.empty((A_sat, A_sut))
    b_in = np.empty((A_sat, 1))

    x_in = np.empty((A_sat, 1))

    # augmented = np.empty((A_sat,A_sut+1))

    for i in range(A_sat):
        for j in range(A_sut):
            print "A matirisin ", i + 1, ". satirinda ve ", j + 1, ". sutunundaki elemani girin"
            # print "\n"
            A_in[i, j] = float(input())
            # augmented[i,j] = A_in[i,j]
            while i == j and A_in[i, j] == 0:
                A_in[i, j] = float(input("0 harici eleman giriniz\n"))
                # augmented[i, j] = A_in[i, j]

    print A_in
    print "-------------------"

    print "b matrisini doldurunuz\n"

    for i in range(A_sat):
        print "\nb matirisin ", i + 1, ". elemani girin"
        b_in[i, 0] = float(input())
        # augmented[i,A_sut] = b_in[i,0]

    print b_in
    print "-------------------"

    # forward elimination

    for k in range(0, A_sut):
        pivot = A_in[k,k]
        for t in range(k,A_sut):
            A_in[k,t]/=pivot
        b_in[k,0] /= pivot

        print k,"th A = "
        print A_in
        print "and b"
        print b_in

        for i in range(0, A_sut):
            if i!=k:
                carpan = A_in[i, k] / A_in[k, k]
                for j in range(0, A_sut):
                    A_in[i, j] = A_in[i, j] - carpan * A_in[k, j]
                b_in[i, 0] -= carpan * b_in[k, 0]

    print "identity = A"
    print A_in

    print "solution B"
    print b_in


    for i in range(0,A_sat):
        x_in[i,0] = b_in[i, 0]


    print "x"
    print x_in

    # x = np.linalg.solve(A_in,b_in)
    # print "solution = ",x

    return x_in


gauss_jordan()
