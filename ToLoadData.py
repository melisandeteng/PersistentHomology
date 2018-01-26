import numpy as np
import pickle as pickle

f = open("/Users/yaguethiam/Centrale_3A/Foundations of Geometric methods/data_acc_rot.dat","rb")
data = pickle.load(f,encoding="latin1")
f.close()

data_A = data[0]
data_B = data[1] 
data_C = data[2]
label = data[3]
print(len(data[3]))