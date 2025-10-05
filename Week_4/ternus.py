from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_BLACK, C_WHITE, C_RED, C_YELLOW, C_BLUE

def load(stims):
    for stim in stims:
        stim.preload()

frame_time = 1000.0 / 60.0

def present_for(stims, canvas, frames=12):
    canvas.clear_surface()
    t0 = exp.clock.time
    for stim in stims:
        stim.plot(canvas)
    canvas.present()
    draw_dt = exp.clock.time - t0
    exp.clock.wait(max(0, int(round(frames * frame_time)) - draw_dt))

def make_circles(radius, positions, colour=C_WHITE):
    circles = []
    for pos in positions:
        c = stimuli.Circle(radius=radius, colour=colour, position=(pos, 0))
        circles.append(c)
    return circles

def add_tags(circles, tag_colours):
    tag_small_circle = max(4, int(circles[0].radius * 0.25))
    for i in range(len(circles)):
        col = tag_colours[i % len(tag_colours)]
        big = circles[i]
        tag = stimuli.Circle(radius=tag_small_circle, colour=col, position=(0, 0))
        tag.plot(big) 
    load(circles)

def run_trial(radius=50, isi_frames=9, with_tags=False, display_frames=12, canvas=None):
    step = int(radius * 2.5)
    A = make_circles(radius, [-step, 0, step],colour=C_WHITE) 
    B = make_circles(radius, [0, step, 2*step],colour=C_WHITE) 

    if with_tags:
        add_tags(A, [C_YELLOW, C_RED, C_BLUE])
        add_tags(B, [C_RED, C_BLUE, C_YELLOW])
    else:
        load(A + B)

    blank_time = int(round(isi_frames * frame_time))

    while True:
        present_for(A, canvas, frames=display_frames)
        if isi_frames > 0:
            canvas.clear_surface(); canvas.present()
            exp.clock.wait(blank_time)
        present_for(B, canvas, frames=display_frames)
        
        if isi_frames > 0:
            canvas.clear_surface(); canvas.present()
            exp.clock.wait(blank_time)
            
        if exp.keyboard.check(K_SPACE):
            exp.keyboard.clear()
            break

exp = design.Experiment("Ternus illusion")
control.set_develop_mode(True)
control.initialize(exp)

canvas = stimuli.Canvas(size=exp.screen.size, colour=C_BLACK)
canvas.present()

exp.keyboard.wait([K_SPACE])
exp.keyboard.clear()

# 1) Element motion (low ISI)
run_trial(radius=50, isi_frames=1,  with_tags=False, display_frames=12, canvas=canvas)

# 2) Group motion (high ISI)
run_trial(radius=50, isi_frames=18, with_tags=False, display_frames=12, canvas=canvas)

# 3) Element motion (high ISI + color tags)
run_trial(radius=50, isi_frames=18, with_tags=True, display_frames=12, canvas=canvas)

control.end()