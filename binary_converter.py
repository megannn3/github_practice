def decimalToBinary(num):
    i=0
    binary =[]
    while i >-1 :
        if num<2**i:
            for k in range(i+1):
                if 2**(i-k)<=num:
                    binary.append(str(1))    
                    num = num-2**(i-k)
                 
                elif k>0:
                    binary.append(str(0))
                    
                  
                elif num==0:
        
                    binary.append(str(0))
                k+=1
            while len(binary)%4 != 0:
                binary.insert(0,"0")
            return ''.join(binary)
        else: 
            i+=1

print(decimalToBinary(2))









def binaryToDecimal(num):
    decimal = 0
    nums = str(num)
    for i in range(len(nums)):
        decimal +=int(nums[i])*(2**(len(nums)-i-1))
    

    return (decimal)



print(binaryToDecimal(1111))