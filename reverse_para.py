print("Enter the string you want to reverse : ")
word = input()
name = word.split()
rev_name = name[::-1]
s = ""
for i in rev_name:
    s = s + i
    s = s + " "
print("The reverse of the above para with words is below")
print(s)
