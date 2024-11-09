import pygame
import random

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monty Hall Problem")

box_img = pygame.image.load('./graphics/box.png')
car_img = pygame.image.load('./graphics/win.png')
goat_img = pygame.image.load('./graphics/lose.png')


box_positions = [(150, 200), (325, 200), (500, 200)]


selected_box = None
revealed_box = None
final_choice = None
prize_box = random.randint(0, 2)
game_stage = 1


pygame.font.init()
font = pygame.font.Font(None, 36)

def draw_boxes():
    for i, pos in enumerate(box_positions):
        if i == revealed_box:
            screen.blit(goat_img, pos)
            text = font.render("Wrong Box", True, (255, 0, 0))
            screen.blit(text, (pos[0], pos[1] - 40))
        elif i == final_choice and game_stage == 3:
            if i == prize_box:
                screen.blit(car_img, pos)
                text = font.render("You won!", True, (0, 255, 0))
                screen.blit(text, (pos[0], pos[1] - 40))
            else:
                screen.blit(goat_img, pos)
                text = font.render("You LOST!", True, (255, 0, 0))
                screen.blit(text, (pos[0], pos[1] - 40))
        else:
            screen.blit(box_img, pos)

    if game_stage == 2:
        prompt_text = font.render("Make your final choice. You can switch or stick.", True, (255, 255, 255))
        screen.blit(prompt_text, (WIDTH // 2 - prompt_text.get_width() // 2, HEIGHT - 50))

def main():
    global selected_box, revealed_box, final_choice, game_stage

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and game_stage == 1:
                for i, pos in enumerate(box_positions):
                    rect = pygame.Rect(pos[0], pos[1], box_img.get_width(), box_img.get_height())
                    if rect.collidepoint(event.pos):
                        selected_box = i
                        game_stage = 2
                        revealed_box = random.choice([x for x in range(3) if x != selected_box and x != prize_box])
            elif event.type == pygame.MOUSEBUTTONDOWN and game_stage == 2:
                for i, pos in enumerate(box_positions):
                    rect = pygame.Rect(pos[0], pos[1], box_img.get_width(), box_img.get_height())
                    if rect.collidepoint(event.pos) and i != revealed_box:
                        final_choice = i
                        game_stage = 3

        screen.fill((0, 0, 0))
        draw_boxes()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()