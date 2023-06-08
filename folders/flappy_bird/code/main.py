import pygame, sys, time, os, pygame_menu, datetime, psycopg2, random
from settings import *
from sprites import BG, Ground, Plane, Obstacle

class DBManager:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def checkIfExists(self, table_name):
        query = f"""
            SELECT *
            FROM INFORMATION_SCHEMA.TABLES
            WHERE TABLE_SCHEMA = 'test'
            AND TABLE_NAME = '{table_name}'
            """

        self.cursor.execute(query)
        output = self.cursor.fetchone()
        print(output)
        return bool(output)

    def getRecords(self):
        query = """SELECT * FROM lab10.test.snake ORDER BY points DESC"""
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def insertIfNotExists(self, username):
        query = f"""INSERT INTO lab10.test.snake(name, points, level)
                SELECT '{username}', 0, 0
                WHERE NOT EXISTS (SELECT 1 FROM lab10.test.snake WHERE name = '{username}')
                """
        self.cursor.execute(query)
        self.commit()

    def updateIfBest(self, username, points, level):
        query = f"""UPDATE lab10.test.snake 
                    SET points = GREATEST(points, {points}), 
                        level = GREATEST(level, {level}) 
                    WHERE name = '{username}'"""
        self.cursor.execute(query)
        self.commit()

    def createTable(self):
        query = """
            CREATE TABLE lab10.test.snake(
                id SERIAL PRIMARY KEY,
                points INTEGER,
                level INTEGER,
                name VARCHAR(255)
            )
            """

        self.cursor.execute(query)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()

    def connect(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="lab10",
            user="postgres",
            port="5432",
            password="Dias2004")
        self.cursor = self.conn.cursor()

        if not self.checkIfExists("snake"):
            print("Not exists")
            self.createTable()
            self.commit()

class RecordsMenu:
    def drawMenu(self, where, data):
        theme = pygame_menu.themes.THEME_BLUE.copy()
        theme.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND  # cursor on scroll
        recordsMenu = pygame_menu.Menu(title='RECORDS', width=450, height=300, enabled=False,
                                       theme=theme, onclose=lambda: recordsMenu.disable())
        recordsMenu.enable()
        recordsMenu.add.vertical_margin(20)  # Adds margin
        table = recordsMenu.add.table()
        max_cell_length = 12
        table.add_row((f"Name{' ' * 8}", f"Points{' ' * 6}", f"Level{' ' * 7}"), cell_font_size=25)
        # recordsMenu.add.label(title=f"Name:{' '*8}Points:{' '*8}Level:{' '*8}", font_size = 25)

        for i in data:
            name = i[3] if len(i[3]) < 9 else i[3][:8] + "..."
            points = str(i[1]) + ' ' * (max_cell_length - len(str(i[1])))
            level = str(i[2]) + ' ' * (max_cell_length - len(str(i[2])))
            table.add_row((name, points, level), cell_font_size=20)
        recordsMenu.mainloop(where)

class PauseMenu:
    def __init__(self, onPlay, onRecord, onQuit):
        self.menu = pygame_menu.Menu('PAUSE', 400, 300, enabled=False,
                                     theme=pygame_menu.themes.THEME_BLUE)
        self.menu.add.button('Play', onPlay)
        self.menu.add.button('Records', onRecord)
        self.menu.add.button("Quit", onQuit)

    def drawMenu(self, where, ):
        self.menu.enable()
        self.menu.mainloop(where)

class Game:
    def __init__(self, db: DBManager):

        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Flappy Bird')
        pygame.display.set_icon(pygame.image.load('../graphics/plane/plane_icon.png'))
        self.clock = pygame.time.Clock()
        self.active = True
        # db
        self.name = ''
        self.dbManager = db
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
        self.pauseMenu = None
        self.recordsMenu = None

        # game state
        self.running = True
        self.isPause = False
        self.gameOver = False
        self.TICK = 150
        self.collectedPoints = 0
        self.currLevel = 1
        self.font = pygame.font.SysFont("Arial", 16)

        # music
        self.music = pygame.mixer.Sound('../sounds/music.wav')
        self.music.play(loops=-1)

    def collisions(self):
        if pygame.sprite.spritecollide(self.plane, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.plane.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == 'obstacle':
                    sprite.kill()
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