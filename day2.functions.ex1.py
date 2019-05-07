documentary = "Documentary movie Titanic"
drama = "Drama movie Home Alone"
comedy = "Comedy movie Ironman"
dramedy = "Dramedy movie Gone With a Wind"

print("Do you enjoy watching documentary?")
response1 = input()
print("Do you enjoy watching drama?")
response2 = input()
print("Do you enjoy watching comedy?")
response3 = input()

if response1 == "yes" and response2 == "no" and response3 == "no":
    print("watch {}.".format(documentary))
elif response1 == "no" and response2 == "yes" and response3 == "yes":
    print("watch {}.".format(dramedy))
elif response1 == "no" and response2 == "yes" and response3 == "no":
    print("watch {}.".format(drama)) 
elif response3 == "yes" and response1 == "no" and response2 == "no":
    print("watch {}.".format(comedy))
else:
    print("Just read a book dude")