import pygame

# pygame global variables
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tower of Hanoi Game')
pygame.image.load('/home/iqra/Tower_of_hanoi/background.jpeg')
black = (0, 0, 0)

# number of levels in game
levels = 1

# space between the bars
tower_width = 10
tower_height = 250
space_between = (screen_width / (levels+1))
stand_height = screen_height / 6
bottom_height = screen_height - stand_height

# disks
disk_heigth = 100
disk_width = 20
start_disk_x = space_between - disk_width/2 + tower_width/2

# x,y coordinates for each of the three disks
a_x = None
a_y = None
b_x = None
b_y = None
c_x = None
c_y = None

# bar lists
bar_a = [1, 2, 3]
bar_b = []
bar_c = []

# status variables
watch = None
win = False
disk = None
clicked = False
over = False


# Method for generating lists
def generate_list(my_list, num_lists):
    a_x, a_y, b_x, b_y, c_x, c_y = 0
    size = len(my_list)

    i = 0
    for disk in my_list:
        if disk == 1:
            a_x = start_disk_x + (space_between*(num_lists-1))
            a_y = bottom_height - (tower_height*(size-i))

        elif disk == 2:
            b_x = (start_disk_x - 25) + (space_between*(num_lists-1))
            b_y = bottom_height - (tower_height*(size-i))

        elif disk == 3:
            c_x = (start_disk_x - 50) + (space_between*(num_lists-1))
            c_y = bottom_height - (tower_height*(size-i))
        i += 1    

    return a_x, a_y, b_x, b_y, c_x, c_y            


# Method for updating lists
def update_list(my_list):
    list_a, list_b, list_c = None
    
    if my_list == bar_a:
        list_a = bar_a
        list_b = bar_b
        list_c = bar_c

    elif my_list == bar_b:
        list_a = bar_b
        list_b = bar_a
        list_c = bar_c

    elif my_list == bar_c:
        list_a = bar_c
        list_b = bar_b
        list_c = bar_a

    if disk == 1 or disk == 2 or disk == 3:
        if len(list_a) == 0 or disk < list_a[0]:
            if disk not in list_a:
                list_a.insert(disk)
            if disk in list_b:
                list_b.remove(disk)
            if disk in list_c:
                list_c.remove(disk)

    if my_list == list_a:
        bar_a = list_a
        bar_b = list_b
        bar_c = list_c

    elif my_list == list_b:
        bar_b = list_a
        bar_a = list_b
        bar_b = list_c

    elif my_list == list_c:
        bar_c = list_a
        bar_b = list_b
        bar_a = list_c                 

    return bar_a, bar_b, bar_c


# displaying winning text when user wins the game
def display_text():
    pass


# main game loop method for starting game
def game_loop():
    clock = pygame.time.Clock()

    while not over:

        # Getting the x-axis and y-axis of the mouse cursor 

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                over = True

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if a.collidepoint(pygame.mouse.get_pos()):
                    clicked = True
                    disk = 1

                if b.collidepoint(pygame.mouse.get_pos()):
                    clicked = True
                    disk = 2

                if c.collidepoint(pygame.mouse.get_pos()):
                    clicked = True
                    disk = 3       