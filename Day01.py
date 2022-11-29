#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 02:07:37 2022

@author: kaushiknandansaha
"""
# 100 days of Python
# Assignment Day 1

#1. Create a greeting for your program.
print("Hello!! Welcome to the Band Name Generator.\n")
print("You can create a band name by answering a few question.\n")

#2. Ask the user for the city that they grew up in.
city_name = input("What is the name of the city you grew up in?\n-> ")

#3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?\n-> ")

#4. Combine the name of their city and pet and show them their band name.
band_name = city_name + " " + pet_name 

#5. Make sure the input cursor shows on a new line:
print("The name of the band could be: ", band_name)