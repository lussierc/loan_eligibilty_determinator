#!/usr/bin/env python3
"""application.py  A program to follow the boolean values and calculations to determine a decision. Please see the lab assignment document for details."""

__author__      = "Christian Lussier, Trent Faulkner, Robert Samuel, Mike Spurr"
__date__        = "3 October 2018"




def myAND(in1_bool, in2_bool, in3_bool):
    return in1_bool and in2_bool and in3_bool


def main(): # lead function
    # defines the list of patients:
    Patient_list = ['Anne', 'Bernard', 'Christian', 'Trent', 'Robert', 'Pascal', 'Benjamin Buttons', 'Tester'] # The names of the patients for whom the data belongs to.
    # define the list of true and false values:
    Nausea_list = [True, True, False] # Patients results for if they have nausea
    Fever_list = [True, True, False] # Patients results for if they have a Fever
    Cough_list = [True, True, False] # Patients results for if they have a unusual cough

    # Header/Program Introduction information:
    print("") # Prints a blank line to make output look cleaner
    print("----- Welcome to Dr. Racket's Flu Clinic! -----") # Tells the user what the program is
    print("This program will help you decide if you need to set up an appointment.") # Tells the user what the program does.
    print("If the program outputs YES, the patient should schedule an appointment! They might be sick.") # Tells the user what possible output means
    print("If the program outputs NO, the patient should not schedule an appointment. They seem to be fine.") # Tells the user what possible output means
    print("") # Prints a blank line to make output look cleaner

    truth_dic1 = {} # dictionary where the truth data will be stored.

    # Checker:
    for a in Nausea_list:
        for b in Fever_list:
            for c in Cough_list:
                myAND_bool = myAND(a,b,c)
                truth_dic1[str(a) + " AND " + str(b) + " AND " + str(c)] = myAND_bool # Adds information to dictionary/boolean

    print("Analyzing Data.....") # Informational line
    print("..... Printing Output: ") # Informational line -- tells user their output is about to print


    print("__OR Column__")
    for i in truth_dic1:
        print("  ",i, ":", truth_dic1[i])

    counter = 0 # sets the value of the counter to 0
    for i in truth_dic1: # iterates through the information in truth_dic1
        if truth_dic1[i] == True: # checks if the boolean value equals True
            print("Patient Name:", Patient_list[counter], "----", "YES!") # Outputs patient information & "YES!" because it was True
        elif truth_dic1[i] == False: # checks if the boolean value equals False
            print("Patient Name:", Patient_list[counter], "----", "NO!") # Outputs patient information & "NO!" because it was False
        counter += 1 # ups the value of the counter by 1

    print("") # Prints a blank line to make output look cleaner
    print("------ The program is finished checking the possible patient data! ------") # Tells the user the program is done checking/analyzing data
#end of main()

main() # driver function
