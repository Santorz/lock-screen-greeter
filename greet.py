#!/bin/python3

from datetime import datetime
import os

current_time = datetime.now()
greet_text = None
hour_now  = current_time.hour

input = input('Enter your name ---> ')
os.system("clear")

if 0 <= hour_now <= 11:
    greet_text = 'Morning'
if 12 <= hour_now <= 15:
    greet_text = 'Afternoon'
if 16 <= hour_now <= 19:
    greet_text = 'Evening'
if 20 <= hour_now <= 23:
    greet_text = 'Night'

print(f"\n  Good {greet_text} {input} ")
print(f"  The time now is {current_time.hour}:{current_time.strftime('%M')} ")

print(f"  Today is {current_time.strftime('%A')}, {current_time.strftime('%d')} {current_time.strftime('%B')} {current_time.strftime('%Y')} \n")

