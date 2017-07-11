import numpy as np
import csv

class sNCal:
    ret = 0;
    def __init__(self, numMatrix):
        self.numMatrix = numMatrix;
        self.length = len(self.numMatrix);
        self.ret =  self.difference();

    def difference(self):
        dataMean = np.mean(self.numMatrix);
        sum1 = 0;
        for i in range(0,self.length):
            sum1 = sum1 + np.power((np.longfloat(self.numMatrix[i][0]-dataMean)),2);

        divide = sum1/(self.length-1);
        return np.sqrt(divide);


class Main:
    def __init__(self):
        path = 'labExercise01.csv';
        fle = open(path,'rb');
        reader = csv.reader(fle);
        myList = list(reader);
        matrix = np.array(myList,dtype=np.longfloat);

        matrix1 = matrix[0:,:1];
        matrix2 = matrix[0:,1:2];
        matrix3 = matrix[0:,2:3];
        matrix4 = matrix[0:,3:4];
        matrix5 = matrix[0:,4:5];

        print 'sN of column 1 : %0.15f'% sNCal(matrix1).ret;
        print 'sN of column 2 : %0.15f'% sNCal(matrix2).ret;
        print 'sN of column 3 : %0.15f'% sNCal(matrix3).ret;
        print 'sN of column 4 : %0.15f'% sNCal(matrix4).ret;
        print 'sN of column 5 : %0.15f'% sNCal(matrix5).ret;


MainObj = Main();

############################Local Minima of a Given Vector#########################


class detect_local_minima:
    array = [];
    minx = np.array([]);

    def __init__(self):
        path = 'bonusExercise.csv';
        fle = open(path, 'rb');
        reader = csv.reader(fle);
        myList = list(reader);
        matrix = np.array(myList, dtype=np.longfloat);
        self.length = len(matrix);
        self.array = self.calminim(matrix);

    def calminim(self, matrix):
        y = matrix[0:,:1];
        x = matrix[0:,1:2];
        minim = np.array([]);
        for i in range(1,self.length-1):
            if (y[i][0]<y[i-1][0]) & (y[i][0]<y[i+1][0]):
                minim = np.insert(minim,0,y[i]);
                self.minx = np.insert(self.minx,0,x[i]);
                print x[i];
                print y[i];

        return np.asarray(minim);


local_minina = detect_local_minima();
print '\nLocal minima\n';
print local_minina.array;

#print local_minina.minx;
