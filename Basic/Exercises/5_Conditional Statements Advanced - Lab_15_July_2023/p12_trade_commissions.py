city = input()
sales = float(input())

Sofia_comm = 0
Varna_comm = 0
Plovdiv_comm = 0
commission = 0

if (city == "Sofia" or city == "Varna" or city == "Plovdiv") and sales > 0:
    if 0 <= sales <= 500:
        Sofia_comm = 0.05
        Varna_comm = 0.045
        Plovdiv_comm = 0.055
        if city == "Sofia":
            commission = sales * Sofia_comm
        elif city == "Varna":
            commission = sales * Varna_comm
        elif city == "Plovdiv":
            commission = sales * Plovdiv_comm
    elif 500 < sales <= 1000:
        Sofia_comm = 0.07
        Varna_comm = 0.075
        Plovdiv_comm = 0.08
        if city == "Sofia":
            commission = sales * Sofia_comm
        elif city == "Varna":
            commission = sales * Varna_comm
        elif city == "Plovdiv":
            commission = sales * Plovdiv_comm
    elif 1000 < sales <= 10000:
        Sofia_comm = 0.08
        Varna_comm = 0.1
        Plovdiv_comm = 0.12
        if city == "Sofia":
            commission = sales * Sofia_comm
        elif city == "Varna":
            commission = sales * Varna_comm
        elif city == "Plovdiv":
            commission = sales * Plovdiv_comm
    elif sales > 10000:
        Sofia_comm = 0.12
        Varna_comm = 0.13
        Plovdiv_comm = 0.145
        if city == "Sofia":
            commission = sales * Sofia_comm
        elif city == "Varna":
            commission = sales * Varna_comm
        elif city == "Plovdiv":
            commission = sales * Plovdiv_comm
    print(f'{commission:.2f}')

else:
    print("error")