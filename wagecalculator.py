

#ask for input on hours worked
#ask for pay per hour


hoursWorked=input('How many hours did you work? ')
payHour=input('How much do you make per hour? ')

#float(hoursWorked)=hoursWorked
#float(payHour)=payHour

totalPay=0

if float(hoursWorked) <= 40:
    totalPay=(float(payHour)*float(hoursWorked))
else:
    totalPay=(float(hoursWorked)-40)*(float(payHour)*1.5) + (float(hoursWorked)*float(payHour))
    
#take out 401k(traditional pre-tax)

retirement=input('What percentage of your weekly salary should put put into your 401k? ')
retirement=(100-float(retirement))/100
totalPay=totalPay*(float(retirement))

#take out taxes after 401k contribution

tax=input('What marginal tax bracket are you in? ')
tax=(100-float(tax))/100
totalPay=totalPay*(float(tax))
    

print('Your total weekly wage less retirement is $',totalPay)
