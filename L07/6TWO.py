import random
rows = 3
cols = 4

def Kuma():
    values = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]
    print(values)
    for r in range(rows):
        for c in range(cols):
            values[r][c] = random.randint(1, 100)
            #print(values)ดูการวนลูป
    print(values)
    
Kuma()
            
 
           