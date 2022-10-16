import time
import pygame

# Declare constant variables
WIDTH = 960
HEIGHT = 540

FPS = 60
VELOCITY = 5

BALL_VELOCITY = 5

class Player():
    def __init__(self, side : int):
        # put player either left 0 or rigth 1
        if side == 0:
            self.x = 20
        elif side ==1:
            self.x = WIDTH - 20

        self.y = int(HEIGHT/2)
        self.size = (5, 60)
        self.velocity = 0
        return

    def update_position(self):
        if  self.velocity == -VELOCITY and  self.y > 0:
            self.y += self.velocity
        elif  self.velocity == VELOCITY and  self.y < HEIGHT-60:
            self.y += self.velocity

    def draw(self, WINDOW):
        self.update_position()
        r = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        pygame.draw.rect(WINDOW, [255, 255, 255], r)
        return

class Ball():
    def __init__(self, right_player : Player, left_player : Player):
        self.position = [int(WIDTH/2), 40]
        self.x_velocity = BALL_VELOCITY
        self.y_velocity = BALL_VELOCITY
        self.right_player = right_player
        self.left_player = left_player
        self.scored = False
        return

    def update_position(self):
        # If ball touches right player
        if self.position[0] + BALL_VELOCITY > self.right_player.x and self.x_velocity > 0 and self.position[1]>self.right_player.y and self.position[1]<self.right_player.y+self.right_player.size[1]:
            self.x_velocity = -BALL_VELOCITY
        # If ball touches left player
        elif self.position[0] - BALL_VELOCITY < self.left_player.x and self.x_velocity < 0 and self.position[1]>self.left_player.y and self.position[1]<self.left_player.y+self.left_player.size[1]:
            self.x_velocity = BALL_VELOCITY
        # If ball touches y screen limit 
        if self.position[1] < BALL_VELOCITY and self.y_velocity < 0:
            self.y_velocity = BALL_VELOCITY
        elif self.position[1] > HEIGHT - BALL_VELOCITY and self.y_velocity > 0:
            self.y_velocity = -BALL_VELOCITY

        # If ball is scored
        if self.position[0] < 0:
            self.scored = True
        elif self.position[0] > WIDTH:
            self.scored = True
        # Move ball
        self.position[0] += self.x_velocity
        self.position[1] += self.y_velocity
        return self.scored

    def draw(self, WINDOW):
        self.update_position()
        r = pygame.Rect(self.position[0], self.position[1], 5, 5)
        pygame.draw.rect(WINDOW, [255, 0, 0], r)
        return self.scored

def create_landscape(WINDOW):
    # create and draw seperating line
    for i in range(0, int(HEIGHT/30)):
        line = pygame.Rect(WIDTH/2 -1, i*30, 2, 20)
        pygame.draw.rect(WINDOW, [255, 255, 255], line)

def main(name = "2"):
    pygame.init() 
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # create my window surface  
    clock = pygame.time.Clock()

    right_player = Player(1)
    left_player = Player(0)
    ball = Ball(right_player, left_player)

    if name == "0":
        import AI
        right_computer = AI.Robot(right_player, ball)
        left_computer = AI.Robot(left_player, ball)
    elif name == "1":
        import AI
        right_computer = AI.Robot(right_player, ball)


    # game loop
    running = True
    while running:
        clock.tick(FPS) # FPS
        # Draw everything
        WINDOW.fill([0, 0, 0])
        create_landscape(WINDOW)
        right_player.draw(WINDOW)
        left_player.draw(WINDOW)
        scored = ball.draw(WINDOW)
        # CHeck if AI 
        if name == "0":
            right_computer.play()
            left_computer.play()
        elif name == "1":
            right_computer.play()
        # Check if scored
        if scored == True:
            running = False

        pygame.display.flip() # update the frames

        # Listen for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                # Right
                if name == "2":
                    if event.key == pygame.K_UP:
                        right_player.velocity = -VELOCITY
                    if event.key == pygame.K_DOWN:
                        right_player.velocity = VELOCITY
                # Left
                if name == "2" or name == "1":
                    if event.key == pygame.K_w:
                        left_player.velocity = -VELOCITY
                    if event.key == pygame.K_s:
                        left_player.velocity = VELOCITY
            if event.type == pygame.KEYUP:
                # Right
                if name == "2":
                    if event.key == pygame.K_UP:
                        right_player.velocity = 0
                    if event.key == pygame.K_DOWN:
                        right_player.velocity = 0
                # Left
                if name == "2" or name == "1":
                    if event.key == pygame.K_w:
                        left_player.velocity = 0
                    if event.key == pygame.K_s:
                        left_player.velocity = 0


if __name__ == "__main__":
    main()
