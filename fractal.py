import random
import math
import ifs
import bitmap

#randomFunction for a IFS like the barnsley fern

def randomWeighted(weights):
    randomNum = random.random()
    k = 0.0
    for i in range(len(weights)):
        if randomNum >= k and randomNum <= k + weights[i]:
            return i
        else: k += weights[i]

#Specify the width and height of the image (in pixels)

width = 1000
height = 1000

#Make image data
pixelList = [[0 for x in range(width)] for y in range(height)]

#set plot range

xRange = (-0.25,1.25)
yRange = (-0.25,1.25)
minX,maxX = xRange
minY,maxY = yRange

xSize = maxX-minX
ySize = maxY-minY

#input IFS (use ifs.treeIFS, ifs.starIFS, ifs.sierpIFS etc...  OR use customIFS)

def f1(point): return ifs.linear((0.5, -0.5, 0.5, 0.5), point, (0.0, 0.0))
def f2(point): return ifs.linear((0.5, -0.5, 0.5, 0.5), point, (1.0, 0.0))

customIFS = [f1,f2]

IFSList = ifs.carpetIFS

print(len(IFSList))

def xyToPixel(point):
    pixelX = int((point[0] - minX)*width/xSize)
    pixelY = int((point[1] - minY)*height/ySize)
    return (pixelX,pixelY)

currentPoint = (0.0,0.0)

numWhitePixels = 0
progressCounter = 0

brightness = 1000000  #sort of, really how many times cursor hits white point
graininess = 1        #set to 255 for fastest rendering

while numWhitePixels < brightness:
    whichFunc = random.randint(0,len(IFSList)-1)
    #Uncomment next line to do a weighted chaos game
    #whichFunc = randomWeighted((math.sqrt(2)/(1+math.sqrt(2)),1.0/(1+math.sqrt(2))))
    currentPoint = IFSList[whichFunc](currentPoint)
    pixelX,pixelY = xyToPixel(currentPoint)
    
    if pixelX < width and pixelY < height and pixelX >= 0 and pixelY >= 0:
        progressCounter += 1
        if progressCounter%1000000 == 0: print str(progressCounter/1000000) + " million points adjusted. Current pixel brightness: " + str(pixelList[pixelY][pixelX])
        if pixelList[pixelY][pixelX] + graininess <= 255:
            pixelList[pixelY][pixelX] += graininess
        else: 
            numWhitePixels += 1
            pixelList[pixelY][pixelX] = 255



bitmap.twoDimArrayToBitmap(pixelList, "newsomething.bmp")
