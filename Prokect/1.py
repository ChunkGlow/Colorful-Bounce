
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player movement speed
PLAYER_SPEED = 5

class Player:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.speed = PLAYER_SPEED
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        
        # Keep player within screen bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class StaticSprite:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

def main():
    # Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pygame Two Sprites Game")
    clock = pygame.time.Clock()
    
    # Create sprites
    player = Player(100, 100, 50, 50, BLUE)  # Controllable blue rectangle
    static_sprite = StaticSprite(400, 300, 60, 60, RED)  # Static red rectangle
    
    # Game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Handle continuous key presses
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx = -player.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx = player.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            dy = -player.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            dy = player.speed
        
        # Move player
        player.move(dx, dy)
        
        # Clear screen
        screen.fill(BLACK)
        
        # Draw sprites
        player.draw(screen)
        static_sprite.draw(screen)
        
        # Update display
        pygame.display.flip()
        clock.tick(FPS)
    
    # Quit
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
