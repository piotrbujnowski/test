import random, string

def pass_gen(size, chars=string.ascii_letters + string.digits + string.punctuation):

    return ''.join(random.choice(chars) for _ in range(size))

pass_length = int(input("Your password's length: "))
print(pass_gen(pass_length))