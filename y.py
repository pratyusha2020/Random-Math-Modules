import pygame

def main():
    pygame.init()
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Color Changing Sprite")
    text_surface = pygame.font.Font(None, 36).render('Hello There ', True,pygame.Color('black'))
    text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))
   

    colors ={'red': pygame.Color('red'), 'green': pygame.Color('green'), 'blue': pygame.Color('blue'), 'yellow': pygame.Color('yellow'),'white': pygame.Color('white')}
    current_color = colors['blue']
    x,y= 285,260
    sprite_width, sprite_height = (50,50)
    clock= pygame.time.Clock()
    done= False
    while not done:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          done = True

      pressed= pygame.key.get_pressed()
      if pressed[pygame.K_UP]:
        y-= 1
      if pressed[pygame.K_DOWN]:
        y+= 1
      if pressed[pygame.K_LEFT]:
          x-= 1
      if pressed[pygame.K_RIGHT]:
          x+= 1
      x= min(max(0,x), screen_width-sprite_width)
      y= min(max(0,y), screen_height-sprite_height)

      if x==0: current_color= colors['red']
      elif x== screen_width-sprite_width: current_color= colors['green']
      elif y==0: current_color= colors['blue']
      elif y== screen_height-sprite_height: current_color= colors['yellow']
      else:
        current_color= colors['blue']

      screen.fill((250,250,250))
      pygame.draw.rect(screen, current_color, pygame.Rect(x,y,sprite_width,sprite_height))
      screen.blit(text_surface, text_rect)
      pygame.display.flip()
      clock.tick(90)
    pygame.quit()

if __name__ == '__main__':
    main()



