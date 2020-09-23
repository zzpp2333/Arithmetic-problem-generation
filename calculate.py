import random
#  
def checkEqu(maximum, numlist, oprlist):
    # numlist(int[3]) exp: 63 85 79
    # oprlist(char[2]/char[4]) exp: -(-) ++
    # 运算过程中不会产生小于0或者大于maximum的结果
    numstack = []
    oprstack = []

    _eval = lambda num1, op, num2: eval(str(num1)+op+str(num2))

    for i in range(len(numlist)):
        if i >= len(oprlist):  # 25- 75 int[3] char[2] i == 1
            res = _eval(numstack[-1], oprlist[-1], numlist[i])
            if res >= maximum or res < 0:
                return False
        if len(oprstack) != 0:  # 63 85 - (
            if oprlist[i] == "(":
                oprstack.append(oprlist[i])
                numstack.append(numlist[i])
            elif oprstack[-1] == "(":  # 63 85  - (  || cur->79 -
                oprstack.pop()  # (
                res = _eval(numstack.pop(), oprlist[i], numlist[i])
                if 0 <= res < maximum:
                    res = _eval(numstack.pop(), oprstack.pop(), res)
                if res < 0 or res >= maximum:
                    return False
            else: #63 +
                res = _eval(numstack.pop(), oprstack.pop(), numlist[i])
                if res < 0 or res >= maximum:
                    return False
                else:
                    numstack.append(res)
                    oprstack.append(oprlist[i])
        else:
            numstack.append(numlist[i])
            oprstack.append(oprlist[i])
    return True

def singleCal_AS(maximum):
    # Add and Subtract
    # maximum以内的加减法,例如100以内的加减法
    # 结果在maximum之内,返回算式(str)和结果(int)
    num1 = num2 = 0
    op_choice = 1
    while True:
        num1 = random.randint(1, maximum-1)
        num2 = random.randint(1, maximum-1)
        op_choice = random.randint(0, 1)  # 0->- 1->+
        if op_choice == 1 and num1 + num2 >= maximum:
            continue
        else:
            break

    if op_choice == 0:
        if num1 > num2:
            return str(num1) + '-' + str(num2) + '=', num1 - num2
        else:
            return str(num2) + '-' + str(num1) + '=', num2 - num1
    else:
        return str(num1) + '+' + str(num2) + '=', num1 + num2

def singleCal_MD(maximum):
    # Multiply and Divide(Integer)
    while True:
        op_choice = random.randint(2, 3) #2->* 3->/
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)
        if op_choice == 2:
            return str(num1) + '*' + str(num2) + '=', num1*num2
        else:
            if num1*num2 == 0:
                continue
            else:
                return str(num1*num2) + '/' + str(num1) + '=', num2



def mixCal(maximum):
    # maimum以内的加减混合运算 运算符包括+ - ( ) 不包括乘除
    # ( )只会出现在第二和第三个运算数
    num1 = num2 = num3 = 0
    oprand1 = oprand2 = 1
    branket = 0
    while True:
        num1 = random.randint(1, maximum-1)
        num2 = random.randint(1, maximum-1)
        num3 = random.randint(1, maximum-1)
        oprand1 = random.randint(0, 1)
        oprand2 = random.randint(0, 1)
        branket = random.randint(0, 1) # 0->无括号 1->有括号
        op1 = "-" if oprand1==0 else "+"
        op2 = "-" if oprand2==0 else "+"
        if branket == 0 and oprand1 == 0 and num1 < num2:
            continue
        elif oprand2 == 0:
            if branket == 1 and num2 < num3:
                continue
            elif branket == 0 and num1+num2 < num3:
                continue
        question = str(num1)+op1+str(num2)+op2+str(num3) if branket == 0 else str(num1)+op1+"("+str(num2)+op2+str(num3)+")"
        answer = eval(question)
        if answer > maximum or answer < 0:
            continue
        else:
            return question+"=", answer

def getList(maximum, num, mode):
    questions = []
    answers = []
    for i in range(num):
        while True:
            que, ans = singleCal(maximum) if mode == 0 else mixCal(maximum)
            if que in questions:
                continue
            else:
                questions.append(que)
                answers.append(ans)
                break
    return questions, answers
        
                
if __name__ == "__main__":
    print(getList(100,20,1))
    # print(checkEqu(100, [63, 15, 29], ['+', '+']))
