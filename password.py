import string
import random
a =int(input())
b = ''.join(random.choices(string.ascii_lowercase + string.digits, k=a))
print("The generated password : {0}".format(b))