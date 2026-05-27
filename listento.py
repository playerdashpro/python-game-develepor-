import pgzrun

WIDTH = 640
height= 680
cell_size = 80

levels = [
    
       [ 0, 0, 1, 0, 0, 0, 1, 0],
[1, 0, 1, 0, 1, 0, 1, 0],
[1, 0, 0,0, 1, 0, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1, 0, 1, 0],
[0, 0, 0, 0, 1, 0, 0, 0],
[1, 1, 1, 0, 1, 1, 1, 2],
],
[


[0, 1, 0, 0, 0, 1, 0, 0],
[0, 1, 0, 1, 0, 1, 0, 1],
[0, 0, 0, 1, 0, 0, 0, 1],
[1, 1, 0, 1, 1, 1, 0, 1],
[0, 0, 0, 0, 0, 1, 0, 0],
[0, 1, 1, 1, 0, 1, 1, 0],
[0, 0, 0, 1, 0, 0, 0, 0],
[1, 1, 0, 0, 1, 1, 1, 2],

],
[

[0, 0, 0, 1, 0, 0, 0, 0],
[1, 1, 0, 1, 0, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[0, 1, 1, 1, 1,
0, 1,0],
[0, 1, 0, 0, 0, 0, 0, 0],
[0, 1, 0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0, 1, 0],
[1, 1, 1, 1, 1, 0, 0, 2],

],
current_level = 0
maze = levels[current_level]

player_row = 0
player_col = 0

game_won = False

player = Actor("grasses")

def draw():
    screen.fill((30, 30, 40))

    for i in range():

        for j in range(8):

            x = j * cell_size
            y = i * cell_size
            rect = Rect((x, y), (cell_size, cell_size))

            if maze[i][j] == 1:
                screen.draw.filled_rect(rect, (0, 150, 140))
            else:
                screen.draw.filled_rect(rect, (255, 248, 220))

            screen.draw.rect(rect, (200, 200, 200))

            if maze[i][j] == 2:

              screen.draw.filled_rect(rect, (255, 215, 0))

              screen.draw.text(
               "GOAL",
               center=(x + 40, y + 40),
               fontsize=24,
               color="black"
              )

    screen.draw.text(
        "LEVEL " + str(current_level + 1),
        topleft=(10, 10),
        fontsize=35,
        color="white"
    )
    player.pos = (
        player_col * cell_size + cell_size // 2,
        player_row * cell_size + cell_size // 2
    )
    player.draw()

    if game_won:
        screen.draw.text(
            "YOU WIN!",
            center=(WIDTH // 2, height // 2),
            fontsize=80,
            color="yellow"
        )
def on_key_down(key):
    global player_row
    global player_col
    global game_won
    global maze
    global current_level

    if game_won:
        return
    
    new_row = player_row
    new_col = player_col

    if key == keys.UP:
        new_row -= 1
    elif key == keys.DOWN:
        new_row += 1

    elif key == keys.LEFT:
        new_col -= 1
    elif key == keys.RIGHT:
        new_col += 1
    if 0 <= new_row < 8 and 0 <= new_col < 8:
        if maze[new_row][new_col] != 1:
            player_row = new_row
            player_col = new_col

        if maze[player_row][player_col] == 2:
            current_level += 1
            if current_level < len(levels):
                maze = levels[current_level]
                player_row = 0
                player_col = 0
            else:
                game_won = True
pgzrun.go()