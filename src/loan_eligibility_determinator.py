#!/usr/bin/env python3

"""This program will check a applicant's eligbility for a loan."""

__authors__      = "Christian Lussier, Trent Faulkner, Robert Samuel, Mike Spurr"
__date__        = "10 Dec 2018"


def start_up_message():
    """Contains the programs start-up message."""
    print("CS102 - Final Project - Christian Lussier, Mike Spurr, Trent Faulker, Robert Samuel") # output information about program
    print() # spacing line for better readability.
    print("Welcome to the Loan Eligibility Determinator!") # output program name
    print("--------------------------------------------------------------------------------")
    print("| * About The Program: This program is for checking a applicant's eligibility  |\n| for a loan from a bank. The banker should ask the user questions and record  |\n| their Yes or No answers in the program. There are two sets of questions: one |\n| quick set and one longer set for more interesting cases. The program will    |\n| give a determination on whether the user should recieve a loan.              |")
    print("--------------------------------------------------------------------------------")
    print() # spacing line for better readability.
# End start_up_message function


def restart_program_menu():
    """Function contains the code that will allow the user to choose if they
    want to restart the program."""
    user_rsrt_decision = input("Do you want to restart the program? YES or NO? --- ") # prompts and gets user decision to restart program
    if user_rsrt_decision == "YES" or user_rsrt_decision == "yes" or user_rsrt_decision == "Yes" or user_rsrt_decision == "y": # checks to see if user responded "yes"
        print() # spacing line for better readability.
        print() # spacing line for better readability.
        main()
        print() # spacing line for better readability.
    else:
        print() # spacing line for better readability.
        print("Closing the program!")
        print() # spacing line for better readability.
# End restart_program function


def save_file(applicant_name, eligbility_status_str, question_set_status):
    """Function that allows the user to choose if they want to change their
    current applicant's name & loan eligibility information to a text file."""
    save_file_question = input("Do you want to save the applicants's loan eligibility status to a text file? YES or NO -- ") # prompts and gets user decision to save information
    if save_file_question == "YES" or save_file_question == "yes" or save_file_question == "Yes": # checks to see if user responded "yes"
        chosen_file_name = input("Please enter a new or already created '.txt' file name to save user information to -- ") # prompts user for and gets user's input on what file to create or save to
        save_file = open(chosen_file_name,'a+') # opens previously created file, creates new file if necessary
        save_file.write(applicant_name + " was determined to be: " +  eligbility_status_str + " -- based on " + question_set_status + "\n") # writes applicant loan eligbility information to file
        save_file.close() # closes the file.
    else:
        print("Data will not be saved.") # prints that data will not be saved if user chooses not to save


def prelim_q_analyzer(in1_bool, in2_bool, in3_bool):
    """The analyzer code/equation for the fast-track/preliminary question set."""
    return in1_bool and in2_bool and in3_bool


def indepth_q_analyzer(in1_bool, in2_bool, in3_bool, in4_bool, in5_bool, in6_bool, in7_bool):
    """The analyzer code/equation for the in-depth question set."""
    return in1_bool and in2_bool or in3_bool and in4_bool or in5_bool and in6_bool and in7_bool


def main():
    """The main 'driver' function of the program."""
    applicant_name = input("What is the applicant's name? -- ")
    print() # spacing line for better readability.
    which_qs = input("Do you want to begin with 3 fast-track questions? Type YES if you do, otherwise, hit enter and the program will move on to a broader set of questions! -- ") # prompts and gets user decision about choosing a question set
    print("Please record applicant responses to the asked questions!") # tells the user some helpful information

    if which_qs == "YES" or which_qs == "yes" or which_qs == "Yes": # if statement that checks to see if user wants to do the 3 fast-track/preliminary questions
        print("** 3 Fast-Track Questions **") # says what set of questions is being used
        question_set_status = "Fast-Track" # sets question set being used to a variable
        ## Question 1
        q1_answer = input("1) Does the applicant present themselves well? YES or NO? -- ") # gets user input for prompted question
        q1_list = [] # creates list where question 1 answer boolean will be stored.
        if q1_answer == "YES" or q1_answer == "yes" or q1_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            q1_list = [True]
        else:
            q1_list = [False]

        ## Question 2
        q2_answer = input("2) Does the applicant have at least a credit score of at least 700 ('Good')? YES or NO? -- ") # gets user input for prompted question
        q2_list = [] # creates list where question 2 answer boolean will be stored.
        if q2_answer == "YES" or q2_answer == "yes" or q2_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            q2_list = [True]
        else:
            q2_list = [False]

        ## Question 3
        # Inspired by https://www.entrepreneur.com/article/227191
        q3_answer = input("3) Does the applicant have adequate cash flow to repay the loan? YES or NO? -- ") # gets user input for prompted question
        q3_list = [] # creates list where question 3 answer boolean will be stored.
        if q3_answer == "YES" or q3_answer == "yes" or q3_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            q3_list = [True]
        else:
            q3_list = [False]

        # Go through user responses and determine eligbility:
        for a in q1_list:
            for b in q2_list:
                for c in q3_list:
                    prelim_bool = prelim_q_analyzer(a,b,c)

        print() # prints a blank line for spacing.
        print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.

        if prelim_bool == True:
            print(applicant_name + " has been determined to be ELIGIBLE for the loan based off the fast-track/preliminary questions.")
            eligbility_status_str = "ELIGIBLE"
            print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.
            print() # prints a blank line for spacing.
        else:
            print(applicant_name + " has been determined to be INELIGIBLE for the loan based off the fast-track/preliminary questions.")
            eligbility_status_str = "INELIGIBLE"
            print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.
            print() # prints a blank line for spacing.
            print("Move on to the broader set of questions.")
    # End fast-track/preliminary questions
    else:
        print("*** 7 In-Depth Questions ***") # says what set of questions is being used
        question_set_status = "In-Depth" # sets question set being used to a variable
        indpth_q1_answer = input("1) Is the applicant in good standing with the bank? YES or NO? -- ") # gets user input for prompted question
        indpth_q1_list = [] # creates list to store user response as boolean
        if indpth_q1_answer == "YES" or indpth_q1_answer == "yes" or indpth_q1_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q1_list = [True]
        else:
            indpth_q1_list = [False]

        ## Question 2
        #https://www.experian.com/blogs/ask-experian/credit-education/score-basics/what-is-a-good-credit-score/
        indpth_q2_answer = input("2) Is the applicant's credit score above a 580 ('Fair')? YES or NO? -- ") # gets user input for prompted question
        indpth_q2_list = [] # creates list to store user response as boolean
        if indpth_q2_answer == "YES" or indpth_q2_answer == "yes" or indpth_q2_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q2_list = [True]
        else:
            indpth_q2_list = [False]

        ## INDEPTH Question 3
        # https://www.entrepreneur.com/article/227191
        indpth_q3_answer = input("3) Does the applicant have enough (or close to enough) collateral for their requested loan amount; or they have a way around having collateral? YES or NO? -- ") # gets user input for prompted question
        indpth_q3_list = [] # creates list to store user response as boolean
        if indpth_q2_answer == "YES" or indpth_q2_answer == "yes" or indpth_q2_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q3_list = [True]
        else:
            indpth_q3_list = [False]

        ## INDEPTH Question 4
        # https://www.finder.com/business-loan-interview
        indpth_q4_answer = input("4) Is the term for loan repayment requested by the applicant realistic? YES or NO? -- ") # gets user input for prompted question
        indpth_q4_list = [] # creates list to store user response as boolean
        if indpth_q4_answer == "YES" or indpth_q4_answer == "yes" or indpth_q4_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q4_list = [True]
        else:
            indpth_q4_list = [False]

        ## INDEPTH Question 5
        indpth_q5_answer = input("5) Will the applicant be using the loan for a practical/realistic purpose that won't interfere with their ability to repay the loan? YES or NO? -- ") # gets user input for prompted question
        indpth_q5_list = [] # creates list to store user response as boolean
        if indpth_q5_answer == "YES" or indpth_q5_answer == "yes" or indpth_q5_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q5_list = [True]
        else:
            indpth_q5_list = [False]

        ## INDEPTH Question 6
        indpth_q6_answer = input("6) Does the applicant currently have any unpaid debts/outstanding payments? YES or NO? -- ") # gets user input for prompted question
        indpth_q6_list = [] # creates list to store user response as boolean
        if indpth_q6_answer == "YES" or indpth_q6_answer == "yes" or indpth_q6_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q6_list = [True]
        else:
            indpth_q6_list = [False]

        ## INDEPTH Question 7
        indpth_q7_answer = input("7) Is the applicant currently employed? YES or NO? -- ") # gets user input for prompted question
        indpth_q7_list = [] # creates list to store user response as boolean
        if indpth_q7_answer == "YES" or indpth_q7_answer == "yes" or indpth_q7_answer == "Yes": # checks user answer, if yes boolean set as true, if not set as false
            indpth_q7_list = [True]
        else:
            indpth_q7_list = [False]

        # Go through user responses and determine eligbility:
        for a in indpth_q1_list:
            for b in indpth_q2_list:
                for c in indpth_q3_list:
                    for d in indpth_q4_list:
                        for e in indpth_q5_list:
                            for f in indpth_q6_list:
                                for g in indpth_q7_list:
                                    indepth_bool = indepth_q_analyzer(a,b,c,d,e,f,g)
        print() # prints a blank line for spacing.
        print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.

        if indepth_bool == True:
            print(applicant_name + " has been determined to be ELIGIBLE for the loan based off the fast-track/preliminary questions.") # outputs determination information for eligible applicants
            eligbility_status_str = "ELIGIBLE" # sets applicant eligbility status
            print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.
            print() # prints a blank line for spacing.
        else:
            print(applicant_name + " has been determined to be INELIGIBLE for the loan based off the fast-track/preliminary questions.") # outputs determination information for ineligible applicants
            eligbility_status_str = "INELIGIBLE" # sets applicant eligbility status
            print("--------------------------------------------------------------------------------") # prints out line for box that will contain user eligbility.
            print() # prints a blank line for spacing.

    save_file(applicant_name, eligbility_status_str, question_set_status) # loads the save menu with variables that will be saved if user chooses to do so
    restart_program_menu() # loads the restart program menu
# End main

# Call needed functions:
start_up_message() # prints the start-up message
main() # runs the main "report"
