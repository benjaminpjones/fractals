import random
import math
import bitmap
import ifs

#randomFunction for a IFS like the barnsley fern

def randomWeighted(weights, accumulated = False):
  if not accumulated:
    randomNum = random.random()
    k = 0.0
    for i in range(len(weights)):
        if randomNum >= k and randomNum <= k + weights[i]:
            return i
        else: k += weights[i]
  else:
    randomNum = random.random()
    i = jump = len(weights)/2
    while True:
        if jump > 1:
            jump /= 2
        if i < 1:
            if randomNum <= weights[0]:
                return 0
            else:
                i += jump
        elif i >= len(weights) - 1:
            if randomNum >= weights[i]:
                return len(weights)-1
            else:
                i -= jump
        elif weights[i] < randomNum:
            i += jump
        elif weights[i-1] > randomNum:
            i -= jump
        else:
            return i

def xyToPixel(point, minX, minY, xSize, ySize, width, height):
    pixelX = int((point[0] - minX)*width/xSize)
    pixelY = int((point[1] - minY)*height/ySize)
    return (pixelX,pixelY)

def makeFractal(ifs,
                height=1000, width=1000,
                xRange=(0.0,1.0), yRange=(0.0,1.0),
                iterations=2000000, graininess=5,
                weights=False,
                bmpname="newfractal"):

    #Make image data
    pixelList = [[0 for x in xrange(width)] for y in xrange(height)]

    #set plot range and size
    minX,maxX = xRange
    minY,maxY = yRange

    xSize = maxX-minX
    ySize = maxY-minY

    IFSList = ifs

    print(len(IFSList))

    currentPoint = (0.0,0.0)
    progressCounter = 0

    #normalize and accumulate weights
    if weights:
        sumWeights = float(sum(weights))
        accumWeights = []
        current = 0.0
        for i in xrange(len(weights)):
            accumWeights.append((weights[i]/sumWeights) + current)

    for i in xrange(iterations):
        if not weights:
            whichFunc = random.randint(0,len(IFSList)-1)
        else:
            whichFunc = randomWeighted(accumWeights, True)
        currentPoint = IFSList[whichFunc](currentPoint)
        pixelX,pixelY = xyToPixel(currentPoint, minX, minY, xSize, ySize, width, height)

        if pixelX < width and pixelY < height and pixelX >= 0 and pixelY >= 0:
            progressCounter += 1
            if progressCounter%1000000 == 0: 
                print (str(progressCounter/1000000)
                      + " million points adjusted. Current pixel brightness: "
                      + str(pixelList[pixelY][pixelX]))
                if progressCounter%10000000 == 0:
                    bitmap.twoDimArrayToBitmap(pixelList, bmpname + str(progressCounter/10000000) + ".bmp")
            if pixelList[pixelY][pixelX] + graininess <= 255:
                pixelList[pixelY][pixelX] += graininess
            else:
                pixelList[pixelY][pixelX] = 255

    bitmap.twoDimArrayToBitmap(pixelList, bmpname + ".bmp")

if __name__ == "__main__":

    makeFractal(ifs=ifs.dragonIFS[:2],
                weights = False,
                height=500, width=500,
                xRange=(-0.475, 1.325), yRange=(-0.44, 0.77),
                iterations=2000000, graininess=51,
                bmpname="newdragon")


            
