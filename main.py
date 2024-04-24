from mymodule import runner
from currency import exchange_currency

db = {}

while True:
    runner()
    select = input('Select (1-add_account, 2-balance, 3-transaction, 4-balance_check, 0-exit): ')
    if select == '1':
        a = input('Add account number: ')
        if len(a) == 5 and a[:2] == 'TB' and a[2:].isdigit() and a not in db.keys():
            db[a] = []
            b = input('Add name: ')
            c = input('Add surname: ')
            db[a].append({'name': b, 'surname': c, 'balance': 0})
            print(f"Account {a} {b} {c}, has been successfully registered")
            print(db)
        else:
            print('Incorrect account number')

    if select == '2':
        a = input('Select your account number: ')
        if a in db.keys():
            b = input('Added balance: ')
            for k, v in db.items():
                if b.isdigit() and a == k:
                    for value in v:
                        value['balance'] += int(b)
                        print(f"{b} GEL was added to the balance")
                        print(db)
        else:
            print('Incorrect account number')

    if select == '3':
        a = input('Select your account number: ')
        b = input('Select person account number: ')
        if a in db.keys() and b in db.keys():
            c = input('How much do you want to transfer?: ')
            transaction = 0
            for k, v in db.items():
                if c.isdigit() and a == k:
                    for value in v:
                        if value['balance'] >= int(c):
                            value['balance'] -= int(c)
                            transaction += int(c)
                        else:
                            print('Not enough balance')
            if transaction > 0:
                for k, v in db.items():
                    if b == k:
                        for value in v:
                            value['balance'] += int(c)
            print(f"{c} GEL was transferred from {a} to {b}")
            print(db)
        else:
            print('Incorrect account')

    if select == '4':
        a = input('Select your account number: ')
        if a in db.keys():
            for k, v in db.items():
                if a == k:
                    for value in v:
                        print(f"Your balance is {value['balance']} GEL, or {exchange_currency(value['balance'])} USD")

    if select == '0':
        print('Exit')
        exit()