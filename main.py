

import requests
import json

'''Question 1: Create a function that takes a list as an argument.'''
#Solution: 

#Create a list
colors = ["red", "yellow", "orange", "brown"]

#create a function with arugument
def nature(colorsoffall):
  for item in colorsoffall:   #Looping through each item in the arguments.
    print(f"Fall is beautiful with {item} colored leaves")    

#call the function and pass the list as argument in it. 
nature(colors)


'''Question 2: Create a function that takes arbitrary arguments *args.'''
#Solution: 

#Create a function with arbitrary arguments in it.
def school(*supplies):
  print(f"You will need following for your school")
  for item in supplies:                 
    print(f" -> {item.title()}")    #Looping through each argument

school("backpack", "lunchbox", "water bottle", "masks")   #calling the function with multiple arguments. 
school("Jackets", "Shoes", "socks")   #Calling the function with another set of arguments. 


'''Question 3: Explain the difference between  **kwargs and *args and show an example (code is optional).'''

# Explaination: *args is used to pass arbitrary number of arguments into a function definition. It uses '*' as syntax. Arbitrary parameter with a single * is a tuple.
#Example for *args

#defnining a function with *args. 
def school(nametag, *supplies):
  print(f"{nametag} will need following for school")
  for item in supplies:                 
    print(f" -> {item.title()}")    #Looping through each argument

school("Julia", "backpack", "lunchbox", "water bottle", "masks")   #calling the function with multiple arguments. 
school("Jade","Jackets", "Shoes", "socks")   #Calling the function with another set of arguments.


##**kwargs is used to pass a keyworded arbitrary number of  argument into the function. It uses ** as syntax and it becomes a dictionary as we add two *. It assigns name of the parameter as key and value the parameter as argument. 
### Example for **kwargs:
def sampleKwargs(**kwargs):
  return kwargs


'''Question 4: Create a function with arbitrary keyword arguments **kwargs.'''
#Solution:


#define a function with **kwargs as arguments along with other arguments. 
def createAccount(firstname, lastname, **securityinfo):
  securityinfo["firstname"] = firstname
  securityinfo["lastname"] = lastname
  return securityinfo

#Passing key, value to the function. we can provide as much information as possible. 
newUser = createAccount("Priyam", "Tiwari", DOB = "02-20-1987", place = "Toronto")
print(newUser)   #Printing the dictionary created. 

'''Question 5: Create a function that prints who is in space right now from within the function. Use the API from http://open-notify.org/Open-Notify-API/People-In-Space/. Print from within the function, don't return any value.'''
#Solution: 

spaceData = requests.get('http://api.open-notify.org/astros.json')
results = json.loads(spaceData.text)
peopleData = results["people"]

#Create a function that will print the names one by one until 

def printPeoplename():
  print("List of people in space:")
  for i in range(len(peopleData)):
   print(peopleData[i]["name"])

printPeoplename()