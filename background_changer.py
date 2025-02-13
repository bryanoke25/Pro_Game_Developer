import pygame

# Initialize Pygame
pygame.init()

# Set display window size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Background Color Changer")

# Define colors dictionary
COLOR_DICT = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "pink": (255, 192, 203),
    "cyan": (0, 255, 255),
    "purple": (128, 0, 128)
}

# Default background color
bg_color = (255, 255, 255)

# Load font for text
font = pygame.font.Font(None, 36)

# User input
user_text = ""

# Game loop
running = True
while running:
    screen.fill(bg_color)  # Fill background with the selected color

    # Render text input
    input_text = font.render("choose a good color: " + user_text, True, (0, 0, 0))
    screen.blit(input_text, (20, HEIGHT // 2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exit when close button is clicked
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # When Enter is pressed
                bg_color = COLOR_DICT.get(user_text.lower(), bg_color)  # Change color if valid
                user_text = ""  # Reset input
            elif event.key == pygame.K_BACKSPACE:  # Remove last character
                user_text = user_text[:-1]
            else:
                user_text += event.unicode  # Add typed character

    pygame.display.flip()  # Update display

# Quit Pygame
pygame.quit()
