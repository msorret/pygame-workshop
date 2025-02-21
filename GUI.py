import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = HEIGHT - 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DINO_COLOR = (50, 168, 82)
CACTUS_COLOR = (200, 50, 50)
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")
clock = pygame.time.Clock()

# Dino Class
class Dino:
    def __init__(self):
        self.x = 50
        self.y = GROUND_HEIGHT - 40
        self.width = 40
        self.height = 40
        self.vel_y = 0
        self.jumping = False

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_STRENGTH
            self.jumping = True

    def update(self):
        self.vel_y += GRAVITY
        self.y += self.vel_y
        if self.y >= GROUND_HEIGHT - self.height:
            self.y = GROUND_HEIGHT - self.height
            self.jumping = False

    def draw(self, screen):
        pygame.draw.rect(screen, DINO_COLOR, (self.x, self.y, self.width, self.height))

# Cactus Class
class Cactus:
    def __init__(self):
        self.x = WIDTH
        self.y = GROUND_HEIGHT - 30
        self.width = 20
        self.height = 30
        self.speed = 5

    def update(self):
        self.x -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, CACTUS_COLOR, (self.x, self.y, self.width, self.height))

    def off_screen(self):
        return self.x + self.width < 0

# Game Loop
running = True
dino = Dino()
cacti = []
score = 0
spawn_timer = 0

while running:
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, GROUND_HEIGHT), (WIDTH, GROUND_HEIGHT), 2)
    
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()
    
    # Update Dino
    dino.update()
    dino.draw(screen)
    
    # Spawn Cactus
    if spawn_timer > random.randint(60, 120):
        cacti.append(Cactus())
        spawn_timer = 0
    spawn_timer += 1
    
    # Update Cacti
    for cactus in cacti[:]:
        cactus.update()
        cactus.draw(screen)
        if cactus.off_screen():
            cacti.remove(cactus)
            score += 1
        
        # Collision Detection
        if (dino.x < cactus.x + cactus.width and dino.x + dino.width > cactus.x and
            dino.y < cactus.y + cactus.height and dino.y + dino.height > cactus.y):
            running = False  # Game Over
    
    # Display Score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
