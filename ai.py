def Home():
    print(".........................")
    print("           HOME          ")
    print(".........................")
    print("1> Create Account")
    print("2> View Income Statement")
    print("3> View Account List")
    print("4> View Balance Sheet")
    print(".........................")


def CreateAccount(Accounts):
    """
    Create a new account for the list of accounts
    """
    created = False
    while created == False:
        try:
            accountNumber = int(input("enter the account number> "))
            if accountNumber in Accounts:
                print("This account number is already in use. Please try again")
            else:
                created = True
        except:
            print("please enter a number")

    
    created = False
    while created == False:
        accountName = input("enter the account name> ")
        for i in Accounts:
            if Accounts[i]["Account Name"] == accountName:
                print(str(i["Account Name"]))
                print(str(accountName))
                print("This account name is already in use. Please try again")
            else:
                created = True    
     
    created = False
    while created == False:
        acctType = input("please enter the account type (A) - Asset, (L)- Liab, (E)- Equity> ").upper()
        if acctType == "A":
            account = {
                accountNumber: {
                    "Account Name": accountName,
                    "Balance":0,
                    "Type": "A"
                    }
            }
            created = True
        elif acctType == "L":
            account = {
                accountNumber: {
                    "Account Name": accountName,
                    "Balance":0,
                    "Type": "L"
                    }
            }
            created = True
        elif acctType == "E":
            account = {
                accountNumber: {
                    "Account Name": accountName,
                    "Balance":0,
                    "Type": "E"
                    }
            }
            created = True
        else:
            print("Please enter a valid account type")    
    
    #check to see if the account exists already
    created = False
    while created == False:
        if accountNumber in Accounts:
            print("you already have an account with this number")
        else:
            created = True
    
    return account, accountNumber


def PrintAccounts(Accounts):
    for i in Accounts:
        print(str(i) + " - " + str(Accounts[i]["Account Name"]) + " - " + str(Accounts[i]["Balance"]))
    


Accounts = {
    1000: {"Account Name": "Cash", "Balance":0, "Type":"A"},
    2000: {"Account Name": "Accounts Payable", "Balance":0, "Type":"L"},
    3000: {"Account Name": "Retained Earnings", "Balance":0, "Type":"E"},
    9000: {"Account Name": "Opening Equity", "Balance":0, "Type":"E"}
}


#loop
loop = True
while loop:
    Home()
    print("Please make a selection")
    selection = input("> ")
    if selection == "1":
        newAccountTuple = CreateAccount(Accounts)
        newAccount = newAccountTuple[0]
        newAccountNumber = newAccountTuple[1]
        Accounts[newAccountNumber] = newAccount[newAccountNumber]
    if selection == "3":
        PrintAccounts(Accounts)

# #debit
# debitSet = False
# while debitSet == False:
#     try:
#         debit = int(input("Please input the debit> "))
#         debitSet = True
#     except:
#         print("please put in a number")

# #credit
# creditSet = False
# while creditSet == False:
#     try:
#         credit = int(input("Please input the credit> "))
#         creditSet = True
#     except:
#         print("please put in a number")



# print("credit was " + str(credit) + " and debit was " + str(debit))
