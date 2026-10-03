total_test_case = int(input())
for i in range (total_test_case):
    
    number_of_mountains = int(input())
    heights = list(map(int,input().split()))
    
    tallest_seen = heights[0]
    
    for current_height in heights:
        if current_height > tallest_seen:
            tallest_seen = current_height
            
    print(tallest_seen)