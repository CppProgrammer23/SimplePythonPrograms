import random
import string 
import secrets

#print(random.randrange(100,999,5))
#print(random.randrange(100,999,5))
#print(random.randrange(100,999,5))

#################################

#
n=[]
for i in range (100):
    n.append(random.randrange(100,999))
win=random.sample(n,2)
#print(win)
##################################

#Pick a random character from a given String
s = 'Hello'
#print(random.choice(s))
##################################

#Generate  random String of different length 
def get_Rand_Str(length):
    s=string.ascii_letters
    res = ''.join(random.choice(s) for i in range (length))
    return res
#print(get_Rand_Str(7))
####################################

#Generate 5 digit random secure OTP
sec_gen=secrets.SystemRandom()
sec_num=sec_gen.randrange(10000,99999,2)
#print(sec_num)
####################################

#Generate a random Password which meets the following conditions
#Password length must be 10 characters long.
#It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
def password_gen():#(length, nbr_up, nbr_digit, nbr_special):
    #if length!=10 and nbr_up<2 and nbr_digit!=1 and nbr_special!=1:
    #    print('format not correct!')
    #    return 
    my_pass=random.sample(string.ascii_letters,6)
    my_pass+=random.sample(string.ascii_uppercase,2)
    my_pass+=random.choice(string.digits)
    my_pass+=random.choice(string.punctuation)
    my_pass=''.join(my_pass)
    return my_pass
#print(password_gen())
########################################

#Calculate multiplication of two random float numbers
n=random.random()
n1=random.uniform(9.5,99.5)
#print(n*n1)
#################################

#Generate random secure token of 64 bytes and random URL
#print('secure token of 64 bytes: ',secrets.token_hex(64))
#print('random URL: ',secrets.token_urlsafe(64))
###############################

#Roll dice in such a way that every time you get the same number
d=[1,2,3,4,5,6]
for i in range(5):
    random.seed(7)
    print(random.choice(d))
