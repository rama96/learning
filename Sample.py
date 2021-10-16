def repeated_sequence(a):

    # counter = {}
    current_no = a[0]
    max_count = 0
    current_count = 0
    max_ele = a[0]
    for i in range(len(a)):
        
        if a[i] == current_no:
           current_count+=1
        else :
            current_no = a[i]
            current_count=1
        
        if current_count > max_count:
            max_count = current_count
            max_ele = a[i]
    
    return max_ele , max_count




print(repeated_sequence([1,1,5,22,3,4,55,5,5,5,5,5,6,7,7]))
