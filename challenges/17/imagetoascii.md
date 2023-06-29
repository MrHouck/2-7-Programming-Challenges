# Challenge #17 - Image to ASCII

Converting an Image to ASCII is really quite simple, but there are multiple ways to go about it. My approach involves converting the image to grayscale, and then mapping each grayscale level to a value in this string:
```$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'.```
This string is a character ramp for grayscale pictures, going from dark -> light. I found this list [here.](http://paulbourke.net/dataformats/asciiart/)

I used the PIL library for python to help deal with the pixel data of an image. You can view the outputs for the three images I tested in the /output/ folder in this directory.

I'm considering revisiting this challenge and making it compatible with a video, but maybe for another time.