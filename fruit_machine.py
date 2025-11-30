def fruit_machine(reels):
    a,b,c = reels
    if a == b == c:
        return 100
    if a == b or a == c or b == c :
        return 50
    
    return 0
# تست‌ها
print(fruit_machine(['apple','apple','apple'])) 
print(fruit_machine(['apple','apple','apple'])) 
print(fruit_machine(['apple','apple','banana']) ) 
print(fruit_machine(['banana','apple','banana']) ) 
print(fruit_machine(['cherry','banana','banana']) ) 
print(fruit_machine(['apple','banana','cherry']) ) 
print(fruit_machine(['🍋','🍋','🍊']))  
print(fruit_machine(['🍉','🍉','🍉']))  
