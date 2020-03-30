def Home():
    print(".........................")
    print("           HOME          ")
    print(".........................")
    print("1> Create Account")
    print("2> View Account List")
    print("3> Create Journal Entry")
    print("4> View Balance Sheet")
    print("4> View Income Statement")
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
    

def SelectAccount(Accounts, text, firstAccount=0):
    """
    Return Selected Account from Account List
    """
    # account list
    for i in Accounts:
        print(str(i) + " - " + str(Accounts[i]["Account Name"]) + " - " + str(Accounts[i]["Balance"]))

    selected = False
    while selected == False:
        account = input(text)
        if account == "":
            continue
        account = int(account)
        if account == firstAccount:
            print("You can't select the same account twice. try again")
            continue
        if account in Accounts:
            print(str(account) + " Selected")
            selected = True
        else:
            print(str(account) + " doesn't exist" )
    
    return account

def JournalEntry(Accounts):
    """
    Create journal entries in the ledger
    """
    # account list
    # for i in Accounts:
    #     print(str(i) + " - " + str(Accounts[i]["Account Name"]) + " - " + str(Accounts[i]["Balance"]))

    # # select account 
    # selected = False
    # while selected == False:
    #     account = input("Select an Account by number> ")
    #     if account == "":
    #         continue
    #     account = int(account)
    #     if account in Accounts:
    #         print(str(account) + " Selected")
    #         account = True
    #     else:
    #         print(str(account) + " doesn't exist" )
    #debit
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

def PrintLedger():
    """
    Print the ledger of journal entries
    """
    pass

def SetAmount(transType):
    """
    Set the amount of the transaction
    """
    if transType == "DR":
        text = "How much are you Debiting?> "
    else:
        text = "How much are you Crediting?>  "
    
    amountSet = False
    while amountSet == False:
        try:
            amount = int(input(text))
            amountSet = True
        except:
            print("please input a number")

    return amount

def SetBalance(accountOne, accountTwo, amount, amount2, transType, transType2):
    """
    Check whether the normal balance should increase or decrease the balance
    and set the new balance accordingly
    """
    acctType = Accounts[accountOne]["Type"]
    acct2Type = Accounts[accountTwo]["Type"]
    balance = 0 
    balance2 = 0
    
    if acctType == "A":
        if transType == "DR":
            balance = Accounts[accountOne]["Balance"] + amount
        else:
            balance = Accounts[accountOne]["Balance"] - amount
    elif acctType == "L":
        if transType == "DR":
            balance = Accounts[accountOne]["Balance"] - amount
        else:
            balance = Accounts[accountOne]["Balance"] + amount
    elif acctType == "E":
        if transType == "DR":
            balance = Accounts[accountOne]["Balance"] - amount
        else:
            balance = Accounts[accountOne]["Balance"] + amount

    # Account Two
    if acct2Type == "A":
        if transType2 == "DR":
            balance2 = Accounts[accountTwo]["Balance"] + amount
        else:
            balance2 = Accounts[accountTwo]["Balance"] - amount
    elif acctType == "L":
        if transType2 == "DR":
            balance2 = Accounts[accountTwo]["Balance"] - amount
        else:
            balance2 = Accounts[accountTwo]["Balance"] + amount
    elif acctType == "E":
        if transType2 == "DR":
            balance2 = Accounts[accountTwo]["Balance"] - amount
        else:
            balance2 = Accounts[accountTwo]["Balance"] + amount

    return balance, balance2

def TransType():
    """
    Set whether you are doing a DR or a CR to the account
    """
    transtypeSelected = False
    while transtypeSelected == False:
        transType = input("is this a DR or a CR?").upper()
        if transType == "DR":
            transtypeSelected = True
        elif transType == "CR":
            transtypeSelected = True
        else:
            print("Please select DR or CR")

    return transType

Accounts = {
    1000: {"Account Name": "Cash", "Balance":0, "Type":"A"},
    2000: {"Account Name": "Accounts Payable", "Balance":0, "Type":"L"},
    3000: {"Account Name": "Retained Earnings", "Balance":0, "Type":"E"},
    9000: {"Account Name": "Opening Equity", "Balance":0, "Type":"E"}
}


#loop
while True:
    Home()
    print("Please make a selection")
    selection = input("> ")
    if selection == "1":
        newAccountTuple = CreateAccount(Accounts)
        newAccount = newAccountTuple[0]
        newAccountNumber = newAccountTuple[1]
        Accounts[newAccountNumber] = newAccount[newAccountNumber]
    if selection == "2":
        PrintAccounts(Accounts)
    if selection == "3":
        
        accountOne = SelectAccount(Accounts, "Select Account ONE by number> ")
        transType = TransType()
        amount = SetAmount(transType)

        accountTwo = SelectAccount(Accounts, "Select Account TWO by number> ", accountOne)
        if transType == "DR":
            transType2 = "CR"
        else:
            transType2 = "DR"
        amount2 = SetAmount(transType2)
        
        #check balance 
        if amount == amount2:
            balanceTuple = SetBalance(accountOne, accountTwo, amount, amount2, transType, transType2)
            newBalAcct1 = balanceTuple[0]
            newBalAcct2 = balanceTuple[1]
            Accounts[accountOne]["Balance"] = newBalAcct1
            Accounts[accountTwo]["Balance"] = newBalAcct1
        else:
            print("Sorry the transaction didn't balance. Try again.")
        
        
        # accountTwo = SelectAccount(Accounts, "Select Account TWO by number> ")
        # JournalEntry(Accounts)




# print("credit was " + str(credit) + " and debit was " + str(debit))
