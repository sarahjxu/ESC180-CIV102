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
    if not date_same_or_later(day, month, last_update_day, last_update_month) and all_three_different(country, last_country, last_country2) == True:
        disabled = True
        return "error"
    if not date_same_or_later(day, month, last_update_day, last_update_month):
        last_country2 = last_country
        last_country = country
        return "error"
    if all_three_different(country, last_country, last_country2) == True or disabled == True:
        disabled = True
        update_intst(month)
        last_update_day, last_update_month = day, month
        return "error"
    update_intst(month)
    cur_balance_owing_recent += amount
    last_update_day, last_update_month = day, month
    last_country2 = last_country
    last_country = country

def amount_owed(day, month):
    global last_update_day, last_update_month, cur_balance_owing_recent, cur_balance_owing_intst
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
    initialize()