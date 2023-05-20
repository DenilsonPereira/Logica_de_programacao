#Um problema típico em ciência da computação consiste em converter um número da sua forma decimal para a forma binária. Crie uma função recursiva que execute essa conversão
def decbin(num):
    if num==1: return 1
    if num==0: return 0
    else: return num%2 + decbin(num-1)
print(decbin(18))