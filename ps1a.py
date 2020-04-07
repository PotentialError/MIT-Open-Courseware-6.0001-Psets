# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:00:10 2020

@author: Michael Rodyushkin
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25
current_saving = 0
r = 0.04
months = 0
while current_saving < total_cost*portion_down_payment:
    current_saving += current_saving*r/12
    current_saving += annual_salary/12 * portion_saved
    months += 1
print("Number of months:", months)