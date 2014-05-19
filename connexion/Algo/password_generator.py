from random import randrange


elements=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def generator():
    password=''
    for i in range(0,9):
        password=password+elements[randrange(0,36)]
    return password

