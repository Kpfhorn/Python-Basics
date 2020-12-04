#Modifying Python Strings
###Strings in Python are immutable. this means that they cannot be modified once created. To alter strings, you must assemble a new string using data from the old string

message = 'hello world'
string_list = message.split("")
string_list[4] = ''
message2 = "".join(string_list)
print(message)
print(message2)