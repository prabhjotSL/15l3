import random
from PIL import Image

def smooth(M,x,y):
    #print(M[x][y])
    if M[x][y] >= 2:
        for j in range (0,M[x][y]+random.randint(1,5)):
            for k in range (0,M[x][y]+random.randint(1,5)):
                r=random.randint(7,10)
                if M[x][y]-(j+k) >= 2:
                    if M[x][y]-(j+k)+M[x+j][y+k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x+j][y+k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x+j][y+k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x-j][y-k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x-j][y-k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x-j][y-k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x+j][y-k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x+j][y-k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x+j][y-k]=M[x][y]-(j+k)+random.randint(1,2)
                    if M[x][y]-(j+k)+M[x-j][y+k]>=r:
                        M[x+j][y+k]=M[x][y]+(j+k)
                    else:
                        if random.randint(0,1) is 1:
                            M[x-j][y+k]=M[x][y]-(j+k)-random.randint(0,5)
                        else:
                            M[x-j][y+k]=M[x][y]-(j+k)+random.randint(1,2)

def bterrain(xy, Matrix, x, y, mutator):
    za=0
    zb=0
    for i in range (0,mutator):
        if i%(xy*int(xy/random.randint(5,30))) is 0:
            print("ding!")
            za=random.randint(0,3)
            zb=random.randint(0,3)
        x=random.randint(5,(xy/2)-5)+random.randint(5,(xy/2)-5)+za
        y=random.randint(5,(xy/2)-5)+random.randint(5,(xy/2)-5)+zb
        Matrix[x][y]=random.randint(-5,5)
        smooth(Matrix,x,y)
        #'''
    for m in range (0,int(mutator/random.uniform(1.0,2.0))):
        x=random.randint(5,(int(xy/2))-5)+random.randint(5,(int(xy/2))-5)
        y=random.randint(5,(int(xy/2))-5)+random.randint(5,(int(xy/2))-5)
        Matrix[x][y]=random.randint(0,5)
        smooth(Matrix,x,y)
    return Matrix

def bimage(xy,Matrix,water,output):
    im=None
    im=Image.new("RGB",(xy,xy),water)
    for a in range(0,xy):
        for b in range(0,xy):
            if Matrix[a][b] >= 1:
                im.putpixel((a,b),(Matrix[a][b]*10+100,Matrix[a][b]*10+50,0))
            '''
            if Matrix[a][b] <= 0:#
                q=None
            elif Matrix[a][b] <= 3:
                im.putpixel((a,b),(210-Matrix[a][b],(Matrix[a][b]*10)+155,60))
            elif Matrix[a][b] <= 6:
                im.putpixel((a,b),(90,(Matrix[a][b]*10)+155,20))
            elif Matrix[a][b]<=9:
                im.putpixel((a,b),((Matrix[a][b]*10)+130,(Matrix[a][b]*10)+155,(Matrix[a][b]*10)+140))
            elif Matrix[a][b] >= 10:
                im.putpixel((a,b),(140,155+Matrix[a][b],150))
                #'''
    im.save("./"+str(output)+".png","PNG")
    smatrix(Matrix,output)
    
def smatrix(Matrix,output):
    open("./"+str(output)+".map",'w').write(str(Matrix))

def run():
    xy=128
    mutator=int(xy/random.uniform(2.0,9.0))*15+1
    land=(200,150,0)
    water=(0,50,0)
    Matrix = [[0 for x in range(xy*2)] for x in range(xy*2)]
    x=0
    y=0
    maps=5      #how many maps to generate.
    start=0     #where do we start to count.
    for u in range (start,start+maps):
        bimage(xy,bterrain(xy,[[0 for x in range(xy)] for x in range(xy)],x,y,mutator),water,u)

