def solve(amount):
    notes =[500,200,100,50,20]
    count = 0
    used_notes = []
    for n in notes:
        num = amount // n
        if num > 0 :
            used_notes += [n] * num
            
            
        count += num 
        amount %= n
        
        
    if amount != 0:
            return -1
        
    return count,used_notes
        
print(solve(770))     
print(solve(125))     
    