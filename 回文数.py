from functools import reduce
l=[]
def int2str(n):
    global l
    if n%10!=0 or n/10!=0:
        if n%10!=0:
            l.insert(0,n%10)
            n=int(n/10)
            int2str(n)
            return 
        if int(n/10)!=0:
            l.insert(0,0)
            n=int(n/10)
            int2str(n)
            return 
        if n/10==0:
            return
def generator(n):
    a=0
    while a<n:
        a=a+1
        yield a
def ff(s):
    global l
    l=[]
    int2str(s)
    # print(l)
    if len(l) and len(l)!=1:
        if len(l)!=2:
            s=reduce(lambda x,y:x*10+y,l[1:len(l)-1])
            f=l[0]==l[len(l)-1] and ff(s)
        if len(l)==2:
            f=l[0]==l[len(l)-1]
        # print(s)
        # f=l[0]==l[len(l)-1] and ff(s)
        return f
    else:
        return True
print(list(filter(ff,generator(1000))))
