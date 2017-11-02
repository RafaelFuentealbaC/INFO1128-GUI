from PIL import Image
import pygame

img = pygame.image.load('F4.PNG')
w_h = pygame.Surface.get_size(img)
destino = pygame.Surface(w_h)
im = pygame.transform.threshold(destino,img,(255,0,0),(100,100,100),(0,0,0),2)
pygame.image.save(destino,'F4_1.PNG')


img = Image.open('F4_1.PNG')
imagen = img.convert('RGB')
pixels = imagen.load()
width,height = imagen.size
for x in range(width):
    for y in range(height):
        r,g,b = pixels[x,y]
        pixels[x,y] = (b,g,r)
imagen.save('F4_Flores_Rojas.PNG')
imagen.show()
