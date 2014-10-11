# Bartender app. Uses dictionaries!
import random


questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

adjectives = ["Spicy", "Sassy", "Superflous", "Splendid", "Silly"]

nouns = ["Sydney", "Sasquatch", "Sweethome", "Singapore"]

def drinkname():
    """ Combine adjectives and nouns to create random drink names"""
    drinkname = str(random.choice(adjectives)) + ' ' + str(random.choice(nouns))
    return drinkname

def createdrink():
    """ Go through customers likes.. then select ingredient for each like"""
    likes = {}
    drink = []
    for key in questions:
        likes[key] = raw_input(questions[key]+ "(type 'y' if true) ")
    for key in likes:
        if likes[key] in ['y','yes']:
            drink.append(random.choice(ingredients[key]))
    return drink


#preferences = {'Kelsey': [['salt-dusted rim', 'glug of rum', 'twist of lemon peel'],['Splendid Sydney']]}
preferences = {}

def customers(cname):
    """Walks a customer through the drink ordering process"""
    customerdrink = createdrink()
    customerdrinkname = drinkname()
    customerpair = (customerdrink, customerdrinkname)
    if customerpair[0] != []:
        print "Cool, I'll make you a drink with '{}'".format(customerdrink)
        print "I call this one the '{}'.".format(customerdrinkname)
        print "..."
        print "..."
        print "..."

    else:
        print "Well, you don't like anything. No drink for you."
## TEst out the dictionary-- what's working/not working here?
    preferences[cname] = customerpair
    for key in preferences:
        print key
        for item in preferences[key]:
            print item

def main2(cname):
    """Main function: checks if we know what the customer had last and offers that"""
    customername = cname
# If customer is in preferences, as if they want the same thing. Then, give it again or go through whole shebang and update preferences.
    if customername in preferences.keys():
        print "Do you want to have '{}' with '{}' again?".format(preferences[customername][1],preferences[customername][0])
        answer = raw_input('y or n: ')
        if answer == 'y':
            print "Excellent, I'll make you the drink again"
            print "Remember, it's the '{}'.".format(preferences[customername][1])
        else:
            customers(customername)
# If customer not in preferences.. make them a drink and do the whole shebang.     
    else:
        customers(customername)


if __name__ == '__main__':
    """Calls the main function over and over again until customer wants to leave. """
    drinking = True
    cname = raw_input("What's your name?")
    while drinking == True:
        main2(cname)
        print "Done with that alreadY?!"
        if raw_input("Would you like another drink? (y/n) ") == 'y':
            print "OK! You'll have another"
        else:
            drinking = False
            print "Goodbye"
    

