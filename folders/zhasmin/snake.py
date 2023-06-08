import random
import sys

import psycopg2
import pygame


def create_table():
    conn = psycopg2.connect(database='pp2', user='postgres', password='adminkbtu')
    # database connection
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE game ( 
    USER_NAME TEXT PRIMARY KEY NOT NULL, 
    score TEXT NOT NULL);""")
    print("[INFO] Table created successfully!")
    conn.commit()
    cursor.close()
    conn.close()


def add_user():
    add = input().split()
    data_toinsert = (add[0], add[1])
    cursor.execute("SELECT * FROM game WHERE user_name=%s", (add[0],))
    result = cursor.fetchone()
    if result:
        c = result[1]
        print('This user already exists! Your score:', c)
    else:
        postgre_query = """INSERT INTO game(user_name, score) VALUES (%s, %s) """
        cursor.execute(postgre_query, data_toinsert)
        conn.commit()
        print("Data added!")


def fetch_users():
    cursor.execute("SELECT * FROM game ")
    table = cursor.fetchall()
    for row in table:
        c = row[0] + " " + row[1]
        print(c)


def update():
    print("Type who's number you want to change")
    name = input()
    print("New number")
    number = input()
    postgre_query = """UPDATE game SET score = %s WHERE user_name = %s """
    cursor.execute(postgre_query, (number, name))
    conn.commit()
    print("Data updated!")


def find():
    print("Insert name who's score you want to see")
    name = input()
    cursor.execute("SELECT * FROM game ")
    table = cursor.fetchall()
    for row in table:
        if name == row[0]:
            c = row[0] + " " + row[1]
            print(c)


def delete_user():
    print("Insert name you want to delete")
    name = input()
    postgre_query = """DELETE FROM game WHERE user_name = %s """
    cursor.execute(postgre_query, (name,))
    conn.commit()
    print("Data deleted!")


def pause_game(user_name, score):
    # Save game data to the database
    cursor.execute("INSERT INTO game (user_name, score) VALUES (%s, %s)", (user_name, score))
    conn.commit()
    print("Game data saved successfully!")
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    paused = False
        message("Paused. Press ESC to continue playing", black)
        pygame.display.update()
        clock.tick(5)


try:
    cond = False
    conn = psycopg2.connect("dbname=pp2 user=postgres password=adminkbtu")
    cursor = conn.cursor()

    while not cond:
        print(
            "\nChoose action:\n0.Create table\n1.Add user and number\n2.Change number of existing user\n3.Delete user\n4.Find number by name\n5.Show all names and numbers\n6.Exit")
        action = input()
        if action == '1':
            print("Insert data")
            add_user()
        if action == '0':
            create_table()
        if action == '2':
            update()
        if action == '3':
            delete_user()
        if action == '4':
            find()
        if action == '5':
            fetch_users()
        if action == '6':
            cond = True

        # except psycopg2.Error as e:
#     print("Failed!")
finally:
    cursor.close()
    conn.close()
    print("Connection closed!")
pygame.init()
# цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
gr = (100, 200, 100)
dis_width = 800
dis_height = 800
snake_List = []
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Просто змейка')
clock = pygame.time.Clock()
snake_block = 25
snake_speed = 4
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)
sound = pygame.mixer.Sound('./musics/song.mp3')
block = pygame.image.load("./img/wall1.png")
pause = pygame.image.load('./img/mg/pause.jpeg')
pause = pygame.transform.scale(pause, (800, 800))


# Функция которая счетает счет
def Your_score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, gr)
    display.blit(value, [30, 20])


# фукция рисует змею
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, yellow, [x[0], x[1], snake_block, snake_block], 2)


def unpause_game():
    global is_paused
    is_paused = False


# функция выводит текст
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width / 10, dis_height / 1.2])


def Your_level(lavel):
    valu = score_font.render("Уровень: " + str(lavel), True, gr)
    display.blit(valu, [35, 50])


class Wall:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        display.blit(block, (self.x, self.y))


# def pauseState(self):
#         global isPause
#         if isPause == False:
#             display.blit(pause, (0, 0, 800, 800))
#             pygame.time.set_timer(pygame.display.update(), 0)
#             isPause = True
#         else:
#             pygame.time.set_timer(pygame.display.update(), snake_speed)
#             isPause = False


# Example usage
# Функция для остановки игры
def stop_game():
    pygame.quit()


def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0
    levels = 0
    cnt = 10
    snake_speed = 7
    snake_List = []
    length_of_snake = 1
    food_timer = pygame.time.get_ticks() + 6000
    food_timer1 = pygame.time.get_ticks() + 6000
    food_timer3 = pygame.time.get_ticks() + 6000
    foodx = round(random.randrange(2, 31)) * 25.0
    foody = round(random.randrange(2, 31)) * 25.0
    foodx1 = round(random.randrange(2, 31)) * 25.0
    foody1 = round(random.randrange(2, 31)) * 25.0
    foodx2 = round(random.randrange(2, 31)) * 25.0
    foody2 = round(random.randrange(2, 31)) * 25.0
    image = pygame.image.load("./img/food.png")
    image1 = pygame.image.load("./img/food1.png")
    image2 = pygame.image.load("./img/food2.png")
    re = image.get_rect()
    re1 = image1.get_rect()
    re2 = image2.get_rect()
    background = pygame.image.load("./img/back.png")
    background = pygame.transform.scale(background, (800, 800))
    background1 = pygame.image.load("./img/lost1.jpg")
    background1 = pygame.transform.scale(background1, (800, 800))
    pause = pygame.image.load('./img/pause.jpeg')
    sound.play()

    # цикл работает пока игра не закончится

    while not game_over:
        # цикл когда игра законцится и начать снова
        while game_close == True:
            # sound.play()
            display.blit(background1, (0, 0))
            # display.fill(yellow)
            message("Вы проиграли! Нажмите Q для выхода или C для повторной игры!", white)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        sound.stop()
                        # sound.play()
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_paused:
                        unpause_game()
                    else:
                        # остановить игру
                        is_paused = True
                        while is_paused:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                    # возобновить игру
                                    unpause_game()

                # if event.type == pygame.KEYDOWN:
                #     if event.key == pygame.K_SPACE:
                #     # Остановка игры при нажатии ESC
                #         stop_game()
                # pygame.draw.rect(display, yellow, [x[0], x[1], snake_block, snake_block],2).stop()
                # pygame.display.update()
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        # Обновление экрана
        pygame.display.update()
        if y1 >= 25 and x1 <= 25 or y1 <= 25 and x1 >= 25:
            game_close = True
        if x1 <= 750 and y1 >= 750 or x1 >= 750 and y1 <= 750:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        display.blit(background, (0, 0))
        # рисуем еду
        display.blit(image, [foodx, foody, snake_block, snake_block])
        display.blit(image1, [foodx1, foody1, snake_block, snake_block])
        display.blit(image2, [foodx2, foody2, snake_block, snake_block])
        # pygame.display.update()
        # pygame.draw.rect(display, green, [foodx, foody, snake_block, snake_block])
        # pygame.draw.rect(display, yellow, [foodx1, foody1, snake_block, snake_block])
        # pygame.draw.rect(display, black, [foodx2, foody2, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        print(snake_List)

        if len(snake_List) > length_of_snake:
            del snake_List[0]
        # если змея столкнется с хвостом
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(length_of_snake - 1)
        Your_level(levels)

        # если змея столкнется с яблоком
        if x1 == foodx and y1 == foody:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            length_of_snake += 2
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
            food_timer = pygame.time.get_ticks() + 6000

            # pygame.display.update()
        if pygame.time.get_ticks() >= food_timer:
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
            food_timer = pygame.time.get_ticks() + 6000
            # если змея столкнется с вишней
        if x1 == foodx1 and y1 == foody1:
            pygame.mixer.Sound('./musics/nam.mp3').play()
            length_of_snake += 3
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 6000
            # pygame.display.update()
        if pygame.time.get_ticks() >= food_timer1:
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
            food_timer1 = pygame.time.get_ticks() + 6000
            # если змея столкнется с зеленой едой
        if x1 == foodx2 and y1 == foody2:
            pygame.mixer.Sound('./musics/pah.mp3').play()
            length_of_snake = length_of_snake - 2
            if length_of_snake > 1:
                snake_List.pop(0)
                snake_List.pop(0)
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 6000

        if pygame.time.get_ticks() >= food_timer3:
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0
            food_timer3 = pygame.time.get_ticks() + 6000
        if [foodx, foody] in snake_List:
            foodx = round(random.randrange(2, 31)) * 25.0
            foody = round(random.randrange(2, 31)) * 25.0
        if [foodx1, foody1] in snake_List:
            foodx1 = round(random.randrange(2, 31)) * 25.0
            foody1 = round(random.randrange(2, 31)) * 25.0
        if [foodx2, foody2] in snake_List:
            foodx2 = round(random.randrange(2, 31)) * 25.0
            foody2 = round(random.randrange(2, 31)) * 25.0

        file = open(f'./img/{levels}.txt', 'r').readlines()
        walls = []
        for i, line in enumerate(file):
            for j, each in enumerate(line):
                if each == '+':
                    walls.append(Wall(j * 25, i * 25))

        for wall in walls:
            wall.draw()
            if snake_List[len(snake_List) - 1][0] == wall.x and snake_List[len(snake_List) - 1][1] == wall.y:
                game_close = True
            if wall.x == foodx and wall.y == foody:
                foodx = round(random.randrange(2, 31)) * 25.0
                foody = round(random.randrange(2, 31)) * 25.0
            if wall.x == foodx1 and wall.y == foody1:
                foodx1 = round(random.randrange(2, 31)) * 25.0
                foody1 = round(random.randrange(2, 31)) * 25.0
            if wall.x == foodx2 and wall.y == foody2:
                foodx2 = round(random.randrange(2, 31)) * 25.0
                foody2 = round(random.randrange(2, 31)) * 25.0

                # если длинна змеи меньше 0
        if length_of_snake <= 0:
            game_close = True
        if length_of_snake > cnt:
            levels += 1
            levels %= 4
            cnt += 10
        elif length_of_snake >= 10:
            snake_speed += 0.001

        clock.tick(snake_speed)
        # pygame.display.update()
        # time.sleep(1)

    print('Your score:', length_of_snake)
    print('Your level:', levels)
    pygame.quit()
    quit()


game_loop()
