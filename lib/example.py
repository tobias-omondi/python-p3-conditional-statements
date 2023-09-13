# Python does not require 
# the variable to be declared
# or initialized prior to the
# conditional. In Python, a 
# variable can be in scope for
# the entire class or function. Therefore, we can use the owner variable for the rest of the class since it is in local scope.


# dog ="cuddy"

# if dog == "hungry":
#     owner ="Reflilling food bowl"
# elif dog =="thirsty":
#     owner ="refilling water bowl"
# elif dog =="playful":
#     owner ="playing tug_of_war"
# elif dog =="cuddly":
#     owner ="snuggling"
# else:
#     owner = "Reading newpaper."

# Use of the finally keyword at the end of a try/except statement allows us to perform actions that we want to occur regardless of whether or not an exception has been thrown.


# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")


dog = "cuddly"

dict_map = {
    "hungry": "Refilling food bowl.",
    "thirsty": "Refilling water bowl.",
    "playful": "Playing tug-of-war.",
    "cuddly": "Snuggling.",
}

# Remember that a dictionary's .get() method lets us set a default value!
owner = dict_map.get(dog, "Reading newspaper.")