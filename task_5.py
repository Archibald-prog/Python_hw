income = float(input("Enter your company's income in the last year: "))
costs = float(input("Enter your company's costs in the last year: "))

if costs > income:
    loss = costs - income
    print('Your company ended the year at a loss of ${:.2f}.' .format(loss))
elif costs == income:
    profit = income - costs
    print('Your company ended the year with profit of ${:.2f}.' .format(profit))
elif costs < income:
    profit = income - costs
    print('Your company ended the year with profit of ${:.2f}.'.format(profit))
    sales_margin = income/profit
    print("Your company's sales margin in the last year was {:.2f}." .format(sales_margin))

    staff_strength = int(input('Enter the number of employees in your company: '))
    profit_per_emp = profit/staff_strength
    print('The profit per one employee equals ${:.2f}.' .format(profit_per_emp))





