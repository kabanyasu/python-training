def main():
    zigyo = calc_business_income()
    kyuyo = calc_employment_income()
    the_total_income = zigyo + kyuyo
    return the_total_income

def calc_dividend_income():
    pass


def calc_business_income():
    income = int(input("今年度の事業収入の合計額はいくらですか？"))
    outcome = int(input("今年度の事業経費合計額はいくらですか？"))
    business_income = income - outcome
    if business_income > 650000:
        return business_income = business_income - 650000
    if business_income < 0:
        pass
    if business_income < 650000:
        return business_income = 0
    return business_income

def calc_employment_income():
    income = int(input("今年度の給与額はいくらですか？"))
    employment_income = income - deducation(income)
    return employment_income
    
def deducation(income):
    if income > 10000000:
        return 2200000
    if income > 6600000:
        return income * 0.1 + 1200000
    if income > 3600000:
        return income * 0.2 + 540000
    if income > 1800000:
        return income * 0.3 +180000
    if income > 1625000:
        return income * 0.4
    return 650000

def calc_retire_income():
    pass

def calc_transfer_income():
    pass

def calc_temporary_income():
    pass

def calc_other_income():
    pass


if __name__ == '__main__': # condsoleから起動した時、ここがtrueになる
    main()_ == '__main__': # condsoleから起動した時、ここがtrueになる
    main()