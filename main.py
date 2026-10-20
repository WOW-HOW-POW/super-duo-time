def on_player2_button_b_pressed():
    global Blue_ray
    if Dire_2 == 1:
        Blue_ray = sprites.create(assets.image("""
            Blue2
            """), SpriteKind.projectile)
        Blue_ray.set_position(P2.x, P2.y)
        for index in range(20):
            pause(15)
            Blue_ray.x += -2
        sprites.destroy(Blue_ray)
    elif Dire_2 == 2:
        Blue_ray = sprites.create(assets.image("""
            Blue
            """), SpriteKind.projectile)
        Blue_ray.set_position(P2.x, P2.y)
        for index2 in range(20):
            pause(15)
            Blue_ray.x += 2
        sprites.destroy(Blue_ray)
controller.player2.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player2_button_b_pressed)

def on_player1_button_up_pressed():
    controller.player1.move_sprite(P1, 0, 0)
controller.player1.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player1_button_up_pressed)

def on_player2_button_a_pressed():
    for index3 in range(20):
        pause(15)
        P2.y += -2
    for index4 in range(20):
        pause(15)
        P2.y += 2
controller.player2.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player2_button_a_pressed)

def on_player2_button_down_pressed():
    controller.player2.move_sprite(P2, 0, 0)
controller.player2.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player2_button_down_pressed)

def on_player2_button_up_pressed():
    controller.player2.move_sprite(P2, 0, 0)
controller.player2.on_button_event(ControllerButton.UP,
    ControllerButtonEvent.PRESSED,
    on_player2_button_up_pressed)

def on_player2_button_right_pressed():
    global Dire_2
    controller.player2.move_sprite(P2)
    Dire_2 = 2
    if controller.player2.is_pressed(ControllerButton.UP):
        controller.player2.move_sprite(P2, 0, 0)
    if controller.player2.is_pressed(ControllerButton.DOWN):
        controller.player2.move_sprite(P2, 0, 0)
controller.player2.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_right_pressed)

def on_player2_button_left_pressed():
    global Dire_2
    controller.player2.move_sprite(P2)
    Dire_2 = 1
    if controller.player2.is_pressed(ControllerButton.UP):
        controller.player2.move_sprite(P2, 0, 0)
    if controller.player2.is_pressed(ControllerButton.DOWN):
        controller.player2.move_sprite(P2, 0, 0)
controller.player2.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player2_button_left_pressed)

def on_player1_button_right_pressed():
    global Dire_1
    controller.player1.move_sprite(P1)
    Dire_1 = 2
    if controller.player1.is_pressed(ControllerButton.UP):
        controller.player1.move_sprite(P1, 0, 0)
    if controller.player1.is_pressed(ControllerButton.DOWN):
        controller.player1.move_sprite(P1, 0, 0)
controller.player1.on_button_event(ControllerButton.RIGHT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_right_pressed)

def on_player1_button_a_pressed():
    for index5 in range(20):
        pause(15)
        P1.y += -2
    for index6 in range(20):
        pause(15)
        P1.y += 2
controller.player1.on_button_event(ControllerButton.A,
    ControllerButtonEvent.PRESSED,
    on_player1_button_a_pressed)

def on_player1_button_b_pressed():
    global Blue_ray
    if Dire_1 == 1:
        Blue_ray = sprites.create(assets.image("""
            Blue2
            """), SpriteKind.projectile)
        Blue_ray.set_position(P1.x, P1.y)
        for index7 in range(20):
            pause(15)
            Blue_ray.x += -2
        sprites.destroy(Blue_ray)
    elif Dire_1 == 2:
        Blue_ray = sprites.create(assets.image("""
            Blue
            """), SpriteKind.projectile)
        Blue_ray.set_position(P1.x, P1.y)
        for index8 in range(20):
            pause(15)
            Blue_ray.x += 2
        sprites.destroy(Blue_ray)
controller.player1.on_button_event(ControllerButton.B,
    ControllerButtonEvent.PRESSED,
    on_player1_button_b_pressed)

def on_player1_button_left_pressed():
    global Dire_1
    controller.player1.move_sprite(P1)
    Dire_1 = 1
    if controller.player1.is_pressed(ControllerButton.UP):
        controller.player1.move_sprite(P1, 0, 0)
    if controller.player1.is_pressed(ControllerButton.DOWN):
        controller.player1.move_sprite(P1, 0, 0)
controller.player1.on_button_event(ControllerButton.LEFT,
    ControllerButtonEvent.PRESSED,
    on_player1_button_left_pressed)

def on_player1_button_down_pressed():
    controller.player1.move_sprite(P1, 0, 0)
controller.player1.on_button_event(ControllerButton.DOWN,
    ControllerButtonEvent.PRESSED,
    on_player1_button_down_pressed)

Dire_1 = 0
Blue_ray: Sprite = None
Dire_2 = 0
P2: Sprite = None
P1: Sprite = None
scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    Map
    """))
P1 = sprites.create(assets.image("""
    myImage
    """), SpriteKind.player)
tiles.place_on_tile(P1, tiles.get_tile_location(1, 6))
P2 = sprites.create(assets.image("""
    myImage0
    """), SpriteKind.player)
tiles.place_on_tile(P2, tiles.get_tile_location(2, 6))
scene.camera_follow_sprite(P1)