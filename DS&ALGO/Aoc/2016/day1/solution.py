from input import direction

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
    