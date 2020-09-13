# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:04:34 2020

@author:  Deep Learning خطوتك نحو ال
"""

import split_folders


Data = ('C:/Users/Your_Name/Desktop/DATA/')
Data_Devided = ('C:/Users/Your_Name/Desktop/Data_Devided/')

split_folders.ratio(Data, Data_Devided , seed = 1337, ratio = (0.8,0.0,0.2))