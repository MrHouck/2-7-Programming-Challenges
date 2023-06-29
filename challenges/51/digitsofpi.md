# Challenge #51 - Calculate the first N Digits of Pi

This challenge had me go down a massive rabbit hole of the way people have been calculating pi, such as the y-cruncher and how Google has calculated 100 trillion digits of pi. Then I got interested in how y-cruncher worked, and found out it had about a half a million lines of code, which is just so interesting to me. How could something as "simple" as calculating digits of pi become 500,000 lines of code? It seems like the algorithm isn't too complex (I am writing this blurb before I write the code). Anyways, very interesting stuff, I highly recommend reading about it because I was completely in awe of how advanced this stuff gets.

To help with precision, I used the libraries `mpmath` and `gmpy2` for arbitrary-precision floating point arithmetic 

I also had to increase the recursion limit since this algorithm does rely on recursion

To improve the speed of this, there are multiplate optimizations that can be made, such as binary splitting, but I don't understand it and I feel like I'd just be ripping someone else's code [(sort of like what this guy did)](https://pi-calculator.netlify.app). You can read about a more optimized chudnovsky's algorithm in python [here](https://www.craig-wood.com/nick/articles/pi-chudnovsky/). Obviously if you really want speed you would program this in C or C++, or hell, even assembly. Too bad!

This program makes use of the Chudnovsky algorithm, which looks something like this:
$$\frac{426880\sqrt{10005}}{\pi }=\sum_{q=0}^{\infty }\frac{\left ( 6q \right )!(545140134q + 13591409)}{\left ( 3q \right )!\left ( q! \right )^{3}\left ( -262537412640768000 \right )^{q}}$$
This is apparently super fast and correct, and it's honestly mind-boggling how this formula could ever be figured out.

To calculate pi, we "simplify" (I say in quotes because of how monstrous this looks) the formula to look like this:
$$\frac{426880\sqrt{10005}}{\sum_{q=0}^{\infty }\frac{\left ( 6q \right )!(545140134q + 13591409)}{\left ( 3q \right )!\left ( q! \right )^{3}\left ( -262537412640768000 \right )^{q}}}=\pi$$

This is actually quite simple to calculate, the problem just arises when dealing with numbers this large and decimals this long, which is where `mpmath` and `gmpy2` come in to do the heavily lifting of arbitrary-precision math. 

Each iteration of the Chudnovsky algorithm produces ~14 (rounded) digits of PI, an improvement upon this code would be to produce the actual # of digits asked for (it does not do that, try inputting 1 for the amount of digits to calculate). All of this math is way too complicated for me right now, so maybe one day I will understand it enough to be able to fix it.