chiffres=['0','1','2','3','4','5','6','7','8','9']
operations=['+','-','*','/']


def no_space(ligne):
    li=''
    for i in range(0,len(ligne)):
        l=ligne[i]
        if not l==' ':
            li=li+l
    return li


def operation(ligne):
    li=no_space(ligne)
    n1=''
    n2=''
    n3=''
    op=''
    check_o=False
    check_e=False
    check_n1=False
    check_n2=False
    for i in li:
        if i in chiffres and not check_o and not check_e:
            n1=n1+i
            check_n1=True
        elif i in operations and not check_o and check_n1:
            op=op+i
            check_o=True
        elif i in chiffres and check_o and not check_e:
            n2=n2+i
            check_n2=True
        elif i=='=' and check_o and check_n2:
            check_e=True
        elif i in chiffres and check_e:
            n3=n3+i
        else:
            return[False]
    return[True,int(n1),int(n2),int(n3),op]
    
def check_operation(numbers,n1,n2,n3,op):
    if n1 in numbers:
        numbers.remove(n1)
        if n2 in numbers and n3>=0:
            if op=='+':
                if n1+n2==n3:
                    numbers.remove(n2)
                    numbers.append(n3)
                    return [True,numbers]
                else:
                    return [False]
            elif op=='-':
                if n1-n2==n3:
                    numbers.remove(n2)
                    numbers.append(n3)
                    return [True,numbers]
                else:
                    return [False]
            elif op=='*':
                if n1*n2==n3:
                    numbers.remove(n2)
                    numbers.append(n3)
                    return [True,numbers]
                else:
                    return [False]
            elif op=='/':
                if n1/n2==n3 and n1%n2==0:
                    numbers.remove(n2)
                    numbers.append(n3)
                    return [True,numbers]
                else:
                    return [False]
        else:
            return[False]
    else:
            return[False]
        
def chiffres_check(lignes,numbers,compte):
    for op in lignes:
        ope=operation(op)
        if ope[0]:
            oper=check_operation(numbers,ope[1],ope[2],ope[3],ope[4])
            if(oper[0]):
                numbers=oper[1]
            else:
                return [False,0]
        else:
            return [False,0]
    diff=10
    for i in numbers:
        temp=abs(i-compte)
        if temp<diff:
            diff=temp
    return [True,10-diff]
