import inquirer
from datetime import datetime
from . import globals
from .utils.util import reset

def customer_loan_selection():
    # Implement select functionality for customer account screen
    question = [
        inquirer.List('selection',
                      message='Choose loan service to avail',
                      choices=['Loan Application', 'Loan Review', 'Cancel']
                      )]
    selection = inquirer.prompt(question)['selection']
    if selection == 'Loan Application':
        customer_loan_application()
    elif selection == 'Loan Review':
        customer_loan_review()
    else:
        reset()


def customer_loan_application():
    # Implement functionality to apply for a loan

    date = datetime.now().strftime("%x")
    for loan in globals.account['loans']:
        if loan['date'] == date:
            print('Cannot apply for two loans on the same day.')
            reset()
    principal = int(input('Enter amount in rs you wish to borrow '))
    tenure = int(input('Enter tenure for which you wish to borrow the principal '))

    print("Principal requested", principal, "Rs.")
    print("For tenure of", tenure, "yrs")
    print("Date Applied:", date)

    globals.account['loans'].append({'principal': principal, 'tenure': tenure, 'status': 'Notified Bank'})
    
    print("""We've notified your bank that you wish to borrow a loan.\n
    Please contact your bank for further details.""")
    reset()


def customer_loan_review():
    # Implement functionality for a customer to review
    # loan application state and loan details
    choices = []
    for loan in globals.account['loans']:
        choices.append(loan['type'] + ' ' + loan['date'])
    choices.append('Cancel')
    question = [inquirer.List('selection',
                  message='Choose loan to review details',
                  choices=choices)]
    selection = inquirer.prompt(question)['selection']
    if selection == 'Cancel':
        reset()
    print()
    t, d = selection.split()
    for loan in globals.account['loans']:
        # loan principal interest due loan status
        if loan['type'] == t and loan['date'] == d:
            print('Principal:', loan['principal'], 'Rs.')
            print('Tenure:', loan['tenure'], 'yrs')
            print('Loan Status:', loan['status'])
            if 'interest' in loan:
                print('Interest Due', loan['interest'])
            print()
            break
    reset()
