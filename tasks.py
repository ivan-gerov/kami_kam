
import json

TASKS_FILE = "./data/dont_dead_open_inside.json"

with open(TASKS_FILE, 'r') as f:
    TASKS = json.loads(f.read())


def pretty_print_answers(answer_list):
    print("Possible answers:")
    for id_, answer in enumerate(answer_list):
        print(f"{id_}. {answer}")


def base_task(question_string, possible_answers):
    MAX_ITERATIONS = 3
    current_iteration = 1
    while True:
        answers = str(input(question_string))
        if answers in possible_answers:
            print("Correct!\n")
            return 1
        elif current_iteration > 1:
            pretty_print_answers(possible_answers)
        else:
            current_iteration += 1
            print("\nSorry, wrong answer,\nPlease try again :^)\n\n")


def task_controller(tasks):
    for question, answers in tasks.items():
        if base_task(question + ": ",
                     answers):
            pass
    return 1
