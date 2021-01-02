import pygame, sys, os, random, math

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.mixer.init()

base_path = os.path.join(os.getcwd(), os.path.dirname(__file__))
sprites_path = os.path.join(base_path, "assets/sprites/")
audio_path = os.path.join(base_path, "assets/audio/")
music_path = os.path.join(audio_path, "music/")
sfx_path = os.path.join(audio_path, "sfx/")

def load_sprite(sprite):
  path = sprites_path + sprite + ".png"
  return pygame.image.load(path).convert()

def load_sound(folder_index, sound):
  path = sfx_path + folder_names[folder_index] + "/" + sound + ".wav"
  return pygame.mixer.Sound(path)

def load_music(folder_index, music):
  path = music_path + folder_names[folder_index] + "/" + music + ".wav"
  return pygame.mixer.Sound(path)

tile_size = 16

muted = False
muted1 = False
muted2 = False
muted3 = False
muted4 = False

colorkey = (255, 0, 255)
screen_scale = 2
screen_size = (256, 224)
screen_size_scaled = (screen_size[0]*screen_scale, screen_size[1]*screen_scale)
screen_color = (0, 0, 0)

icon = pygame.Surface((16, 16))
icon.fill(colorkey)
icon.set_colorkey(colorkey)
pygame.display.set_caption("Proto Man")

screen = pygame.display.set_mode(screen_size_scaled)
screen_surface = pygame.Surface(screen_size)
screen_rect = screen_surface.get_rect()

icon.convert()
pygame.display.set_icon(icon)

folder_names = [
    'SQUARE1',
    'SQUARE2',
    'TRIANGLE',
    'NOISE',
]

select1 = load_music(0, 'select_new')
select2 = load_music(1, 'select_new')
select3 = load_music(2, 'select_new')
select4 = load_music(3, 'select_new')

boss_intro1 = load_music(0, 'boss_intro')
boss_intro2 = load_music(1, 'boss_intro')
boss_intro3 = load_music(2, 'boss_intro')
boss_intro4 = load_music(3, 'boss_intro')

boss_battle_intro1 = load_music(0, 'boss_battle_intro')
boss_battle_intro2 = load_music(1, 'boss_battle_intro')
boss_battle_intro3 = load_music(2, 'boss_battle_intro')
boss_battle_intro4 = load_music(3, 'boss_battle_intro')

boss_battle1 = load_music(0, 'boss_battle')
boss_battle2 = load_music(1, 'boss_battle')
boss_battle3 = load_music(2, 'boss_battle')
boss_battle4 = load_music(3, 'boss_battle')

fireman_intro1 = load_music(0, 'fireman_intro')
fireman_intro2 = load_music(1, 'fireman_intro')
fireman_intro3 = load_music(2, 'fireman_intro')
fireman_intro4 = load_music(3, 'fireman_intro')

fireman1 = load_music(0, 'fireman')
fireman2 = load_music(1, 'fireman')
fireman3 = load_music(2, 'fireman')
fireman4 = load_music(3, 'fireman')

proto = load_music(0, 'proto')

bugtest1 = load_music(0, 'bugtest')
bugtest2 = load_music(1, 'bugtest')
bugtest3 = load_music(2, 'bugtest')
bugtest4 = load_music(3, 'bugtest')

square1 = pygame.mixer.Channel(0)
square1_END = pygame.USEREVENT + 1
square1.set_endevent(square1_END)
square2 = pygame.mixer.Channel(1)
square2_END = pygame.USEREVENT + 2
square2.set_endevent(square2_END)
triangle = pygame.mixer.Channel(2)
triangle_END = pygame.USEREVENT + 3
triangle.set_endevent(triangle_END)
noise = pygame.mixer.Channel(3)
noise_END = pygame.USEREVENT + 4
noise.set_endevent(noise_END)
sfx1 = pygame.mixer.Channel(4)
sfx1_END = pygame.USEREVENT + 5
sfx1.set_endevent(sfx1_END)
sfx2 = pygame.mixer.Channel(5)
sfx2_END = pygame.USEREVENT + 6
sfx2.set_endevent(sfx2_END)
sfx3 = pygame.mixer.Channel(6)
sfx3_END = pygame.USEREVENT + 7
sfx3.set_endevent(sfx3_END)
sfx4 = pygame.mixer.Channel(7)
sfx4_END = pygame.USEREVENT + 8
sfx4.set_endevent(sfx4_END)

sfx_select = load_sound(1, 'select')
sfx_confirm1 = load_sound(0, 'confirm')
sfx_confirm2 = load_sound(1, 'confirm')
sfx_entrance = load_sound(1, 'entrance')
sfx_land2 = load_sound(1, 'land')
sfx_land4 = load_sound(3, 'land')
sfx_shot = load_sound(1, 'shot')
sfx_hit3 = load_sound(2, 'hit')
sfx_hit4 = load_sound(3, 'hit')
sfx_hurt2 = load_sound(1, 'hurt')
sfx_hurt4 = load_sound(3, 'hurt')
sfx_death1 = load_sound(0, 'death')
sfx_death2 = load_sound(1, 'death')
sfx_lightning_ball = load_sound(3, 'lightning_ball')
sfx_deflect = load_sound(1, 'deflect')
sfx_enemy_shot = load_sound(1, 'enemy_shot')
sfx_health1 = load_sound(0, 'health')
sfx_health2 = load_sound(1, 'health')
sfx_life = load_sound(1, 'life')
sfx_fall = load_sound(1, 'fall')
sfx_explosion2 = load_sound(1, 'explosion')
sfx_explosion4 = load_sound(3, 'explosion')
sfx_menu = load_sound(1, 'menu')
sfx_charge = load_sound(1, 'charge')
sfx_charge_full = load_sound(1, 'charge_full')
sfx_charge_shot = load_sound(3, 'charge_shot')
sfx_charge_shot_mid = load_sound(3, 'charge_shot_mid')

square1.play(select1, -1)
square2.play(select2, -1)
triangle.play(select3, -1)
noise.play(select4, -1)

sprites_map = {
    "portrait":load_sprite("portrait"),
    "chars":load_sprite("chars"),
    "background":load_sprite("background"),
    "intro":load_sprite("boss_intro"),
    "zeus":load_sprite("zeus"),
    "proto":load_sprite("proto"),
    "tile":load_sprite("tiles"),
    "life":load_sprite("life"),
    "met":load_sprite("met"),
    "effects":load_sprite("effects"),
    "helikoppa":load_sprite("helikoppa"),
    "explosion":load_sprite("explosion"),
    "menu":load_sprite("menu"),
}

charsCoords = {}
charsOrder = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!?.,c:;\'" '
x = 0
y = 0
charsWidth = 80
charsHeight= 80
for index in range(len(charsOrder)):
    if x > charsWidth/8-1:
        x = 0
        y += 1
    c = charsOrder[index]
    charsCoords[c] = {}
    charsCoords[c]['x'] = x
    charsCoords[c]['y'] = y
    x += 1

class Rectangle(object):
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
    def intersect(a, b):
        return a.left < b.right and a.right > b.left and a.top < b.bottom and a.bottom > b.top
screen_rect = Rectangle(0, 0, screen_size[0], screen_size[1])

sprites = []
updates = []
rectangles = []
portraits = []
tiles = []
class Star(object):
    def __init__(self, x=random.randint(0, screen_size[0]), y=screen_size[1], t=2):
        if t == 2:
            width = 4
            height = 4
            subX = 0
            subY = 8
            speed = 3
        elif t == 1:
            width = 2
            height = 2
            subX = 4
            subY = 8
            speed = 0.75
        elif t == 0:
            width = 1
            height = 1
            subX = 6
            subY = 8
            speed = 0.1
        self.sprite = Sprite(x, y, width, height, 0, "intro", subX, subY, width, height)
        self.sprite.update = self.update
        self.sprite.speed = speed
    def update(self):
        self.sprite.x -= self.sprite.speed
        self.sprite.y -= self.sprite.speed
        if self.sprite.x < -self.sprite.width:
            self.sprite.x = screen_size[0]
        if self.sprite.y < -self.sprite.height:
            self.sprite.y = screen_size[1]
class BossIntroPreview(object):
    def __init__(self):
        self.sprite = Sprite(103, 128-50, 48, 48, 2, "zeus")
        self.sprite.update = self.update
        self.sprite.gravity = 0.4
        self.sprite.velocityX = 1
        self.sprite.velocityY = -12
        self.sprite.grounded = False
        self.sprite.landing = False
        self.sprite.indexX = 0
        self.sprite.frames = [0, 1, 2, 3]
        self.sprite.limits = [30, 7, 5, -1]
        self.sprite.frame_index = 0
        self.sprite.timer = 0
        self.sprite.fade_limit = 10
        self.sprite.fading = False
        self.sprite.fade_index = 4
        self.sprite.idle = True
        self.sprite.idle_limit = 120
    def update(self):
        if self.sprite.idle:
            self.sprite.timer += 1
            if self.sprite.timer >= self.sprite.idle_limit:
                self.sprite.timer = 0
                self.sprite.idle = False
                self.sprite.fading = True
        elif self.sprite.fading:
            self.sprite.timer += 1
            if self.sprite.timer >= self.sprite.fade_limit:
                self.sprite.timer = 0
                self.sprite.fade_index -= 1
                if self.sprite.fade_index < 0:
                    self.sprite.fade_index = 0
                    self.sprite.fading = False
        else:
            if self.sprite.frame_index < len(self.sprite.frames)-1:
                self.sprite.timer += 1
                if self.sprite.timer >= self.sprite.limits[self.sprite.frame_index]:
                    self.sprite.timer = 0
                    self.sprite.frame_index += 1
            self.sprite.indexX = self.sprite.frames[self.sprite.frame_index]
            self.sprite.subX = self.sprite.indexX*self.sprite.width
class BossIntro(object):
    def __init__(self):
        self.part_width = 32
        self.part_height = 8
        self.parts_top = []
        self.parts_bottom = []
        self.parts_placed = int(screen_size[0]/self.part_width)
        self.fading = True
        self.timer = 0
        self.fade_limit = 5
        self.star_timer = 0
        self.star_limit = 30
        self.star_index = 0
        self.star_fade_index = 4
        self.stars = []
        self.star_positions = [
            (64, 32, 2),
            (192, 80, 2),
            (128, 128, 2),
            (32, 176, 2),
            (224, 224, 2),

            (50, 150, 1),
            (100, 200, 1),
            (150, 100, 1),
            (200, 50, 1),
            (25, 25, 1),
            (175, 225, 1),
            (125, 175, 1),
            (75, 125, 1),
            (225, 75, 1),

            (32, 224, 0),
            (64, 32, 0),
            (96, 182, 0),
            (128, 112, 0),
            (160, 56, 0),
            (192, 100, 0),
            (224, 200, 0),

            (48, 150, 0),
            (80, 224, 0),
            (112, 0, 0),
            (144, 132, 0),
            (176, 96, 0),
            (208, 188, 0),
            (16, 48, 0),
        ]
        for pos in self.star_positions:
            star = Star(pos[0], pos[1], pos[2]).sprite
            star.fade_index = self.star_fade_index
            star.parent = self
            self.stars.append(star)
        self.light_top = 0
        self.light_bottom = 2
        self.light_limit = 10
        self.name_timer = 0
        self.name_limit = 210
        self.end_timer = 0
        self.end_limit = 420
        self.ended = False
        self.naming = True
        self.exceeded = False
        self.boss_text = 'ZEUS'
        self.bg_rect = Sprite_Rect(0, screen_size[1]/2+1, screen_size[0], 1, 1, (110, 0, 64))
        self.preview = BossIntroPreview().sprite
        for p in range(self.parts_placed):
            pt = Sprite(p*self.part_width, screen_size[1]/2-self.part_height, self.part_width, self.part_height, 3, "intro")
            pb = Sprite(p*self.part_width, screen_size[1]/2, self.part_width, self.part_height, 3, "intro")
            pt.direction = -1
            pt.limit = pt.y+32*pt.direction
            pb.direction = 1
            pb.limit = pb.y+32*pb.direction
            pt.speed = 2
            pb.speed = 2
            pt.fade_index = 4
            pb.fade_index = 4
            self.parts_top.append(pt)
            self.parts_bottom.append(pb)
        updates.append(self)
    def remove(self):
        self.bg_rect.remove()
        for star in self.stars:
            star.remove()
        self.preview.remove()
        for part in self.parts_top:
            part.remove()
        for part in self.parts_bottom:
            part.remove()
        self.name.remove()
        updates.remove(self)
    def update(self):
        global introducing
        if not self.ended:
            self.end_timer += 1
            if self.end_timer >= self.end_limit:
                self.end_timer = 0
                self.ended = True
                introducing = False
                fade()
            if self.naming:
                self.name_timer += 1
                if self.name_timer >= self.name_limit:
                    self.name_timer = 0
                    self.naming = False
                    self.name = ScreenText(128-len(self.boss_text)*4, 128, self.boss_text, 1, 3)
            if self.star_fade_index > 0:
                self.star_timer += 1
                if self.star_timer >= self.star_limit:
                    self.star_timer = 0
                    self.star_fade_index -= 1
                    for star in self.stars:
                        star.fade_index = self.star_fade_index
            if self.fading:
                self.timer += 1
                if self.timer >= self.fade_limit:
                    self.timer = 0
                    for part in self.parts_top:
                        if part.fade_index > 0:
                            part.fade_index -= 1
                        else:
                            self.fading = False
                    for part in self.parts_bottom:
                        if part.fade_index > 0:
                            part.fade_index -= 1
            else:
                for part in self.parts_top:
                    part.y += -part.speed
                    if part.y < part.limit:
                        part.y = part.limit
                        self.exceeded = True
                for part in self.parts_bottom:
                    part.y += part.speed
                    if part.y > part.limit:
                        part.y = part.limit
                self.bg_rect.y = self.parts_top[0].y+self.part_height+1
                self.bg_rect.width = int(screen_size[0])
                self.bg_rect.height = int(self.parts_bottom[0].y-self.bg_rect.y-1)
            if self.exceeded:
                self.timer += 1
                if self.timer >= self.light_limit:
                    self.timer = 0
                    self.light_top += 1
                    if self.light_top > 2:
                        self.light_top = 0
                    self.light_bottom -= 1
                    if self.light_bottom < 0:
                        self.light_bottom = 2
                    for i in range(len(self.parts_top)):
                        part = self.parts_top[i]
                        if i % 3 == self.light_top:
                            part.subX = self.part_width
                        else:
                            part.subX = 0
                    for i in range(len(self.parts_bottom)):
                        part = self.parts_bottom[i]
                        if i % 3 == self.light_bottom:
                            part.subX = self.part_width
                        else:
                            part.subX = 0
class Sprite_Rect(object):
    def __init__(self, x, y, width, height, depth, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.depth = depth
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)
        self.visible = True
        self.fade_index = 0
        self.type = 'rectangle'
        sprites.append(self)
        rectangles.append(self)
        updates.append(self)
    def remove(self):
        updates.remove(self)
        try:
            sprites.remove(self)
        except ValueError:
            print("Glitch averted.")
        rectangles.remove(self)
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.width = self.width
        self.rect.height = self.height
class Sprite(object):
    def __init__(self, x, y, width, height, depth, path, subX=0, subY=0, subWidth=0, subHeight=0):
        if subWidth == 0:
            subWidth = width
        if subHeight == 0:
            subHeight = height
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.subX = subX
        self.subY = subY
        self.subWidth = subWidth
        self.subHeight = subHeight
        self.on_level = False
        self.flip_x = False
        self.flip_y = False
        self.depth = depth
        self.path = path
        self.indexX = self.subX/self.subWidth
        self.indexY = self.subY/self.subHeight
        self.surface = sprites_map[self.path].subsurface(subX, subY, subWidth, subHeight).convert()
        self.rect = self.surface.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.visible = True
        self.color_list = []
        self.fade_index = 0
        self.type = 'surface'
        sprites.append(self)
        updates.append(self)
    def updateSprite(self, indexX, indexY):
        self.indexX = indexX
        self.indexY = indexY
        self.surface = sprites_map[self.path].subsurface(self.indexX*self.width, self.indexY*self.height, self.width, self.height)
    def update(self):
        print
    def remove(self):
        try:
            sprites.remove(self)
            updates.remove(self)
        except ValueError:
            print("Glitch averted.")
class ScreenText(object):
    def __init__(self, x, y, string, style=0, timer=0):
        self.x = x
        self.y = y
        self.string = string
        self.style = style
        self.timer = 0
        self.limit = timer
        self.chars = []
        self.char_index = 0
        self.visible = True
        if timer > 0:
            updates.append(self)
        else:
            self.draw()
    def phase(self, visibility=None):
        if visibility == None:
            visibility = not self.visible
        self.visible = visibility
        for char in self.chars:
            char.visible = visibility
    def erase(self):
        for char in self.chars:
            char.remove()
        self.chars = []
    def draw(self):
        i = 0
        for char in self.string:
            indexY = charsCoords[char]['y']+self.style*5
            c = Sprite(self.x+8*i, self.y, 8, 8, 10, "chars", charsCoords[char]['x']*8, indexY*8, 8, 8)
            c.on_level = True
            c.offset_x = c.x
            c.offset_y = c.y
            self.chars.append(c)
            i += 1
    def redraw(self, string):
        self.erase()
        self.x = 0
        self.y = 0
        self.string = string
        self.draw()
    def move(self, x, y):
        self.x = x
        self.y = y
        for char in self.chars:
            char.x = self.x + char.offset_x
            char.y = self.y + char.offset_y
    def remove(self):
        for char in self.chars:
            char.remove()
        if self.limit > 0:
            updates.remove(self)
    def update(self):
        if self.char_index < len(self.string):
            self.timer += 1
            if self.timer >= self.limit:
                self.timer = 0
                char = self.string[self.char_index]
                indexY = charsCoords[char]['y']+self.style*5
                self.chars.append(Sprite(self.x+8*self.char_index, self.y, 8, 8, 1, "chars", charsCoords[char]['x']*8, indexY*8, 8, 8))
                self.char_index += 1
class Portrait(object):
    def __init__(self, index, selected):
        if selected == None:
            sele
        index_y = 0
        if index <= 1:
            index_x = index+0.5
            index_y = 0
        elif index <= 4:
            index_x = index-2
            index_y = 1
        elif index <= 6:
            index_x = index-4.5
            index_y = 2
        x = index_x*80+24
        y = index_y*64+16
        self.sprite = Sprite(x, y, 48, 48, 2, "portrait")
        self.sprite.selected = selected
        if index == 0:
            self.sprite.index_face = 0
        elif index == 2:
            self.sprite.index_face = 1
        elif index == 3:
            self.sprite.index_face = 2
        elif index == 4:
            self.sprite.index_face = 3
        else:
            self.sprite.index_face = 4
        self.sprite.timer = 0
        self.sprite.limit = 10
        self.sprite.surface_face = Sprite(x+8, y, 32, 40, 3, "portrait", self.sprite.index_face*32, 48, 32, 40)
        self.sprite.surface_face.index = self.sprite.index_face
        portraits.append(self.sprite)
        self.sprite.update = self.update
    def update(self):
        if self.sprite.selected:
            self.sprite.timer += 1
            if self.sprite.timer > self.sprite.limit:
                self.sprite.timer = 0
                self.sprite.subX += self.sprite.width
                if self.sprite.subX > self.sprite.width:
                    self.sprite.subX = 0
        else:
            if self.sprite.subX != 0 or self.sprite.timer != 0:
                self.sprite.subX = 0
                self.sprite.timer = 0

class Shot(object):
    def __init__(self, x, y, parent, angle, damage, piercing, shot_type, enemies, size='small'):
        speed = parent.shot_speed
        if shot_type == 'proto':
            subX = 0
            width = 8
            height = 8
            frames = 1
            if size == 'mid':
                subX = 8
                width = 12
                height = 12
                y -= 2
                frames = 2
                if angle < 0:
                    x -= width
            if size == 'large':
                subX = 32
                width = 29
                height = 10
                y -= 1
                frames = 3
                speed += 2
                if angle < 0:
                    x -= width
            subY = 32
        elif shot_type == 'met':
            subX = 0
            subY = 24
            width = 8
            height = 8
            frames = 1
        self.sprite = Sprite(x, y, width, height, 3, shot_type, subX, subY, width, height)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.start_subX = subX
        self.parent = parent
        self.timer = 0
        self.limit = 2
        self.index = 0
        self.frames = frames
        self.size = size
        self.speed = speed
        self.angle = angle
        self.radians = (self.angle-90)*math.pi/180
        self.shot_type = shot_type
        self.velocity_x = math.cos(self.radians)*self.speed
        self.velocity_y = math.sin(self.radians)*self.speed
        if self.velocity_x < 0:
            self.direction = -1
        elif self.velocity_x > 0:
            self.direction = 1
        else:
            self.direction = parent.facing
        self.enemies = enemies
        self.damage = damage
        self.piercing = piercing
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height
        )
        self.deflecting = False
        self.deflect_speed = 4
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height
        )
    def remove(self):
        if self.size == 'large':
            self.parent.shots_fired -= 2
        self.parent.shots_fired -= 1
        self.sprite.remove()
    def deflect(self):
        if not sfx2.get_sound() == sfx_life:
            sfx2.play(sfx_deflect)
        self.deflecting = True
        self.velocity_x = self.deflect_speed*-self.direction
        self.velocity_y = -self.deflect_speed
    def update(self):
        if not game == None:
            if not game.paused:
                self.timer += 1
                if self.timer >= self.limit:
                    self.timer = 0
                    self.index += 1
                    if self.index+1 > self.frames:
                        self.index = 0
                        if self.size == 'large':
                            self.index = 1
                    self.sprite.subX = self.start_subX+self.index*self.sprite.width
                self.sprite.x += self.velocity_x
                self.sprite.y += self.velocity_y
                self.update_rect()
                if not self.rect.intersect(game.rect):
                    self.remove()
                if not self.deflecting:
                    for enemy in self.enemies:
                        if not self.shot_type == 'proto':
                            if not game.player == None:
                                if not game.player.shield_rect == None:
                                    if not self.direction == game.player.facing:
                                        if self.rect.intersect(game.player.shield_rect):
                                            self.deflect()
                                            return
                        if not enemy.invincible and not enemy.dead:
                            if self.rect.intersect(enemy.rect):
                                if not enemy.shielded:
                                    if self.shot_type == 'proto':
                                        sfx3.play(sfx_hit3)
                                        sfx4.play(sfx_hit4)
                                    else:
                                        if not sfx2.get_sound() == sfx_life:
                                            sfx2.play(sfx_hurt2)
                                        sfx4.play(sfx_hurt4)
                                    enemy.hit(self.damage, self.direction)
                                    if not self.piercing:
                                        if self.size == 'large' and enemy.health > 0 or not self.size == 'large':
                                            self.remove()
                                    break
                                else:
                                    self.deflect()
                self.sprite.flip_x = self.direction == -1
class Tile(object):
    def __init__(self, x, y, subX, subY, tileX, tileY, roomX, roomY, solid=False, through=False, ladder=False):
        global tiles
        self.offset_x = x
        self.sprite = Sprite(x, y, tile_size, tile_size, 1, "tile", subX*tile_size, subY*tile_size, tile_size, tile_size)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.tile_x = subX
        self.tile_y = subY
        self.rect = Rectangle(x, y, x+tile_size, y+tile_size)
        self.solid = solid
        self.through = through
        self.ladder = ladder
        self.child = None
        self.child_type = None
        self.created = False
        self.room_x = int(roomX)
        self.room_y = int(roomY)
        self.tile_x = int(tileX)
        self.tile_y = int(tileY)
        tiles.append(self)
        self.create()
    def create(self):
        if self.child == None:
            room_index = int(game.map[self.room_y][self.room_x])
            room = game.rooms[room_index]
            room_rel_x = int(self.tile_x%(screen_size[0]/tile_size))
            room_rel_y = int(self.tile_y%(screen_size[1]/tile_size))
            char = room[room_rel_y][room_rel_x]
            if char == 'm':
                self.child = Met((self.sprite.x, self.sprite.y))
                self.child_type = 'enemy'
            if char == 'h':
                self.child = Helikoppa((self.sprite.x, self.sprite.y))
                self.child_type = 'enemy'
            if not self.created:
                if char == 'V':
                    self.child = Pickup((self.sprite.x, self.sprite.y), False, 'life')
                    self.created = True
                    self.child_type = 'pickup'
                if char == 'O':
                    self.child = Pickup((self.sprite.x, self.sprite.y), False, 'health_big')
                    self.created = True
                    self.child_type = 'pickup'
            if not self.child == None:
                if self.child_type == 'enemy':
                    game.enemies.append(self.child)
                if self.child_type == 'pickup':
                    game.pickups.append(self.child)
    def transfer(self, direction):
        moves_x = int((screen_size[0]/tile_size+1)*direction)
        self.tile_x += moves_x
        if self.tile_x > len(game.map[0])*screen_size[0]/tile_size-1:
            return
        new_world_x = self.tile_x*tile_size
        self.room_x = math.floor(new_world_x/screen_size[0])
        new_room_index = int(game.map[self.room_y][self.room_x])
        new_room = game.rooms[new_room_index]
        new_room_rel_x = int(self.tile_x%(screen_size[0]/tile_size))
        try:
            char = new_room[self.tile_y][new_room_rel_x]
        except IndexError:
            char = ' '
        self.sprite.x = new_world_x
        self.create()
        self.sprite.subX = game.parser[char]['index']*tile_size
        self.solid = game.parser[char]['solid']
        self.through = game.parser[char]['through']
        self.ladder = game.parser[char]['ladder']
        self.update_rect()
    def update_rect(self):
        x = self.sprite.x
        y = self.sprite.y
        self.rect = Rectangle(
            x,
            y,
            x+tile_size,
            y+tile_size
        )
    def update(self):
        if not self.child == None:
            if not self.child.sprite in updates:
                self.child = None
                self.child_type = None
        if not game == None:
            if not game.paused:
                if not self.rect.intersect(game.rect):
                    if self.sprite.x+self.sprite.width/2 < game.rect.left:
                        self.transfer(1)
                    elif self.sprite.x+self.sprite.width/2 > game.rect.right:
                        self.transfer(-1)
class HUDBar(object):
    def __init__(self, x, y, ticks, ticks_max, index):
        self.sprite = Sprite(x, y, 8, 56, 8, 'life')
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.offset_x = x
        self.ticks = ticks
        self.ticks_max = ticks_max
        self.ticks_list = []
        self.index = index
        self.update_ticks(self.ticks)
    def update_ticks(self, ticks):
        if ticks > self.ticks_max:
            ticks = self.ticks_max
        self.ticks = ticks
        for tick in self.ticks_list:
            tick.remove()
        self.ticks_list = []
        for i in range(ticks):
            x = self.sprite.x
            y = self.sprite.y+self.sprite.height-2*(i+1)
            tick = Sprite(x, y, 8, 52, 8, 'life', 8, self.index, 8, 1)
            tick.on_level = True
            self.ticks_list.append(tick)
    def remove(self):
        for tick in self.ticks_list:
            tick.remove()
        self.sprite.remove()
    def update(self):
        if not game == None:
            if not game.paused:
                self.update_ticks(self.ticks)
class Smoke(object):
    def __init__(self, pos, direction, smoke_type):
        x, y = pos
        if smoke_type == 'hurt':
            subY = 24
        if smoke_type == 'slide':
            subY = 32
        self.sprite = Sprite(x, y, 8, 8, 4, 'effects', 0, subY, 8, 8)
        if smoke_type == 'slide':
            if direction == -1:
                self.sprite.flip_x = True
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.timer = 0
        self.limit = 8
        self.index = 0
        self.indexes = 3
    def update(self):
        if not game == None:
            if not game.paused:
                self.timer += 1
                if self.timer >= self.limit:
                    self.sprite.y -= 1
                    self.timer = 0
                    self.index += 1
                    if self.index >= self.indexes:
                        self.sprite.remove()
                self.sprite.subX = self.index*8
class HurtEffect(object):
    def __init__(self, parent):
        x = parent.center['x']-12
        y = parent.center['y']-12
        self.sprite = Sprite(x, y, 24, 24, 7, 'effects', 0, 0, 24, 24)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.parent = parent
        self.sprite.visible = not self.parent.sprite.visible
    def update(self):
        if not game == None:
            if not game.paused:
                self.sprite.x = self.parent.center['x']-12
                self.sprite.y = self.parent.center['y']-12
                self.sprite.visible = not self.parent.sprite.visible
                if not self.parent.hurt:
                    self.sprite.remove()
class SmallExplosion(object):
    def __init__(self, pos, start_frame=0, limit=3, depth=7):
        x = pos[0]-12
        y = pos[1]-12
        self.sprite = Sprite(x, y, 24, 24, depth, 'effects', 24, 0, 24, 24)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.timer = 0
        self.limit = limit
        self.index = start_frame
        self.indexes = 4
    def update(self):
        if not game == None:
            if not game.paused:
                self.timer += 1
                if self.timer >= self.limit:
                    self.timer = 0
                    self.index += 1
                    if self.index >= self.indexes:
                        self.sprite.remove()
                self.sprite.subY = self.index*self.sprite.height
class Explosion(object):
    def __init__(self, pos):
        x = pos[0]-32
        y = pos[1]-32
        self.sprite = Sprite(x, y, 64, 64, 7, 'explosion', 0, 0, 64, 64)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.timer = 0
        self.limit = 2
        self.index = 0
        self.indexes = sprites_map[self.sprite.path].get_rect().width/self.sprite.subWidth
        self.rect_offset_x1 = 20
        self.rect_offset_x2 = 44
        self.rect_offset_y1 = 20
        self.rect_offset_y2 = 44
        self.rect_width = self.rect_offset_x2-self.rect_offset_x1
        self.rect_height = self.rect_offset_y2-self.rect_offset_y1
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.center = {
            'x':self.rect.left+self.rect_width/2,
            'y':self.rect.top+self.rect_height/2
        }
        self.damage = 4
        sfx2.play(sfx_explosion2)
        sfx4.play(sfx_explosion4)
    def update(self):
        if not game == None:
            if not game.paused:
                if self.index < self.indexes-4:
                    if not game == None:
                        if not game.player == None:
                            if self.rect.intersect(game.player.rect):
                                direction = 1
                                if game.player.rect.right < self.rect.right:
                                    direction = -1
                                elif game.player.rect.left > self.rect.left:
                                    direction = 1
                                game.player.hit(self.damage, direction)
                self.timer += 1
                if self.timer >= self.limit:
                    self.timer = 0
                    self.index += 1
                    if self.index >= self.indexes:
                        self.sprite.remove()
                self.sprite.subX = self.index*self.sprite.width
class OrbExplosion(object):
    def __init__(self, pos):
        x = pos[0]-12
        y = pos[1]-12
        i = 0
        while i < 8:
            angle = 45*i
            Orb((x, y), angle, 1)
            Orb((x, y), angle, 2)
            i += 1
class Orb(object):
    def __init__(self, pos, angle, speed):
        x = pos[0]
        y = pos[1]
        self.speed = speed
        self.angle = angle
        self.radians = angle*math.pi/180
        self.sprite = Sprite(x, y, 24, 24, 7, 'effects', 24, 0, 24, 24)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.velocity_x = math.cos(self.radians)*self.speed
        self.velocity_y = math.sin(self.radians)*self.speed
        self.index = 0
        self.timer = 0
        self.limit = 3
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height
        )
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height
        )
    def update(self):
        if not game == None:
            if not game.paused:
                self.timer += 1
                if self.timer >= self.limit:
                    self.index += 1
                    if self.index > 3:
                        self.index = 0
                    self.timer = 0
                self.sprite.x += self.velocity_x
                self.sprite.y += self.velocity_y
                self.update_rect()
                if not self.rect.intersect(game.rect):
                    self.sprite.remove()
                self.sprite.subY = self.index*self.sprite.height
class Player(object):
    def __init__(self, pos):
        x = pos[0]*tile_size-8
        y = pos[1]*tile_size-16
        self.sprite = Sprite(x, y, 22, 24, 2, "proto", 96, 0, 32, 32)
        self.sprite.update = self.update
# blue-yellow color swap
##        self.sprite.color_list.append(((183, 30, 123), (21, 95, 217)))
##        self.sprite.color_list.append(((173, 173, 173), (234, 158, 34)))
        self.sprite.on_level = True
        self.health_max = 28
        self.health = self.health_max
        self.health_bar = HUDBar(24, 17, self.health, self.health_max, 0)
        self.lives = 2
        self.life_text = ScreenText(0, 0, str(self.lives), 1)
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.2
        self.jump_height = 4.64453125
        self.grounded = False
        self.jumping = False
        self.rect_offset_x1 = 8
        self.rect_offset_x2 = 24
        self.rect_offset_y1 = 3
        self.rect_offset_y2 = 26
        self.sprite.width = self.rect_offset_x2-self.rect_offset_x1
        self.sprite.height = self.rect_offset_y2-self.rect_offset_y1
        self.direction = 1
        self.last_direction = self.direction
        self.facing = 1
        self.landing = False
        self.land_timer = 0
        self.land_limit = 4
        self.idle_timer = 0
        self.idle_limit_a = 10
        self.idle_limit_b = 10
        self.idle_limit = self.idle_limit_a
        self.run_start = False
        self.run_start_timer = 0
        self.run_start_limit = 8
        self.run_stop = False;
        self.run_stop_timer = 0
        self.run_stop_limit = 4
        self.running = False
        self.run_speed = 1.375
        self.run_speed_air = 1.3125
        self.run_timer = 0
        self.run_limit = 7
        self.run_index = 0
        self.run_indexes = 3
        self.run_index_direction = 1
        self.hanging = False
        self.climbing = False
        self.climb_timer = 0
        self.climb_limit = 9
        self.climb_index = 0
        self.climb_speed = 1.296875
        self.climb_fire_direction = self.direction
        self.attacking = False
        self.attack_timer = 0
        self.attack_limit = 15
        self.charging = False
        self.charge_timer = 0
        self.charge_limit = 2
        self.charge_array = [
            0,1,0,1,0,1,0,1,
            0,2,0,2,0,2,0,2,
            0,3,0,3,0,3,0,3,
            0,3,0,3,0,3,0,3,
        ]
        self.charge_array_full = [4, 5, 0]
        self.charge_full = False
        self.charge_key_timer = 0
        self.charge_key_limit = 30
        self.charge_level = 0
        self.charge_index = 0
        self.charge_colors = [
            [],
            [
                ((0, 0, 0), (0, 42, 136)),
            ],
            [
                ((0, 0, 0), (21, 95, 217)),
            ],
            [
                ((0, 0, 0), (100, 176, 255)),
            ],
            [
                ((183, 30, 123), (0, 0, 1)),
                ((173, 173, 173), (0, 0, 2)),
                ((0, 0, 0), (183, 30, 123)),
                ((0, 0, 1), (173, 173, 173)),
                ((0, 0, 2), (0, 0, 0))
            ],
            [
                ((183, 30, 123), (0, 0, 1)),
                ((173, 173, 173), (0, 0, 2)),
                ((0, 0, 0), (173, 173, 173)),
                ((0, 0, 1), (0, 0, 0)),
                ((0, 0, 2), (183, 30, 123))
            ]
        ]
        self.sliding = False
        self.slide_timer = 0
        self.slide_limit = 25
        self.slide_anim_timer = 0
        self.slide_anim_limit = 5
        self.slide_speed = 2.5
        self.slide_stopping = True
        self.slide_anim_index = 0
        self.underfoot = []
        self.underfoot_climb = []
        self.shots = []
        self.shots_fired = 0
        self.shots_max = 3
        self.shot_speed = 4
        self.shot_direction = 1
        self.shot_type = 'normal'
        self.shot_width = 8
        self.shot_height = 8
        self.shot_damage = 2
        self.shot_mid_damage = 3
        self.shot_large_damage = 6
        self.shot_piercing = False
        self.warping = True
        self.warp_timer = 0
        self.warp_limit = 2
        self.warp_speed = 8
        self.warp_x = self.sprite.x
        self.warp_y = self.sprite.y-7
        self.warp_indexes = [2, 0, 1]
        self.warp_index = 0
        self.warp_line = True
        self.shielded = False
        self.sprite.y = -self.sprite.height
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.slide_rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y2-tile_size,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.shield_rect = None
        self.charge_full_sound = False
        self.rect_last = self.rect
        self.idle_index = 0
        self.index_idle = 3
        self.index_charge = 3#5
        self.index_run_phase = 6
        self.index_run = 7
        self.index_jump = 10
        self.index_land = 11
        self.index_climb = 12
        self.index_climb_end = 14
        self.index_slide = 15
        self.index_dash = 17
        self.index_attack = 19
        self.index_run_attack = 20
        self.index_jump_attack = 23
        self.index_climb_attack = 24
        self.index_hurt = 25
        self.index_slip = 26
        self.index_warp = 0
        self.center = {}
        self.room = {}
        self.overhead = False
        self.jumped = False
        self.attacked = False
        self.dead = False
        self.hurt = False
        self.hurt_timer = 0
        self.hurt_limit = 30
        self.hurt_speed = 0.5
        self.invincible = False
        self.invincible_timer = 0
        self.invincible_limit = 90
        self.update_rect()
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.slide_rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y2-tile_size,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.center['x'] = self.rect.left+self.sprite.width/2
        self.center['y'] = self.rect.top +self.sprite.height/2
        self.room['x'] = math.floor(self.center['x']/screen_size[0])
        self.room['y'] = math.floor(self.center['y']/screen_size[1])
        if not (self.sliding or self.attacking or self.hanging or (self.running and self.grounded) or self.hurt or self.dead):
            if self.grounded:
                if self.facing == -1:
                    self.shield_rect = Rectangle(
                        self.center['x']-11,
                        self.center['y']-6,
                        self.center['x']-5,
                        self.center['y']-6+15
                    )
                elif self.facing == 1:
                    self.shield_rect = Rectangle(
                        self.center['x']+5,
                        self.center['y']-6,
                        self.center['x']+11,
                        self.center['y']-6+15
                    )
            else:
                if self.facing == -1:
                    self.shield_rect = Rectangle(
                        self.center['x']-12,
                        self.center['y']-10,
                        self.center['x']-7,
                        self.center['y']+5
                    )
                elif self.facing == 1:
                    self.shield_rect = Rectangle(
                        self.center['x']+7,
                        self.center['y']-10,
                        self.center['x']+12,
                        self.center['y']+5
                    )
        else:
            self.shield_rect = None
    def kill(self, explosion=False):
        if not self.dead:
            self.dead = True
            if explosion:
                OrbExplosion((self.center['x'], self.center['y']))
            self.sprite.remove()
            square1.play(sfx_death1)
            square2.play(sfx_death2)
            triangle.stop()
            noise.stop()
    def hit(self, damage, direction=0):
        if not self.invincible and not self.dead:
            if direction == 0:
                direction = -self.facing
                if self.direction == 0:
                    direction = 1
            self.attacking=self.running=self.jumping=self.climbing=self.hanging=False
            if not self.overhead and self.sliding:
                self.stop_sliding()
            self.stop_charging()
            self.velocity_y = 0
            self.hurt = True
            self.hurt_timer = 0
            self.invincible = True
            self.invincible_timer = 0
            self.health -= damage
            self.health_bar.update_ticks(self.health)
            self.direction = direction
            self.facing = -self.direction
            if not sfx2.get_sound() == sfx_life:
                sfx2.play(sfx_hurt2)
            sfx4.play(sfx_hurt4)
            if self.health <= 0 and not self.dead:
                self.kill(True)
            else:
                HurtEffect(self)
                Smoke((self.sprite.x+2, self.sprite.y-6), self.facing, 'hurt')
                Smoke((self.sprite.x+14, self.sprite.y-10), self.facing, 'hurt')
                Smoke((self.sprite.x+26, self.sprite.y-6), self.facing, 'hurt')
    def shoot(self, shot_type='small'):
        if not self.sliding:
            if self.shots_fired < self.shots_max:
                if self.run_start:
                    self.run_start = False
                    self.run_start_timer = 0
                    self.running = False
                    self.run_timer = 0
                    self.run_index = 0
                    self.run_index_direction = 1
                if self.hanging:
                    self.climbing = False
                    self.velocity_y = 0
                    facing = self.climb_fire_direction
                else:
                    facing = self.facing
                if facing == 0:
                    facing = 1
                if not sfx2.get_sound() == sfx_life:
                    if shot_type == 'large':
                        sfx4.play(sfx_charge_shot)
                    elif shot_type == 'mid':
                        sfx4.play(sfx_charge_shot_mid)
                    else:
                        sfx2.play(sfx_shot)
                self.attacking = True
                self.attack_timer = 0
                shot_x = self.center['x']+8*facing
                shot_y = self.center['y']
                piercing = self.shot_piercing
                if shot_type == 'small':
                    if facing < 0:
                        shot_x -= 8
                    damage = self.shot_damage
                if shot_type == 'mid':
                    if facing < 0:
                        shot_x -= 8
                    damage = self.shot_mid_damage
                if shot_type == 'large':
                    if facing < 0:
                        shot_x -= 8
                    damage = self.shot_large_damage
                    SmallExplosion((shot_x+4, shot_y+4), 1, 4, 1)
                    self.shots_fired += 2
                shot = Shot(shot_x, shot_y, self, 90*facing, damage, piercing, 'proto', game.enemies, shot_type)
                self.shots_fired += 1
                self.attacked = True
    def move(self, dx=0, dy=0):
        self.underfoot = []
        self.underfoot_climb = []
        self.overhead = False
        self.slide_stopping = False
        if not dx == 0: self.move_axis(dx, 0)
        if not dy == 0: self.move_axis(0, dy)
        if self.center['y'] < game.rect.top and self.climbing:
            if not game.map[self.room['y']-1][self.room['x']] == ' ':
                game.scrolling = True
                game.scroll_direction_x = 0
                game.scroll_direction_y = -1
        if self.rect.left < 0:
            self.sprite.x = -self.rect_offset_x1
        if self.rect.right > len(game.map[0])*screen_size[0]*tile_size:
            self.sprite.x = len(game.map[0])*screen_size[1]*tile_size-self.rect_offset_x2
        if self.rect.top > game.rect.bottom:
            self.kill()
        self.update_rect()
        if len(self.underfoot) > 0:
            if not self.grounded:
                if not self.running and not self.attacking:
                    self.landing = True
                    self.land_timer = 0
                if not sfx2.get_sound() == sfx_life and not sfx2.get_sound() == sfx_charge_full and not sfx2.get_sound() == sfx_charge:
                    sfx2.play(sfx_land2)
                if not sfx4.get_busy():
                    sfx4.play(sfx_land4)
            self.hanging = False
            self.climbing = False
            self.jumping = False
            self.velocity_y = 0
        else:
            if self.landing:
                self.landing = False
                self.land_timer = 0
        self.grounded = len(self.underfoot) > 0
        if self.hanging:
            valid = False
            for tile in tiles:
                if tile.ladder:
                    if Rectangle(
                        self.sprite.x+self.rect_offset_x1,
                        self.sprite.y+self.rect_offset_y1,
                        self.sprite.x+self.rect_offset_x2,
                        self.sprite.y+self.rect_offset_y1+20
                        ).intersect(tile.rect):
                        valid = True
                        break
            self.hanging = valid
            if not valid:
                self.velocity_y = 0
                self.climbing = False
                if keys[pygame.K_UP]:
                    self.grounded = True
        for tile in tiles:
            if tile.solid:
                if self.rect.intersect(tile.rect) and not self.slide_rect.intersect(tile.rect):
                    self.overhead = True
        if not self.grounded and self.sliding:
            if self.sliding:
                if self.overhead:
                    self.stop_sliding()
                    self.sprite.y += self.slide_rect.top-self.rect.top
                    self.update_rect()
                else:
                    self.stop_sliding()
        if self.slide_stopping:
            self.stop_sliding()
        elif self.slide_timer == 1:
            if self.facing == -1:
                x = self.rect.right-4
            if self.facing == 1:
                x = self.rect.left+4
            Smoke((x, self.rect.bottom-8), self.facing, 'slide')
    def move_axis(self, dx, dy):
        self.sprite.x += dx
        self.sprite.y += dy
        self.update_rect()
        rect = self.rect
        if self.sliding:
            rect = self.slide_rect
        for tile in tiles:
            if tile.solid or tile.through:
                if Rectangle(
                    self.sprite.x+self.rect_offset_x1+4,
                    self.sprite.y+self.rect_offset_y1,
                    self.sprite.x+self.rect_offset_x2-4,
                    self.sprite.y+32-5
                    ).intersect(tile.rect):
                    if dy > 0:
                        self.underfoot_climb.append(tile)
            if rect.intersect(tile.rect):
                if tile.solid:
                    if dx < 0:
                        self.sprite.x = tile.rect.right-self.rect_offset_x1
                        self.update_rect()
                        if not self.rect.intersect(tile.rect):
                            self.slide_stopping = True
                    if dx > 0:
                        self.sprite.x = tile.rect.left-self.rect_offset_x2
                        self.update_rect()
                        if not self.rect.intersect(tile.rect):
                            self.slide_stopping = True
                    if dy < 0:
                        self.sprite.y = tile.rect.bottom-self.rect_offset_y1
                        self.velocity_y = 0.25
                    if dy > 0:
                        self.sprite.y = tile.rect.top-self.rect_offset_y2
                        self.velocity_y = 0
                        self.underfoot.append(tile)
                if tile.through and not self.hanging:
                    if dy > 0 and rect.bottom >= tile.sprite.y and self.rect_last.bottom <= tile.sprite.y+8 and self.rect.right > tile.rect.left+6 and self.rect.left < tile.rect.right-6:
                        self.sprite.y = tile.rect.top-self.rect_offset_y2
                        self.velocity_y = 0
                        self.underfoot.append(tile)
                self.update_rect()
        for enemy in game.enemies:
            if rect.intersect(enemy.rect):
                direction = 1
                if rect.right < enemy.rect.right:
                    direction = -1
                elif rect.left > enemy.rect.left:
                    direction = 1
                self.hit(enemy.damage, direction)
        for pickup in game.pickups:
            if rect.intersect(pickup.rect):
                if pickup.type == 'health_big':
                    game.refill_health = self.health + 10
                    game.refill_timer = 0
                    game.refilling = True
                    game.refill_recipient = self
                if pickup.type == 'health_small':
                    game.refill_health = self.health + 2
                    game.refill_timer = 0
                    game.refilling = True
                    game.refill_recipient = self
                if pickup.type == 'life':
                    self.lives += 1
                    if self.lives > 9:
                        self.lives = 9
                    sfx2.play(sfx_life)
                    self.life_text.redraw(str(self.lives))
                pickup.destroy()
    def stop_sliding(self):
        if not self.overhead:
            self.sliding = False
            self.slide_timer = 0
            self.slide_anim_timer = 0
            self.slide_anim_index = 0
    def stop_charging(self):
        self.charging = False
        self.charge_timer = 0
        self.charge_level = 0
        self.charge_index = 0
        self.charge_full = False
        self.charge_full_sound = False
        self.sprite.color_list = []
        sfx2.stop()
    def update(self):
        if not game == None:
            if not game.paused:
                if self.health > self.health_max:
                    self.health = self.health_max
                self.attacked = False
                self.jumped = False
                index = 0
                if self.warping:
                    if self.sprite.y >= self.warp_y:
                        if self.warp_line:
                            self.warp_line = False
                            if not sfx2.get_sound() == sfx_life:
                                sfx2.play(sfx_entrance)
                        self.warp_timer += 1
                        index = self.index_warp+self.warp_indexes[self.warp_index]
                        if self.warp_timer >= self.warp_limit:
                            self.warp_timer = 0
                            self.warp_index += 1
                            if self.warp_index > len(self.warp_indexes)-1:
                                self.warp_index = len(self.warp_indexes)-1
                                self.warping = False
                                self.grounded = True
                                index = self.index_idle
                                self.sprite.y = self.warp_y+5
                                self.update_rect()
                    else:
                        self.sprite.y += self.warp_speed
                else:
                    self.velocity_x = 0
                    self.last_direction = self.direction
                    if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                        self.direction = 0
                    elif keys[pygame.K_LEFT]:
                        self.direction = -1
                    elif keys[pygame.K_RIGHT]:
                        self.direction = 1
                    else:
                        self.direction = 0
                    if not self.hurt:
                        if self.run_start:
                            self.run_start_timer += 1
                            if self.run_start_timer >= self.run_start_limit:
                                self.run_start = False
                                self.run_start_timer = 0
                                self.running = True
                                self.run_timer = 0
                                self.run_index = 0
                                self.run_index_direction = 1
                        if not self.hanging:
                            if not self.direction == 0:
                                if self.grounded and not self.run_start and not self.running and not (self.sliding and self.overhead):
                                    if self.sliding and not self.direction == self.facing or not self.sliding:
                                        self.velocity_x = 2*self.direction
                                        self.run_start = True
                                        self.run_start_timer = 0
                                        self.run_stop = False
                                        self.run_stop_timer = 0
                                        self.stop_sliding()
                                    if self.landing:
                                        self.landing = False
                                        self.land_timer = 0
                                if not self.sliding and self.running or not self.grounded:
                                    if not self.running:
                                        self.run_timer = 0
                                        self.run_index = 0
                                        self.run_index_direction = 1
                                        self.running = True
                                    if self.landing:
                                        self.landing = False
                                        self.land_timer = 0
                                    if self.grounded:
                                        self.velocity_x = self.run_speed * self.facing
                                    else:
                                        self.velocity_x = self.run_speed_air * self.facing
                                    self.run_timer += 1
                                    if self.run_timer >= self.run_limit:
                                        self.run_timer = 0
                                        self.run_index += self.run_index_direction
                                        if self.run_index <= 0:
                                            self.run_index = 0
                                            self.run_index_direction = 1
                                        if self.run_index >= self.run_indexes-1:
                                            self.run_index = self.run_indexes-1
                                            self.run_index_direction = -1
                                if not self.direction == self.facing:
                                    self.facing = self.direction
                            else:
                                if self.run_stop:
                                    self.run_stop_timer += 1
                                    if self.run_stop_timer >= self.run_stop_limit:
                                        self.run_stop = False
                                        self.run_stop_timer = 0
                                        self.run_timer = 0
                                        self.run_index = 0
                                        self.run_index_direction = 1
                                if not self.direction == self.last_direction and self.running:
                                    if self.grounded:
                                        self.velocity_x = self.run_speed * self.facing
                                        self.run_stop = True
                                        self.run_stop_timer = 0
                                self.running = False
                                self.run_timer = 0
                                self.run_index = 0
                                self.run_index_direction = 1
                                if self.run_start:
                                    self.run_start = False
                                    self.run_start_timer = 0
                        else:
                            if not self.direction == 0 and not (self.hanging and self.attacking):
                                self.climb_fire_direction = self.direction
                            else:
                                self.climb_fire_direction = self.facing
                        if not keys[pygame.K_DOWN]:
                            if keys[pygame.K_UP]:
                                if not self.hanging:
                                    if not self.attacking:
                                        for tile in tiles:
                                            if tile.ladder and not tile.through:
                                                if self.rect.intersect(tile.rect):
                                                    if self.sliding and not self.overhead or not self.sliding:
                                                        if self.sliding:
                                                            self.stop_sliding()
                                                        self.hanging = True
                                                        self.climbing = True
                                                        self.grounded = False
                                                        self.velocity_x = tile.sprite.x-self.rect_offset_x1-self.sprite.x
                                                        self.attacking = False
                                                        break
                                if self.hanging:
                                    if self.attacking:
                                        self.climbing = False
                                        self.velocity_y = 0
                                    else:
                                        self.climbing = True
                                        self.velocity_y = -self.climb_speed
                            elif self.hanging:
                                self.climbing = False
                                self.velocity_y = 0
                        if not keys[pygame.K_UP]:
                            if keys[pygame.K_DOWN]:
                                if not self.hanging:
                                    if not self.attacking:
                                        for tile in tiles:
                                            if tile.ladder:
                                                if Rectangle(
                                                self.sprite.x+self.rect_offset_x1,
                                                self.sprite.y+self.rect_offset_y1,
                                                self.sprite.x+self.rect_offset_x2,
                                                self.sprite.y+32+3
                                                ).intersect(tile.rect):
                                                    if tile in self.underfoot_climb and self.grounded or not self.grounded:
                                                        if self.sliding:
                                                            self.stop_sliding()
                                                        self.hanging = True
                                                        self.climbing = True
                                                        self.grounded = False
                                                        self.velocity_x = tile.sprite.x-self.rect_offset_x1-self.sprite.x
                                                        self.velocity_y = 12
                                                        self.attacking = False
                                                        break
                                else:
                                    if self.attacking:
                                        self.climbing = False
                                        self.velocity_y = 0
                                    else:
                                        self.climbing = True
                                        self.velocity_y = self.climb_speed
                            elif self.hanging:
                                self.climbing = False
                                self.velocity_y = 0
                        if self.hanging:
                            self.jumping = False
                            self.run_start = False
                            self.run_start_timer = 0
                            self.run_stop = False
                            self.run_stop_timer = 0
                            if self.landing:
                                self.landing = False
                                self.land_timer = 0
                            self.running = False
                            self.run_timer = 0
                            self.run_index = 0
                            self.run_index_direction = 1
                            if not self.climbing or keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                                self.velocity_y = 0
                            else:
                                self.climb_timer += 1
                                if self.climb_timer >= self.climb_limit:
                                    self.climb_timer = 0
                                    self.climb_index += 1
                                    if self.climb_index > 1:
                                        self.climb_index = 0
                        if keys[pygame.K_z]:
                            if not last_keys[pygame.K_z]:
                                if self.grounded:
                                    if keys[pygame.K_DOWN]:
                                        self.sliding = True
                                        self.running = False
                                        self.run_stop = False
                                        self.run_stop_timer = 0
                                        self.run_start = False
                                        self.run_start_timer = 0
                                        self.run_timer = 0
                                        self.run_index = 0
                                        self.run_index_direction = 1
                                    else:
                                        if self.sliding:
                                            self.stop_sliding()
                                        else:
                                            self.velocity_y = -self.jump_height
                                            self.jumping = True
                                            self.jumped = True
                                            if self.run_start or self.run_stop:
                                                self.running = True
                                            self.run_stop = False
                                            self.run_stop_timer = 0
                                            self.run_start = False
                                            self.run_start_timer = 0
                                            self.run_timer = 0
                                            self.run_index = 0
                                            self.run_index_direction = 1
                                if self.hanging:
                                    if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                                        self.hanging = False
                                        self.climbing = False
                        else:
                            if self.jumping:
                                if self.velocity_y < 0.5:
                                    self.velocity_y = 0.5
                        if keys[pygame.K_x]:
                            self.charge_key_timer += 1
                            if not last_keys[pygame.K_x]:
                                self.shoot()
                            elif self.charge_key_timer > self.charge_key_limit:
                                if not self.charging:
                                    self.charging = True
                                    sfx2.play(sfx_charge)
                                else:
                                    if not self.charge_full_sound and not sfx2.get_busy():
                                        sfx2.play(sfx_charge_full, -1)
                                        self.charge_full_sound = True
                                    self.charge_timer += 1
                                    if self.charge_timer >= self.charge_limit:
                                        self.charge_timer = 0
                                        self.charge_index += 1
                                        if self.charge_index >= len(self.charge_array):
                                            self.charge_index = 0
                                            self.charge_full = True
                                        if self.charge_index >= len(self.charge_array_full):
                                            if self.charge_full:
                                                    self.charge_index = 0
                                        if self.charge_full:
                                            self.charge_level = self.charge_array_full[self.charge_index]
                                        else:
                                            self.charge_level = self.charge_array[self.charge_index]
                                        self.sprite.color_list = self.charge_colors[self.charge_level]
                                    if not sfx2.get_busy():
                                        self.charge_full_sound = True
                        else:
                            self.charge_key_timer = 0
                            if self.charging:
                                if self.charge_full:
                                    shot_type = 'large'
                                else:
                                    shot_type = 'mid'
                                self.stop_charging()
                                self.shoot(shot_type)
                            self.sprite.color_list = []
                    if self.attacking:
                        self.attack_timer += 1
                        if self.attack_timer >= self.attack_limit:
                            self.attacking = False
                            self.attack_timer = 0
                    if self.landing:
                        self.land_timer += 1
                        if self.land_timer >= self.land_limit:
                            self.landing = False
                            self.land_timer = 0
                    if self.sliding:
                        self.running = False
                        self.run_stop = False
                        self.run_stop_timer = 0
                        self.run_start = False
                        self.run_start_timer = 0
                        self.run_timer = 0
                        self.run_index = 0
                        self.run_index_direction = 1
                        self.velocity_x = self.slide_speed * self.facing
                        self.slide_anim_timer += 1
                        if self.slide_anim_timer >= self.slide_anim_limit:
                            self.slide_anim_timer = 0
                            self.slide_anim_index += 1
                            if self.slide_anim_index > 1:
                                self.slide_anim_index = 0
                        self.slide_timer += 1
                        if self.slide_timer >= self.slide_limit and not self.overhead:
                            self.stop_sliding()
                            self.run_stop = True
                            self.run_stop_timer = 0
                    if self.hurt:
                        self.velocity_x = self.hurt_speed * -self.facing
                        self.hurt_timer += 1
                        if self.hurt_timer >= self.hurt_limit:
                            self.hurt_timer = 0
                            self.hurt = False
                    if self.invincible:
                        self.invincible_timer += 1
                        self.sprite.visible = not self.sprite.visible
                        if self.invincible_timer >= self.invincible_limit:
                            self.invincible_timer = 0
                            self.invincible = False
                            self.sprite.visible = True
                    if not self.hanging:
                        self.velocity_y += self.gravity
                    if self.velocity_y > 7:
                        self.velocity_y = 7
                    self.move(self.velocity_x, self.velocity_y)
                    self.rect_last = self.rect
                    idle = False
                    if self.grounded:
                        if self.hurt:
                            index = self.index_hurt
                        elif self.running:
                            if self.attacking:
                                index = self.index_run_attack+self.run_index
                            else:
                                index = self.index_run+self.run_index
                        elif self.landing:
                            index = self.index_land
                        elif self.sliding:
                            index = self.index_slide+self.slide_anim_index
                        elif self.attacking:
                            index = self.index_attack
                        elif self.run_start or self.run_stop:
                            index = self.index_run_phase
                        elif self.charging:
                            index = self.index_charge
                        else:
                            idle = True
                            index = self.index_idle + self.idle_index
                            self.idle_timer += 1
                            if self.idle_timer >= self.idle_limit:
                                self.idle_timer = 0
                                if self.idle_index == 0:
                                    self.idle_limit = self.idle_limit_b
                                    self.idle_index = 1
                                elif self.idle_index == 1:
                                    self.idle_limit = self.idle_limit_a
                                    self.idle_index = 0
                        if not idle:
                            self.idle_timer = 0
                            self.idle_limit = self.idle_limit_a
                            self.idle_index = 0
                    else:
                        if self.hurt:
                            index = self.index_hurt
                        elif self.hanging:
                            if self.attacking:
                                index = self.index_climb_attack
                                self.facing = self.climb_fire_direction
                                self.direction = self.climb_fire_direction
                                self.climb_index = 1
                            else:
                                valid = False
                                for tile in tiles:
                                    if tile.ladder:
                                        if Rectangle(
                                            self.sprite.x+self.rect_offset_x1,
                                            self.sprite.y+self.rect_offset_y1-3,
                                            self.sprite.x+self.rect_offset_x2,
                                            self.sprite.y+self.rect_offset_y2-14
                                            ).intersect(tile.rect):
                                            valid = True
                                            break
                                if valid:
                                    index = self.index_climb+self.climb_index
                                else:
                                    index = self.index_climb_end
                        else:
                            if self.attacking:
                                index = self.index_jump_attack
                            else:
                                index = self.index_jump
                    self.sprite.flip_x = self.facing == -1
                    if self.hanging and self.attacking:
                        self.sprite.flip_x = self.climb_fire_direction == -1
                self.sprite.subX = index*self.sprite.subWidth
class Pickup(object):
    def __init__(self, pos, hop=False, pickup_type='health_small'):
        subX = 0
        subY = 0
        width = 16
        height = 16
        if pickup_type == 'health_big':
            subX = 16
            subY = 16
            width = 16
            height = 16
        elif pickup_type == 'health_small':
            subX = 8
            subY = 32
            width = 8
            height = 8
        elif pickup_type == 'energy_big':
            subX = 32
            width = 16
            height = 12
        elif pickup_type == 'energy_small':
            subX = 8
            subY = 16
            width = 8
            height = 8
        elif pickup_type == 'life':
            subX = 16
            width = 16
            height = 16
        else:
            return None
        x = pos[0]-width/2
        y = pos[1]-height/2
        self.sprite = Sprite(x, y, width, height, 4, "life", subX, subY, width, height)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.timer = 0
        self.limit = 10
        self.index = 0
        self.velocity_y = 0
        self.life = 0
        self.life_blink = 180
        self.life_limit = 300
        self.subX = subX
        self.subY = subY
        self.type = pickup_type
        self.hop = hop
        if hop:
            self.velocity_y = 0
        else:
            self.sprite.x += tile_size/2
            self.sprite.y += tile_size/2
        self.gravity = 0.2
        self.rect = Rectangle(
            x,
            y,
            x+width,
            y+height
        )
    def destroy(self):
        game.pickups.remove(self)
        self.sprite.remove()
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height
        )
    def update(self):
        if not game == None:
            if not game.paused:
                if game.playing:
                    if not game.player == None:
                        if not self.type == 'health_big' and not self.type == 'health_small':
                            self.sprite.color_list = game.player.sprite.color_list
                    if self.hop:
                        self.life += 1
                        self.velocity_y += self.gravity
                        self.sprite.y += self.velocity_y
                        self.update_rect()
                        for tile in tiles:
                            if self.rect.intersect(tile.rect):
                                if tile.solid:
                                    if self.velocity_y < 0:
                                        self.sprite.y = tile.rect.bottom
                                        self.velocity_y = 0.25
                                    if self.velocity_y > 0:
                                        self.sprite.y = tile.rect.top-self.sprite.height
                                        self.velocity_y = 0
                                if tile.through:
                                    if self.velocity_y > 0:
                                        self.sprite.y = tile.rect.top-self.sprite.height
                                        self.velocity_y = 0
                            self.update_rect()
                        if not self.rect.intersect(game.rect):
                            self.sprite.remove()
                    if not self.type == 'life':
                        self.timer += 1
                        if self.timer >= self.limit:
                            self.timer = 0
                            self.index += 1
                            if self.index > 1:
                                self.index = 0
                    if self.life >= self.life_blink:
                        self.sprite.visible = not self.sprite.visible
                    else:
                        self.sprite.visible = True
                    if self.life >= self.life_limit:
                        self.destroy()
                    self.sprite.subY = self.subY+self.sprite.height*self.index
                else:
                    self.sprite.visible = False
class Helikoppa(object):
    def __init__(self, pos):
        x = pos[0]-6
        y = pos[1]-12
        self.sprite = Sprite(x, y, 32, 24, 2, "helikoppa", 0, 0, 32, 24)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.rect_offset_x1 = 6
        self.rect_offset_x2 = self.sprite.width-6
        self.rect_offset_y1 = -4
        self.rect_offset_y2 = self.sprite.height
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2,
        )
        self.center = {}
        self.facing = -1
        self.update_rect()
        self.rotor_index = 0
        self.rotor_timer = 0
        self.rotor_limit = 2
        self.index = 0
        self.health = 5
        self.damage = 3
        self.speed = 1
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 0.125
        self.dead = False
        self.falling = False
        self.invincible = False
        self.shielded = False
        self.pos = pos
        self.turn()
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2,
        )
        self.center['x'] = self.rect.left + 10
        self.center['y'] = self.rect.top + 10
        if not game == None:
            if not game.player == None:
                self.dist_x = game.player.center['x'] - self.center['x']
                self.dist_y = game.player.center['y'] - self.center['y']
    def kill(self, explosion=False):
        if not self.dead:
            if explosion:
                game.pickup((self.center['x'], self.center['y']))
                Explosion((self.center['x'], self.center['y']+10))
            self.dead = True
            game.enemies.remove(self)
            self.sprite.remove()
    def hit(self, damage, direction):
        self.health -= damage
        if self.health <= 0:
            self.kill(True)
    def turn(self):
        if not game == None:
            if not game.player == None:
                if self.dist_x < 0:
                    self.facing = -1
                elif self.dist_x >= 0:
                    self.facing = 1
        self.sprite.flip_x = self.facing == 1
    def move(self, dx, dy):
        if not dx == 0:
            self.move_axis(dx, 0)
        if not dy == 0:
            self.move_axis(0, dy)
    def move_axis(self, dx, dy):
        self.sprite.x += dx
        self.sprite.y += dy
        self.update_rect()
        for tile in tiles:
            if tile.solid:
                if self.rect.intersect(tile.rect):
                    if self.velocity_x < 0:
                        self.sprite.x = tile.rect.right-self.rect_offset_x1
                    if self.velocity_x > 0:
                        self.sprite.x = tile.rect.left-self.rect_offset_x2
                    if self.velocity_y < 0:
                        self.sprite.y = tile.rect.bottom-self.rect_offset_y1
                    if self.velocity_y > 0:
                        self.sprite.y = tile.rect.top-self.rect_offset_y2
                    self.update_rect()
                    Explosion((self.center['x'], self.center['y']+10))
                    self.kill()
                    break
    def update(self):
        if not game == None:
            if not game.paused:
                if game.playing:
                    self.sprite.visible = True
                    if not self.falling:
                        self.velocity_x = self.speed*self.facing
                        self.rotor_timer += 1
                        if self.rotor_timer >= self.rotor_limit:
                            self.rotor_timer = 0
                            self.index += 1
                            if self.index > 1:
                                self.index = 0
                    else:
                        self.velocity_x = 0
                        self.velocity_y += self.gravity
                        self.rotor_timer = 0
                        self.index = 2
                    self.move(self.velocity_x, self.velocity_y)
                    if self.dist_x*self.facing < self.speed and self.dist_y > 0:
                        if not self.falling:
                            SmallExplosion((self.center['x'], self.center['y']-10))
                            self.falling = True
                            sfx2.play(sfx_fall)
                    self.sprite.subX = self.index*self.sprite.width
                    if not self.rect.intersect(game.rect_out):
                        self.kill()
                else:
                    self.sprite.visible = False
class Met(object):
    def __init__(self, pos):
        x = pos[0]-4
        y = pos[1]-8
        self.sprite = Sprite(x, y, 24, 24, 2, "met", 0, 0, 24, 24)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.rect = Rectangle(
            self.sprite.x+4,
            self.sprite.y+8,
            self.sprite.x+self.sprite.width-4,
            self.sprite.y+self.sprite.height,
        )
        self.center = {}
        self.facing = -1
        self.update_rect()
        self.hid = True
        self.shielded = True
        self.hiding = False
        self.hide_timer = 0
        self.hide_limit = 60
        self.hide_anim_limit = 5
        self.hide_quick_anim_limit = 2
        self.hide_index = 0
        self.hide_indexes = 3
        self.open_limit = 30
        self.shot = False
        self.shot_speed = 2
        self.shot_damage = 2
        self.shot_piercing = True
        self.shots_fired = 0
        self.in_range = False
        self.dist_max = tile_size*6
        self.dist_x = self.dist_max
        self.dist_y = 0
        self.health = 2
        self.damage = 3
        self.dead = False
        self.invincible = False
        self.pos = pos
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x+4,
            self.sprite.y+8,
            self.sprite.x+self.sprite.width-4,
            self.sprite.y+self.sprite.height,
        )
        self.center['x'] = self.rect.left + 8
        self.center['y'] = self.rect.top + 8
        if not game == None:
            if not game.player == None:
                self.dist_x = game.player.center['x'] - self.center['x']
                self.dist_y = game.player.center['y'] - self.center['y']
    def kill(self, explosion=False):
        if not self.dead:
            if explosion:
                game.pickup((self.center['x'], self.center['y']))
                SmallExplosion((self.center['x'], self.center['y']))
            self.dead = True
            game.enemies.remove(self)
            self.sprite.remove()
    def hit(self, damage, direction):
        self.health -= damage
        if self.health <= 0:
            self.kill(True)
    def shoot(self):
        angles = [45*self.facing, 90*self.facing, 135*self.facing]
        for angle in angles:
            Shot(self.center['x']+8*self.facing, self.center['y'], self, angle, self.shot_damage, self.shot_piercing, 'met', [game.player])
        if not sfx2.get_sound() == sfx_life:
            sfx2.play(sfx_enemy_shot)
    def turn(self):
        if not game == None:
            if not game.player == None:
                if self.dist_x < 0:
                    self.facing = -1
                elif self.dist_x >= 0:
                    self.facing = 1
        self.sprite.flip_x = self.facing == 1
    def update(self):
        if not game == None:
            if not game.paused:
                if game.playing:
                    self.sprite.visible = True
                    self.update_rect()
                    if abs(self.dist_x) < self.dist_max:
                        self.in_range = True
                    else:
                        self.in_range = False
                        if self.hid:
                            self.hide_timer = 0
                    if self.in_range:
                        if self.hid:
                            self.turn()
                            self.hide_timer += 1
                            if self.hide_timer >= self.hide_limit:
                                self.hide_timer = 0
                                self.hide_index = 0
                                self.hid = False
                    if not self.hid:
                        if self.hiding:
                            self.hide_timer += 1
                            if self.hide_timer >= self.hide_quick_anim_limit:
                                self.hide_timer = 0
                                if self.hide_index == 2:
                                    self.hide_index = 8
                                elif self.hide_index == 8:
                                    self.hide_index = 0
                                    self.hiding = False
                                    self.hid = True
                        elif not self.shot:
                            self.hide_timer += 1
                            if self.hide_timer >= self.hide_anim_limit:
                                self.hide_timer = 0
                                self.hide_index += 1
                                if self.hide_index > self.hide_indexes:
                                    self.hide_index = 2
                                    self.shoot()
                                    self.shot = True
                        else:
                            self.hide_timer += 1
                            if self.hide_timer >= self.open_limit:
                                self.hide_timer = 0
                                self.hiding = True
                                self.shot = False
                    self.sprite.subX = self.hide_index*self.sprite.width
                    self.shielded = self.hide_index == 0
                    if not self.rect.intersect(game.rect_out):
                        self.kill()
                else:
                    self.sprite.visible = False
class Shot_Zeus(object):
    def __init__(self, pos, target):
        x = pos[0]-8
        y = pos[1]-8
        self.sprite = Sprite(x, y, 16, 16, 4, "zeus", 0, 48, 16, 16)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height,
        )
        self.center = {}
        self.target = target
        self.update_rect()
        self.target_x = self.target.center['x']
        self.target_y = self.target.center['y']
        self.dist_x = self.target_x - self.center['x']
        self.dist_y = self.target_y - self.center['y']
        self.radians = math.atan2(self.dist_y, self.dist_x)
        self.angle = self.radians*180/math.pi
        self.speed = 3.5
        self.index = 0
        self.timer = 0
        self.limit = 5
        self.direction = 1
        self.velocity_x = math.cos(self.radians)*self.speed
        self.velocity_y = math.sin(self.radians)*self.speed
        self.repel = False
        self.stopped = False
        self.stop_timer = 0
        self.stop_limit = 60
        self.damage = 4
        sfx4.play(sfx_lightning_ball)
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x,
            self.sprite.y,
            self.sprite.x+self.sprite.width,
            self.sprite.y+self.sprite.height,
        )
        self.center['x'] = self.sprite.x+self.sprite.width/2
        self.center['y'] = self.sprite.y+self.sprite.height/2
    def update(self):
        if not game == None:
            if not game.paused:
                self.timer += 1
                if self.timer >= self.limit:
                    self.timer = 0
                    self.index += self.direction
                    if self.index < 0:
                        self.index = 3
                    if self.index > 3:
                        self.index = 0
                if not self.stopped:
                    self.sprite.x += self.velocity_x
                    self.sprite.y += self.velocity_y
                    if self.velocity_x < 0:
                        self.direction = -1
                    else:
                        self.direction = 1
                    self.update_rect()
                    self.dist_x = self.target_x - self.center['x']
                    self.dist_y = self.target_y - self.center['y']
                    self.dist = math.sqrt(self.dist_x*self.dist_x+self.dist_y*self.dist_y)
        ##            if not self.repel:
        ##                if self.dist < self.speed:
        ##                    self.stopped = True
                else:
                    self.stop_timer += 1
                    if self.stop_timer >= self.stop_limit:
                        self.stop_timer = 0
                        self.stopped = False
                        self.repel = True
                        self.update_rect()
                        self.target_x = self.target.center['x']
                        self.target_y = self.target.center['y']
                        self.dist_x = self.target_x - self.center['x']
                        self.dist_y = self.target_y - self.center['y']
                        self.radians = math.atan2(self.dist_y, self.dist_x)
                        self.velocity_x = math.cos(self.radians)*self.speed
                        self.velocity_y = math.sin(self.radians)*self.speed

                self.sprite.subX = self.index*self.sprite.subWidth
                if self.rect.intersect(game.player.rect):
                    game.player.hit(self.damage, self.direction)
                if not self.rect.intersect(screen_rect):
                    self.sprite.remove()
class Boss_Zeus(object):
    def __init__(self, pos):
        x = pos[0]*tile_size-16
        y = pos[1]*tile_size-36
        self.sprite = Sprite(x, y, 48, 48, 2, "zeus", 0, 0, 48, 48)
        self.sprite.update = self.update
        self.sprite.on_level = True
        self.health = 28
        self.health_bar = HUDBar(40, 17, self.health, 28, 1)
        self.rect_offset_x1 = 16
        self.rect_offset_y1 = 15
        self.rect_offset_x2 = 32
        self.rect_offset_y2 = 44
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.sprite.width = self.rect_offset_x2-self.rect_offset_x1
        self.sprite.height = self.rect_offset_y2-self.rect_offset_y1
        self.run_timer = 0
        self.run_limit = 6
        self.run_index = 0
        self.run_indexes = 3
        self.run_index_direction = 1
        self.run_speed = 2
        self.dash_speed = 3.5
        self.dash_timer = 0
        self.dash_limit = 25
        self.gravity = 0.2
        self.jump_height = 4.64453125
        self.jump_back_height = 3
        self.jump_bolt_height = 7.5
        self.jump_shoot_height = 4
        self.direction = -1
        self.facing = -1
        self.running = False
        self.velocity_x = 0
        self.velocity_y = 0
        self.underfoot = []
        self.grounded = True
        self.invincible = False
        self.shielded = False
        self.damage = 6
        self.state = 'idle'
        self.state_timer = 0
        self.timers = {
            'land':5,
            'shoot':6
        }
        self.shoot_index = 0
        self.shots = 0
        self.jump_timer = 0
        self.jump_limit = 14
        self.jump_shoot_limit = 23
        self.reloading = False
        self.reload_timer = 0
        self.reload_limit = 10
        self.rounds = 0
        self.jumping_forward = False
        self.bolt_timer = 0
        self.bolt_limit = 7
        self.bolt_index = 0
        self.index_idle = 0
        self.index_land = 4
        self.index_jump_forward = 5
        self.index_jump_back = 6
        self.index_dash = 7
        self.index_bolt_jump = 8
        self.index_bolt_charge = 9
        self.index_bolt = 11
        self.index_run = 13
        self.index_shoot = 16
        self.index_shoot_air = 18
        self.dead = False
        self.dumb_fall = False
        self.dash_fall = False
        self.last_dash = False
        self.sprite.subX = self.index_run*self.sprite.subWidth
        self.center = {}
        self.update_rect()
    def update_rect(self):
        self.rect = Rectangle(
            self.sprite.x+self.rect_offset_x1,
            self.sprite.y+self.rect_offset_y1,
            self.sprite.x+self.rect_offset_x2,
            self.sprite.y+self.rect_offset_y2
        )
        self.rect_dash = Rectangle(
            self.sprite.x+11,
            self.sprite.y+21,
            self.sprite.x+30,
            self.sprite.y+32
        )
        self.center['x'] = self.rect.left+self.sprite.width/2
        self.center['y'] = self.rect.top +self.sprite.height/2
    def move_axis(self, dx, dy):
        self.sprite.x += dx
        self.sprite.y += dy
        self.update_rect()
        for tile in tiles:
            if tile.solid:
                if self.rect.intersect(tile.rect):
                    if dx < 0:
                        self.sprite.x = tile.sprite.x+tile.sprite.width-self.rect_offset_x1
                        self.update_rect()
                    if dx > 0:
                        self.sprite.x = tile.sprite.x-self.rect_offset_x2
                        self.update_rect()
                    if dy < 0:
                        self.sprite.y = tile.sprite.y+tile.sprite.height-self.rect_offset_y1
                        self.velocity_y = 0.25
                    if dy > 0:
                        self.sprite.y = tile.sprite.y-self.rect_offset_y2
                        self.velocity_y = 0
                        self.underfoot.append(tile)
                    self.update_rect()
    def move(self, dx, dy):
        self.underfoot = []
        if not dx == 0:
            self.move_axis(dx, 0)
        if not dy == 0:
            self.move_axis(0, dy)
        rect = self.rect
        if self.state == 'dash':
            rect = self.rect_dash
        if rect.intersect(game.player.rect):
            game.player.hit(4, self.facing)
        if len(self.underfoot) > 0:
            if not self.grounded:
                self.state = 'land'
                self.state_timer = 0
            self.grounded = True
        else:
            self.grounded = False
    def hit(self, damage, direction):
        self.health -= damage
        self.health_bar.update_ticks(self.health)
        self.sprite.visible = False
    def jump(self, direction='forward'):
        self.stop_run()
        self.state = 'jump_'+direction
        self.velocity_y = -self.jump_height
        if direction == 'back':
            self.velocity_y = -self.jump_back_height
        if direction == 'bolt':
            self.velocity_y = -self.jump_bolt_height
        if direction == 'shoot':
            self.velocity_y = -self.jump_shoot_height
    def shoot(self):
        Shot_Zeus((self.center['x']+8*self.direction, self.center['y']), game.player)
        self.stop_run()
        self.turn()
        self.change_state('shoot')
        self.shots += 1
    def run(self):
        self.shots = 0
        self.running = True
        self.target_x = game.player.center['x']
        self.run_timer = 0
        self.run_index = 0
        self.run_index_direction = 0
        self.change_state('run')
        self.turn()
    def stop_run(self):
        self.running = False
        self.run_timer = 0
        self.run_index = 0
        self.run_index_direction = 0
        self.change_state('idle')
    def dash(self):
        self.stop_run()
        self.dash_timer = 0
        self.change_state('dash')
    def change_state(self, new_state):
        self.state_last = self.state
        self.state = new_state
    def turn(self):
        if self.center['x'] < game.player.center['x']:
            self.direction = 1
        if self.center['x'] > game.player.center['x']:
            self.direction = -1
    def update(self):
        if not game == None:
            if not game.paused:
                if self.health <= 0 and not self.dead:
                    self.dead = True
                    OrbExplosion((self.center['x'], self.center['y']))
                    self.sprite.remove()
                    game.enemies.remove(self)
                    square1.play(sfx_death1)
                    square2.play(sfx_death2)
                    triangle.stop()
                    noise.stop()
                self.sprite.visible = True
                index = 0
                if self.running:
                    if abs(self.target_x-self.center['x']) > tile_size*3:
                        self.velocity_x = self.run_speed * self.direction
                        self.run_timer += 1
                        if self.run_timer >= self.run_limit:
                            self.run_timer = 0
                            self.run_index += self.run_index_direction
                            if self.run_index <= 0:
                                self.run_index = 0
                                self.run_index_direction = 1
                            if self.run_index >= self.run_indexes-1:
                                self.run_index = self.run_indexes-1
                                self.run_index_direction = -1
                        index = self.index_run+self.run_index
                        if game.player.attacked:
                            self.turn()
                            if game.player.grounded:
                                self.jump()
                            else:
                                self.jump()
                    else:
                        self.turn()
                        self.jump('dash')
                if self.state == 'idle':
                    self.velocity_x = 0
                    index = self.index_idle
                    if not game.player.warping:
                        self.run()
                if self.state == 'shoot':
                    self.velocity_x = 0
                    self.velocity_y = 0
                    index = self.index_shoot_air+self.shoot_index
                    self.state_timer += 1
                    if self.reloading:
                        self.reload_timer += 1
                        self.shoot_index = 0
                        self.state_timer = 0
                        if self.reload_timer >= self.reload_limit:
                            self.reload_timer = 0
                            self.reloading = False
                            self.shots = 0
                    if not self.reloading or self.shoot_index > 0:
                        if self.state_timer >= self.timers['shoot']:
                            self.state_timer = 0
                            self.shoot_index += 1
                            if self.shoot_index > 2:
                                self.shoot_index = 0
                            if self.shoot_index == 1:
                                if self.shots < 3:
                                    self.shoot()
                                else:
                                    if self.rounds < 1:
                                        self.rounds += 1
                                        self.reloading = True
                                        self.shots = 0
                                        self.shot_index = 0
                                    else:
                                        self.rounds = 0
                                        self.state = 'dumb_fall'
                                        self.shots = 0
                                        self.shot_index = 0
                if self.state == 'land':
                    self.velocity_x = 0
                    index = self.index_land
                    self.state_timer += 1
                    if self.state_timer >= self.timers['land']:
                        self.state_timer = 0
                        if self.dash_fall:
                            self.turn()
                            self.jump('shoot')
                        elif self.jumping_forward:
                            self.turn()
                            self.jump('back')
                        elif self.last_dash:
                            self.last_dash = False
                            self.jump('shoot')
                        else:
                            self.run()
                        self.dash_fall = False
                        self.dumb_fall = False
                if self.state == 'jump_forward':
                    index = self.index_jump_forward
                    self.velocity_x = self.run_speed * self.direction
                    self.jumping_forward = True
                if self.state == 'jump_dash':
                    index = self.index_jump_back
                    self.velocity_x = self.run_speed/2 * -self.direction
                    self.jump_timer += 1
                    if self.jump_timer >= 42:
                        self.jump_timer = 0
                        self.turn()
                        self.dash()
                    self.jumping_forward = False
                if self.state == 'jump_shoot':
                    index = self.index_jump_back
                    self.jump_timer += 1
                    if self.jump_timer >= self.jump_shoot_limit:
                        self.jump_timer = 0
                        self.shoot()
                        self.turn()
                    self.jumping_forward = False
                if self.state == 'jump_back':
                    index = self.index_jump_back
                    self.velocity_x = self.run_speed * -self.direction
        ##            self.jump_timer += 1
        ##            if self.jump_timer >= self.jump_limit:
        ##                self.jump_timer = 0
        ##                self.state = 'dash'
        ##                self.turn()
                    self.jumping_forward = False
                if self.state == 'jump_bolt':
                    self.velocity_x = 0
                    index = self.index_bolt_jump
                    if self.sprite.y < 16:
                        self.sprite.y = 16
                        self.velocity_y = 0
                        self.state = 'bolt_charge'
                if self.state == 'bolt_charge':
                    index = self.index_bolt_charge+self.bolt_index
                    self.bolt_timer += 1
                    if self.bolt_timer >= self.bolt_limit:
                        self.bolt_timer = 0
                        self.bolt_index += 1
                        if self.bolt_index > 1:
                            self.bolt_index = 0
                            self.state = 'bolt'
                if self.state == 'bolt':
                    if self.bolt_index > 1:
                        index = self.index_bolt+1
                    else:
                        index = self.index_bolt+self.bolt_index
                    self.bolt_timer += 1
                    if self.bolt_timer >= self.bolt_limit:
                        self.bolt_timer = 0
                        self.bolt_index += 1
                        if self.bolt_index > 4:
                            self.bolt_index = 0
                            self.state = 'dumb_fall'
                if self.state == 'dash_fall':
                    index = self.index_jump_back
                    self.velocity_x = self.run_speed * self.direction
                    self.jumping_forward = False
                    self.dash_fall = True
                if self.state == 'dumb_fall':
                    index = self.index_jump_back
                    self.velocity_x = 0
                    self.jumping_forward = False
                    self.dumb_fall = True
                if self.state == 'dash':
                    index = self.index_dash
                    self.velocity_x = self.dash_speed * self.direction
                    self.dash_timer += 1
                    if self.dash_timer >= self.dash_limit:
                        self.dash_timer = 0
                        self.state = 'dash_fall'
                    self.jumping_forward = False
                if self.state == 'dash' or self.state == 'shoot' or self.state == 'bolt' or self.state == 'bolt_charge':
                    self.velocity_y = 0
                else:
                    self.velocity_y += self.gravity
                self.move(self.velocity_x, self.velocity_y)
                if self.state == 'idle':
                    self.turn()
                if self.center['x'] < 0 or self.center['x'] > screen_size[0]:
                    if not self.state == 'dash':
                        self.dash()
                    else:
                        self.state = 'dumb_fall'
                    self.turn()
                self.facing = self.direction
                self.sprite.flip_x = self.facing == 1
                self.sprite.subX = index*self.sprite.subWidth
class PauseMenu(object):
    def __init__(self):
        self.sprite = Sprite(0, 0, screen_size[0], screen_size[1], 0, 'menu')
        self.text_start_x = 56
        self.text_start_y = 42
        self.text_interval_x = 112
        self.text_interval_y = 20
        self.texts = []
        self.names = ['P.BUSTER', 'P.SHIELD', 'V.RUSH', 'D.SPIKE', 'V.DART', 'T.SLICER', '', '']
        index = 0
        for i in range(4):
            for j in range(2):
                x = self.text_start_x+self.text_interval_x*j
                y = self.text_start_y+self.text_interval_y*i
                text = ScreenText(x, y, self.names[index], 2)
                self.texts.append(text)
                for char in text.chars:
                    char.on_level = False
                index += 1
    def remove(self):
        for text in self.texts:
            text.remove()
        self.sprite.remove()
class Game(object):
    def __init__(self):
        global game
        game = self
        self.enemies = []
        self.pickups = []
        self.parser = {
            'm':{'index':0, 'solid':False, 'through':False, 'ladder':False},
            'h':{'index':0, 'solid':False, 'through':False, 'ladder':False},
            'O':{'index':0, 'solid':False, 'through':False, 'ladder':False},
            'V':{'index':0, 'solid':False, 'through':False, 'ladder':False},
            ' ':{'index':0, 'solid':False, 'through':False, 'ladder':False},
            '.':{'index':1, 'solid':False, 'through':False, 'ladder':False},
            ',':{'index':2, 'solid':False, 'through':False, 'ladder':False},
            '\'':{'index':3, 'solid':False, 'through':False, 'ladder':False},
            'F':{'index':4, 'solid':False, 'through':False, 'ladder':False},
            'E':{'index':5, 'solid':False, 'through':False, 'ladder':False},
            '#':{'index':6, 'solid':True, 'through':False, 'ladder':False},
            'H':{'index':7, 'solid':True, 'through':False, 'ladder':False},
            '=':{'index':8, 'solid':True, 'through':False, 'ladder':False},
            '|':{'index':9, 'solid':False, 'through':False, 'ladder':True},
            'T':{'index':9, 'solid':False, 'through':True, 'ladder':True},
        }
        self.rooms = []
        self.rooms.append([
            "......           ",
            ".'..             ",
            "..               ",
            ".                ",
            "                 ",
            "                 ",
            "                 ",
            "                 ",
            "..               ",
            "...              ",
            ".....            ",
            "..'....          ",
            "=================",
            "#######HHHH######",
            "HHH############HH",
        ])
        self.map = [
            "0",
        ]
        self.room_id = (0, 0)
        self.player = None
        self.parse(self.map)
        self.bounds = Rectangle(0, 0, len(self.map[0])*screen_size[0], len(self.map)*screen_size[1])
        self.rect = screen_rect
        self.rect_out = screen_rect
        fade(True, 2)
        square1.play(proto)
        square2.stop()
        triangle.stop()
        noise.stop()
        self.level_surface = pygame.Surface((self.bounds.right, self.bounds.bottom))
        self.level_x = self.room_id[0]*screen_size[0]
        self.level_y = self.room_id[1]*screen_size[1]
        self.scrolling = False
        self.blinks = 0
        self.blinks_max = 12
        self.blink_timer = 0
        self.blink_limit = 8
        self.blinking = True
        self.scroll_speed = 4
        self.scrolling = False
        self.scroll_direction_x = 0
        self.scroll_direction_y = 0
        self.refill_health = 0
        self.refill_timer = 0
        self.refill_limit = 2
        self.refilling = False
        self.refill_recipient = None
        self.paused = False
        self.pause_fade_speed = 2
        self.death_timer = 0
        self.death_limit = 150
        self.playing = False
        self.ready = ScreenText(108, 108, 'READY', 1)
    def parse(self, stage):
        global tiles
        for enemy in self.enemies:
            enemy.sprite.remove()
        self.enemies = []
        for pickup in self.pickups:
            pickup.sprite.remove()
        self.pickups = []
        for tile in tiles:
            tile.sprite.remove()
        tiles = []
        self.parse_cell(self.room_id[0], self.room_id[1], self.rooms[int(stage[self.room_id[1]][self.room_id[0]])])
    def parse_cell(self, cx, cy, cell):
        x = cx*screen_size[0]/tile_size
        y = cy*screen_size[1]/tile_size
        for row in cell:
            x = cx*screen_size[0]/tile_size
            for t in row:
                if x < cx*screen_size[0]/tile_size+screen_size[0]/tile_size+1:
                    tx = x*tile_size
                    ty = y*tile_size-8
                    tile = Tile(tx, ty, self.parser[t]['index'], 0, x, y, cx, cy, self.parser[t]['solid'], self.parser[t]['through'], self.parser[t]['ladder'])
                else:
                    break
                x += 1
            y += 1
    def pause(self):
        self.menu = PauseMenu()
        self.paused = True
        fade(True, self.pause_fade_speed)
    def unpause(self):
        self.menu.remove()
        self.paused = False
        fade(True, self.pause_fade_speed)
    def reset(self):
        self.level_x = 0
        square1.play(proto)
        square2.stop()
        triangle.stop()
        noise.stop()
        self.blinking = True
        self.parse(self.map)
        for sprite in sprites:
            sprite.visible = False
        for tile in tiles:
            tile.sprite.visible = True
        self.update_rect()
        fade(True, 2)
        self.playing = False
        redraw()
        self.refill_timer = 0
        self.refilling = False
        self.refill_recipient = None
    def pickup(self, pos):
        pickup_type = 'none'
        n = random.randint(1, 128)
        if n <= 1:
            pickup_type = 'life'
        elif n <= 6:
            pickup_type = 'energy_big'
        elif n <= 10:
            pickup_type = 'health_big'
        elif n <= 35:
            pickup_type = 'energy_small'
        elif n <= 50:
            pickup_type = 'health_small'
        if not pickup_type == 'none':
            self.pickups.append(Pickup(pos, True, pickup_type))
    def update_rect(self):
        self.rect = Rectangle(
            -self.level_x,
            0,
            -self.level_x+screen_size[0],
            screen_size[1]
        )
        self.rect_out = Rectangle(
            -self.level_x,
            0,
            -self.level_x+screen_size[0],
            screen_size[1]
        )
    def update(self):
        self.level_surface.fill(screen_color)
        if self.blinking:
            self.blink_timer += 1
            if self.blink_timer >= self.blink_limit:
                self.blink_timer = 0
                self.ready.phase(not self.ready.visible)
                if self.ready.visible:
                    self.blinks += 1
                    if self.blinks >= self.blinks_max:
                        self.blinks = 0
                        self.blinking = False
                        self.ready.remove()
                        self.player = Player((2+self.room_id[0]*screen_size[0]/tile_size, 11+self.room_id[1]*screen_size[1]/tile_size))
                        self.playing = True
                        self.enemies.append(Boss_Zeus((13, 11)))
        else:
            if not self.player == None:
                if not self.player.warping:
                    if keys[pygame.K_RETURN]:
                        if not last_keys[pygame.K_RETURN]:
                            if not fading:
                                if not self.paused:
                                    sfx2.play(sfx_menu)
                                    fade(False, self.pause_fade_speed)
                                else:
                                    sfx1.play(sfx_confirm1)
                                    sfx2.play(sfx_confirm2)
                                    fade(False, self.pause_fade_speed)
                if self.player.dead:
                    self.death_timer += 1
                    if self.death_timer >= self.death_limit:
                        self.death_timer = 0
                        self.player.health_bar.remove()
                        self.player.life_text.remove()
                        self.player.sprite.remove()
                        self.player = None
                        self.ready = ScreenText(108, 108, 'READY', 1)
                        fade(False, 2)

selectBG = Sprite(0, 0, 256, 224,  0, "background", 0, 0, 256, 224)

for i in range(7):
    Portrait(i, False)

text_press_start = ScreenText(80, 8, "PRESS  START", 1)
text_zeus = ScreenText(72, 64, "ZEUS", 1)
text_heracles = ScreenText(136, 64, "HERACLES", 1)
text_nessos = ScreenText(24, 128, "NESSOS", 1)
text_cronus = ScreenText(184, 128, "CRONUS", 1)
text = [text_press_start, text_zeus, text_heracles, text_nessos, text_cronus]

def pxarray_colors(pxarray):
    colors = []
    shape = pxarray.shape
    for i in range(shape[1]):
        for j in range(shape[0]):
            col = screen_surface.unmap_rgb(pxarray[j, i])
            if not col in colors:
                colors.append(col)
    return colors
def scale(new_scale):
    global screen_scale, screen_size_scaled, screen
    screen_scale = new_scale
    screen_size_scaled = (screen_size[0]*screen_scale, screen_size[1]*screen_scale)
    screen = pygame.display.set_mode(screen_size_scaled)

fade_color_table = [
[],
[(13,147,0),
 (56,135,0),
 (12,72,0),
 (0,0,0),
 (0,0,0),
 (86,29,0),
 (153,78,0),
 (234,158,34),
 (0,0,0),
 (0,0,0),
 (20,18,167),
 (0,0,0),
 (0,0,0),
 (86,29,0),
 (0,0,0),
 (0,0,0),
 (0,0,0,0),
 (0,0,0),
 (110,0,64),
 (59,0,164),
 (0,42,136),
 (173,173,173),
 (102,102,102),
 (0,0,0),
 (21,95,217), (66, 64, 255), (108,7,0), (153,78,0), (181,49,32), (234,158,34), (0,82,0)],
[(0,82,0), (12,72,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (86,29,0), (153,78,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (102,102,102), (0,0,0), (0,0,0), (0,42,136), (0,42,136), (0,0,0), (86,29,0), (108,7,0), (153,78,0), (0,0,0)],
[(0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (86,29,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (0,0,0), (86,29,0), (0,0,0)],
]
color_table = [
    (92,228,48),
    (136,216,0),
    (56,135,0),
    (12,72,0),
    (86,29,0),
    (153,78,0),
    (234,158,34),
    (228,229,148),
    (108,7,0),
    (20,18,167),
    (66,64,255),
    (59,0,164),
    (86,29,0),
    (153,78,0),
    (0,42,136),
    (102,102,102),
    (255,0,255,255),
    (110,0,64),
    (183,30,123),
    (117,39,254),
    (21,95,217),
    (255,255,255),
    (173,173,173),
    (0,0,0),
    (100,176,255),
    (146,144,255),
    (181,49,32),
    (234,158,34),
    (255,129,112),
    (247,216,165),
    (13,147,0)
]

fading = False
fade_timer = 0
fade_limit = 2
fade_index = 0
fade_type = 'out'

flashing = False
flash_timer = 0
flash_limit = 5
flashes = 0
flashes_limit = 4
flash_index = 0
def flash():
    global flashing, flash_timer, flashes, flash_index
    flashing = True
    flash_timer = 0
    flashes = 0
    flash_index = 1
def fade(type=False, limit=1):
    global fading, fade_type, fade_timer, fade_limit, fade_index
    fading = True
    fade_timer = 0
    fade_limit = limit
    if type == True:
        fade_index = 4
        fade_type = 'in'
    else:
        fade_index = 0
        fade_type = 'out'

def redraw():
    global sprites
    blits = 0
    screen.fill(screen_color)
    screen_surface.fill(screen_color)
    for rectangle in rectangles:
        pygame.draw.rect(screen_surface, (110,0,64), rectangle)
    spritesByDepths = [];
    for sprite in sprites:
        d = sprite.depth
        if d >= len(spritesByDepths):
            i = len(spritesByDepths)
            while i <= d:
                spritesByDepths.append([])
                i += 1
        spritesByDepths[d].append(sprite)
    sprites = []
    for i in range(len(spritesByDepths)):
            for j in range(len(spritesByDepths[i])):
                    sprites.append(spritesByDepths[i][j])
    for sprite in sprites:
        if sprite.visible:
            if sprite.type == 'surface':
                sprite.surface = sprites_map[sprite.path].convert().subsurface(sprite.subX, sprite.subY, sprite.subWidth, sprite.subHeight)
                sprite.surface = pygame.transform.flip(sprite.surface, sprite.flip_x, sprite.flip_y)
                sprite_surface = sprite.surface
                if len(sprite.color_list) > 0:
                    sprite_pxarray = pygame.PixelArray(sprite.surface)
                    for element in sprite.color_list:
                        try:
                            sprite_pxarray.replace(element[0], element[1])
                        except ValueError:
                            pass
                    sprite_surface = sprite_pxarray.make_surface().convert()
                if sprite.fade_index > 0:
                    sprite_pxarray = pygame.PixelArray(sprite.surface)
                    if sprite.fade_index < 4 and sprite.fade_index > 0:
                        for color in pxarray_colors(sprite_pxarray):
                            if not (color.r == 255 and color.g == 0 and color.b == 255):
                                try:
                                    sprite_pxarray.replace(color, fade_color_table[sprite.fade_index][color_table.index(color)])
                                except ValueError:
                                    print("ValueError encountered. Color at fault is "+str(color))
                                    sprite_pxarray.replace(color, (0, 0, 0))
                            else:
                                sprite_pxarray.replace(color, pygame.Color(255, 0, 255, 0))
                    if sprite.fade_index == 4:
                        for color in pxarray_colors(sprite_pxarray):
                            if not (color.r == 255 and color.g == 0 and color.b == 255):
                                sprite_pxarray.replace(color, (0, 0, 0))
                    sprite_surface = sprite_pxarray.make_surface().convert()
                sprite_surface.set_colorkey(colorkey)
                if not game == None and sprite.on_level:
                    if not game.paused:
                        game.level_surface.blit(sprite_surface, (sprite.x, sprite.y))
                else:
                    screen_surface.blit(sprite_surface, (sprite.x, sprite.y))
            elif sprite.type == 'rectangle':
                sprite_color = sprite.color
                if sprite.fade_index > 0:
                    sprite_pxarray = pygame.PixelArray(sprite.surface)
                    if sprite.fade_index < 4 and sprite.fade_index > 0:
                        try:
                            sprite_color = fade_color_table[sprite.fade_index][color_table.index(color)]
                        except ValueError:
                            print("ValueError encountered. Color at fault is "+str(color))
                            sprite_color = (0, 0, 0)
                    if sprite.fade_index == 4:
                        sprite_color = (0, 0, 0)
                pygame.draw.rect(screen_surface, sprite_color, sprite.rect)
    if not game == None:
        if not game.paused:
            screen_surface.blit(game.level_surface, (game.level_x, -game.level_y))
    screen_pxarray = pygame.PixelArray(screen_surface)
    if flash_index == 1:
        screen_pxarray.replace((0, 0, 0), (255, 255, 255))
    if fade_index < 4 and fade_index > 0:
        for color in pxarray_colors(screen_pxarray):
            try:
                screen_pxarray.replace(color, fade_color_table[fade_index][color_table.index(color)])
            except ValueError:
                print("ValueError encountered. Color at fault is "+str(color))
                screen_pxarray.replace(color, (0, 0, 0))
    if fade_index == 4:
        for color in pxarray_colors(screen_pxarray):
            screen_pxarray.replace(color, (0, 0, 0))
    screen.blit(pygame.transform.scale(screen_pxarray.make_surface(), screen_size_scaled), (0, 0))
    pygame.display.flip()

def pause():
    global paused, square1, square2, triangle, noise, sfx1, sfx2, sfx3, sfx4
    paused = True
    square1.pause()
    square2.pause()
    triangle.pause()
    noise.pause()
    sfx1.pause()
    sfx2.pause()
    sfx3.pause()
    sfx4.pause()
def unpause():
    global paused, square1, square2, triangle, noise, sfx1, sfx2, sfx3, sfx4
    paused = False
    square1.unpause()
    square2.unpause()
    triangle.unpause()
    noise.unpause()
    sfx1.unpause()
    sfx2.unpause()
    sfx3.unpause()
    sfx4.unpause()

paused = False
confirmed = False
fading = False
introducing = False
intro = False
state = 'select'
keys = pygame.key.get_pressed()
last_keys = keys
index = 3
last_index = index
portraits[index].selected = True
game_timer = 0
game_limit = 60
game = None
fps_fast = 240
fps_normal = 60
fps = fps_normal
interval = 1000
milliseconds = 0
time = interval
frames = 0
done = False
clock = pygame.time.Clock()
#screen_text = ScreenText(0, 0, "FPS: "+str(fps)+".00", True)
redraw()
while not done:
    milliseconds = clock.tick(fps)
    #if not screen_text == None:
        #screen_text.remove()
    #screen_text = ScreenText(0, 0, "", True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.ACTIVEEVENT:
            if event.state == 2:
                pause()
            if event.state == 6:
                unpause()
        if event.type == square1_END:
            if not game == None:
                print("play some music!")
                if not intro:
                    intro = True
                    square1.play(boss_battle_intro1)
                    square2.play(boss_battle_intro2)
                    triangle.play(boss_battle_intro3)
                    noise.play(boss_battle_intro4)
                elif game.player != None and not game.player.dead and len(game.enemies) != 0:
                    square1.play(boss_battle1, -1)
                    square2.play(boss_battle2, -1)
                    triangle.play(boss_battle3, -1)
                    noise.play(boss_battle4, -1)
        if event.type == sfx1_END:
            if confirmed and game == None:
                square1.play(boss_intro1)
                square2.play(boss_intro2)
                triangle.play(boss_intro3)
                noise.play(boss_intro4)
            square1.set_volume(1)
        if event.type == sfx2_END:
            square2.set_volume(1)
        if event.type == sfx3_END:
            triangle.set_volume(1)
        if event.type == sfx4_END:
            noise.set_volume(1)
    time += 1/60
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RSHIFT]:
        fps = fps_fast
    else:
        fps = fps_normal
    if not paused:
        if fading:
            fade_timer += 1
            if fade_timer >= fade_limit:
                fade_timer = 0
                if fade_type == 'out':
                    fade_index += 1
                    if fade_index > 4:
                        fade_index = 0
                        fading = False
                        if state == 'select':
                            for portrait in portraits:
                                portrait.surface_face.remove()
                                portrait.remove()
                            for t in text:
                                t.remove()
                            introducing = True
                            selectBG.remove()
                            boss_intro = BossIntro()
                            state = 'intro'
                        elif state == 'intro':
                            boss_intro.remove()
                            state = 'game'
                        elif state == 'game':
                            if not game.player == None:
                                if not game.paused:
                                    game.pause()
                                else:
                                    game.unpause()
                            else:
                                game.reset()
                elif fade_type == 'in':
                    fade_index -= 1
                    if fade_index < 0:
                        fade_index = 0
                        fading = False
                redraw()
        if state == 'game':
            if not game == None:
                game.update()
        if not fading:
            if state == 'game':
                if game == None:
                    game_timer += 1
                    if game_timer >= game_limit:
                        Game()
                        game_timer = 0
            if flashing:
                flash_timer += 1
                if flash_timer >= flash_limit:
                    flash_timer = 0
                    if flash_index == 0:
                        flashes += 1
                    flash_index += 1
                    if flash_index > 1:
                        flash_index = 0
                    if flashes >= flashes_limit:
                        flashes = 0
                        flash_index = 0
                        flashing = False
            if not (not game == None and game.refilling):
                if confirmed and not flashing and not fading and state == 'select':
                    fade()
                elif not confirmed:
                    if keys[pygame.K_LEFT]:
                        if not last_keys[pygame.K_LEFT]:
                            index -= 1
                    if keys[pygame.K_RIGHT]:
                        if not last_keys[pygame.K_RIGHT]:
                            index += 1
                    if keys[pygame.K_UP]:
                        if not last_keys[pygame.K_UP]:
                            if index == 0:
                                index = 5
                            elif index == 1:
                                index = 6
                            elif index == 2:
                                index = 0
                            elif index == 3:
                                index = 0
                            elif index == 4:
                                index = 1
                            elif index == 5:
                                index = 2
                            elif index == 6:
                                index = 4
                    if keys[pygame.K_DOWN]:
                        if not last_keys[pygame.K_DOWN]:
                            if index == 0:
                                index = 2
                            elif index == 1:
                                index = 4
                            elif index == 2:
                                index = 5
                            elif index == 3:
                                index = 6
                            elif index == 4:
                                index = 6
                            elif index == 5:
                                index = 0
                            elif index == 6:
                                index = 1
                    while index < 0:
                        index += 7
                    while index > 6:
                        index -= 7
                    if not index == last_index:
                        if not sfx2.get_sound() == sfx_life:
                            sfx2.play(sfx_select)
                        portraits[index].subX = portraits[index].width
                        portraits[index].selected = True
                        portraits[last_index].selected = False
                    if keys[pygame.K_RETURN]:
                        if not last_keys[pygame.K_RETURN]:
                            sfx1.play(sfx_confirm1)
                            if not sfx2.get_sound() == sfx_life:
                                sfx2.play(sfx_confirm2)
                            confirmed = True
                            flash()
                if keys[pygame.K_LALT]:
                    if keys[pygame.K_1]:
                        scale(1)
                    if keys[pygame.K_2]:
                        scale(2)
                    if keys[pygame.K_3]:
                        scale(3)
                    if keys[pygame.K_4]:
                        scale(4)
                if sfx1.get_busy() or muted1 or muted:
                    square1.set_volume(0)
                if sfx2.get_busy() or muted2 or muted:
                    square2.set_volume(0)
                if sfx3.get_busy() or muted3 or muted:
                    triangle.set_volume(0)
                if sfx4.get_busy() or muted4 or muted:
                    noise.set_volume(0)
                for sprite in updates:
                    sprite.update()
                for sprite in rectangles:
                    sprite.update()
                if not game == None:
                    if not game.player == None:
                        game.level_x = -game.player.center['x']+screen_size[0]/2
                        if game.level_x > 0:
                            game.level_x = 0
                        if game.level_x < -game.bounds.right+screen_size[0]:
                            game.level_x = -game.bounds.right+screen_size[0]
                        game.update_rect()
                        game.player.health_bar.sprite.x = -game.level_x + game.player.health_bar.offset_x
                        game.player.health_bar.update()
                        game.player.life_text.move(-game.level_x+game.player.health_bar.offset_x, game.player.health_bar.sprite.y+game.player.health_bar.sprite.height)
                       # screen_text.move(-game.level_x, 0)
                if not fading:
                    redraw()
                last_index = index
            elif not game == None and game.refilling:
                if game.refill_health > game.refill_recipient.health_max:
                    game.refill_health = game.refill_recipient.health_max
                game.refill_timer += 1
                if game.refill_timer >= game.refill_limit:
                    game.refill_timer = 0
                    game.refill_recipient.health += 1
                    if game.refill_recipient.health > game.refill_health:
                        game.refilling = False
                    else:
                        sfx1.play(sfx_health1)
                        if not sfx2.get_sound() == sfx_life:
                            sfx2.play(sfx_health2)
                    game.refill_recipient.health_bar.update_ticks(game.refill_recipient.health)
                    game.level_x = -game.player.center['x']+screen_size[0]/2
                    if game.level_x > 0:
                        game.level_x = 0
                    if game.level_x < -game.bounds.right+screen_size[0]:
                        game.level_x = -game.bounds.right+screen_size[0]
                    game.update_rect()
                    #screen_text.move(-game.level_x, 0)
                    redraw()
    last_keys = keys
pygame.display.quit()
pygame.mixer.quit();
pygame.quit();
sys.exit()
