import random
import string

s1=string.ascii_letters
s2=string.punctuation
s3=string.digits
s=[]
s.extend(s1)
s.extend(s2)
s.extend(s3)
# print(s)
random.shuffle(s)
# print(s)
password_len=int(input("Enter the lenght of password : " ))
# print(random.sample(s,password_len))
print(''.join(random.sample(s,password_len)))
