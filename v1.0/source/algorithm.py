l1st=[
    [0,0,9]+[0,5,0]+[0,0,0],
    [3,7,0]+[6,0,4]+[0,9,0],
    [5,0,4]+[2,0,8]+[0,0,3],

    [6,0,7]+[0,0,0]+[0,0,5],
    [0,2,0]+[5,0,3]+[0,8,0],
    [9,0,0]+[0,0,0]+[3,0,4],

    [2,0,0]+[7,0,1]+[6,0,9],
    [0,9,0]+[4,0,2]+[0,5,1],
    [0,0,0]+[0,6,0]+[4,0,0]]
############################
############################
############################
def clear_nonzeros(l):
    sw=''
    for i in l:
        sw+=str(i)
    sk=[]
    for H in range(9):
        if sw.find(str(H+1))==-1:
            sk.append(H+1)
    return list(sk)
###########################
def clear_zeros(l):
    a=[]
    for i in l:
        if i!=0:
            a.append(i)
    return a
###########################
def maincheck(a,b,kvadrati):
    result=[]
    j=''
    a=clear_nonzeros(a)
    b=clear_zeros(b+kvadrati)
    for o in b:
        j+=str(o)
    for i in a:
        if j.find(str(i))==-1:
            result.append(int(i))
    return result

def fill(LIST):
    v_1,v_2,v_3,v_4,v_5,v_6,v_7,v_8,v_9=[],[],[],[],[],[],[],[],[]
    for h in range(9):
        for v in range(9):
            eval('v_'+str(h+1)).append(LIST[v][h])
    for m in range(9):
        for n in range(9):
            if LIST[m][n]!=0:
                continue
            T=[0,1,2]
            U=[3,4,5]
            V=[6,7,8]
            m1=LIST[0]
            m2=LIST[1]
            m3=LIST[2]
            m4=LIST[3]
            m5=LIST[4]
            m6=LIST[5]
            m7=LIST[6]
            m8=LIST[7]
            m9=LIST[8]
            if m in T:
                if n in T:
                    kvadr=m1[:3]+m2[:3]+m3[:3]
                elif n in U:
                    kvadr=m1[3:6]+m2[3:6]+m3[3:6]
                elif n in V:
                    kvadr=m1[6:9]+m2[6:9]+m3[6:9]
            elif m in U:
                if n in T:
                    kvadr=m4[:3]+m5[:3]+m6[:3]
                elif n in U:
                    kvadr=m4[3:6]+m5[3:6]+m6[3:6]
                elif n in V:
                    kvadr=m4[6:9]+m5[6:9]+m6[6:9]
            elif m in V:
                if n in T:
                    kvadr=m7[:3]+m8[:3]+m9[:3]
                elif n in U:
                    kvadr=m7[3:6]+m8[3:6]+m9[3:6]
                elif n in V:
                    kvadr=m7[6:9]+m8[6:9]+m9[6:9]
            q=maincheck(LIST[m],eval('v_'+str(n+1)),kvadr)
            print m+1,'x',n+1,q
            if len(q)==1:
                LIST[m][n]=q[0]
    return LIST

def solve(l15t):
    i='0'
    l=[]
    while i.find('0')!=-1:
        i=''
        l=[]
        w=[]
        l15t=fill(l15t)
        for j in range(len(l15t)):
            w+=l15t[j]
        for n in range(len(w)):
            i+=str(w[n])
        for D in range(9):
            l+=[list(i[9*D:9*D+9])]
    return l
#print FuCk(l1st)