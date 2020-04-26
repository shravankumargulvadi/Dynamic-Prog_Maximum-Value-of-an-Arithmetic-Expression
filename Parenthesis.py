
# coding: utf-8

# In[44]:


def parenthesis(string):
    d=[]
    op=[]
    
    for i in range(len(string)):
        if i%2!=0:
            op.append(string[i])
        else:
            d.append(string[i])
    n=len(d)
            
    M=dict()
    m=dict()
    
    
    def evalt(a, b, op):
        a=int(a)
        b=int(b)
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            assert False

    def minandmax(i,j):
        min_no=100000000
        max_no=-100000000
        amin=[]
        amax=[]
        for k in range(i,j):
            #print(k)
            a=evalt(M[i,k],M[k+1,j],op[k-1])
            b=evalt(M[i,k],m[k+1,j],op[k-1])
            c=evalt(m[i,k],M[k+1,j],op[k-1])
            d=evalt(m[i,k],m[k+1,j],op[k-1])
            #print(a,b,c,d)
            amin.append(min(a,b,c,d))
            amax.append(max(a,b,c,d))
        #print('i,j',i,j)
        min_no=min(amin)
        max_no=max(amax)
        #print(min_no,max_no)
        return(min_no,max_no)
        
    
    for i in range(1,n+1):
        M[i,i]=d[i-1]
        m[i,i]=d[i-1]
    for s in range(1,n-1+1):
        for i in range(1,n+1-s):
            j=i+s
            m[i,j],M[i,j]=minandmax(i,j)
    #print(M)
    #print(m)
    return M[1,n]

if __name__ == "__main__":
    print(parenthesis(input()))



        
    


# In[43]:




