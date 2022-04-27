# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

days = str(int(365 * 90) - (365 * int(age)))
weeks = str(int(90 * 52) - (52 * int(age)))
months = str(int(90 * 12) - (12*int(age))) 

#Tradition Concatenation Down Here
#print("You have " +  days +" days"+ ", " + weeks + " weeks, and " + months + " months left." )

#FString to combine multiple different data types
print(f"You have {days} days, {weeks} weeks, and {months} months left. ")

print(6 + 4 / 2 - (1 * 2))
