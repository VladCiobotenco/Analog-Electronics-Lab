import matplotlib.pyplot as plt
import numpy as np

figure, img = plt.subplots(1,3, figsize=(15,5))

def SiDiodeBiased():

    XPlot=[[0.1],[0.2],[0.3],[0.39],[0.48],[0.53],[0.56],[0.58],[0.59],[0.6],[0.6],[0.61],[0.62],[0.62],[0.62],[0.63],[0.63]]
    YPlot=[[0],[0],[0],[0],[0.02],[0.05],[0.12],[0.2],[0.28],[0.36],[0.46],[0.54],[0.62],[0.7],[0.78],[0.9],[1]]

    img[0].plot(XPlot, YPlot, marker='o', color='r')
    img[0].set_title("Caracteristica tensiune-curent\nDioda de siliciu cu polarizare directa")
    img[0].set_xlabel("Tensiune curentului (V)")
    img[0].set_ylabel("Intensitatea curentului (mA)")
    img[0].grid()
    #plt.show()

def LEDBiased():

    XPlot=[[0.1],[0.2],[0.3],[0.4],[0.5],[0.6],[0.7],[0.79],[0.9],[0.99],[1.11],[1.19],[1.3],[1.39],[1.5],[1.59],[1.67],[1.72],[1.76],[1.78],[1.79],[1.8],[1.81],[1.82],[1.83],[1.84],[1.84],[1.85],[1.85],[1.85],[1.86],[1.86],[1.86],[1.87],[1.87],[1.87],[1.87],[1.88],[1.88],[1.88],[1.88]]
    YPlot=[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0.01],[0.03],[0.06],[0.1],[0.14],[0.18],[0.22],[0.26],[0.3],[0.34],[0.39],[0.44],[0.48],[0.52],[0.58],[0.62],[0.66],[0.7],[0.76],[0.8],[0.84],[0.88],[0.92],[0.96],[1]]
    Xo=[[0]]
    Yo=[[0]]

    img[1].scatter(Xo,Yo, marker='X', color='black')
    img[1].plot(XPlot, YPlot, marker='x', color='g')
    img[1].set_title("Caracteristica tensiune-curent\nLED")
    img[1].set_xlabel("Tensiune curentului (V)")
    img[1].set_ylabel("Intensitatea curentului (mA)")
    img[1].grid()
    img[1].set_xlim(-3, 3)  # Extends the x-axis to the right past 0
    img[1].set_ylim(-1.3, 1.3) # Extends the y-axis above 0
    #plt.show()

def SiDiodeReverseBiased():

    XPlot=[[-0.5],[-0.99],[-1.5],[-1.99],[-2.5],[-2.99],[-3.49],[-3.99],[-4.49],[-5.0],[-5.49],[-5.99],[-6.49],[-6.99],[-7.48],[-7.99],[-8.48],[-8.86],[-8.9],[-8.93]]
    YPlot=[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[-0.12],[-0.54],[-0.98]]

    img[2].plot(XPlot, YPlot, marker='v', color='orange')

# Add these lines to center the origin
    img[2].set_xlim(-9.5, 9.5)  # Extends the x-axis to the right past 0
    img[2].set_ylim(-1.2, 1.2) # Extends the y-axis above 0

    img[2].set_title("Caracteristica tensiune-curent\nDioda Zener de siliciu cu polarizare inversa")
    img[2].set_xlabel("Tensiune curentului (V)")
    img[2].set_ylabel("Intensitatea curentului (mA)")
    img[2].grid()
#plt.show()

SiDiodeBiased()
LEDBiased()
SiDiodeReverseBiased()
plt.show()


