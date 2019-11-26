# thecouponcode.py
'''
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".
'''
import time, datetime


def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code != correct_code:
        return False
    # Clean up the comma's so we can split on spaces
    current_date = current_date.replace(',','')
    expiration_date = expiration_date.replace(',','')

    # Split on spaces
    lstcurrent_date = current_date.split(" ")
    lstexpiration_date = expiration_date.split(" ")

    # lets store the month as a number
    lstcurrent_date.append(int(month_string_to_number(lstcurrent_date[0])))
    lstexpiration_date.append(int(month_string_to_number(lstexpiration_date[0])))

    #str(lstcurrent_date[1]) + " " + str(lstcurrent_date[3]) + " " + str(lstcurrent_date[2])
    if lstcurrent_date[2] > lstexpiration_date[2]:
        return False
    elif lstcurrent_date[2] < lstexpiration_date[2]:
        return True
    else:
        if lstcurrent_date[3] > lstexpiration_date[3]:
            return False
        elif lstcurrent_date[3] < lstexpiration_date[3]:
            return True
        else:
            if lstcurrent_date[1] > lstexpiration_date[1]:
                return False
            elif lstcurrent_date[1] < lstexpiration_date[1]:
                return True
            else:
                return True




def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()
    return m[s]



def month_string_to_number(string):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = string.strip()[:3].lower()
    return m[s]

print(check_coupon('123','123','September 5, 2014','October 1, 2014'))
print(check_coupon('123a','123','September 5, 2014','October 1, 2014'))