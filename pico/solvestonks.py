from ctypes import sizeof


sipher='ocip{FTC0l_I4_t5m_ll0m_y_y3n2fc10a10ÿý.}÷ùZø'
message=''
stack=[]
for i in range(len(sipher)):
    stack.append(sipher[i])
    if(i%4==3):
        for j in range(4):
            message+=stack[3-j]
            #print(message)
        stack=[]
print(message)
