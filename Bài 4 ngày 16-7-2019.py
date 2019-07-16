a= float(input("Input a to solve equation: ax^2+bx+c=0 "))
b= float(input("Input b to solve equation: ax^2+bx+c=0 "))
c= float(input("Input c to solve equation: ax^2+bx+c=0 "))
if a==0 and b==0 and c==0:
    print('This equation has infinity solution')
elif a==0 and b==0 and c!=0:
    print('This equation has no solution')
elif a==0 and b!=0 and c!=0:
    x= -c/b
    print('This equation has one soultion',x)
else:
    if b**2-4*a*c<0:
        print('This equation has no real root')
    elif b**2-4*a*c>=0:
        t=(b**2-4*a*c)**(1/2)
        print(t)
        x1= (-b+t)/(2*a)
        x2= (-b-t)/(2*a)
        print('This equation has two real root',x1,x2)
        

    


