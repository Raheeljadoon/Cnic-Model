import copy
from mmap import PROT_EXEC
import random
from random import randint
from datetime import datetime
import csv



from names import Name




Name = random.choice(Name)
print("Name is :",Name)

from names import Father_Name

Father_Name = random.choice(Father_Name)
print("Father name is:",Father_Name)

from names import Mother_Name 






Mother_Name = random.choice(Mother_Name)
print("Mother name is:",Mother_Name)

Spouse_Name = copy.copy(Father_Name)
print("Spouse Name is:",Spouse_Name)

Religion =["Islam","Christianity","Judaism","Hinduism","Buddhism","Sikhism"]
Religion =random.choice(Religion)
print("Religion is:",Religion)

Gender=["Male","Female"]
Gender=random.choice(Gender)
print("Gender is : ",Gender)

Cnic_Number = 1234567895634
Cnic_Number = randint(0,Cnic_Number)
print("Cnic Number is:",Cnic_Number)

from names import Country

Country = random.choice(Country)
print("Nationality is :" , Country)


def gen_Date_Of_Birth(number):
   for item in range(number):
        yield random.randrange(1980,2003), random.randrange(1, 12), random.randrange(1, 29)

date_Time = gen_Date_Of_Birth(1)

for year, month, date in date_Time:
    print("Date of Birth is :", year ,"/", month ,"/", date)


Random_address_1 = randint(1,1000)


Random_address_2 = randint(1,100)

Permanent_Address = "house no. {0} street no {1}, country {2}".format(Random_address_1, Random_address_2, Country)
print("Permanent address is :" , Permanent_Address)

Present_Address = "house no. {0} street no {1}, country {2}".format(Random_address_1, Random_address_2, Country)
print("Present address is :" , Present_Address)



print("Family_Religion is : " , Religion)

Csv_writer = Name,Father_Name,Mother_Name,Gender, Religion,Country,Permanent_Address,Present_Address,year,month,date

with open('data.csv' ,'w') as file:
    writer = csv.writer(file)
    writer.writerow(Csv_writer) 

    file.closed
   











