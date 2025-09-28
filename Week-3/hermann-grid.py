# hermann-grid.py
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK

def hermann_grid(rows, cols,
                 square_size,          
                 spacing,              
                 square_color=C_BLACK,
                 bg_color=C_WHITE):

    control.set_develop_mode(True)

    exp = design.Experiment(name="Hermann Grid", background_colour=bg_color)
    control.initialize(exp)

    screen_w, screen_h = exp.screen.size
    
    #If square_size is written as fraction (<1), convert it into pixels    
    if square_size < 1:
        square_size = int(min(screen_w, screen_h) * square_size)
        square_size = int(square_size)
        spacing = int(spacing)

    #squares + spacing between them
    grid_w = cols * square_size + (cols - 1) * spacing
    grid_h = rows * square_size + (rows - 1) * spacing

    #starting coordinates for displaying the grid at the center of the screen
    start_x = -grid_w // 2 + square_size // 2
    start_y = -grid_h // 2 + square_size // 2

    control.start(subject_id=1)
    exp.screen.clear()

    #Draw squares
    for i in range(rows):       
        for j in range(cols):   
            cx = start_x + j * (square_size + spacing)
            cy = start_y + i * (square_size + spacing)
            rect = stimuli.Rectangle(size=(square_size, square_size),
                                     colour=square_color,
                                     position=(cx, cy))
            rect.present(clear=False, update=False)

    exp.screen.update()
    exp.keyboard.wait()
    control.end()

hermann_grid(rows=5, cols=5, square_size=0.1, spacing=15 , square_color=C_BLACK, bg_color=C_WHITE)
