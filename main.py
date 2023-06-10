import pygame
import time
import random


class Snakepart:
    def __init__(self, x, y, color, w, h, filename):
        self.x = x
        self.y = y
        self.color = color
        self.w = w
        self.h = h
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (20, 20))

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])

    # def imageload(self , filename):
        # self.image = pygame.image.load(filename)
        # self.image = pygame.transform.scale(self.image,(10 , 10))


class Apple:
    def __init__(self, a, b, c, d, filename):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.rect = pygame.Rect(self.a, self.b, self.c, self.d)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (30, 30))

    def render(self, screen):
        # pygame.draw.rect(screen, (0,0,255) , self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


class Badapple:
    def __init__(self, a, b, c, d, filename):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.rect = pygame.Rect(self.a, self.b, self.c, self.d)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (30, 30))

    def render(self, screen):
        # pygame.draw.rect(screen, (0,0,255) , self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


class Bit:
    def __init__(self, a, b, c, d, filename, speedx, speedy):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.speedx = speedx
        self.speedy = speedy
        self.rect = pygame.Rect(self.a, self.b, self.c, self.d)
        self.image = pygame.image.load(filename)
        self.image = pygame.transform.scale(self.image, (30 , 30))

    def render(self, screen):
        # pygame.draw.rect(screen, (0,0,255) , self.rect)
        screen.blit(self.image, [self.rect.x, self.rect.y])


pygame.init()
speed = 0
hp = 1
score = 0
global fri
lastChanges = time.time()
starttime = time.time()
starttime2 = time.time()
starttime3 = time.time()
timer = int(time.time() - starttime)
bacground = pygame.image.load("1670018457_8-kartinkin-net-p-fon-dlya-igri-zmeika-vkontakte-10.png")
bacground = pygame.transform.scale(bacground, (700, 700))
screen = pygame.display.set_mode((641, 641))
fps = pygame.time.Clock()
frlist = []
applist = []
badlist = []
bitlist = []
applist.append(Apple(100, 100, 20, 20, "pixelart2.png"))
badlist.append(Badapple(300, 300, 20, 20, "pixil-frame-0.png"))
frlist.append(Snakepart(200, 200, (0, 255, 0), 20, 20, "pixelart5.png"))
bitlist.append(Bit(250, 250, 20, 20, "pixil-frame-0 (17).png", 1, 1))
loseText = pygame.font.Font(None, 48).render("ти програв", True, (0, 0, 0))
scoreText = pygame.font.Font(None, 48).render("рахунок: " + str(score), True, (150, 150, 0))
scoreLose = pygame.font.Font(None, 48).render("рахунок: " + str(score), True, (0, 0, 0))
scoreno = pygame.font.Font(None, 48).render("рахунок нижче нуля", True, (0, 0, 0))
LegendText = pygame.font.Font(None, 48).render("", True, (255, 0, 0))
# frlist[len(frlist)-1].imageload("pixelart6.png")
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                if speed != 2:
                    speed = 1

            if event.key == pygame.K_d:
                if speed != 1:
                    speed = 2

            if event.key == pygame.K_w:
                if speed != 4:
                    speed = 3

            if event.key == pygame.K_s:
                if speed != 3:
                    speed = 4

            if event.key == pygame.K_LEFT:
                if speed != 2:
                    speed = 1

            if event.key == pygame.K_RIGHT:
                if speed != 1:
                    speed = 2

            if event.key == pygame.K_UP:
                if speed != 4:
                    speed = 3

            if event.key == pygame.K_DOWN:
                if speed != 3:
                    speed = 4

    if time.time() - starttime > 0.2:
        starttime = time.time()
        if speed == 1:
            frlist.append(Snakepart(frlist[len(frlist) - 1].x - 20, frlist[len(frlist) - 1].y, (0, 255, 0), 20, 20,
                                    "pixelart5.png"))
            frlist.pop(0)
            # frlist[len(frlist)-1].imageload("pixelart6.png")

        if speed == 2:
            frlist.append(Snakepart(frlist[len(frlist) - 1].x + 20, frlist[len(frlist) - 1].y, (0, 255, 0), 20, 20,
                                    "pixelart5.png"))
            frlist.pop(0)
            # frlist[len(frlist)-1].imageload("pixelart6.png")

        if speed == 3:
            frlist.append(Snakepart(frlist[len(frlist) - 1].x, frlist[len(frlist) - 1].y - 20, (0, 255, 0), 20, 20,
                                    "pixelart5.png"))
            frlist.pop(0)
            # frlist[len(frlist)-1].imageload("pixelart6.png")

        if speed == 4:
            frlist.append(Snakepart(frlist[len(frlist) - 1].x, frlist[len(frlist) - 1].y + 20, (0, 255, 0), 20, 20,
                                    "pixelart5.png"))
            frlist.pop(0)
            # frlist[len(frlist)-1].imageload("pixelart6.png")

    if score < 0:
        screen.fill((255, 0, 0))
        bacground2 = pygame.image.load("pixelart 8.png")
        bacground2 = pygame.transform.scale(bacground2, (2500, 3000))
        screen.blit(bacground2, [0, 0])
        screen.blit(loseText, [100, 100])
        screen.blit(scoreno, [200, 200])
        pygame.display.flip()
        time.sleep(1000)

    if score > 49:
        LegendText = pygame.font.Font(None, 48).render("ВИ ЛЕГЕНДА !!!", True, (255, 0, 0))

    if hp < 1:
        screen.fill((255, 0, 0))
        bacground2 = pygame.image.load("pixelart 8.png")
        bacground2 = pygame.transform.scale(bacground2, (700, 700))
        screen.blit(bacground2, [0, 0])
        screen.blit(loseText, [100, 100])
        screen.blit(scoreLose, [200, 200])
        pygame.display.flip()
        time.sleep(3000)


    if bitlist[0].rect.x > 300:
        bitlist[0].speedx = -(bitlist[0].speedx)

    if bitlist[0].rect.y > 300:
        bitlist[0].speedx = -(bitlist[0].speedx)

    if bitlist[0].rect.x < 50:
        bitlist[0].speedx = -(bitlist[0].speedx)

    if bitlist[0].rect.y < 50:
        bitlist[0].speedy = -(bitlist[0].speedy)

    if frlist[len(frlist) - 1].rect.colliderect(applist[0].rect):
        applist.append(Apple(random.randint(100, 300), random.randint(100, 300), 20, 20, "pixelart2.png"))
        frlist.append(
            Snakepart(frlist[len(frlist) - 1].x, frlist[len(frlist) - 1].y + 10, (0, 255, 0), 20, 20, "pixelart5.png"))
        badlist.append(
            Badapple(random.randint(100, 400) - 100, random.randint(100, 400) - 100, 20, 20, "pixil-frame-0.png"))
        applist.pop(0)
        badlist.pop(0)
        score += 1

    if frlist[len(frlist) - 1].rect.colliderect(badlist[0].rect):
        badlist.append(
            Badapple(random.randint(100, 400) - 100, random.randint(100, 400) - 100, 20, 20, "pixil-frame-0.png"))
        applist.append(Apple(random.randint(100, 300), random.randint(100, 300), 20, 20, "pixelart2.png"))
        frlist.pop(0)
        badlist.pop(0)
        applist.pop(0)
        score -= 3

    if frlist[len(frlist) - 1].rect.colliderect(bitlist[0].rect):
        applist.append(Apple(random.randint(100, 300), random.randint(100, 300), 20, 20, "pixelart2.png"))
        bitlist.append(Bit(random.randint(100, 300), random.randint(100, 300), 20, 20, "pixil-frame-0 (17).png", 1, 1))
        badlist.append(
            Badapple(random.randint(100, 400) - 100, random.randint(100, 400) - 100, 20, 20, "pixil-frame-0.png"))
        frlist.append(
            Snakepart(frlist[len(frlist) - 1].x, frlist[len(frlist) - 1].y + 10, (0, 255, 0), 20, 20, "pixelart5.png"))
        bitlist.pop(0)
        applist.pop(0)
        badlist.pop(0)
        score += 2

    if frlist[0].x < 1 or frlist[0].y < 1 or frlist[0].x > 630 or frlist[0].y > 620 or frlist[len(frlist) - 1].x < 2 or frlist[len(frlist) - 1].y < 2 or frlist[len(frlist) - 1].x > 630 or frlist[len(frlist) - 1].y > 620:
        hp -= 1

    for fri in range(len(frlist) - 3):

        if frlist[len(frlist) - 1].rect.colliderect(frlist[fri].rect):
            hp -= 1

    scoreText = pygame.font.Font(None, 48).render("рахунок: " + str(score), True, (150, 150, 0))
    scoreLose = pygame.font.Font(None, 48).render("рахунок: " + str(score), True, (0, 0, 0))

    if time.time() - starttime2 > 1:
        starttime2 = time.time()
        bitlist[0].speedx = random.randint(-3, 3)
        bitlist[0].speedy = random.randint(-3, 3)

    bitlist[0].rect.x += bitlist[0].speedx
    bitlist[0].rect.y += bitlist[0].speedy

    if time.time() - starttime3 > 10:
        starttime3 = time.time()
        bitlist[0].rect.x = random.randint(100, 300)
        bitlist[0].rect.y = random.randint(100, 300)

    screen.fill((0, 255, 0))
    screen.blit(bacground, [0, 0])
    for i in range(len(frlist)):
        frlist[i].render(screen)

    applist[0].render(screen)
    badlist[0].render(screen)
    bitlist[0].render(screen)
    screen.blit(scoreText, [320, 10])
    screen.blit(LegendText, [50, 10])

    pygame.display.flip()
    fps.tick(60)
