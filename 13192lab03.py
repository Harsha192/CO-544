import pandas as pd
import numpy as np
import unittest

class Covariance:
    covxy = 0.0;

    def __init__(self, X, Y):
        self.cov(X, Y);

    def cov(self, X, Y):
        X = X.fillna(0.0);
        Y = Y.fillna(0.0);
        length = len(X);
        xMean = X.mean();
        yMean = Y.mean();
        sum_cor = np.float(0);
        for i in range(0,length):
            diff = (X[i]-xMean)*(Y[i]-yMean);
            sum_cor = sum_cor + diff;

        self.covxy = sum_cor/(length-1);


class CovarianceMatrix:
    def __init__(self, file):
        df = pd.read_csv(file, names=['a', 'b', 'c', 'd', 'e']);
        self.matrix(df);
        df = df.fillna(0);

    def matrix(self, df):
        mat = np.zeros(shape=(5,5), dtype='float');
        for i in range(0,5):
            for j in range(0,5):
                var = 0.0;
                if i==j:
                    var = df.var()[i];
                    mat[i][i] = var;
                else:
                    x = [];
                    y = [];
                    if j==0:
                        y = df.a;
                    elif j==1:
                        y = df.b;
                    elif j==2:
                        y = df.c;
                    elif j==3:
                        y = df.d;
                    elif j==4:
                        y = df.e;

                    if i==0:
                        x = df.a;
                    elif i==1:
                        x = df.b;
                    elif i==2:
                        x = df.c;
                    elif i==3:
                        x = df.d;
                    elif i==4:
                        x = df.e;

                    cov = Covariance(x,y).covxy;
                    mat[j][i] = cov;


        print mat;

print 'Covariance Matrix';
print '-----------------\n'
print 'Result Matrix\n';
covarianceMatrix = CovarianceMatrix('lab03Exercise.csv');

df = pd.read_csv('lab03Exercise.csv', names=['a', 'b', 'c', 'd', 'e']);
df = df.fillna(0.0);
print '\nExpected Matrix\n';
print df.cov();

##########################################################################################

class Correlation:
    corxy = 0;

    def __init__(self, X, Y):
        self.cor(X,Y);

    def cor(self, X, Y):
        X = X.fillna(0.0);
        Y = Y.fillna(0.0);
        length = len(X);
        xSTD =  X.std();
        ySTD =  Y.std();
        self.corxy = Covariance(X,Y).covxy/(xSTD*ySTD);


class CorrelationMatrix:
    def __init__(self, file):
        df = pd.read_csv(file, names=['a', 'b', 'c', 'd', 'e']);
        self.matrix(df);

    def matrix(self, df):
        mat = np.zeros(shape=(5,5), dtype='float');
        for i in range(0,5):
            for j in range(0,5):
                x = [];
                y = [];
                if j == 0:
                    y = df.a;
                elif j == 1:
                    y = df.b;
                elif j == 2:
                    y = df.c;
                elif j == 3:
                    y = df.d;
                elif j == 4:
                    y = df.e;

                if i == 0:
                    x = df.a;
                elif i == 1:
                    x = df.b;
                elif i == 2:
                    x = df.c;
                elif i == 3:
                    x = df.d;
                elif i == 4:
                    x = df.e;

                cor = Correlation(x,y).corxy;
                mat[j][i] = cor;

        print mat;

print '\n\nCorrelation Matrix';
print '------------------\n'
print 'Result Matrix\n';
correlationMatrix = CorrelationMatrix('lab03Exercise.csv');

df = pd.read_csv('lab03Exercise.csv', names=['a', 'b', 'c', 'd', 'e']);
df = df.fillna(0.0);
print '\nExpected Matrix\n';
print df.corr();

# 2. most covariance values between coloumns are closest to zero and few are not. so, most of the
#    coloumns are not much correlated with each other.

