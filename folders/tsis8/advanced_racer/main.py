import pygame, sys
import random
import time
from pygame import mixer

# initial game configs
screen_width = 800
screen_height = 600
fps = 60
car_speed = 1

# enemy car configs
side_list = ['left', 'middle', 'right']


class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.size = (screen_width, screen_height)
        self.bg_num = 1
        self.image = pygame.transform.scale(pygame.image.load(f"./assets/bg{self.bg_num}.png"), self.size)

    def draw(self, surf):
        surf.blit(self.image, (0, 0))
        if self.bg_num < 2:
            self.bg_num += 1
        else:
            self.bg_num = 1


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = [75, 50]
        self.side = side_list[random.randint(0, 2)]
        self.image = pygame.transform.scale(pygame.image.load(f"./assets/{random.randint(1, 4)}_car_{self.side}.png"),
                                            self.size)
        self.rect = self.image.get_rect()
        match self.side:
            case 'left':
                self.rect.center = (370, 390)
            case 'middle':
                self.rect.center = (420, 390)
            case 'right':
                self.rect.center = (470, 390)

    def move(self):
        match self.side:
            case 'left':
                self.rect.move_ip(-1.7, car_speed)
            case 'middle':
                self.rect.move_ip(0, car_speed)
            case 'right':
                self.rect.move_ip(1.7, car_speed)
        if self.rect.bottom > 600:
            self.side = side_list[random.randint(0, 2)]
            self.image = pygame.transform.scale(
                pygame.image.load(f"./assets/{random.randint(1, 4)}_car_{self.side}.png"), self.size)
            match self.side:
                case 'left':
                    self.rect.center = (370, 390)
                case 'middle':
                    self.rect.center = (420, 390)
                case 'right':
                    self.rect.center = (470, 390)


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("./assets/main_car_middle.png"), (150, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (420, 550)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left < 150:
            self.image = pygame.transform.scale(pygame.image.load('./assets/main_car_left.png'), (150, 100))
        elif self.rect.right > 650:
            self.image = pygame.transform.scale(pygame.image.load('./assets/main_car_right.png'), (150, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load('./assets/main_car_middle.png'), (150, 100))

        if self.rect.left > 0 and self.rect.right < 780:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(20, 0)
        if self.rect.right < 800 and self.rect.left > 20:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-20, 0)


def main():
    global car_speed
    car_speed = 1
    # pygame initialization
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Rider on the Storm")
    # background image
    bg_image = pygame.image.load('./assets/bg1.png')
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    # background class
    bg = Background()

    # all cars initializing
    enemy_car1 = EnemyCar()
    player_car = PlayerCar()

    # enemy cars sprite groups
    enemy_sprites = pygame.sprite.Group()
    enemy_sprites.add(enemy_car1)

    # all cars sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(enemy_car1)
    all_sprites.add(player_car)

    # enemy cars speed
    inc_speed = pygame.USEREVENT + 1
    pygame.time.set_timer(inc_speed, 1000)

    # loading music
    mixer.music.load('./assets/tsis8_racer_assets_bg_music.mp3')
    mixer.music.play()
    while True:
        for event in pygame.event.get():
            if event.type == inc_speed:
                car_speed += 0.1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # drawing background
        screen.fill((255, 255, 255))
        bg.draw(screen)
        # drawing all sprites
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
            sprite.move()

        # collision detection
        if pygame.sprite.spritecollideany(player_car, enemy_sprites):
            screen.fill((255, 0, 0))
            pygame.display.update()
            for sprite in all_sprites:
                sprite.kill()
            mixer.music.pause()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()