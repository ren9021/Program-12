#***************************************************************
#
#  Developer:         Renee White
#  File Name:         Program12.py
#  Description:       This program computes the weekly gross pay of employees
#  
#***************************************************************


#***************************************************************
#
#  Function:     Class Employee
# 
#  Description:  A class called Employee that defines the methods
#                that are used to set and return values.
#
#  Parameters:   self, name, rate, hours
#
#  Returns:      name, hourly_rate, reg_hours, ot_hours,
#                hours_worked (total hours), monthly_reg,
#                monthly_ot, gross, taxes, and net pay.
#
#**************************************************************



class Employee:

    def __init__(self):
        self.__name = ""
        self.__hourly_rate = 7.25
        self.__reg_hours = 0.0
        self.__ot_hours = 0.0
        
        
    def set_name(self, name):
        self.__name = name


    def set_hourly_rate(self, rate):
        self.__hourly_rate = rate


    def set_hours(self, hours):
        if hours <= 40.00:
           self.__reg_hours += hours
        else:
           self.__reg_hours += 40
           self.__ot_hours += hours - 40

        self.__hours_worked = (self.__reg_hours + self.__ot_hours)


    def set_pay(self):
        self.__monthly_reg = self.__reg_hours * self.__hourly_rate
        self.__monthly_ot = self.__ot_hours * self.__hourly_rate * 1.5
        self.__gross = (self.__monthly_reg + self.__monthly_ot)

        if self.__gross < 2000.00:
            self.__taxes = self.__gross * 0.10
        elif self.__gross < 3500.00:
            self.__taxes = self.__gross * 0.15
        elif self.__gross < 6000.00:
            self.__taxes = self.__gross * 0.28
        elif self.__gross < 10000.00:
            self.__taxes = self.__gross * 0.31
        elif self.__gross > 10000.00:
            self.__taxes = self.__gross * 0.36


        self.__net_pay = self.__gross - self.__taxes

        
            
      
#*****************************************************************

                

    def get_name(self):
        return self.__name

    def get_hourly_rate(self):
        return self.__hourly_rate

    def get_reg_hours(self):
        return self.__reg_hours
    
    def get_ot_hours(self):
        return self.__ot_hours

    def get_hours_worked(self):
        return self.__hours_worked

    def get_monthly_reg(self):
        return self.__monthly_reg
    
    def get_monthly_ot(self):
        return self.__monthly_ot

    def get_gross(self):
        return self.__gross

    def get_taxes(self):
        return self.__taxes

    def get_net_pay(self):
        return self.__net_pay







    def __str__(self):
        Output = str("Employee's Name:               %10s\n" % (self.__name))
        Output += str("Regular Hours:                %10.2f\n" % (self.__reg_hours))
        Output += str("Overtime Hours:               %10.2f\n" % (self.__ot_hours))
        Output += str("Total Hours:                  %10.2f\n" % (self.__hours_worked))
        Output += str("Pay Rate:                     %10.2f\n" % (self.__hourly_rate))
        Output += str("Regular Pay:                  %10.2f\n" % (self.__monthly_reg))
        Output += str("Overtime Pay:                 %10.2f\n" % (self.__monthly_ot))
        Output += str("Monthly Gross Pay:            %10.2f\n" % (self.__gross))
        Output += str("Taxes:                        %10.2f\n" % (self.__taxes))
        Output += str("Monthly Net Pay:              %10.2f\n" % (self.__net_pay))
        return Output
    


#***************************************************************
#
#  Function:     main
# 
#  Description:  The main function of the program
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************

def main():
    
    developerInfo()
    
    print('Welcome back to your employee payroll management system!')
    print()
    employees = Employee()
    again = 'y'
    while again == 'y':
        name = input('Enter your name (First Last): ')
        employees.set_name(name)
    
        rate = float(input('Enter your hourly rate: '))
        employees.set_hourly_rate(rate)
    
        for idx in range(1, 5):
            value = float(input('Enter hours worked for week ' + str(idx) + ':' + ' '))
            
        employees.set_hours(value)
    
        employees.set_pay()
        
        print()
        print()
        print(employees)

        again = input('Do you want to calculate another employee? ( Enter Y for YES or N for NO ): ')


# End of the main function


#***************************************************************
#
#  Function:     developerInfo
# 
#  Description:  Prints Programmer's information
#
#  Parameters:   None
#
#  Returns:      Nothing 
#
#**************************************************************
def developerInfo():
    print('Name:     Renee White')
    print('Program:  Twelve')
    print()
    # End of the developerInfo function

# Call the main function.
main()

