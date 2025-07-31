#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
WILLIAMS KWAO'S Personal Assistant
A command-line tool that collects personal details and displays a customized summary

Author: [Your Name]
Date: July 2025
"""

def collect_user_info():
    """Collect personal information from the user"""
    print("\n" + "="*40)
    print(" WILLIAMS KWAO ASSISTANT".center(40))
    print("="*40 + "\n")
    
    print("Please answer the following questions:\n")
    
    user_data = {
        'name': input("What is your name? : "),
        'age': input("How old are you?: "),
        'color': input("What is your favorite color?: "),
        'food': input("What is your favorite food?: "),
        'city': input("Which city do you live in?: "),
        'shs': input("Which Senior High School did you attend?: "),
        'team': input("What is your favorite soccer team?: ")
    }
    
    return user_data

def generate_summary(user_data):
    """Generate a personalized summary based on user input"""
    print("\n" + "="*40)
    print("YOUR PERSONALIZED SUMMARY".center(40))
    print("="*40 + "\n")
    
    print(f"Hello, {user_data['name']}!")
    print(f"You are {user_data['age']} years old and love the color {user_data['color'].lower()}.")
    print(f"Your favorite food is {user_data['food'].lower()} - yum!")
    print(f"You attended {user_data['shs']} and proudly support {user_data['team']}.")
    print(f"Life in {user_data['city']} must be treating you well!\n")
    
    print("="*40)
    print("Thanks for using Simple Personal Assistant!".center(40))
    print("="*40)

def main():
    """Main function to run the personal assistant"""
    try:
        user_data = collect_user_info()
        generate_summary(user_data)
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()