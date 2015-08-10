slow_initial = 1000
fast_initial = 1
counter = 1

while counter <= 100: 
    slow_number = slow_initial * (2-0.8)**counter
    fast_number = fast_initial * (2-0.6)**counter
    if slow_number <= fast_number:
        break
    else: 
        counter += 1
        
print slow_number
print fast_number
print counter
        
        