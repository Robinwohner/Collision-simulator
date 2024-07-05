import numpy as np
import pygame
import sys

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Collision Simulator")

        # pygame.display.set_caption('Collision Simulator')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((640, 480))

        # small box 1 
        self.smallbox1 = pygame.image.load('images/smallbox.png')# 50 x 50
        self.smallbox1_size = 50
        self.smallbox1_pos = [200, 480//2-25]
        self.smallbox1_mass = 1    # mass in kg
        self.smallbox1_velocity = 0.0

        # small box 2
        self.smallbox2 = pygame.image.load('images/smallbox.png')# 50 x 50
        self.smallbox2_pos = [500, 480//2-25]
        self.smallbox2_mass = 1    # mass in kg
        self.smallbox2_velocity = -3.0

        # big boxes 1-4
        self.bigbox1 = pygame.image.load('images/bigbox1.png')  # 75 x 75
        self.bigbox1_pos = [500, 480/2-37.5]
        self.bigbox1_mass = 100.0    # mass in kg
        self.bigbox1_velocity = 3.0

        self.bigbox2 = pygame.image.load('images/bigbox2.png')  # 100 x 100
        self.bigbox2_pos = [500, 480/2-50]
        self.bigbox2_mass = 10000.0    # mass in kg

        self.bigbox3 = pygame.image.load('images/bigbox3.png')  # 125 x 125
        self.bigbox3_pos = [500, 480/2-72.5]
        self.bigbox3_mass = 100000.0    # mass in kg

        self.bigbox4 = pygame.image.load('images/bigbox4.png')  # 150 x 150
        self.bigbox4_pos = [500, 480/2-75]
        self.bigbox4_mass = 1000000.0    # mass in kg

        # set up text display
        self.count = 0



    def run(self):
        self.count = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    
                    # changing the animations by clicking 1-5
                    if event.key == pygame.K_1:
                        # reset position and velocity for left box
                        self.smallbox2 = pygame.image.load('images/smallbox.png')# 50 x 50
                        self.smallbox1_pos = [200, 480//2-25]
                        self.smallbox1_velocity = 0.0
                        self.smallbox2_mass = 1

                        self.smallbox2_pos = [500, 480//2-25]
                        self.smallbox2_velocity = -3.0

                        m2 = self.smallbox2_mass
                        self.count = 0

                    if event.key == pygame.K_2:
                        # reset position and velocity
                        self.smallbox1_pos = [200, 480//2-25]
                        self.smallbox1_velocity = 0.0

                        self.smallbox2 = pygame.image.load('images/bigbox1.png')  # 75 x 75
                        self.smallbox2_pos = [500, 480/2-37.5]
                        self.smallbox2_mass = self.bigbox1_mass

                        m2 = self.bigbox1_mass
                        self.smallbox2_velocity = -3.0
                        self.count = 0

                    if event.key == pygame.K_3:
                        # reset position and velocity
                        self.smallbox1_pos = [200, 480//2-25]
                        self.smallbox1_velocity = 0.0

                        self.smallbox2 = pygame.image.load('images/bigbox2.png')
                        self.smallbox2_pos = [500, 480/2-50]
                        self.smallbox2_mass = self.bigbox2_mass

                        m2 = self.bigbox2_mass
                        self.smallbox2_velocity = -3.0
                        self.count = 0

                    if event.key == pygame.K_4:
                        # reset position and velocity
                        self.smallbox1_pos = [200, 480//2-25]
                        self.smallbox1_velocity = 0.0

                        self.smallbox2 = pygame.image.load('images/bigbox3.png')
                        self.smallbox2_pos = [500, 480/2-72.5]
                        self.smallbox2_mass = self.bigbox3_mass

                        m2 = self.bigbox3_mass
                        self.smallbox2_velocity = -3.0
                        self.count = 0

                    if event.key == pygame.K_5:
                        # reset position and velocity
                        self.smallbox1_pos = [200, 480//2-25]
                        self.smallbox1_velocity = 0.0

                        self.smallbox2 = pygame.image.load('images/bigbox4.png')
                        self.smallbox2_pos = [500, 480/2-75]
                        self.smallbox2_mass = self.bigbox4_mass

                        m2 = self.bigbox4_mass
                        self.smallbox2_velocity = -3.0
                        self.count = 0

            self.screen.fill((115,161,186))

            self.screen.blit(self.smallbox1, (int(self.smallbox1_pos[0]), int(self.smallbox1_pos[1])))
            self.screen.blit(self.smallbox2, (int(self.smallbox2_pos[0]), int(self.smallbox2_pos[1])))

            self.smallbox1_pos[0] += self.smallbox1_velocity
            self.smallbox2_pos[0] += self.smallbox2_velocity


            m1 = self.smallbox1_mass
            v1 = self.smallbox1_velocity
            m2 = self.smallbox2_mass
            v2 = self.smallbox2_velocity

            # collision handling
            if self.smallbox2_pos[0] < self.smallbox1_pos[0] + self.smallbox1_size:
                self.count += 1
                # include physics to calculator post-collision velocities
                A = np.array([[m1, m2],
                            [1, -1]])
                
                # Set up the constants vector b
                b = np.array([m1*v1 + m2*v2,
                            v2 - v1])
                
                # Solve the system of equations
                u1, u2 = np.linalg.solve(A, b)

                self.smallbox1_velocity = u1
                self.smallbox2_velocity = u2 

            # collision with left-side wall:
            if self.smallbox1_pos[0] <= 0:
                self.smallbox1_velocity = -(self.smallbox1_velocity)
                self.count += 1

            font = pygame.font.Font(None, 32)
            text = font.render(str(self.count), True, (0,255,0), (0,0,128))
            textRect = text.get_rect()
            text_pos = (30,50)
            self.screen.blit(text, textRect)

            pygame.display.update()
            self.clock.tick(30)

Game().run()