import numpy as np
import matplotlib.pyplot as plt

figure, img = plt.subplots(1,2, figsize=(15,5))

def CaracteristicaAmplitudinii():
    # R1 = 10K
    # R2 = 5K1

    Vi1=[[0.2],[0.5],[1],[1.5],[2],[2.5],[3],[3.5],[4],[4.5]]
    Vo1=[[0.42],[1.07],[2.1],[3.14],[4.2],[5.1],[5.5],[5.6],[5.7],[5.8]]

    Vi2=[[0.2],[0.5],[1],[1.5],[2],[2.5],[3],[3.5],[4],[4.5]]
    Vo2=[[0.3],[0.8],[1.5],[2.4],[3.15],[3.85],[4.4],[4.5],[4.6],[4.6]]

    img[0].plot(Vi1,Vo1, c='orange', marker='o', label='R2=5K1')
    img[0].scatter(Vi1,Vo1)
    img[0].plot(Vi2,Vo2, c='green', marker='o', label='R2=10K')
    img[0].scatter(Vi2,Vo2)
    img[0].set_title('Caracteristica amplitudinii')
    img[0].set_xlabel('Tensiunea de intrare (V)')
    img[0].set_ylabel('Tensiunea de iesire (V)')
    img[0].legend()
    img[0].grid()


def CaracteristicaFrecventei():

    Vi = np.array([0.81,1.8,1.9,1.9,1.97,1.96,1.97,1.95,1.82,1.87,1.83,1.77,0.001,0.0003], dtype=float)
    Vo = np.array([2.3,4.2,5.2,5.9,6.27,6.28,5.52,2.20,1.61,1.14,0.1,1.01,0.02,0.02], dtype=float)
    A=np.abs(Vo/Vi)
    frecv = np.array([2,3,5,10,100,1e3,1e4,1e5,5e5,7e5,9e5,1e6,3e6,5e6], dtype=float)
    img[1].plot(np.log(frecv), np.log(A))
    plt.scatter(np.log(frecv),np.log(A))
    img[1].set_title('Caracteristica de frecventa')
    img[1].set_xlabel('Frecventa (Hz)')
    img[1].set_ylabel('Amplificarea')
    img[1].grid()

CaracteristicaAmplitudinii()
CaracteristicaFrecventei()
plt.show()