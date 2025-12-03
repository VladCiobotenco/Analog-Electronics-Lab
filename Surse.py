import matplotlib.pyplot as plt
import numpy as np

figure, img = plt.subplot(1,2, figsize=(15,5))

def sursaTensiune():

    XPlot=[[99.2],[182.96],[937.26],[1.23]]
    YPlot=[[4.96],[4.94],[4.78],[2.45]]

    img[0].plot(XPlot, YPlot, marker='o', color='r')
    img[0].set_title("Caracteristica tensiune-curent\nSursa de tensiune")
    img[0].set_xlabel("Intensitatea curentului (mA)")
    img[0].set_ylabel("Tensiune curentului (V)")
    img[0].grid()

def sursaCurent():

    XPlot=[[4.65],[4.43],[1.83],[4.5],[3.85]]
    YPlot=[[3.49],[13.3],[18.26],[6.75],[18.1]]

    img[1].plot(XPlot, YPlot, marker='o', color='b')
    img[1].set_title("Caracteristica tensiune-curent\nSursa de curent")
    img[1].set_xlabel("Intensitatea curentului (mA)")
    img[1].set_ylabel("Tensiunea curentului (V)")
    img[1].grid()


sursaTensiune()
plt.show()