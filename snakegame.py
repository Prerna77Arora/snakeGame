import pygame
import random
import time 

pygame.init()

#constants 
Width , Height = 800,600
Snake_size = 20
Fps = 15 #fps means frame rate higher frame rate means smoother animation 

#colours 
blue = (0,0,102)
pink =(255,179,217)
orange=(255,204,153)
green=(170,255,128)

#snake initializtion 
snake = [{"x":Width/2 , "y" : Height/2}]
snake_direction = "RIGHT"

#Food initialization 
food = {"x": round (random.randrange(0,Width-Snake_size)/20)*20,
        "y":round (random.randrange(0,Height-Snake_size)/20)*20}

#pygame setup
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

#Game loop
def game_loop():
      global snake_direction
      global food

      while True :
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                         pygame.quit()
                         quit()

                  
                  elif event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_UP and not snake_direction == "DOWN":
                        snake_direction = "UP"
                     elif event.key == pygame.K_DOWN and not snake_direction == "UP":
                        snake_direction = "DOWN"
                     elif event.key == pygame.K_LEFT and not snake_direction == "RIGHT":
                        snake_direction = "LEFT"
                     elif event.key == pygame.K_RIGHT and not snake_direction == "LEFT":
                        snake_direction = "RIGHT"

            #Move the Snake 
            if snake_direction =="UP":
                snake[0]["y"] -= Snake_size
            elif snake_direction =="DOWN":
                    snake[0]["y"] += Snake_size
            elif snake_direction =="RIGHT":
                 snake[0]["x"] += Snake_size

            elif snake_direction =="LEFT":
                 snake[0]["x"] -= Snake_size

            #check for the collision of snake with the walls 
            if snake[0]["x"]<0 or  snake[0]["x"]>=Width or snake[0]["y"]<0  or snake[0]["y"]>=Height:
                 game_over()

            #check for collison of snake with food
            if snake[0]["x"]== food["x"]  and snake[0]["y"]== food["y"]:
                 
                 food ={"x": round(random.randrange(0, Width - Snake_size) / 20.0) * 20.0,
                 "y": round(random.randrange(0, Height - Snake_size) / 20.0) * 20.0}
            snake.append({"x": 0, "y": 0}) 

            #update the screen 
            screen.fill(blue)
            draw_snake()
            draw_food()
            pygame.display.update()

            #set the frame rate 
            clock.tick(Fps)

# function to draw snakes
def draw_snake():
     for segment in snake :
          pygame.draw.rect(screen,pink,[segment ["x"],segment ["y"],Snake_size,Snake_size])

# function to draw food 
def draw_food():
     pygame.draw.rect(screen,green,[food["x"],food["y"],Snake_size,Snake_size])

# function to display game over message 
def game_over():
     font = pygame.font.SysFont(None, 75)
     text = font.render("Game Over", True, pink)
     screen.blit(text, [Width/ 4, Height / 2])
     pygame.display.update()
     time.sleep()
     game_loop()

game_loop()     

          


                        

      


      