import numpy as np
import prettytable as pt

# Step 1: get friends' names
friends_input = input("Enter friends' names separated by commas: ")
friends = [name.strip().lower() for name in friends_input.split(",") if name.strip()]

expenses_matrix = np.zeros([len(friends), len(friends)])


def add_expenses():
    print("\nAdd expense")
    amount = float(input("Enter amount: "))
    print("Amount:", amount)

    paid_by = input("Who paid: ").strip().lower()

    participants_input = input("Who is sharing (comma separated): ")
    participants = [p.strip().lower() for p in participants_input.split(",")]
    print("Sharing:", participants)

    share = amount / len(participants)
    print("Each person's equal share:", share)

    paid_by_index = friends.index(paid_by)

    print("\nUpdating balances:")
    for person in participants:
        if person != paid_by:
            person_index = friends.index(person)
            # person owes paid_by their share
            expenses_matrix[person_index][paid_by_index] += share
            print(f"{person} owes {paid_by} {share:.2f}")


def show_balance_matrix():
    print("\nBalance Matrix:")
    table = pt.PrettyTable()
    table.field_names = ["person"] + friends
    for i in range(len(friends)):
        row = [friends[i]] + list(expenses_matrix[i])
        table.add_row(row)
    print(table)

    print("\nWho owes whom:")
    for i in range(len(friends)):
        for j in range(len(friends)):
            if expenses_matrix[i][j] > 0:
                print(friends[i], "owes", friends[j], round(expenses_matrix[i][j], 2))


def add_custom_amounts():
    total_expense = float(input("\nEnter the total expense amount: "))

    custom_amount = {}
    for person in friends:
        custom_amount[person] = float(input(f"Enter amount for {person}: "))

    total_custom = sum(custom_amount.values())
    print(f"Total expense expected: {total_expense}")
    print(f"Total custom amount entered: {total_custom}")

    if total_custom != total_expense:
        print("Warning: custom amounts do not add up to the total expense!")


# ---- Main flow ----
add_expenses()
show_balance_matrix()
add_custom_amounts()