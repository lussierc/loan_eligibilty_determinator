#!/usr/bin/env python3
"""This program will check a client's eligbility for a loan."""

__author__      = "Christian Lussier, Trent Faulkner, Robert Samuel, Mike Spurr"
__date__        = "28 Nov 2018"

def start_up_message():
    """Contains the programs start-up message."""
    print() # spacing line for better readability.
    print("Welcome to the Loan Eligibility Checker!")
    print("--------------------------------------------------------------------------------")
    print("** About The Program: This program is for checking a client's eligibility for a loan from a bank.")
    print("The banker should ask the user questions and record their Yes or No answers in the program.")
    print("There are two sets of questions: one quick set and one longer set for more interesting cases.")
    print("The program will then give a determination on whether the user should recieve a loan.")
    print("--------------------------------------------------------------------------------")
    print() # spacing line for better readability.
def main():
    start_up_message()

main()
