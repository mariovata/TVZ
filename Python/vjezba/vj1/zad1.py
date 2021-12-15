import random


def human():
    user_c = 0

    # while user_c != 1 and user_c != 2 and user_c != 3:
    while user_c not in (1, 2, 3):
        user_c = input("Choose: [R]ock, [P]aper, [S]cissors! ")
        # if user_c == "R" or user_c == "r":
        if user_c in ("R", "r"):
            user_c = 1
        # if user_c == "P" or user_c == "p":
        if user_c in ("P", "p"):
            user_c = 2
        # if user_c == "S" or user_c == "s":
        if user_c in ("S", "s"):
            user_c = 3
    return user_c


def robot():
    computer_c = random.randint(1, 3)
    return computer_c


def check(user_c, robot_c):
    if user_c == robot_c:
        print("The result is a Draw!")
    if user_c == 1 and robot_c == 2:
        print("Robot victory! Paper beats Rock!")
    if user_c == 2 and robot_c == 1:
        print("Human victory! Paper beats Rock!")
    if user_c == 3 and robot_c == 1:
        print("Robot victory! Rock beats Scissors!")
    if user_c == 1 and robot_c == 3:
        print("Human victory! Rock beats Scissors!")
    if user_c == 2 and robot_c == 3:
        print("Robot victory! Scissors beats Paper!")
    if user_c == 3 and robot_c == 2:
        print("Human victory! Scissors beats Paper!")


def conversion(user_c, computer_c):
    if user_c == 1:
        user_c = "Rock"
    elif user_c == 2:
        user_c = "Paper"
    else:
        user_c = "Scissors"
    if computer_c == 1:
        computer_c = "Rock"
    elif computer_c == 2:
        computer_c = "Paper"
    else:
        computer_c = "Scissors"
    return user_c, computer_c


def main():
    user_c = human()
    robot_c = robot()
    check(user_c, robot_c)
    user_c, robot_c = conversion(user_c, robot_c)
    print(f"Human, your choice was {user_c}")
    print(f"My choice was {robot_c}")


main()
