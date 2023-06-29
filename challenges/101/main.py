from PIL import Image, ImageDraw
import random, numpy as np
W=H=256

im = Image.new(mode="RGB", size=(W,H))
draw = ImageDraw.Draw(im)

def generatePoints(n=10, width=256, height=256):
    return np.array([(random.choice(range(width)), random.choice(range(height))) for _ in range(n)])
    

points = generatePoints(25)

#from p5js
def map_value(n, start1, stop1, start2, stop2):
    return (n - start1) / (stop1 - start1) * (stop2 - start2) + start2


for x in range(0, H):
    for y in range(0, W):
        distances = []
        for point in points:
            x_dist = np.power(point[0]-x, 2)
            y_dist = np.power(point[1]-y, 2)
            dist = np.sqrt(x_dist+y_dist)
            distances.append(dist)
        
        n = 0
        sortedDistances = np.sort(distances)
        noise = int(map_value(sortedDistances[n], 0, 75, 0, 255))
        im.putpixel((x,y), (noise, noise, noise))

        for point in points:
            draw.point((int(point[0]), int(point[1])), fill=(255, 0, 0))




im.save("texture.png")