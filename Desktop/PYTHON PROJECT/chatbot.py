print("Hello, I am a chatbot")
print("How may I help you?\n")
print("Hit 1 for software installation request")
print("Hit 2 for software update request")
print("Hit 3 for software uninstall request")
print("Hit 4 for software repair request")
print("Hit 5 for other requests")

userInput = int(input("Enter your choice: "))

if userInput == 1:
    softwareNeeded = input("please provide the software name")
elif userInput == 2:
    softwareupdate = input("please provide the software name to be updated")
elif userInput == 3:
    softwareUninstall = input("please provide the software name to ne unintalled")
elif userInput == 4:
    softwareRepair = input("please provide the software name to be repaired")
else:
    softwareRequest = input("please provide deatails of your request")

print("Thank you for using our serice , Our team will get back to you soon")