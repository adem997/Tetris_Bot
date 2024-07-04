from numpy import array

# my strategy here is to keep track of the block in matrice t
# and the hieght in table f 
# and start searching for the best move by trying every move
# a good move is to place tetriminos as low as possible
# without leafing a gap under


# places of blocks False = no block, True = there is a block .
t = array([[bool()]*10]*21)

# bumpiness
f = array([int()]*10)

def main():

    in_v = input()
    if in_v=="name :":
        print('Linderhof')
    while in_v!='end':
        in_v = input()
        # get current piece
        newPiece = ""
        reqcordPieceName = 0
        # get next piece
        nextPiece = ""
        for c in in_v:
            if c==':':
                if reqcordPieceName==0:
                    reqcordPieceName=1
            elif reqcordPieceName==1 and not c.isspace():
                newPiece=newPiece+c
            if c.isspace() and  reqcordPieceName==1 :
                reqcordPieceName=2
            if c==':' and reqcordPieceName==2:
                reqcordPieceName=3
            elif reqcordPieceName==3 and not c.isspace():
                nextPiece=nextPiece+c


        hieght()

        if newPiece=="Square":
            square()
        elif newPiece=="Line":
            Line()
        elif newPiece=="L":
            Lettre_L()
        elif newPiece=="T":
            print("MR-MR-MR-D")
        elif newPiece=="MirroredL":
            MirroredL()
        elif newPiece=="S":
            Lettre_S()
        else:
            print("MR-MR-MR-D")


        
            
def playGround():
    
    for i in range(20):
        for j in range(10):
            t[i][j]=False
    for i in range(10):
        t[20][i]=True


# gets the number of the hieghest block in each column
def hieght():
    j=0
    i=0
    while j<10:
        if t[i][j]==True:
            f[j]=20-i
            j=j+1
            i=0
        else:
            i=i+1
    


# this controls the movement of squares

def square():
    hieght()
    # find the best move and the best move it
    # is to find the lowest 2 blocks without leaving an empty block under

    min=f[0]
    position=0
    for j in range(5):
        for i in range(1, 9):
            if f[i]==f[i+1]-j or f[i]==f[i+1]+j:
                if f[i]<min:
                    min=f[i]
                    position=i

                
    movy(position)
    # fills the new position of the square
    # position is x and pos is y, looks like f(x)=x
    pos=f[position]
    for i in range(18,20):
        t[i-pos][position]=True
        t[i-pos][position+1]=True
    # update the hieght
    hieght()
    # checks if there is a completed line
    check(18, 20, pos)


def Line():
    min=f[0]
    position=0
    for i in range(1,10):
        if f[i]<min:
            min=f[i]
            position=i

    movy(position)

    # add the line to the matrix
    pos=f[position]
    for i in range(16,20):
        t[i-pos][position]=True

    hieght()
    check(16, 20, pos)


def Lettre_T():
    hieght()
    min=f[0]
    position=0
    TestT=False
    for i in range(1,8):
        if f[i]==f[i+1]-1==f[i+2]:
            if f[i]<min:
                min=f[i]
                position=i
                TestT=True
    if TestT==False:
        print("w")


def Lettre_S():
    hieght()
    position=0

    #find is number of rotation 
    find=0
    min=50
    for i in range(1,9):
        if f[i-1]==f[i]==f[i+1]-1:   
            print(f[i],f[i+1],f[i+2]-1) 
            if f[i]<min:
                min=f[i]
                position=i
                find=1
    if find==0:
        for i in range(1,10):
            if f[i-1]-1==f[i]:
                if f[i]<min:
                    min=f[i]
                    position=i
                    find=2
    if find==1:
        print("RL-",end="")
        movy(position)
        pos=f[position]

        t[19-pos][position-1]=True
        t[19-pos][position]=True
        t[18-pos][position]=True
        t[18-pos][position+1]=True

        hieght()
        check(17, 20, pos)


    elif find==2:
        
        movy(position-1)
        pos=f[position]

        t[19-pos][position]=True
        t[18-pos][position]=True
        t[18-pos][position-1]=True
        t[17-pos][position-1]=True
        

        hieght()
        check(17, 20, pos)
    else:
        print("D")
        

def Lettre_Z():
    print("Z")


def Lettre_L():
    hieght()
    position=0
    
    #find is number of rotation 
    find=0
    min=50
    for i in range(1,10):
        if f[i-1]==f[i]+2:
            if f[i]<min:
                min=f[i]
                position=i
                find=1
    if find==0:
        for i in range(1,9):
            if f[i-1]==f[i]-1==f[i+1]-1:
                if f[i]<min:
                    min=f[i]
                    position=i
                    find=2
        
        if find==0:
            for i in range(1,9):
                if f[i-1]==f[i]==f[i+1]:
                    if f[i]<min:
                        min=f[i]
                        position=i
                        find=3


    if find==1:
        movy(position)
        pos=f[position]

        for i in range(17,20):
            t[i-pos][position]=True

        t[17-pos][position-1]=True
        hieght()
        check(17, 20, pos)

    elif find==2:
        print("RL-",end="")
        movy(position)
        pos=f[position]

        t[20-pos][position]=True
        t[20-pos][position-1]=True
        t[20-pos][position+1]=True

        t[19-pos][position-1]=True

        hieght()
        check(19, 20, pos)

    elif find==3:
        print("RR-",end="")
        movy(position)
        pos=f[position]

        t[19-pos][position]=True
        t[19-pos][position-1]=True
        t[19-pos][position+1]=True
        t[18-pos][position+1]=True

        hieght()
        check(19, 20, pos)
    
    elif find==4:
        print("RR-RR-", end="")
        movy(position)
        pos=f[position]

        t[19-pos][position]=True
        t[18-pos][position]=True
        t[17-pos][position]=True
        t[19-pos][position+1]=True

        hieght()
        check(17, 20, pos)

    else:
        print("RR-MR-MR-MR-D")




def MirroredL():
    hieght()
    position=0
    
    #find is number of rotation 
    find=0
    min=50
    for i in range(1,10):
        if f[i-1]+2==f[i]:
            if f[i]<min:
                min=f[i]
                position=i
                find=1
    if find==0:
        for i in range(1,9):
            if f[i-1]-1==f[i]-1==f[i+1]:
                if f[i]<min:
                    min=f[i]
                    position=i
                    find=2
        
        if find==0:
            for i in range(1,9):
                if f[i-1]==f[i]==f[i+1]:
                    if f[i]<min:
                        min=f[i]
                        position=i
                        find=3
                if f[i-1]==f[i]:
                    if f[i]<min:
                        min=f[i]
                        position=i
                        find=4



    if find==1:
        movy(position-1)
        pos=f[position]-2

        t[19-pos][position-1]=True
        t[18-pos][position-1]=True
        t[17-pos][position-1]=True

        t[17-pos][position]=True
        hieght()
        check(17, 20, pos)

    elif find==2:
        print("RR-",end="")
        movy(position)
        pos=f[position]

        t[19-pos][position]=True
        t[19-pos][position-1]=True
        t[19-pos][position+1]=True

        t[20-pos][position+1]=True

        hieght()
        check(19, 20, pos)

    elif find==3:
        print("RL-",end="")
        movy(position)
        pos=f[position]

        t[19-pos][position]=True
        t[19-pos][position-1]=True
        t[19-pos][position+1]=True
        t[18-pos][position-1]=True

        hieght()
        check(18, 20, pos)

    elif find==4:
        print("RR-RR-", end="")
        movy(position)
        pos=f[position]

        t[19-pos][position]=True
        t[18-pos][position]=True
        t[17-pos][position]=True
        t[19-pos][position-1]=True

        hieght()
        check(17, 20, pos)

    else:
        print("RR-MR-MR-MR-D")

    



# checks if there is a completed line                    
def check(a, b, pos):
    for i in range(a,b):
        isFull=True
        for j in range(10):
            if t[i-pos][j]==False:
                isFull=False
                break
        if isFull==True:
            posY=i-pos
            removeLine(posY)

# remove the complted line and move down the above 
def removeLine(Y):
    for i in range(Y, 0, -1):
        t[i]=t[i-1]
    t[0]=[0] * len(t[0])
    hieght()
    
        
def movy(position):
    if 6-position>0:
        for i in range(0, 6-position):
            print("ML-",end="")
        print("D")
    elif 6-position<0:
        for i in range(0, position-6):
            print("MR-",end="")
        print("D")
    elif 6-position==0:
        print("D")



playGround()
main()








