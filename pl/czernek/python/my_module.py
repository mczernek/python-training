'''
Created on 8 wrz 2014

@author: mczernek
'''
def add(*x):
    result = 0;
    for a in x:
        result+=a;
    return result;