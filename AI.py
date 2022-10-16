import random as rand
import time
import main

class Robot():
    def __init__(self, player : main.Player, ball : main.Ball) -> None:        
        if player.x < main.WIDTH /2:
            self.prep = -1
            self.player = [player, 0] # 0 cause left
        else:
            self.prep = 1
            self.player = [player, 1] # 1 cause right

        self.ball = ball

        return

    def calc_ball_trajectory(self):        
        # init variables
        player_position = [self.player[0].x, self.player[0].y]
        self.ball_position = [self.ball.position[0], self.ball.position[1]]
        self.BALL_VELOCITY = [self.ball.x_velocity, self.ball.y_velocity]

        if self.player[1] == 1: # if player is right
            while self.ball_position[0] + main.BALL_VELOCITY < player_position[0]: # while ball still didnt reach player.x
                # If ball touches y screen limit 
                if self.ball_position[1] < main.BALL_VELOCITY and self.BALL_VELOCITY[1] < 0:
                    self.BALL_VELOCITY[1] = main.BALL_VELOCITY
                elif self.ball_position[1] > main.HEIGHT - main.BALL_VELOCITY and self.BALL_VELOCITY[1] > 0:
                    self.BALL_VELOCITY[1] = -main.BALL_VELOCITY
            
                self.ball_position[0] += self.BALL_VELOCITY[0]
                self.ball_position[1] += self.BALL_VELOCITY[1]

        elif self.player[1] == 0: # if player is left
            while self.ball_position[0] - main.BALL_VELOCITY > player_position[0]: # while ball still didnt reach player.x
                # If ball touches y screen limit 
                if self.ball_position[1] < main.BALL_VELOCITY and self.BALL_VELOCITY[1] < 0:
                    self.BALL_VELOCITY[1] = main.BALL_VELOCITY
                elif self.ball_position[1] > main.HEIGHT - main.BALL_VELOCITY and self.BALL_VELOCITY[1] > 0:
                    self.BALL_VELOCITY[1] = -main.BALL_VELOCITY
            
                self.ball_position[0] += self.BALL_VELOCITY[0]
                self.ball_position[1] += self.BALL_VELOCITY[1]

        final_position = self.ball_position 
        return final_position                 


    def play(self):
        if self.ball.x_velocity == self.prep * main.BALL_VELOCITY: # if ball coming AI way

            final_ball_position = self.calc_ball_trajectory()
            # Calc Frames to humanize AI
            frames_nec = int(abs(final_ball_position[0]-self.ball.position[0]) / main.BALL_VELOCITY)
            frame_min = int(abs(final_ball_position[1] - self.player[0].y) / main.VELOCITY)
            # If 
            if frames_nec - frame_min < 40:
                if self.player[0].y + (self.player[0].size[1] /4) < final_ball_position[1] and self.player[0].y + (self.player[0].size[1] * 3 /4) > final_ball_position[1]:
                    self.player[0].velocity = 0
                elif self.player[0].y + (self.player[0].size[1] /2) < final_ball_position[1]:
                    self.player[0].velocity = main.VELOCITY            
                elif self.player[0].y + (self.player[0].size[1] /2) > final_ball_position[1]:
                    self.player[0].velocity = -main.VELOCITY

            else:
                if self.player[0].y + (self.player[0].size[1] /4) < main.HEIGHT/2 and self.player[0].y + (self.player[0].size[1] * 3 /4) > main.HEIGHT/2:
                    self.player[0].velocity = 0
                elif self.player[0].y + (self.player[0].size[1] /2) < main.HEIGHT/2:
                    self.player[0].velocity = main.VELOCITY            
                else:
                    self.player[0].velocity = -main.VELOCITY

        else:
            self.player[0].velocity = 0        
        return        


if __name__ == "__main__":
    while 1:
        chosen = input("2 players[2], 1 player[1] or 0 players[0]?")
        if chosen == "1":
            option = "1"
            break
        elif chosen == "0":
            option = "0"
            break
        elif chosen == "2":
            option = "2"
            break
        else:
            print("I didnt understand please type 0, 1 or 2")

    main.main(name = option)
