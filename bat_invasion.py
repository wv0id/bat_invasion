import pygame

from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import game_functions as gf

def run_game():
  pygame.init()

  ai_settings = Settings()
  stats = GameStats(ai_settings)
  screen = pygame.display.set_mode(
    (ai_settings.screen_width, ai_settings.screen_height))
  sb = Scoreboard(ai_settings, screen, stats)
  ship = Ship(ai_settings, screen)
  bullets = Group()
  bats = Group()
  gf.create_fleet(ai_settings, screen, ship, bats)

  pygame.display.set_caption("Bat Invasion")

  play_button = Button(ai_settings, screen, "Play")

  while True:
    gf.check_events(ai_settings, screen, ship, bullets, bats, stats, sb, play_button)

    if stats.game_active:
      ship.update()
      gf.update_bullets(ai_settings, screen, ship, bats, bullets, stats, sb)
      gf.update_bats(ai_settings, stats, sb, screen, ship, bats, bullets)

    gf.update_screen(ai_settings, screen, stats, ship, bats, bullets, play_button, sb)

run_game()