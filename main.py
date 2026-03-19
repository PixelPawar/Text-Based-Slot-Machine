import random 

MAX_LINES = 3
MIN_BET = 200
MAX_BET = 10000

ROWS = 3
COLS = 3

symbols = {
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbols_values = {
    
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_winnings(columns , lines,bet , values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbols_to_check = column[line]
            if symbol != symbols_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings  , winning_lines


def get_slot_machine_spin(ROWS,COLS,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i , column in enumerate(columns):
            if i != len(columns) -1:
                print(f"{column[row]}",end=" | ")
            else:
                print(f"{column[row]}",end="\n")


def deposit():
    while True:
        amount = input("Enter amount you want to deposit (in ₹):- \n ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Deposit must be greater than 0(zero) !")
        else:
            print("Please enter numerical value !")
    return amount

def get_no_of_lines():
    while True:
        lines = input("How many lines do you want to bet on (1-" + str(MAX_LINES) + ") ? \n")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES :
                break
            else:
                print("Number of lines must be between the specified range !")
        else:
            print("Please enter numerical value !")
    return lines

def bet_per_line():
    while True:
        bet = input(f"How much do you want to bet ?\t[ Minimun {MIN_BET} &\t Maximum {MAX_BET} ] \n")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET :
                break
            else:
                print("Bet must be between ₹200 to ₹1000!")
        else:
            print("Please enter numerical value !")
    return bet

def spin(balance):
    lines = get_no_of_lines()
    while True:
        bet_amount = bet_per_line()
        total_bet = bet_amount * lines
        if total_bet > balance :
            print(f"You do not have enough deposit to bet {bet_amount}. \n Your balance is {balance}")
        else:
            break

    print(f"You are betting ₹{bet_amount} on {lines} Lines. Total bet amount is ₹{bet_amount * lines}")
    

    slot = get_slot_machine_spin(ROWS,COLS,symbols)
    print_slot_machine(slot)
    winning, winning_lines  = check_winnings(slot,lines,bet_amount,symbols_values)
    
    print(f"You won ₹{winning}")
    print(f"You won on lines:",*winning_lines)
    return winning   - total_bet

def main():
    balance = deposit()
    while True :
        print(f"current balance is ₹{balance}")
        answer_spin = input("Press enter to spin (q to quit)")
        if answer_spin.lower() == 'q':
            break
        balance += spin(balance)

    print(f"You left with ₹{balance}")
    




if __name__ == "__main__"  :
    main()