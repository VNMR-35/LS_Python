import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import savgol_filter

class dice_roll:    #Class to Simulate and Plot
    def __init__(self, n):
        self.n = n
    
    def experiment(self):
        return np.random.randint(low=1, high=7) + np.random.randint(low=1, high=7) + np.random.randint(low=1, high=7)

    def repeat(self):
        for i in range(self.n):
            yield self.experiment()

    #The function experiment() and generator repeat() make the simulation
    def plot_pdf(self):    #Plots the pdf
        x_axis = np.linspace(3, 18, 16)
        y_axis = np.zeros(16)
        for i in self.repeat():
            y_axis[i-3] += 1/self.n
        plt.figure()
        plt.plot(x_axis, y_axis)
        y_savgol = savgol_filter(y_axis, 15, 5)
        plt.plot(x_axis, y_savgol, color='red')
        plt.xlabel("Sum of number on 3 dice")
        plt.ylabel("Probability of Sum of numbers to be x")
        plt.title("PDF of Dice Roll Simulation")
        plt.legend(['PDF', 'Savgol Filter'])
        plt.savefig('plot1.png')

    def bar_graph(self):    #Plots the Bar Graph
        x_axis = np.linspace(3, 18, 16)
        y_axis = np.zeros(16)
        for i in self.repeat():
            y_axis[i-3] += 1/self.n
        plt.figure()
        plt.bar(x_axis, y_axis, width=0.6)
        plt.xlabel("Sum of number on 3 dice")
        plt.ylabel("Probability of Sum of numbers to be x")
        plt.title("Bar Graph for Dice Roll Simulation")
        plt.savefig('plot2.png')
        
#The class is called below:
obj = dice_roll(1000)
obj.plot_pdf()
obj.bar_graph()