start = (1,1)

if start == (1,1):
    way = '(N)orth'
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 'n' or direction == 'N':
        start = (1,2)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start
        

if start == (1,2):
    way = '(N)orth or (E)ast or (S)outh'
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 'n' or direction =='N':
        start = (1,3)
    elif direction == 'E' or direction =='e':
        start = (2,2)
    elif direction == 's' or direction =='S':
        start = (1,1)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (1,3):
    way = '(S)outh or (E)ast'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 's' or direction == 'S':
        start = (1,2)
    elif direction == 'e' or direction =='E':
        start = (2,3)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (2,2):
    way = '(W)est or (S)outh'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 's' or direction == 'S':
        start = (2,1)
    elif direction == 'w' or direction == 'W':
        start = (1,2)    
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (2,1):
    way = '(N)orth'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 'n' or direction =='N':
        start = (2,2)    
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (2,3):
    way = '(E)ast or (W)est'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 'e' or direction =='E':
        start = (3,3)
    elif direction == 'w' or direction =='W':
        start = (1,3)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (3,3):
    way = '(S)outh or (W)est'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 'w' or direction =='W':
        start = (2,3)
    elif direction == 's' or direction == 'S':
        start = (3,2)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (3,2):
    way = '(S)outh or (N)orth'    
    print('You can travel:',way)
    direction = input('Direction: ')
    if direction == 's' or direction == 'S':
        start = (3,1)    
    elif direction == 'n' or direction == 'N':
        start = (3,3)
    else:
        print('Not a valid direction!')
        direction = input('Direction: ')
        start = start

if start == (3,1):
    print('Victory')