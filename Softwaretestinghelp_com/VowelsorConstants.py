def VnC(S):
    counter_v = 0
    counter_c = 0
    counter_o = 0
    for i in range(0,len(S)):
        if S[i] in {'a','e','i','o','u'}:
            counter_v += 1
        elif S[i] in {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','w','v','y','z'}:
            counter_c += 1
        else:
            counter_o += 1
            
    print('There are '+str(counter_v)+' vowel(s) & There are '+str(counter_c)+' constant(s)')
    
VnC('Hello World')
