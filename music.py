import pygame
import os

pygame.init()
pygame.mixer.init()

MUSIC_FOLDER = "Music/" 
SUPPORTED_FORMATS = (".mp3")

playlist = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith(SUPPORTED_FORMATS)]
current_track = 0 if playlist else None

# Function to play music
def play_music():
    if playlist:
        pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, playlist[current_track]))
        pygame.mixer.music.play()
        print(f"Playing: {playlist[current_track]}")

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

# Function to play next track
def next_track():
    global current_track
    if playlist:
        current_track = (current_track + 1) % len(playlist)
        play_music()

# Function to play previous track
def previous_track():
    global current_track
    if playlist:
        current_track = (current_track - 1) % len(playlist)
        play_music()

# Start playing the first track (if available)
if current_track is not None:
    play_music()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next
                next_track()
            elif event.key == pygame.K_b:  # Previous
                previous_track()

pygame.quit()
