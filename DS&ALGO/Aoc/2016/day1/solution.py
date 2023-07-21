from input import direction




def part1():

    direction_array = direction.replace(' ','').split(',')


    START_POINT = (0,0)

    # current facing direction
    fd = 'N'

    # current position
    cp = START_POINT


    # direction data



    DIRECTION_INFO = {
        'N':{'L':[(-1,0),'W'],'R':[(1,0),'E']},
        'W':{'L':[(0,-1),'S'],'R':[(0,1),'N']},
        'S':{'L':[(1,0),'E'],'R':[(-1,0),'W']},
        'E':{'L':[(0,1),'N'],'R':[(0,-1),'S']}
        }


    ## loop  move the direction

    for MV in direction_array:
        #move direction ,move step
        MD,MS = MV[:1],int(MV[1:])

        # moving points, new facing direction
        mp,fd_new = DIRECTION_INFO[fd][MD]

        cp = (cp[0]+MS*mp[0],cp[1]+MS*mp[1])
        fd = fd_new

    print(fd,cp)

    print(abs(cp[0]-0)+abs(cp[1]-0))
    

def part2():

    direction_array = direction.replace(' ','').split(',')


    START_POINT = (0,0)

    # current facing direction
    fd = 'N'

    # current position
    cp = START_POINT


    # direction data



    DIRECTION_INFO = {
        'N':{'L':[(-1,0),'W'],'R':[(1,0),'E']},
        'W':{'L':[(0,-1),'S'],'R':[(0,1),'N']},
        'S':{'L':[(1,0),'E'],'R':[(-1,0),'W']},
        'E':{'L':[(0,1),'N'],'R':[(0,-1),'S']}
        }


    visisted_locations = [cp]


    ## loop  move the direction

    for MV in direction_array:
        #move direction ,move step
        MD,MS = MV[:1],int(MV[1:])

        # moving points, new facing direction
        mp,fd_new = DIRECTION_INFO[fd][MD]
        found =False
        # cp = (cp[0]+MS*mp[0],cp[1]+MS*mp[1])
        for _ in range(MS):
            cp = (cp[0]+mp[0],cp[1]+mp[1])
            if cp in visisted_locations:
                found=True
                break
            visisted_locations.append(cp)
        
        fd = fd_new
        if found:
            break

    print(visisted_locations)    

    print(fd,cp)
    print(abs(cp[0]-0)+abs(cp[1]-0))
    

if __name__=='__main__':

    part2()