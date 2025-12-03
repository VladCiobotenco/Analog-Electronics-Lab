import matplotlib.pyplot as plt
import numpy as np

figure, img = plt.subplots(1,3, figsize=(15,5))

def CaracteristicaIntrare():
    VBE = [[0.05],[0.09],[0.27],[0.43],[0.58],[0.61],[0.67],[0.69],[0.71],[0.70],[0.70],[0.68],[0.69],[0.69]]
    IB = [[0],[0],[0],[0],[5.9],[17],[24.4],[30.5],[36],[46],[56.6],[68.4],[74.85],[80]]

    img[0].plot(VBE,IB)
    img[0].scatter(VBE,IB, marker='o', color='orange')
    img[0].set_title('Caracteristica de intrare a tranzistorului')
    img[0].set_xlabel('Tensiunea VBE(V)')
    img[0].set_ylabel('Intensitatea IB(μA)')
    img[0].grid()

def CaracteristicaTransfer():
    IB = [[0],[0],[0],[0],[5.9],[17],[24.4],[30.5],[36],[46],[56.6],[68.4],[74.85],[80]]
    IC = [[0],[0],[0],[0],[0.5],[1.2],[2],[2.5],[3],[4.2],[5.2],[6.4],[7],[7.6]]

    coefficients = np.polyfit(np.array(IB).flatten(), np.array(IC).flatten(), 1)
    fit_line = np.poly1d(coefficients)
    img[1].plot(np.array(IB).flatten(), fit_line(np.array(IB).flatten()), 'r--')
    img[1].scatter(IB,IC, marker='o', color='green')
    img[1].set_title('Caracteristica de transfer a tranzistorului')
    img[1].set_xlabel('Intensitatea IB(μA)')
    img[1].set_ylabel('Intensitatea IC(mA)')
    img[1].grid()
    print(coefficients[0])

def CaracteristicaIesire():
    VCE = [[0.03],[0.06],[0.09],[0.12],[0.15],[0.18],[0.21],[1],[3],[5],[9],[12]]
    IC = [[0.08],[0.26],[0.46],[0.66],[0.88],[2.4],[2.6],[3],[3],[3],[3],[3]]

    img[2].plot(VCE,IC,'magenta', label='IB=40μA')
    img[2].scatter(VCE,IC, marker='o', color='blue')
    img[2].set_title('Caracteristica de iesire a tranzistorului')
    img[2].set_xlabel('Tensiunea VCE(V)')
    img[2].set_ylabel('Intensitatea IC(mA)')
    img[2].grid()

    #VCE = [[0.03],[0.06],[0.09],[0.12],[0.15],[0.18],[0.21],[1],[3],[5],[9],[12]]
    IC = [[0.14],[0.34],[0.56],[0.8],[2.6],[3.2],[3.8],[5.1],[5.1],[5.1],[5.1],[5.1]]
    img[2].plot(VCE,IC,'cyan',label='IB=60μA')
    img[2].scatter(VCE,IC, marker='o', color='red')
    img[2].legend()

CaracteristicaIntrare()
CaracteristicaTransfer()
CaracteristicaIesire()
plt.show()