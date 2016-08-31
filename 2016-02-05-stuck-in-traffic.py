#------------------------------------------------------------------------------+
#
#   Nathan A. Rooy
#   FiveThirtyEight: The Riddler [July 8th, 2016]
#
#------------------------------------------------------------------------------+

#--- IMPORT DEPENDENCIES ------------------------------------------------------+

from __future__ import division
from collections import defaultdict
import random

#--- MAIN ----------------------------------------------------------------+

def traffic(ncars):
    cars=[]

    # GENERATE RANDOM CAR SPEEDS
    for i in range(ncars):
        cars.append(random.random())

    groups=0
    slowest_car=cars[0]

    # CYCLE THROUGH CAR LIST
    for i in range(ncars-1):
        if cars[i]<=slowest_car:
            slowest_car=cars[i]
            groups+=1

    # CHECK LAST CAR
    if cars[-1]<slowest_car:
        groups+=1

    return groups

def main(iters,ncars):
    group_hist=[]
    for i in range(0,iters):
        group_hist.append(traffic(ncars))
    return group_hist

#--- RUN ---------------------------------------------------------------------+

ncars_list=[3,4,5,6,7,8,9,10,
            15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,
            150,200,250,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000,
            2000,3000,4000,5000,6000,7000,8000,9000,10000]

iters=1000000
for ncars in ncars_list:
    group_hist=main(iters,ncars)

    # RESULTS
    results_dict=defaultdict(int)
    for item in group_hist:
        results_dict[item]+=1

    results_sorted=sorted(results_dict.items(),key=lambda(group,count):group,reverse=False)

    # SAVE RESULTS TO CSV
    with file('results.csv','a') as csvFile:
        csvFile.write(str(ncars)+','+str(results_sorted[:30])+'\n')
    csvFile.close()

#--- END ----------------------------------------------------------------------+
