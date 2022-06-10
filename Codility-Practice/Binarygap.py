# Compute binary numbers
def Binary_gap(N):
    Powers = []
    new_power = 0
    n = 0
    while N > new_power:
        new_power = pow(2,n)
        Powers.append(new_power)
        n = n + 1
# Delete last number if bigger than N
    if Powers[-1] > N:
        del Powers[-1]
        
# Compute Binary numbers
    Powers.reverse()
    Reminder = N
    i = -1
    Binary = []
    while Reminder != 0:
    # Compute 1s
        i = i + 1
        if Powers[i] <= Reminder:
            Reminder = Reminder - Powers[i]
            Binary.append(1)
        # Fills zeros if Reminder is 0
            if Reminder == 0:
                Powers_left = len(Powers) - (i+1)
                for n in range(0,Powers_left):
                    Binary.append(0)
                
        else:
            Binary.append(0)
            
# Compute highest 0 sequence
    zero_seq = 0
    highest_seq = 0
    for i in range(0,len(Binary)):
        if Binary[i] == 0:
            zero_seq = zero_seq + 1
        else:
            if zero_seq >= highest_seq:
                highest_seq = zero_seq
                zero_seq = 0
    return highest_seq, Binary
        
        
