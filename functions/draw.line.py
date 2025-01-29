# 

def drawLine( length, direction ):
    if direction == "h":
        print("-" * length)
    elif direction == "v":
            print('\n'.join(['|'] * length))

drawLine( 5, 'h' )
drawLine( 3, 'v' )