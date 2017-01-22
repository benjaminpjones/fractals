- -   - -         - -   - -                           - -   - -         - -   - -
     This program was my solution to making high quality raster images of self-similar fractals.  For more information on the mathematics of these fractals, see [1].  The chaos game [2] is utilized for memory efficiency.

     The chaos game effectively randomly generates points in a given fractal, giving us a decent approximation of the fractal in question. Generally, implementations of the chaos game generate many (~millions) of points contained in our fractal set, then plot thos points in an image.  My implementation is modified slightly so that we can increase the visual quality of the image while maintaining constant space usage with respect to the number of points plotted. The program runs as follows:
         
  1) Initialize a 2-D byte array, with dimensions of the final image - each byte representative of the brightness of one pixel.
  2) Run chaos game, increasing the brightness each time we land on a pixel
  3) Convert byte array to bitmap

     Essentially, probability density is measured at each pixel. Because every fractal has different measure and dimension, some the runtime of the program needs to be adjusted accordingly.  One need to plot more points for the Sierpinski Gasket than for the Cantor Set with similar detail.  Therefore, a brightness parameter is included to vary the runtime. Think of this like the exposure on a camera: nothing will show up if it is too low, and every point will be white if it is too high. In addition, great detail is not always required, and can be counterproductive because of the additional time. To increase the speed of fractal generation, in exchange for accuracy, one can adjust the graininess parameter. This is roughly analogus to the ISO on a camera. Finally, the user can adjust the weights of each function in the IFS. This is necessary for fractals like the barnsley fern. For more information about these parameters, see the comments in the code.


Notes:

1. Hutchinson, John, Fractals and Self-Similarity, Indiana Univ. Math. J. 30 No.5 (1981), 713-747.

2. https://en.wikipedia.org/wiki/Chaos_game