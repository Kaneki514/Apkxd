import pygame

class Buttons:
    def __init__(self, interfaz):
        self.interfaz = interfaz
        self.color = (255, 0, 0)
        
    def buttons(self):
        self.button1 = pygame.Rect(55, 0, 200, 200)
        self.button2 = pygame.Rect(255, 0, 200, 200)
        self.button3 = pygame.Rect(455, 0, 200, 200)
        self.button4 = pygame.Rect(55, 200, 200, 200)           
        self.button5 = pygame.Rect(255, 200, 200, 200)     
        self.button6 = pygame.Rect(455, 200, 200, 200)
        self.button7 = pygame.Rect(55, 400, 200, 200)
        self.button8 = pygame.Rect(255, 400, 200, 200)
        self.button9 = pygame.Rect(455, 400, 200, 200)
        
        
    def draw(self):
        self.buttons()
        self.image()
        pygame.draw.rect(self.interfaz, self.color, self.button1, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button2, 1)        
        pygame.draw.rect(self.interfaz, self.color, self.button3, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button4, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button5, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button6, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button7, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button8, 1)
        pygame.draw.rect(self.interfaz, self.color, self.button9, 1)
        
    def image(self):
        def redimencionar(imagen, scale):
            w = imagen.get_width()
            h = imagen.get_height()
            imagen = pygame.transform.scale(imagen, (w*scale, h*scale))
            return imagen
        self.image1 = pygame.image.load("assets/X.png")
        self.image1 = redimencionar(self.image1, 0.105)
        self.image2 = pygame.image.load("assets/X.png")
        self.image2 = redimencionar(self.image2, 0.105)
        
        