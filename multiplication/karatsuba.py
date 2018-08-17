def multiply(num1, num2):
    if(len(str(num1)) == 1 or len(str(num2)) == 1):
        return num1 * num2

    n1 = len(str(num1))
    n2 = len(str(num2))

    if(n1 > n2):
        m = n1 / 2
    else:
        m = n2 / 2

    s = str(num1)
    a, b = s[:int(m)], s[int(m):]

    s = str(num2)
    c, d = s[:int(m)], s[int(m):]

    z0 = multiply(int(b), int(d))
    z1 = multiply((int(a)+ int(b)), (int(c)+ int(d)))
    z2 = multiply(int(a), int(c))

    return (z2*10^(2* int(m)))+((z1-z2-z0)*10^(int(m)))+(z0)





nu1 = 3141592653589793238462643383279502884197169399375105820974944592
nu2 = 2718281828459045235360287471352662497757247093699959574966967627
nu3 = multiply(nu1, nu2)
print(nu3)


    
