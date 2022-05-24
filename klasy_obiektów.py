import pygame

class Tankowiec:
  def __init__(self):
    self.x_cord = 0
    self.y_cord = 0
    self.image = pygame.image.load("tankowiec.png")
    
  def tick(self):
    pass
  
  def draw(self):
    window.blit(self.image(self.x_cord,self.y_cord)
               
       
