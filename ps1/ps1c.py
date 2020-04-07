# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:12:37 2020

@author: Michael Rodyushkin
"""
annual_salary = float(input("Enter the starting salary: "))
annual_salary_temp = annual_salary
low = 1
high = 10000
portion_saved = (low+high)/2
epsilon = 100
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
current_saving = 0
r = 0.04
guesses = 0

while abs(current_saving - total_cost * portion_down_payment) >= 100 and guesses < 14:
    current_saving = 0
    months = 0
    annual_salary_temp = annual_salary
    while months < 36:
        current_saving += current_saving*r/12
        current_saving += annual_salary_temp/12 * (portion_saved/10000)
        months+=1
        if months % 6 == 0:
            annual_salary_temp += annual_salary_temp * semi_annual_raise
    if current_saving > total_cost * portion_down_payment:
        high = portion_saved
    else:
        low = portion_saved
    portion_saved = int((low+high)/2)
    guesses+=1
if guesses >= 14:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved/10000)
    print("Steps in bisection search:",guesses)

