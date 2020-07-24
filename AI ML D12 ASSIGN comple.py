# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 12:48:36 2020

@author: ADMIN
"""

#wilcoxon test
import pandas as pd
dataset=pd.read_excel("C:/Users/ADMIN/Testing/1 Wilcoxon.xlsx")
print(dataset.head())
d1=dataset.TOTALCIN
d2=dataset.TOTALCW2

from scipy.stats import wilcoxon
stat,p=wilcoxon(d1,d2)
print(stat,p)
#29.5 0.00259741456482452
#P value is < then 0.05 so H0 accepted & Ha rejected

#friedmanchi test
d3=dataset.TOTALCW4

from scipy.stats import friedmanchisquare
stat,p=friedmanchisquare(d1,d2,d3)
print(stat,p)
#27.927710843373504 8.62133745016363e-07
#here p value is greater than 0.05
#means H0rejcted ,Ha accapted


#manwhitney test
import pandas as pd
from scipy.stats import mannwhitneyu

dataset1=pd.read_excel("C:/Users/ADMIN/Testing/3 Mann Whitney.xlsx",sheet_name=1)

print(dataset1.head())

a1=dataset1.Design1

a2=dataset1.Design2

stat,p=mannwhitneyu(a1,a2)

print(stat,p)
#9.0 0.2641796636354743
# p value > 0.05 H0 accpted, Ha rejected

# kruskal test
from scipy.stats import kruskal

dataset2=pd.read_excel("C:/Users/ADMIN/Testing/4 Kruskal Wallis.xlsx",sheet_name=0)

print(dataset2.head())
b1=dataset2.Design1

b2=dataset2.Design2

b3=dataset2.Design3

stat,p=kruskal(b1,b2,b3)

print(stat,p)
#2.7345323741007226 0.25480259087913626

#p value> 0.05 so H0 accpted & Ha rejected

# one sample T test

from scipy.stats import ttest_1samp

dataset6=pd.read_excel("C:/Users/ADMIN/Testing/1. One Sample.xlsx",sheet_name=0)

print(dataset6.head())
h1=dataset6.Height

stat,p=ttest_1samp(h1,65)

print(stat,p)
#11.498800238580099 1.087893570160242e-26
#p value > 0.05 hence H0 accpted Ha rejected


#TWO pair T test
from scipy.stats import ttest_rel

dataset3=pd.read_excel("C:/Users/ADMIN/Testing/2. Paired Sample.xlsx",sheet_name=0)

print(dataset3.head())
p1=dataset3.English

p2=dataset3.Math

stat,p=ttest_rel(p1,p2)

print(stat,p)

#36.312568981719856 3.0710987192210606e-128
#p vlue >0.05 so H0 accepted Ha rejected

# independent test
from scipy.stats import ttest_ind

dataset4=pd.read_excel("C:/Users/ADMIN/Testing/3. Independent Sample.xlsx",sheet_name=3)

print(dataset4.head())

z1=dataset4.Nonathelete

z2=dataset4.Athelete

stat,p=ttest_ind(z1,z2)

print(stat,p)
#13.368790432137319 7.116633157230895e-33
#P value >0.05 so H0 accpted HA REJECTED









































