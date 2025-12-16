import matplotlib.pyplot as plt
import numpy as np

figure, img = plt.subplots(1,3, figsize=(15,5))

def sursaTensiune():

    XPlot=[[937.26],[182.96],[99.2],[1.23]]
    YPlot=[[4.78],[4.94],[4.96],[2.45]]

    img[0].plot(XPlot, YPlot, marker='o', color='r')
    img[0].set_title("Caracteristica tensiune-curent\nSursa de tensiune")
    img[0].set_xlabel("Intensitatea curentului (mA)")
    img[0].set_ylabel("Tensiune curentului (V)")
    img[0].grid()

def sursaCurent():

    XPlot=[[4.65],[4.5],[4.43],[3.85],[1.83]]
    YPlot=[[3.49],[6.75],[13.3],[18.1],[18.26]]

    img[1].plot(XPlot, YPlot, marker='o', color='b')
    img[1].set_title("Caracteristica tensiune-curent\nSursa de curent")
    img[1].set_xlabel("Intensitatea curentului (mA)")
    img[1].set_ylabel("Tensiunea curentului (V)")
    img[1].grid()

def divizorRezistiv():

    XPlot=[[1.76],[1.07],[0.6],[0.4],[0.2]]
    YPlot=[[1.32],[1.61],[1.8],[1.88],[1.96]]

    img[2].plot(XPlot,YPlot, marker='o', color='g')
    img[2].set_title("Caracteristica tensiune-curent\nDivizor rezistiv")
    img[2].set_xlabel("Intensitatea curentului (mA)")
    img[2].set_ylabel("Tensiunea curentului (V)")
    img[2].grid()
    
sursaTensiune()
sursaCurent()
divizorRezistiv()
plt.show()
