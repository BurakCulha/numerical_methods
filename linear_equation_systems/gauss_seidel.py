import numpy as np
def gauss_seidel():


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

    x_sol = np.zeros((A_sat,1))
    x_next_sol = np.ones((A_sat, 1))
    x_past = np.zeros((A_sat, 1))
    # x_in = x_sol
    # print x_in

    err = float(input("tolerans degeri girin\n"))

    while not solutions_fit(x_next_sol, x_past, A_sat, err):
        print "xpast while basi = ", x_past

        for i in range(A_sat):
            sol = b_in[i][0]
            for j in range(A_sut):
                if i != j:
                    sol -= A_in[i][j]*x_sol[j][0]

            sol /= A_in[i][i]
            print "sol = ", sol
            x_sol[i][0] = sol
            # print "inner for xpast = ", x_past

        # bos = raw_input()
        x_past = x_next_sol.copy()
        x_next_sol = x_sol.copy()
        print "xnext = ", x_next_sol
        print "xpast = ", x_past

        bos = raw_input()


    print "solution matrix = ", x_sol







def solutions_fit(x_next_sol, x_sol, A_sat, err):
    value = False

    for i in range(A_sat):
        if abs((x_next_sol[i][0]-x_sol[i][0])) > err:
            print "error vec val = ", abs((x_next_sol[i][0]-x_sol[i][0]))
            value = False
            return value
    value = True
    return value

gauss_seidel()
