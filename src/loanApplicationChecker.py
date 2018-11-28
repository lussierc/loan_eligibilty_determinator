#!/usr/bin/env python3
"""This program will check a applicant's eligbility for a loan."""

__author__      = "Christian Lussier, Trent Faulkner, Robert Samuel, Mike Spurr"
__date__        = "28 Nov 2018"


def start_up_message():
    """Contains the programs start-up message."""
    print() # spacing line for better readability.
    print("Welcome to the Loan Eligibility Checker!")
    print("--------------------------------------------------------------------------------")
    print("** About The Program: This program is for checking a applicant's eligibility for a loan from a bank.")
    print("The banker should ask the user questions and record their Yes or No answers in the program.")
    print("There are two sets of questions: one quick set and one longer set for more interesting cases.")
    print("The program will then give a determination on whether the user should recieve a loan.")
    print("--------------------------------------------------------------------------------")
    print() # spacing line for better readability.


def myAND(in1_bool, in2_bool, in3_bool):
    return in1_bool and in2_bool and in3_bool



def main():
    applicant_name = input("What is the applicant's name? -- ")
    print() # spacing line for better readability.
    which_qs = input("Do you want to begin with 3 preliminary questions? Type YES if you do, otherwise the program will move on to a broader set of questions! -- ")
    print("Please record applicant responses to the asked questions!")
    if which_qs == "YES":
        print("** 3 Preliminary Questions **")
        ## Question 1
        q1_answer = input("1) Does the applicant present themselves well? YES or NO? -- ")
        q1_list = []
        if q1_answer == "YES":
            q1_list = [True]
        else:
            q1_list = [False]

        ## Question 2
        q2_answer = input("2) Does the applicant have a 'Good' credit score? YES or NO? -- ")
        q2_list = []
        if q2_answer == "YES":
            q2_list = [True]
        else:
            q2_list = [False]

        ## Question 3
        q3_answer = input("3) Is the applicant in good standing with the bank? YES or NO? -- ")
        q3_list = []
        if q3_answer == "YES":
            q3_list = [True]
        else:
            q3_list = [False]

        truth_dic3 = {} # dictionary where the truth data will be stored.

        for a in q1_list:
            for b in q2_list:
                for c in q3_list:
                    myAND_bool = myAND(a,b,c)
                    truth_dic3[str(a) + " AND " + str(b) + " AND " + str(c)] = myAND_bool # Adds information to dictionary/boolean

        if myAND_bool == True:
            print(applicant_name + "has been determined to be ELIGIBLE for the loan based off the preliminary questions.")
        else:
            print(applicant_name + " has been determined to be INELIGIBLE for the loan based off the preliminary questions.")
            print("Move on to the broader set of questions.")

    else:
        print("*** 7 All-Encompassing Questions ***")

    # print("Analyzing Question Response ...")
    # if q1_answer == "YES":
    #     q1_boolean = True
    # else:
    #     q1_boolean = False
    # if q2_answer == "YES":
    #     q1_boolean = True
    # else:
    #     q2_boolean = False
    # if q3_answer == "YES":
    #     q3_boolean = True
    # else:
    #     q3_boolean = False
    #
    # truth_dic1 = {} # dictionary where the truth data will be stored.
    #
    # myAND_bool = myAND(q1_boolean,q2_boolean,q3_boolean)
    # truth_dic1[str(q1_boolean) + " AND " + str(q2_boolean) + " AND " + str(q3_boolean)] = myAND_bool # Adds information to dictionary/boolean


    # print("... Printing Determination: ")
    #
    # print("__OR Column__")
    # for i in truth_dic1:
    #     print("  ",i, ":", truth_dic1[i])


start_up_message()
main()
