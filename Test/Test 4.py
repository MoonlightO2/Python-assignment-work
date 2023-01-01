def main():
    """To print a names numeric value"""
    name = input("Enter your full name here: ") #enters a name
    name.replace("", "") #removes all spaces
    str.lower(name) #converts all characters to lower case
    output = [] #creates an empty list
    for character in name:
        number = ord(character) - 100 #ASCII code to make a=1
        output.append(number) #adds number to the empty list
    print(sum(output)) #prints sum of output
main()
