import pygame
import random
import sys


# initializing the pygame

pygame.init()

# Screen Size
screen_height = 600
screen_width = 800

# WHITE COLOR

WHITE = (255 , 255 , 255)

# screen display
screen = pygame.display.set_mode((screen_width , screen_height))

# pygame title
pygame.display.set_caption("Monkey Jump")

# Background Image
background1 = pygame.transform.scale(pygame.image.load(f'D:\\python\\Games\\jungle.png').convert(),
                                     (screen_width , screen_height))
background2 = pygame.transform.scale(pygame.image.load(f'D:\\python\\Games\\jbackground2.png').convert(), 
                                     (screen_width , screen_height))
background3 = pygame.transform.scale(pygame.image.load(f'D:\\python\\Games\\jbackground3.png').convert(), 
                                     (screen_width , screen_height))
# Get screen width
bg1_width = background1.get_width()
bg2_width = background2.get_width()
bg3_width = background3.get_width()




# load Bird images
bird_sprites = [pygame.transform.scale(pygame.image.load(f"D:\\python\\Games\\bird{i}.png").convert(), (100 , 100)) 
                for i in range(1 , 3)]

for sprite in bird_sprites:
    sprite.set_colorkey(WHITE)
    
# Object Images
Obj_image =pygame.image.load('D:\\python\\Games\\Treewine3.png')
obj_width , obj_height = Obj_image.get_size()

# BIRD CLASS

class Bird:
    def __init__(self):
        self.x = 700
        self.y = random.randint(200 , 500)
        self.speed = 5
        self.sprites = bird_sprites
        self.current_sprite = 0
        self.frame_counter = 0
        self.animation_speed = 10
        
    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.current_sprite = (self.current_sprite + 1)%len(self.sprites)
            self.frame_counter = 0
            
        self.x -= self.speed
        
        if self.x <= -100:
            self.x = 800
            self.y = random.randint(200 , 500)
            
    def draw(self , screen):
        screen.blit(self.sprites[self.current_sprite] , (self.x , self.y))
            
        
    
   

def game_loop():

    # set up the clock
    clock = pygame.time.Clock()
    bird= Bird()
    
    
    #background positions
    bg_x = 0
    bg2_x1 = bg1_width
    bg2_x2 = bg2_x1 + bg2_width
    
    bg3_x1 = bg2_x2
    bg3_x2 = bg3_x1 + bg3_width
    
    bg_stopped = False
   
    scroll_speed = 3
    
    
    obj_x = screen_width
    obj_y = screen_height//2 - obj_height// 2
 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        if not bg_stopped:
            bg_x-=scroll_speed
            if bg_x <= -bg1_width:
                bg_x = - -bg1_width
                bg_stopped = True 
            
        # Move Background
        bg2_x1 -= scroll_speed
        bg2_x2 -= scroll_speed
        bg3_x1 -= scroll_speed
        bg3_x2 -= scroll_speed
        
        
        
        # Reset background
        
        if bg2_x1 <= -bg2_width:
            bg2_x1 = bg2_x2 + bg2_width  
            
        if bg2_x2 <= -bg2_width:
            bg2_x2 = bg2_x1 +bg2_width
            
        if bg3_x1 <= -bg3_width:
            bg3_x1 = bg3_x2 + bg3_width 
        if bg3_x2 <= -bg1_width:
            bg3_x2 = bg3_x1 + bg3_width
            
            
        
        
        screen.blit(background1 , (bg_x, 0))
         
        screen.blit(background2 , (bg2_x1 , 0)) 
        screen.blit(background2 , (bg2_x2 , 0)) 
        
        screen.blit(background3 , (bg3_x1 , 0)) 
        screen.blit(background3 , (bg3_x2 , 0)) 
            
        
                
                
        
        
            
          
        # Update Tree Vine
        obj_x -= scroll_speed
        if obj_x <= -obj_width:
            obj_x = bg2_x2 + -75
        
        
        
        screen.blit(Obj_image ,(obj_x , obj_y) )
           
        # Update and draw bird
        
        bird.update()
        bird.draw(screen)
        
        
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    sys.exit()
        
    
if __name__ == '__main__':
    game_loop()
    