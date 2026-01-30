import pygame
import var
import buttons

pygame.init()
interfaz = pygame.display.set_mode((var.interfazWidth, var.interfazHeight))
reloj = pygame.time.Clock()


buttons = buttons.Buttons(interfaz)

def turno(turno, button, casilla):
    if turno == 1 and var.casilla[casilla]:
        interfaz.blit(buttons.image1, button)
        var.turno = 2
        var.casilla[casilla] = False
        var.X[casilla] = True 
    elif turno == 2 and var.casilla[casilla]:
        interfaz.blit(buttons.image2, button)
        var.turno = 1
        var.casilla[casilla] = False 
        var.O[casilla] = True
        
def winer():
    if var.casilla[0] == False and var.casilla[1] == False and var.casilla[2] == False:
        if var.X[0] == True and var.X[1] == True and var.X[2] == True:
            var.winer = True
        if var.O[0] == True and var.O[1] == True and var.O[2] == True:
            var.winer = True
    if var.casilla[3] == False and var.casilla[4] == False and var.casilla[5] == False:
        if var.X[3] == True and var.X[4] == True and var.X[5] == True:
            var.winer = True
        if var.O[3] == True and var.O[4] == True and var.O[5] == True:
            var.winer = True
        
    if var.casilla[6] == False and var.casilla[7] == False and var.casilla[8] == False:
        if var.X[6] == True and var.X[7] == True and var.X[8] == True:
            var.winer = True
        if var.O[6] == True and var.O[7] == True and var.O[8] == True:
            var.winer = True
        
    if var.casilla[0] == False and var.casilla[4] == False and var.casilla[8] == False:
        if var.X[0] == True and var.X[4] == True and var.X[8] == True:
            var.winer = True
        if var.O[0] == True and var.O[4] == True and var.O[8] == True:
            var.winer = True
    
    if var.casilla[2] == False and var.casilla[4] == False and var.casilla[6] == False:
        if var.X[2] == True and var.X[4] == True and var.X[6] == True:
            var.winer = True
        if var.O[2] == True and var.O[4] == True and var.O[6] == True:
            var.winer = True
        
    if var.casilla[0] == False and var.casilla[3] == False and var.casilla[6] == False:
        if var.X[0] == True and var.X[3] == True and var.X[6] == True:
            var.winer = True
        if var.O[0] == True and var.O[3] == True and var.O[6] == True:
            var.winer = True
        
    if var.casilla[1] == False and var.casilla[4] == False and var.casilla[7] == False:
        if var.X[1] == True and var.X[4] == True and var.X[7] == True:
            var.winer = True
        if var.O[1] == True and var.O[4] == True and var.O[7] == True:
            var.winer = True
        
    if var.casilla[2] == False and var.casilla[5] == False and var.casilla[8] == False:
        if var.X[2] == True and var.X[5] == True and var.X[8] == True:
            var.winer = True
        if var.O[2] == True and var.O[5] == True and var.O[8] == True:
            var.winer = True
        
interfaz.fill((0, 0, 0))
                
while var.running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False                
        if event.type == pygame.FINGERDOWN:
            x = event.x * interfaz.get_width()
            y = event.y * interfaz.get_height()
            if buttons.button1.collidepoint(x, y):
                turno(var.turno, buttons.button1, 0)
                winer()
            if buttons.button2.collidepoint(x, y):
                turno(var.turno, buttons.button2, 1)   
                winer() 
            if buttons.button3.collidepoint(x, y):
                turno(var.turno, buttons.button3, 2)
                winer()
            if buttons.button4.collidepoint(x, y):
                turno(var.turno, buttons.button4, 3)
                winer()
            if buttons.button5.collidepoint(x, y):
                turno(var.turno, buttons.button5, 4)
                winer()
            if buttons.button6.collidepoint(x, y):
                turno(var.turno, buttons.button6, 5)
                winer()
            if buttons.button7.collidepoint(x, y):
                turno(var.turno, buttons.button7, 6)
                winer()
            if buttons.button8.collidepoint(x, y):
                turno(var.turno, buttons.button8, 7)
                winer()
            if buttons.button9.collidepoint(x, y):
                turno(var.turno, buttons.button9, 8)
                winer()
                
    if var.winer == False:
        buttons.draw()
    if var.winer == True:
        interfaz.fill(var.pantallaMuerte)                                                                
    
    pygame.display.update()
                                                
pygame.quit()            