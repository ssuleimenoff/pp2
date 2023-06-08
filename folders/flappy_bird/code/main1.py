import pygame, sys, time, psycopg2
from settings import *
from sprites import BG, Ground, Plane, Obstacle
import pygame_menu.locals

# SQL connection
conn = psycopg2.connect("dbname=postgres user=postgres password=ayan2004")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS records (name VARCHAR(255) NOT NULL, score INT)")
conn.commit()


def name_checker():
    global player_name
    player_name = input("Insert your name: ")

class MenuPage:
    def __init__(self):
        # set up the menu
        self.menu = pygame_menu.Menu('Flappy Bird', WINDOW_WIDTH, WINDOW_HEIGHT)
        self.menu.add.label('Main Menu')
        self.menu.add.vertical_margin(30)
        self.menu.add.button('Start New Game', self.start_game)
        self.menu.add.button('View Records', self.view_records)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)

        # some var for the table
        self.player_name = ''
        self.record = 0

    def start_game(self):
        # reset game var
        self.player_name = ''
        self.record = 0

        # start the game
        self.menu.disable()
        game.start()

    def view_records(self):
        # show records
        self.menu.disable()
        self.menu.clear()

        # retrieve records from db
        cur.execute("SELECT * FROM records ORDER BY score DESC ")
        records = cur.fetchall()

        # display records
        self.menu.add.label('Records', align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.vertical_margin(20)
        for record in records:
            self.menu.add.label(f'{record[0]} - {record[1]}', align=pygame_menu.locals.ALIGN_CENTER)
        self.menu.add.vertical_margin(20)
        self.menu.add.button('Back', self.back_to_menu)

        self.menu.enable()

    def back_to_menu(self):
        # back to the menu page
        self.menu.disable()
        self.menu.clear()
        self.menu.enable()

    def set_player_name(self, val):
        # set the player name as input type
        self.player_name = val

    def update_record(self, score):
        # updating record
        if score > self.record:
            self.record = score

            name_input = self.menu.add.text_input('Insert Your Name: ', default='', maxchar=20, onreturn=self.save_record)
            self.menu.disable()
            self.menu.enable()


    def save_record(self, player_name):
        cur.execute("INSERT INTO records (name, score) VALUES (%s, %s)", (player_name, self.record))
        conn.commit()

    def show_menu(self):
        self.menu.enable()
        self.menu.mainloop(game.display_surface)


class Game:
    def __init__(self):

        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        pygame.display.set_icon(pygame.image.load('../graphics/plane/plane_icon.png'))
        self.clock = pygame.time.Clock()
        self.active = True

        # sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # scale factor
        bg_height = pygame.image.load('../graphics/environment/background.png').get_height()
        self.scale_factor = WINDOW_HEIGHT / bg_height

        # sprite setup
        BG(self.all_sprites, self.scale_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scale_factor)
        self.plane = Plane(self.all_sprites, self.scale_factor / 1.7)

        # timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

        # text
        self.font = pygame.font.Font('../graphics/font/BD_Cartoon_Shout.ttf', 30)
        self.score = 0
        self.start_offset = 0

        # menu
        self.menu_surf = pygame.image.load('../graphics/ui/menu.png').convert_alpha()
        self.menu_rect = self.menu_surf.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.menu_page = MenuPage

        # music
        self.music = pygame.mixer.Sound('../sounds/music.wav')
        self.music.play(loops=-1)

    def start(self):
        self.score = 0
        self.start_offset = pygame.time.get_ticks()
        self.active = True

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.plane.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
                if not self.active:
                    # Game over, update the record
                    self.menu_page.update_record(self.score)
            self.active = False
            self.plane.kill()

    def display_score(self):
        if self.active:
            self.score = (pygame.time.get_ticks() - self.start_offset) // 1000
            y = WINDOW_HEIGHT / 10
        else:
            y = WINDOW_HEIGHT / 2 + (self.menu_rect.height / 1.5)

        score_surf = self.font.render(str(self.score), True, 'black')
        score_rect = score_surf.get_rect(midtop=(WINDOW_WIDTH / 2, y))
        self.display_surface.blit(score_surf, score_rect)

    def run(self):
        last_time = time.time()
        while True:

            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    if self.active:
                        self.plane.jump()
                    else:
                        self.plane = Plane(self.all_sprites, self.scale_factor / 1.7)
                        self.active = True
                        self.start_offset = pygame.time.get_ticks()

                if event.type == self.obstacle_timer and self.active:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scale_factor * 1.1)

            # game logic
            self.display_surface.fill('black')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)
            self.display_score()

            if self.active:
                self.collisions()
            else:
                self.display_surface.blit(self.menu_surf, self.menu_rect)

            pygame.display.update()
        # self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()