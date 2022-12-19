import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter
print("specifier Pf Tf F")
Pf = 100
Tf = 115
F = 100
Z1 = 0.3
Z2 = 0.3
Z3 = 0.4
T1 = 65
T2 = 90
T3 = 115
T4 = 140
T5 = 165
V1 = 0
V2 = 150
V3 = 150
V4 = 150
V5 = 150

V6 = 0
D = 50
A1 = 6.80398
B1 = 803.81
C1 = 246.99
A2 = 6.80896
B2 = 935.860
C2 = 238.730
A3 = 6.87632
B3 = 1075.780
C3 = 233.205
i=0
ps = perf_counter()
#boucle aui satisfaite la condition
while True:
    # Do some processing...
    # Update the condition...

    ##pour la composition 1 :
    ##def K1(T):
    i=i+1
    K11 = float((10 ** (A1 - B1 / (C1 + ((T1 - 32) * 5 / 9)))) / 5171.49)
    K12 = float((10 ** (A1 - B1 / (C1 + ((T2 - 32) * 5 / 9)))) / 5171.49)
    K13 = float((10 ** (A1 - B1 / (C1 + ((T3 - 32) * 5 / 9)))) / 5171.49)
    K14 = float((10 ** (A1 - B1 / (C1 + ((T4 - 32) * 5 / 9)))) / 5171.49)
    K15 = float((10 ** (A1 - B1 / (C1 + ((T5 - 32) * 5 / 9)))) / 5171.49)
    print("k11 = ", K11)
    print("k12 = ", K12)
    print("k13 = ", K13)
    print("k14 = ", K14)
    print("k15 = ", K15)
    A12 = A22 = A32 = V2 - D
    A13 = A23 = A33 = V3 - D
    A14 = A24 = A34 = V4 + F - D
    A15 = A25 = A35 = V5 + F - D
    B11 = -V2 - V1 * K11
    B12 = -V3 + D - V2 * K12
    B13 = -V4 - F + D - V3 * K13
    B14 = -V5 - F + D - V4 * K14
    B15 = -V6 - F + D - V5 * K15
    D11 = D21 = D31 = 0
    D12 = D22 = D32 = 0
    D13 = -F * Z1
    D14 = D24 = D34 = 0
    D15 = D25 = D35 = 0
    C11 = V2 * K12
    C12 = V3 * K13
    C13 = V4 * K14
    C14 = V5 * K15
    ##input systeme of equation
    a1 = np.array([[B11, C11, 0, 0, 0],
                   [A12, B12, C12, 0, 0],
                   [0, A13, B14, C13, 0],
                   [0, 0, A14, B14, C14],
                   [0, 0, 0, A15, B15]], dtype=float)
    print("a1 = ", a1)
    b1 = np.array([D11, D12, D13, D14, D15], dtype=float)
    print("b1 = ", b1)
    x1 = np.linalg.solve(a1, b1)
    print("x1 = ", x1)
    ##pour la composition 2 :
    K21 = float((10 ** (A2 - B2 / (C2 + ((T1 - 32) * 5 / 9)))) / 5171.49)
    K22 = float((10 ** (A2 - B2 / (C2 + ((T2 - 32) * 5 / 9)))) / 5171.49)
    K23 = float((10 ** (A2 - B2 / (C2 + ((T3 - 32) * 5 / 9)))) / 5171.49)
    K24 = float((10 ** (A2 - B2 / (C2 + ((T4 - 32) * 5 / 9)))) / 5171.49)
    K25 = float((10 ** (A2 - B2 / (C2 + ((T5 - 32) * 5 / 9)))) / 5171.49)
    print("k21 = ", K21)
    print("k22 = ", K22)
    print("k23 = ", K23)
    print("k24 = ", K24)
    print("k25 = ", K25)
    B21 = -V2 - V1 * K21
    B22 = -V3 + D - V2 * K22
    B23 = -V4 - F + D - V3 * K23
    B24 = -V5 - F + D - V4 * K24
    B25 = -V6 - F + D - V5 * K25
    D23 = -F * Z2
    C21 = V2 * K22
    C22 = V3 * K23
    C23 = V4 * K24
    C24 = V5 * K25
    a2 = np.array([[B21, C21, 0, 0, 0],
                   [A22, B22, C22, 0, 0],
                   [0, A23, B24, C23, 0],
                   [0, 0, A24, B24, C24],
                   [0, 0, 0, A25, B25]], dtype=float)
    print("a2 = ", a2)
    b2 = np.array([D21, D22, D23, D24, D25], dtype=float)
    print("b2 = ", b2)
    x2 = np.linalg.solve(a2, b2)
    print("x2 = ", x2)
    ##pour la composition 3:
    K31 = float((10 ** (A3 - B3 / (C3 + ((T1 - 32) * 5 / 9)))) / 5171.49)
    K32 = float((10 ** (A3 - B3 / (C3 + ((T2 - 32) * 5 / 9)))) / 5171.49)
    K33 = float((10 ** (A3 - B3 / (C3 + ((T3 - 32) * 5 / 9)))) / 5171.49)
    K34 = float((10 ** (A3 - B3 / (C3 + ((T4 - 32) * 5 / 9)))) / 5171.49)
    K35 = float((10 ** (A3 - B3 / (C3 + ((T5 - 32) * 5 / 9)))) / 5171.49)
    print("k31 = ", K31)
    print("k32 = ", K32)
    print("k33 = ", K33)
    print("k34 = ", K34)
    print("k35 = ", K35)
    B31 = -V2 - V1 * K31
    B32 = -V3 + D - V2 * K32
    B33 = -V4 - F + D - V3 * K33
    B34 = -V5 - F + D - V4 * K34
    B35 = -V6 - F + D - V5 * K35
    D33 = -F * Z2
    C31 = V2 * K32
    C32 = V3 * K33
    C33 = V4 * K34
    C34 = V5 * K35
    a3 = np.array([[B31, C31, 0, 0, 0],
                   [A32, B32, C32, 0, 0],
                   [0, A33, B34, C33, 0],
                   [0, 0, A34, B34, C34],
                   [0, 0, 0, A35, B35]], dtype=float)
    print("a3 = ", a3)
    b3 = np.array([D31, D32, D33, D34, D35], dtype=float)
    print("b3 = ", b3)
    x3 = np.linalg.solve(a3, b3)
    print("x3 = ", x3)
    # calcul de la somme pour verifier la condition s=1
    print("les solution obtenue est recuperee dans une matrice")
    M = np.array([x1, x2, x3]).T
    print("M =", M)

    # Normlisation de X :
    print("calcule de la somme de xi pour chaque etage : ")
    p1 = M[0, 0] + M[0, 1] + M[0, 2]
    print("p1= ", p1)
    p2 = M[1, 0] + M[1, 1] + M[1, 2]
    print("p2= ", p2)
    p3 = M[2, 0] + M[2, 1] + M[2, 2]
    print("p3=", p3)
    p4 = M[3, 0] + M[3, 1] + M[3, 2]
    print("p4=", p4)
    p5 = M[4, 0] + M[4, 1] + M[4, 2]
    print("p5=", p5)
    # normalisation des solution
    print("les valeur de xi apres normalisation pour chaque etage : ")
    S = []
    N1 = np.array([x1[0] / p1, x1[1] / p2, x1[2] / p3, x1[3] / p4, x1[4] / p5], float)
    print("N1 = ", N1)
    N2 = np.array([x2[0] / p1, x2[1] / p2, x2[2] / p3, x2[3] / p4, x2[4] / p5], float)
    print("N2 = ", N2)
    N3 = np.array([x3[0] / p1, x3[1] / p2, x3[2] / p3, x3[3] / p4, x3[4] / p5], float)
    print("N3 = ", N3)
    print("les valeurs de xi normalise :recupere dans une matrice s  ")
    S = np.array([N1, N2, N3]).T
    print("S = ", S)
    print("calcule de la somme des nouvel xi pour chaque etage : ")
    Som1 = S[0, 0] + S[0, 1] + S[0, 2]
    print("Som 1 = ", Som1)
    Som2 = S[1, 0] + S[1, 1] + S[1, 2]
    print("Som 2 = ", Som2)
    Som3 = S[2, 0] + S[2, 1] + S[2, 2]
    print("Som 3 = ", Som3)
    Som4 = S[3, 0] + S[3, 1] + S[3, 2]
    print("Som 4 = ", Som4)
    Som5 = S[4, 0] + S[4, 1] + S[4, 2]
    print("Som 5 = ", Som5)
    ##la verification de la relation somme ki*xi-1 = 0
    Y1 = (K11 * S[0, 0] + K21 * S[0, 1] + K31 * S[0, 2])
    print("Y1 = ", Y1)
    Y2 = (K12 * S[1, 0] + K22 * S[1, 1] + K32 * S[1, 2])
    print("Y2 = ", Y2)
    Y3 = (K13 * S[2, 0] + K23 * S[2, 1] + K33 * S[2, 2])
    print("Y3 = ", Y3)
    Y4 = (K14 * S[3, 0] + K24 * S[3, 1] + K34 * S[3, 2])
    print("Y4 = ", Y4)
    Y5 = (K15 * S[4, 0] + K25 * S[4, 1] + K35 * S[4, 2])
    print("Y5 = ", Y5)
    k = np.array([[K11, K12, K13, K14, K15],
                  [K21, K22, K23, K24, K25],
                  [K31, K32, K33, K34, K35]], float).T
    print("k =", k)
    # Autre méthode
    print("vérification avec une autre méthode")
    sum_etage1 = np.dot(k[0], S[0])
    print("sum etage1 =", sum_etage1)
    sum_etage2 = np.dot(k[1], S[1])
    print("sum etage2 =", sum_etage2)
    sum_etage3 = np.dot(k[2], S[2])
    print("sum etage3 =", sum_etage3)
    sum_etage4 = np.dot(k[3], S[3])
    print("sum etage4 =", sum_etage4)
    sum_etage5 = np.dot(k[4], S[4])
    print("sum etage5 =", sum_etage5)


    def func1(T):
        a = ((S[0, 0] * pow(10, (A1 - B1 / (C1 + ((T - 32) * 5 / 9)))) + S[0, 1] * pow(10, (
                    A2 - B2 / (C2 + ((T - 32) * 5 / 9)))) + S[0, 2] * pow(10, (
                    A3 - B3 / (C3 + ((T - 32) * 5 / 9))))) / 5171.5) - 1
        return a


    T1 = fsolve(func1, [65])
    print("T1 =", T1)


    def func2(T):
        b = ((S[1, 0] * pow(10, (A1 - B1 / (C1 + ((T - 32) * 5 / 9)))) + S[1, 1] * pow(10, (
                    A2 - B2 / (C2 + ((T - 32) * 5 / 9)))) + S[1, 2] * pow(10, (
                    A3 - B3 / (C3 + ((T - 32) * 5 / 9))))) / 5171.5) - 1

        return b


    T2 = fsolve(func2, [90])
    print("T2 =", T2)


    def func3(T):
        c = ((S[2, 0] * pow(10, (A1 - B1 / (C1 + ((T - 32) * 5 / 9)))) + S[2, 1] * pow(10, (
                    A2 - B2 / (C2 + ((T - 32) * 5 / 9)))) + S[2, 2] * pow(10, (
                    A3 - B3 / (C3 + ((T - 32) * 5 / 9))))) / 5171.5) - 1
        return c


    T3 = fsolve(func3, [115])
    print("T3 =", T3)


    def func4(T):
        d = ((S[3, 0] * pow(10, (A1 - B1 / (C1 + ((T - 32) * 5 / 9)))) + S[3, 1] * pow(10, (
                    A2 - B2 / (C2 + ((T - 32) * 5 / 9)))) + S[3, 2] * pow(10, (
                    A3 - B3 / (C3 + ((T - 32) * 5 / 9))))) / 5171.5) - 1
        return d


    T4 = fsolve(func4, [140])
    print("T4 =", T4)


    def func5(T):
        e = ((S[4, 0] * pow(10, (A1 - B1 / (C1 + ((T - 32) * 5 / 9)))) + S[4, 1] * pow(10, (
                    A2 - B2 / (C2 + ((T - 32) * 5 / 9)))) + S[4, 2] * pow(10, (
                    A3 - B3 / (C3 + ((T - 32) * 5 / 9))))) / 5171.5) - 1
        return e


    T5 = fsolve(func5, [165])
    print("T5 =", T5)

    sum_etage = [sum_etage1, sum_etage2, sum_etage3, sum_etage4, sum_etage5]
    if (np.isclose(sum_etage1, [1.0]) == True and np.isclose(sum_etage2, [1.0]) == True and np.isclose(sum_etage3, [
        1.0]) == True and np.isclose(sum_etage4, [1.0]) == True and np.isclose(sum_etage5, [1.0]) == True):
        break
print("le nombre des itérations est N = ",i)
# calculer le temps d'execussion
pf = perf_counter()
time = pf - ps
print(time)
# tracage de la courbe-profil de température à chaque étage
TT= [T1,T2,T3,T4,T5]
T= np.array(TT)
X1=[1,2,3,4,5]
X= np.array(X1)
plt.plot(X,T)
plt.show()
# plot x as function of stage by python
x1 = np.array(x1)
x2 = np.array(x2)
x3 = np.array(x3)
fig, axx = plt.subplots()
axx.plot(X1, x1, "o-", label="propane fraction ")
axx.plot(X1, x2, "o-", label="n-butane fraction ")
axx.plot(X1, x3, "o-", label="n-pentane fraction ")
axx.legend()
axx.set_title("ETAGE")
axx.set_xlabel(X)
axx.set_ylabel("fraction molaire xij")
plt.show()
# plot k as function of stage by python
k11 = [1.1503114916291486, 1.6274763648293842, 2.2280855125059538, 2.9648682991740967, 3.848913798489272]
k22 = [0.2849462013308443, 0.43790251223640214, 0.6453470093810417, 0.9173790326728801, 1.263953841671814]
k33 = [0.07689549690126614, 0.1287334012303479, 0.2047508902642312, 0.31165011313565666, 0.45667398440333695]
k11 = np.array(k11)
k22 = np.array(k22)
k33 = np.array(k33)
fig, axy = plt.subplots()
axy.plot(X1, k11, "o-", label="k_propane ")
axy.plot(X1, k22, "o-", label="k_n-butane ")
axy.plot(X1, k33, "o-", label="k_n-pentane ")
axy.legend()
axy.set_title("ETAGE")
axy.set_xlabel(k)
axy.set_ylabel("volatilité kij ")
plt.show()
# fin
