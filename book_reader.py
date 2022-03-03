import csv
import time

with open("underground_kingdom.csv") as f:
    decisions_story_tuples = {}
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        decisions_story_tuples[row[0]] = row[1], row[2]

def get_possible_decisions(possible_decisions):
    dec_list = []
    for decision in possible_decisions.split(" ; "):
        dec_list.append(decision)
    if len(dec_list) == 1:
        return dec_list[0], None, None
    elif len(dec_list) == 2:
        return dec_list[0], dec_list[1], None
    else:
        return dec_list[0], dec_list[1], dec_list[2]

def book_reader(curr_story):
    try:
        for line in curr_story:
            for letter in line:
                print(letter, end="")
                time.sleep(0.001)
    except KeyboardInterrupt:
        print(curr_story)
        print('\nYou skipped forward!')

def story_continuation(dec_key):
    curr_story, story_continuation.possible_decisions = decisions_story_tuples[dec_key] 
    book_reader(curr_story)
    print(story_continuation.possible_decisions)

def invalid_input(curr_decision, temp_dict):  #??
    if not curr_decision.isnumeric() or int(curr_decision) not in temp_dict.keys():
        return True

def reading_book():
    temp_dict = {1:"If you run from the strange creature, turn to page 15.", 2:"If you hold your ground and face it, turn to page 10."}
    with open("main_storyline") as f:
        curr_story = f.readlines()
        try:
            for line in curr_story:
                for letter in line:
                    print(letter, end="")
                    time.sleep(0.001)
        except KeyboardInterrupt:
            for line in curr_story:
                print(line, end="")
            print('\nYou skipped forward!')

    while True:
        curr_decision = input("Choose a path (1 or 2): ")
        if invalid_input(curr_decision, temp_dict):
            print('Invalid input')
            continue
        dec_key = temp_dict[int(curr_decision)]
        story_continuation(dec_key)
        decision_a, decision_b, decision_c = get_possible_decisions(story_continuation.possible_decisions)
        break

    while True: 
        if decision_b is None:
            if decision_a == "":
                break

            elif decision_a == "Final end":
                print("Congratulations!")
                break

            else: 
                curr_decision = input("Press 1 to continue: ")
                if curr_decision == 'q':
                    break
                temp_dict = {1:decision_a}
                if invalid_input(curr_decision, temp_dict):
                    print('Invalid input')
                    continue
                dec_key = temp_dict[int(curr_decision)]
                story_continuation(dec_key)
                decision_a, decision_b, decision_c = get_possible_decisions(story_continuation.possible_decisions)  
                continue

        elif decision_b is not None and decision_c is None:
            temp_dict = {1:decision_a, 2:decision_b}
            curr_decision = input("Choose a path (1 or 2): ")
            if curr_decision == 'q':
                break
            if invalid_input(curr_decision, temp_dict):
                print('Invalid input')
                continue
            dec_key = temp_dict[int(curr_decision)]
            story_continuation(dec_key)
            decision_a, decision_b, decision_c = get_possible_decisions(story_continuation.possible_decisions)
            continue

        else:
            temp_dict = {1:decision_a, 2:decision_b, 3:decision_c}
            curr_decision = input("Choose a path (1, 2 or 3): ")
            if curr_decision == 'q':
                break
            if invalid_input(curr_decision, temp_dict):
                print('Invalid input')
                continue
            else:
                dec_key = temp_dict[int(curr_decision)]
                story_continuation(dec_key)
                decision_a, decision_b, decision_c = get_possible_decisions(story_continuation.possible_decisions)
                continue

if __name__ == "__main__":
    introduction = input("Welcome to the secret path book! \nThese pages contain many different adventures you can have as you try to reach the Underground Kingdom. \nFrom time to time as you read along, you will be asked to make a choice. \nYour choice may lead to success or to disaster! \nThe adventures you have will be the result of the decisions you make.\n\nPress Ctrl + C to skip forward!\n\nPress ENTER to continue! ")
    reading_book()
    print("Goodbye")