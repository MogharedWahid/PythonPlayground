from art import logo, vs
from game_data import data
import random

def get_compare():
    compare_a = random.choice(data)
    compare_b = random.choice(data)
    while compare_a == compare_b:
        compare_b = random.choice(data)
    return compare_a, compare_b

def display_compare(compare_a_dict, compare_b_dict):
    print(f"Compare A: {compare_a_dict['name']}, a {compare_a_dict['description']} from {compare_a_dict['country']}.")
    print(vs)
    print(f"Compare B: {compare_b_dict['name']}, a {compare_b_dict['description']} from {compare_b_dict['country']}.")

def check_answer(answer, compare_a, compare_b):
    if answer == 'a':
        return compare_a['follower_count'] > compare_b['follower_count']
    elif answer == 'b':
        return compare_b['follower_count'] > compare_a['follower_count']
    return False

def play_game():
    print(logo)
    score = 0
    while True:
        compare_a, compare_b = get_compare()
        display_compare(compare_a, compare_b)
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        
        if answer not in ['a', 'b']:
            print("Invalid input! Please type 'A' or 'B'.")
            continue  

        if check_answer(answer, compare_a, compare_b):
            score += 1
            print("\n" * 5)
            print(logo)
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

play_game()

