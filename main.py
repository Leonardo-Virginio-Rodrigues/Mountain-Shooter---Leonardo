import pygame

print("Setup start")
pygame.init()
windows = pygame.display.set_mode((800, 600))
print("Setup end")

print("Loop Setup")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
