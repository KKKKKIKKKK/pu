string = "Yojulab !"
len(string)
pass


# copy 
len(string)
9
"ju" in string
True
"Not" in string
False
"Not" not in string
True

#slicing
string[3]
#'u'
string[3:6]
#'ula'
string [3:]
#'ulab !'
string[:-2]
#'Yojulab'


string[3]
pass

# format 
age = 36
txt = "My name is John, I am " + str(age) 
print(txt)
# txt_second
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# NameError: name 'txt_second' is not defined
# txt_second = "My name is John, I am {}."
# txt_second
# 'My name is John, I am {}.'
# txt_second.format(age)
# 'My name is John, I am 36.'

#변수 3개    
quantity = 3    # index 0
itemno = 567    # index 1
price = 49.95   # index 2
myorder = "I want {0} pieces of item {1} for {2} dollars. I have just{2}."

#myorder.format(quantity, itemno, price)
'I want 3 pieces of item 567 for 49.95 dollars. I have just49.95.'
pass  

