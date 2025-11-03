userReply = input("""Would you like to buy stamps, buy an envelope, or make a copy? 
(Enter stamps, envelope, or copy) """)
if userReply == "stamps":
    print("Stamps can be chosen from.")
elif userReply == "envelope":
    print("Can choose any size of envelope.")
elif userReply == "copy":
    copies = input("How many copies needed? (Number) ")
    print("Will print {} copies".format(copies))
else:
    print("Thank you for visiting. See you again!!!")