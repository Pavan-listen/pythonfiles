import random

def data_gen():
    # List of real names
    real_names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Henry", "Ivy", "Jack"]

    # Initialize an empty list to store the account data
    accounts = []

    # Set of digits to be used in account numbers
    available_digits = set(range(10))

# Loop to generate 20 sets of data
    for i in range(20):
    # Shuffle the real names list to randomize the selection
        random.shuffle(real_names)
    
    # Take the first name from the shuffled list
        name = real_names[0]

    # Shuffle the available digits to randomize the selection
        shuffled_digits = list(available_digits)
        random.shuffle(shuffled_digits)
    
    # Take the first 6 digits to form the account number
        acc_num = ' '.join(str(digit) for digit in shuffled_digits[:6])

        data = {
            'name': name,
            'password': f'password{i+1}',
            'acc_num': acc_num,
            'initial_deposit': (i+1) * 100.0,  # Example initial deposit: 100.0, 200.0, 300.0, ...
            'transaction': [f'{(i+1)*100.0 - 100.0} is Credited', f'{i*50.0} is Debited']  # Example transaction history
        }
        accounts.append(data)
    return accounts


