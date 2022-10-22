"""The Credit Card Simulator starter code
Author: Michael Guerzhoy.  Last modified: Oct. 3, 2022
"""

def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global disabled
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
        
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None   

    disabled = False 

def date_same_or_later(day1, month1, day2, month2):
    if (day1 == day2 and month1 == month2) or (month1 > month2) or (month1 == month2 and day1 > day2):
        return True
    return False
    
def all_three_different(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3 and c3 == None:
        return False
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    return False

def update_intst(month):
    global last_update_month, cur_balance_owing_intst, cur_balance_owing_recent
    month_gap = month - last_update_month
    if month > last_update_month:
        cur_balance_owing_intst *= 1.05**month_gap
        cur_balance_owing_intst += cur_balance_owing_recent*1.05**(month_gap-1)
        cur_balance_owing_recent = 0

def purchase(amount, day, month, country):
    global last_update_day, last_update_month, last_country, last_country2, cur_balance_owing_recent, cur_balance_owing_intst, disabled
    if all_three_different(country, last_country, last_country2) == True:
        disabled = True
    if disabled == True or not date_same_or_later(day, month, last_update_day, last_update_month) or all_three_different(country, last_country, last_country2) == True:
        return "error"
    update_intst(month)
    cur_balance_owing_recent += amount
    last_update_day, last_update_month = day, month
    last_country2 = last_country
    last_country = country

def amount_owed(day, month):
    global last_update_day, last_update_month, cur_balance_owing_recent, cur_balance_owing_intst
    print(date_same_or_later(day, month, last_update_day, last_update_month))
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    update_intst(month)
    last_update_day, last_update_month = day, month
    return cur_balance_owing_recent + cur_balance_owing_intst
    
def pay_bill(amount, day, month):
    global cur_balance_owing_intst, cur_balance_owing_recent, last_update_day, last_update_month
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        return "error"
    update_intst(month)
    last_update_day, last_update_month = day, month
    if amount >= cur_balance_owing_intst:
        cur_balance_owing_recent -= (amount - cur_balance_owing_intst)
        cur_balance_owing_intst = 0
    else:
        cur_balance_owing_intst -= amount
    return cur_balance_owing_intst + cur_balance_owing_recent    
        
initialize()		
    
if __name__ == '__main__':

    # TESTING THE PURCHASE FUNCTION
    print()
    initialize()

    # making a purchase with a disabled card on a later date should update the date
    initialize()
    purchase(50, 1, 1, "c")
    purchase(50, 1, 1, "b")
    purchase(25, 1, 1, "a")     # card is disabled here
    purchase(0, 1, 12, "pp")
    print(amount_owed(1, 2))
    if amount_owed(1, 2) == 'error' and amount_owed(1, 12) == 162.8894626777442:
        print("test P_IDTC passed")
    else:
        print(amount_owed(1, 12))   # problem found: interest not applied after card disabled
        all_tests_passed = False


    # TESTS FOR THE INTEREST FUNCTION
    print()
    initialize()

    # just a test idk what to call it
    initialize()
    purchase(100, 1, 1, "a")
    purchase(100, 1, 1, "b")
    purchase(100, 1, 1, "c")        # card disabled
    purchase(100, 20, 1, "a")       # disabled card still updates day
    if last_update_day == 20:
        print("test M_UD passed")
    else:
        all_tests_passed = False
    purchase(100, 17, 4, "a")       # disabled card still updates month
    purchase(100, 1, 1, "a")        # doesnt update because invalid date
    if (last_update_day, last_update_month) == (17, 4):
        print("test M_UMD passed")
    else:
        all_tests_passed = False