# Enter the weekly sales of the store. + 
# Then find out which days the products sell the most and which days sell the least. +
# And display the sales sum and average. +
# Ask the user to include the second week's sales. 
# Then do the calculations for the 2nd week.
day_count = 7

def report():
    sales_w1 = []
    day = 0

    while day<day_count:
        day += 1
        profit = int(input(f"{day}-ci gun ne qeder satis oldu: " ))
        sales_w1.append(profit)
        
    print(sales_w1)
    max_profit = max(sales_w1)
    print('max_profit', max_profit)
    max_profit_day = sales_w1.index(max_profit) + 1
    print('max_profit_day', max_profit_day)

    min_profit = min(sales_w1)
    print('min_profit', min_profit)
    min_profit_day = sales_w1.index(min_profit) + 1
    print('min_profit_day', min_profit_day)

    summary = sum(sales_w1)
    print('summary profit', summary)

    avg = summary/len(sales_w1)

    print('average ', "{:.2f}".format(avg))
    return summary 

print('Birinci hefte ucun daxil edin: ')
summary1 = report()

print('Ikinci hefteni daxil edin! ')
summary2 = report()

if summary1 > summary2:
    print('Birinci hefte daha cox qazanc oldu')
else:
    print('Ikinci hefte daha cox qazanc oldu')

