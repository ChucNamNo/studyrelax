import pygame
import time

# Khởi tạo pygame
pygame.init()

# Cài đặt kích thước cửa sổ đồ họa
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chill Music Player")

# Load hình ảnh và âm thanh
background = pygame.image.load("background.jpg")
disc_original = pygame.image.load("disc.png")
disc_size = (200, 200)
disc = pygame.transform.scale(disc_original, disc_size)

# Tạo đối tượng âm thanh
music = pygame.mixer.Sound("music.wav")

# Cờ để theo dõi trạng thái của âm nhạc và đĩa quay
music_playing = False
disc_rotating = False

# Biến để tính thời gian
start_time = None
paused_time = 0
time_paused = None
previous_tick = 0
rotated_disc = disc
rotation_angle = 0

# Load hình ảnh nút bật/tắt nhạc
play_button = pygame.image.load("play_button.png")
play_button = pygame.transform.scale(play_button, (50, 50))
play_button_rect = play_button.get_rect(center=(width // 2, height - 60))

# Load font cho thời gian và dòng chữ chill
font = pygame.font.Font(None, 36)
chill_font = pygame.font.Font(None, 24)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_button_rect.collidepoint(event.pos):
                if music_playing:
                    pygame.mixer.pause()
                    music_playing = False
                    paused_time = time.time() - start_time
                    disc_rotating = False
                else:
                    pygame.mixer.unpause()
                    start_time = time.time() - paused_time
                    music.play(-1)
                    music_playing = True

    # Hiển thị hình nền
    screen.blit(background, (0, 0))

    # Vẽ đĩa nhạc
    if music_playing:
        current_tick = pygame.time.get_ticks()
        time_diff = (current_tick - previous_tick) / 1000  # Đổi đơn vị từ milliseconds sang seconds
        previous_tick = current_tick

        if disc_rotating:
            rotation_angle = (rotation_angle + time_diff * 10) % 360
        rotated_disc = pygame.transform.rotate(disc, rotation_angle)
    else:
        if disc_rotating:
            rotation_angle = (rotation_angle + time_diff * 10) % 360
        rotated_disc = pygame.transform.rotate(disc, rotation_angle)
    disc_rect = rotated_disc.get_rect(center=(width // 2, height // 2))
    screen.blit(rotated_disc, disc_rect.topleft)

    # Vẽ nút bật/tắt nhạc
    screen.blit(play_button, play_button_rect.topleft)

    # Tính thời gian
    if music_playing:
        current_time = time.time() - start_time
        hours = int(current_time // 3600)
        minutes = int((current_time % 3600) // 60)
        seconds = int(current_time % 60)
        time_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        if paused_time:
            current_time = paused_time
            hours = int(current_time // 3600)
            minutes = int((current_time % 3600) // 60)
            seconds = int(current_time % 60)
            time_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        else:
            time_text = "00:00:00"
    time_surface = font.render(time_text, True, (255, 255, 255))
    screen.blit(time_surface, (width // 2 - 50, 20))

    # Vẽ dòng chữ chill
    chill_text = chill_font.render("Have a wonderful day!", True, (255, 255, 255))
    chill_text_rect = chill_text.get_rect(center=(width // 2, height // 2 + 150))
    screen.blit(chill_text, chill_text_rect.topleft)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
