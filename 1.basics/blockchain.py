# Initialized blockchain
blockchain = []


def get_last_blockchain_value():
    """ Return the last block of the chain """
    if len(blockchain) < 1:
        return None

    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """
    Arguments:
        :transaction_amount: the amount
        :last_transaction: last stransaction
    """
    if last_transaction == None:
        last_transaction = [1]

    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Your transaction amount please: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print(block)
    else:
        print('-' * 30)


def add_new_transaction():
    tx_amount = get_transaction_value()
    add_value(last_transaction=get_last_blockchain_value(),
              transaction_amount=tx_amount)


def verify_chain():
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break

    return is_valid


waiting_for_input = True
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        add_new_transaction()
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'q':
        waiting_for_input = False
       # break  # interrompe il loop
       # continue # skippa solo la corrente iterazione del loop e va direttamente alla successiva
   elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = 2
    else:
        print('Input is invalid')

    if not verify_chain():
        print('Invalid blockchain!')
        break
else: # else dopo il while (viene eseguito quando si esce dal while)
    print('User left!')


print('Done!')
