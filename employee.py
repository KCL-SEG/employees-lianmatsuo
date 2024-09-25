"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commision, contractRate, commisionRate, hours, comissions):
        self.name = name
        self.contract = contract
        self.commision = commision
        self.contractRate = contractRate
        self.commisionRate = commisionRate
        self.hours = hours
        self.commisionContractNum = comissions

    def get_pay(self):
        pay = 0
        if(self.contract == "salary"):
            if(self.commision == "bonus"):
                pay = self.contractRate+self.commisionRate
            elif(self.commision == "contract"):
                pay = self.contractRate+(self.commisionRate*self.commisionContractNum)
            else:
                pay = self.contractRate
        else:
            if(self.commision == "bonus"):
                pay = (self.contractRate*self.hours)+self.commisionRate
            elif(self.commision == "contract"):
                pay = (self.contractRate*self.hours)+(self.commisionRate*self.commisionContractNum)
            else:
                pay = (self.contractRate*self.hours)

        return pay

    def __str__(self):
        if(self.contract == "salary"):
            if(self.commision == "bonus"):
                return f"{self.name} works on a monthly salary of {self.contractRate} and receives a bonus commision of {self.commisionRate}. Their total pay is {self.get_pay()}."
            elif(self.commision == "contract"):
                return f"{self.name} works on a monthly salary of {self.contractRate} and receives a commision for {self.commisionContractNum} contracts at {self.commisionRate}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.contractRate}. Their total pay is {self.get_pay()}."
        else:
            if(self.commision == "bonus"):
                return f"{self.name} works on a contract of {self.hours} hours at {self.contractRate}/hour and receives a bonus commision of {self.commisionRate}. Their total pay is {self.get_pay()}."
            elif(self.commision == "contract"):
                return f"{self.name} works on a contract of {self.hours} hours at {self.contractRate}/hour and receives a commision for {self.commisionContractNum} contracts at {self.commisionRate}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.contractRate}/hour. Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', "salary", "none", 4000, 0, 0 , 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', "contract", "none", 25, 0, 100, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', "salary", "contract", 3000, 200, 0, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', "contract", "contract", 25, 220, 150, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', "salary", "bonus", 2000, 1500, 0, 0)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', "contract", "bonus", 30, 600, 120, 0)

print(str(billie))