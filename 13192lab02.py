import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class GradientDescentAlgorithm:
    precision = 0.0;
    learning_rate = 0.0;
    current_x = 0.0;
    regnumber = 'E13192';

    def __init__(self,precision,learning_rate):
        self.precision = precision;
        self.learning_rate = learning_rate;
        self.plot_graph();

    def plot_graph(self):
        x = np.linspace(-2, 2, 100, dtype='float');
        print x;
        y = np.array([]);
        for i in range(0, len(x)):
            y = np.insert(y, 0, self.fx(x[i]));
        print y;
        fig = plt.figure(figsize=(100, 100));
        fig.subplots_adjust(hspace=.5);
        axes = plt.subplot(1, 1, 1);
        axes.plot(x, y, linewidth=1.0, ls='--', color='r', marker=".");
        plt.show();

        current_x = 5;
        self.repeat(current_x);

    def repeat(self, current_x):
        #current_x = self.current_x;
        #previous_step_size = current_x;
        x = np.array([]);
        y = np.array([]);
        while True:
            previous_x = current_x;
            der = self.derivate(current_x);
            current_x = current_x - (self.learning_rate * der);
            print current_x;
            previous_step_size = np.abs(current_x - previous_x);
            print previous_step_size;

            if (previous_step_size<=self.precision):
                break;
            x = np.insert(x, 0, current_x);
            y = np.insert(y, 0, self.fx(current_x));

        print current_x;

    def derivate(self,x):
        p = np.poly1d([-2,0,-1,9,2]);
        q = p.deriv();
        print p;
        print q;
        return q(x);

    def fx(self,x):
        p = np.poly1d([-2, 0, -1, 9, 2]);
        return p(x);


gda = GradientDescentAlgorithm(0.001,0.00001);


# (1). typically initial x need to be define as closest to the local minima of a function graph.
#      when it closest to local minima number of iteratives of the while loop can be less
#      but, in this case there are no local minimas to this function
#(2).
#(3).  there are no local minimas to this function. so while loop run infinitely to anu current_x value.



