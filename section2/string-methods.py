message = "Hello there. My name is Sadık Turan"

# message = message.upper()
# message = message.lower()

# message =message.title()

# message = message.capitalize()

# message = message.strip()

# message = message.split()
# message = "---".join(message)

# message = message.split(".")


index = message.find("Sadık")
#isFound = message.startswith("H")
isFound = message.endswith("n")

message = message.replace("Sadık", "Çınar")
message = message.replace(" ", "*")


message = message.center(50)


print(message)
print(index)
print(isFound)