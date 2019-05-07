documentary = "Documentary movie Titanic"
drama = "Drama movie Home Alone"
comedy = "Comedy movie Ironman"
dramedy = "Dramedy movie Gone With a Wind"

print("Rate documentary movie from 1 to 5, please")
response1 = input() #documentary
print("Rate drama movie from 1 to 5, please")
response2 = input() #drama
print("Rate comedy movie from 1 to 5, please")
response3 = input() #comedy


if response1 == "4" and response1 == "5":
    print("watch {}.".format(documentary))
elif response1 == "3" and response1 == "2" and response1 == "1" and response3 == "4" and response3 == "5" and response2 == "4" and response2 == "5":
    print("watch {}.".format(dramedy))
elif response2 == "4" and response2 == "5":
    print("watch {}.".format(drama)) 
elif response3 == "4" and response3 == "5":
    print("watch {}.".format(comedy))
else:
    print("Just read a book")