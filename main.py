import pygame
import sys, time

rect_1 = pygame.Rect( 100, 100 , 100, 100 )
rect_2 = pygame.Rect( 200, 250, 20, 20 )
def _Game():
  pygame.init()
  screen = pygame.display.set_mode(( 400, 600 ))
  pygame.display.set_caption("Example game")
  clock = pygame.time.Clock()
  red = (255, 0, 0) # Red Green Blue
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    screen.fill( (255,255,255) )
    # Rendering
    Boxie(screen, red, rect_1)
    Boxie(screen, red, rect_2)
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #rect_2.move( mouse_x, mouse_y )
    rect_2.update( (mouse_x-10, mouse_y-10), (20, 20) )
    if collision( rect_1, rect_2 ):
      print("Collision")
    #pygame.draw.circle(screen, (0, 0, 255), (mouse_x, mouse_y), 10)
    pygame.draw.line( screen, red, (rect_1.x, 0), (rect_1.x, 500) )
    pygame.draw.line( screen, red, (0,rect_1.y), (500,rect_1.y) )
    pygame.display.flip()

    clock.tick(60)
  
def collision( ra, rb ):
  ax1 = ra.x
  ay1 = ra.y
  ax2 = ax1 + ra.width
  ay2 = ay1 + ra.height
  
  bx1 = rb.x
  by1 = rb.y
  bx2 = bx1 + rb.width
  by2 = by1 + rb.height
  
  if bx2 >= ax1 and bx1 <= ax1 and by2 >= ay1 and by1 <= ay2:
    print("Touch", time.time())
    return True
  
  if bx2 >= ax2 and bx1 <= ax2 and by2 >= ay1 and by1 <= ay2:
    print("Second x axis", time.time())
    return True
  if bx2 >= ax1 and bx1 <= ax1 and by2 >= ay1 and by1 <= ay2:
    print("Second x axis", time.time())
    return True
  if by2 >= ay2 and by1 <= ay2 :
    print("Second x axis", time.time())
    return True

def Boxie(scr, color, my_box):
  pygame.draw.rect(scr, color, my_box, 1)

if __name__ == "__main__":
  _Game( )
