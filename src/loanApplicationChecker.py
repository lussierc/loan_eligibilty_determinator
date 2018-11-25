#!/usr/bin/env python3
# Group Members: Christian Lussier, Trent Faulkner, Robert Samuel, Mikey Spurr


def myAND(in1_bool, in2_bool):
# function to determine the boolean AND calculation.
    return in1_bool and in2_bool
#end of myAND()


def myOR(in1_bool, in2_bool, in3_bool):
# function to determine the boolean OR calculation.
    return in1_bool or in2_bool
#end of myOR()

def main(): # lead function
#define the list of true and false values

    A_list = [True, True, False, False, True] # Sets the boolean values in a list
    B_list = [True, False, True, False, True] # Sets the boolean values in a list
    C_list = [True, True, False, True, True] # Sets the boolean values in a list
    print(" Welcome to the loan eligibility checker!") # Tells the user what the program is

    truth_dic1 = {} # Creates the second truth dictionary

    # AND Checker:
    for a in A_list:
        for b in B_list:
            for c in C_list:
                myOR_bool = myOR(a,b,c)
                truth_dic1[str(a) + " AND " + str(b) + " AND " + str(c)] = myOR_bool # Adds information to dictionary/boolean

    # Prints information from "OR":
    print("Results:")
    for i in truth_dic1:
        print("  ",i, ":", truth_dic1[i])

    print("") # Prints an empty line to make output look cleaner
    print("Program Complete!") #Tells the user the program is done running
#end of main()

main() # driver function
