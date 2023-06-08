import pygame as p
import sys, random, time

p.init()
WIDTH = 400
HEIGHT = 600
FPS = 50
clock = p.time.Clock()


class Stone(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = p.transform.scale(p.image.load("Stone.png"), (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.choice(["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])

    def update(self):
        if self.direction == "up":
            self.rect.y -= 2
        elif self.direction == "down":
            self.rect.y += 2
        elif self.direction == "left":
            self.rect.x -= 2
        elif self.direction == "right":
            self.rect.x += 2
        elif self.direction == "upright":
            self.rect.x += 2
            self.rect.y += 2
        elif self.direction == "upleft":
            self.rect.x -= 2
            self.rect.y += 2
        elif self.direction == "downright":
            self.rect.x += 2
            self.rect.y -= 2
        elif self.direction == "downleft":
            self.rect.x -= 2
            self.rect.y -= 2

        if self.rect.right < 17 or self.rect.left > WIDTH - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])
        if self.rect.bottom < 17 or self.rect.top > HEIGHT - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])


class Paper(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = p.transform.scale(p.image.load("Paper.png"), (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.choice(["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])

    def update(self):
        if self.direction == "up":
            self.rect.y -= 2
        elif self.direction == "down":
            self.rect.y += 2
        elif self.direction == "left":
            self.rect.x -= 2
        elif self.direction == "right":
            self.rect.x += 2
        elif self.direction == "upright":
            self.rect.x += 2
            self.rect.y += 2
        elif self.direction == "upleft":
            self.rect.x -= 2
            self.rect.y += 2
        elif self.direction == "downright":
            self.rect.x += 2
            self.rect.y -= 2
        elif self.direction == "downleft":
            self.rect.x -= 2
            self.rect.y -= 2

        if self.rect.right < 17 or self.rect.left > WIDTH - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])
        if self.rect.bottom < 17 or self.rect.top > HEIGHT - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])


class Scissors(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = p.transform.scale(p.image.load("Scissors.png"), (35, 35))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = random.choice(["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])

    def update(self):
        if self.direction == "up":
            self.rect.y -= 2
        elif self.direction == "down":
            self.rect.y += 2
        elif self.direction == "left":
            self.rect.x -= 2
        elif self.direction == "right":
            self.rect.x += 2
        elif self.direction == "upright":
            self.rect.x += 2
            self.rect.y += 2
        elif self.direction == "upleft":
            self.rect.x -= 2
            self.rect.y += 2
        elif self.direction == "downright":
            self.rect.x += 2
            self.rect.y -= 2
        elif self.direction == "downleft":
            self.rect.x -= 2
            self.rect.y -= 2

        if self.rect.right < 17 or self.rect.left > WIDTH - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])
        if self.rect.bottom < 17 or self.rect.top > HEIGHT - 17:
            self.direction = random.choice(
                ["up", "down", "left", "right", "upright", "upleft", "downright", "downleft"])


screen = p.display.set_mode((WIDTH, HEIGHT))
screen.fill(p.Color('grey'))

stone_group = p.sprite.Group()
paper_group = p.sprite.Group()
scissors_group = p.sprite.Group()
for i in range(7):
    stone = Stone(random.randint(100, 300), random.randint(50, 240))
    paper = Paper(random.randint(35, 165), random.randint(275, 565))
    scissors = Scissors(random.randint(235, 365), random.randint(275, 565))
    stone_group.add(stone)
    paper_group.add(paper)
    scissors_group.add(scissors)
while True:
    for event in p.event.get():
        if event.type == p.QUIT:
            p.quit()
            sys.exit()
    collisions = p.sprite.groupcollide(stone_group, paper_group, False, True)
    for stone, paper_list in collisions.items():
        for paper in paper_list:
            stone = paper
    collisions1 = p.sprite.groupcollide(paper_group, scissors_group, False, True)
    for paper, scissors_list in collisions1.items():
        for scissors in scissors_list:
            paper = scissors
    collisions2 = p.sprite.groupcollide(scissors_group, stone_group, False, True)
    for scissors, stone_list in collisions2.items():
        for stone in stone_list:
            scissors = stone
    stone_group.update()
    paper_group.update()
    scissors_group.update()
    screen.fill(p.Color('grey'))
    stone_group.draw(screen)
    paper_group.draw(screen)
    scissors_group.draw(screen)

    p.display.update()
    clock.tick(FPS)

    p.display.update()
    clock.tick(FPS)