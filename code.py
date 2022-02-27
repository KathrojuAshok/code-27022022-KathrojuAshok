# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 19:10:30 2022

@author: Ashok
"""

import json
import pandas as pd
import numpy as np
import os
from sys import argv


class form:

    def format_data(fi):
    
    
        data = pd.read_json(fi)
        
        data['bmi']=data['WeightKg']/(data["HeightCm"]/100)
        
        
        
        table_1=[{'BMI_Category':'Underweight',"BMI_Range_(kg/m2)":"18.4 and below","Health_risk":"Malnutrition risk"},
                  {'BMI_Category':'Normal_weight',"BMI_Range_(kg/m2)":"18.5 - 24.9","Health_risk":"Low risk"},
                  {'BMI_Category':'Overweight',"BMI_Range_(kg/m2)":"25 - 29.9","Health_risk":"Enhanced risk"},
                  {'BMI_Category':'Moderately obese',"BMI_Range_(kg/m2)":"30 - 34.9","Health_risk":"Medium risk"},
                  {'BMI_Category':'Severely obese',"BMI_Range_(kg/m2)":"35 - 39.9","Health_risk":"High risk"},
                  {'BMI_Category':'Very severely obese',"BMI_Range_(kg/m2)":"40 and above","Health_risk":"Very high risk"}]
        
        table_1_df=pd.DataFrame(table_1)
        
        table_1_df['BMI_Range_(kg/m2)']=[i.split() for i in table_1_df['BMI_Range_(kg/m2)']]
        
        
        
        #table_1_df['low']=table_1_df['BMI_Range_(kg/m2)'].split()
        
        
        conditions=[
                (data['bmi']<float(table_1_df['BMI_Range_(kg/m2)'][0][0])),
                (data['bmi']>float(table_1_df['BMI_Range_(kg/m2)'][1][0])) & (data['bmi']<=float(table_1_df['BMI_Range_(kg/m2)'][1][2])),
                (data['bmi']>float(table_1_df['BMI_Range_(kg/m2)'][2][0])) & (data['bmi']<float(table_1_df['BMI_Range_(kg/m2)'][2][2])),
                (data['bmi']>float(table_1_df['BMI_Range_(kg/m2)'][3][0])) & (data['bmi']<float(table_1_df['BMI_Range_(kg/m2)'][3][2])),
                (data['bmi']>float(table_1_df['BMI_Range_(kg/m2)'][4][0])) & (data['bmi']<float(table_1_df['BMI_Range_(kg/m2)'][4][2])),
                (data['bmi']>float(table_1_df['BMI_Range_(kg/m2)'][5][0]))
                
                ]
        
        data["BMI_Category"]=np.select(conditions,table_1_df["BMI_Category"])
         
        data["Health_risk"]=np.select(conditions,table_1_df["Health_risk"])
        try:
            c=data[data["BMI_Category"]=='Overweight']['BMI_Category'].value_counts()['Overweight']
            c={"Overweight":c}
        except:
            c=0
        print(data.to_json())
        print("\n")
        print("\n")
        print("The total number of Overweight candidates are :"+str(c))
#        with open(fi+"_output.json","w") as outfile:
#            outfile.write(data.to_json())
        return data,c
    


#import unittest
##
#class test_case(unittest.TestCase):
#    def test1(self):
#        ob=format_data(fi)
#        self.assertEqual(ob[1],{'Overweight': 0},"should be {'Overweight': 0}")
if __name__=="__main__":
    form.format_data(*argv[1:])



