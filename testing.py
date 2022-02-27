# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 12:10:35 2022

@author: Ashok
"""

import unittest
import os
os.chdir("D:\\assessment_test")
import sys,code
from pandas.util.testing import assert_frame_equal
import pandas as pd
#import vamster


#from vamster import form.format_data

class test_case(unittest.TestCase):
    
    def test1(self):
        op1_output=pd.read_json("test_input1.json_output.json")
    
        output1=code.form.format_data("test_input1.json")
        op1=output1[0]
        op2=output1[1]
        assert_frame_equal(op1,op1_output)
#            self.assertIs(op1,op1,"should be "+op1)
        self.assertEqual(op2,0,"should be 0")
    def test2(self):
        op2_output=pd.read_json("test_input2.json_output.json")
    
        output2=code.form.format_data('test_input2.json')
        op1=output2[0]
        op2=output2[1]['Overweight']
        assert_frame_equal(op1,op2_output)
#            self.assertIs(op1,op1,"should be "+op1)
        self.assertEqual(op2,2,"should be 2")
    def test3(self):
        op3_output=pd.read_json("test_input3.json_output.json")
        output3=code.form.format_data('test_input3.json')
        op1=output3[0]
        op2=output3[1]['Overweight']
        assert_frame_equal(op1,op3_output)
#            self.assertIs(op1,op1,"should be "+op1)
        self.assertEqual(op2,3,"should be 3")
            



if __name__=="__main__":
    unittest.main()









