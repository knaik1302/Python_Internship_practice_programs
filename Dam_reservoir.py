"""Objective of this PoC
      To learn to do arithmetic operations in very less number of lines of code
      To understand the use of yet another kind of 'numeric literal' which can represent 'power of base 10' : 1e2 means 100.0 and 1e3 means 1000.0 in python
Proof of Concept
    A dam reservoir's capacity is 250e100 cubic meter where it holds 199.5e85 cu.m water.
    A rain occurred in the area which gave 25e8 cu.m water but 25% amount of this rain water ran-off useless.
    The remaining water from this rainfall flowed to the reservoir and there it was collected. On another day, a heavy storm increased the water level of this dam to its 15% of the current water level. 
    Ground water sources contributed 5% to reservoir's current level. 5% of the present level of reservoir evaporated and later 15% amount of water was passed for irrigation to arid regions.
Task
    Write a python program using less number of lines of code to find the current water level of the reservoir using the given data?
"""

dam_res=199.5e85+(25e8-25e8 *0.25)
print(dam_res)

'''
dam_res+=dam_res*0.15
dam_res+=dam_res*0.05
dam_res-=dam_res*0.05
dam_res-=dam_res*0.15 

print(dam_res)'''
