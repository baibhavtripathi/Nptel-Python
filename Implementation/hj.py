def alternating(l):
    if(len(l)>1):
        if(l[0]>l[1]):
            for i in range(len(l)-1):
                if(l[i]==l[i-1]):
                    return False
            if(i%2==0):
                if(l[i]<l[i+1]):
                    return False
        if(l[0]==l[i+1]):
            return False
    return True



