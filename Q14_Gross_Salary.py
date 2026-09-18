def gross_salary(basic):
    if basic <= 10000:
        hra, da = basic * 0.20, basic * 0.80
    elif basic <= 20000:
        hra, da = basic * 0.25, basic * 0.90
    else:
        hra, da = basic * 0.30, basic * 0.95
    return hra, da, basic + hra + da

basic = float(input("Enter basic salary: "))
hra, da, gross = gross_salary(basic)
print("HRA =", hra)
print("DA =", da)
print("Gross Salary =", gross)
