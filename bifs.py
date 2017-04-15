import fractal

def makeFunc(n):
    def f(x):
        # f(x) is the function u will create. use n as a variable parameter
        return x    #should return a tuple
    return f

NUM_OF_FUNCS = 20
bifs = []
weights = []

for i in xrange(NUM_OF_FUNCS):
    ifs.append(makeFunc(i))
    weights.append(1.0)   # generally weight should be approx. indirectly
                          # related to contraction constant
                          # use best judgement

#normalize weights
sumWeights = float(sum(weights))
for i in xrange(len(weights)):
    weights[i] = weights[i]/sumWeights

# draw fractal
fractal.makeFractal(ifs=bifs,
            weights=weights,
            height=1000, width=1000,
            xRange=(-0.25, 1.25), yRange=(-0.25, 1.25),
            iterations=3000000, graininess=5,
            bmpname="carpetBIFS")