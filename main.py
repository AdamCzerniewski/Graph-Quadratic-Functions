#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 13:49:53 2023

@author: Adam Czerniewski


"""

import xlsxwriter
import math
import openpyxl
from simplifiedExcelUtil import ExcelUtil
from openpyxl.chart import LineChart, Reference


class quadratic:
    
    def __init__(self):
        
       
        self.excelUtil = ExcelUtil()
        print("y = ax² + bx + c") # Formula in use
        
        self.a = float(input("a = ")) # Input a
        self.b = float(input("b = ")) # Input b
        self.c = float(input("c = ")) # Input c
        #print("y = {}x² + {}x + c".format(self.a, self.b, self.c)) # Formula w/ user inputs
        print(f"y = {self.a}x² + {self.b}x + {self.c}")
        
        
        # This is where the file will be written to, the last part (linearFunction) is the name of the file itself, we will append a date and time to the filename  
        self.filename = "/home/coco/pyApps/graphFunctions/quadratic/xlsxGraphs/quadraticFunction" 
        
        fileName = self.filename + ".xlsx" # Makes the file an xlsx file
        print("fileName = ", fileName) # Shows the name of the file
        self.excelUtil.createFile(fileName) # Creates the file      
    
        self.calcValues(self.a, self.b, self.c) 
    
    
    # This function calculates the y values of the inputted equation
    def calcValues(self, a, b, c):
        # Array contains x values from -10 to 10, once inputted in the linear function, it will output the y values
        self.x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
        self.y = [] # y values will be calculated and appended to this array
        
        # Loop goes through each x value in the array and calculates the output
        for i in range(len(self.x)):
            y = self.a * self.a * self.x[i] * self.x[i] + self.b * self.x[i] + self.c # Calculate
            
            self.y.append(y) # Appends the calculated y values to the array
        
            # This writes the data to a specific column
            self.excelUtil.writeData(1,i,self.x[i])
            self.excelUtil.writeData(2,i,y)
         
        self.excelUtil.createExcelChart() 
        
        # Saves excel file    
        self.excelUtil.closeFile()
        
        # Debugs
        print("x values =",self.x)
        print("y values =",self.y)     

    
          



    

q = quadratic()