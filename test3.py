# 聚类分析样例
from pylab import *
from scipy.cluster.vq import *

list1=[88,64,96,85]
list2=[92,99,95,94]
list3=[91,87,99,95]
list4=[78,99,97,81]
list5=[88,78,98,84]
list6=[100,95,100,92]
data=vstack((list1,list2,list3,list4,list5,list6))
centroids,_=kmeans(data,2)
results,_=vq(data,centroids)
print(results)