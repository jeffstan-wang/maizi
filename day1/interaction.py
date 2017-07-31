import getpass
# user=input('Please input your name here:')
# password=getpass.getpass("Input your password:")
# print(user,password)
real_age=40
count=1
while count <= 3:
    age=int(input('Please input the age:'))
    if age > real_age:
        print('thinking small')
    elif age < real_age:
        print('thinking biggre')
    else:
        print('right answer!')
        break
    count+=1
else:
    print("you have no change to guess the age!")
