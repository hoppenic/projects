

#ask for input on hours worked
#ask for pay per hour


(hoursWorked)=input('How many hours did you work?')
(payHour)=input('How much do you make per hour?')

#float(hoursWorked)=hoursWorked
#float(payHour)=payHour

totalPay=0

if float(hoursWorked) <= 40:
    totalPay=(float(payHour)*float(hoursWorked))
else:
    totalPay=(float(hoursWorked)-40)*(float(payHour)*1.5) + (float(hoursWorked)*float(payHour))
    
#take out 401k(traditional)
#take out taxes

401k=input('What % of your weekly salary should put put into your 401k?')
    
    

print('Your total weekly wage is $',totalPay)
