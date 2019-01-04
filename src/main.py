def main():
    data = read_data()
    koujo_table = read_koujo_table()
    amount_calculator = create_amount_calculator(1.08)
    koujo_calculator = create_koujo_calculator(koujo_table, amount_calculator)
    koujo_amount = koujo_calculator(data)

    return


def read_data():
    pass


def read_koujo_table():
    def get_koujo(amount): 
        if amount > 40000000:
            return 4796000
        if amount > 18000000:
            return 2796000
        if amount > 9000000:
            return 1536000
        if amount > 6950000:
            return 636000
        if amount > 3300000:
            return 427500
        if amount > 1950000:
            return 97500
        return 0
    return get_koujo
    

def create_amount_calculator(zeiritsu):                    
    def calculate_amount(data):
        zeikomi = [zeiritsu * e for e in data]              # map
        amount = reduce(zeikomi, lambda acc, x: acc + x)    # reduce / fold
        return amount
    return calculate_amount


def create_koujo_calculator(table, amount_calculator):
    def calculate_koujo(data):
        amount = amount_calculator(data)
        koujo = table(amount)
        return koujo
    return calculate_koujo


if __name__ == '__main__': # condsoleから起動した時、ここがtrueになる
    main()_ == '__main__': # condsoleから起動した時、ここがtrueになる
    main()