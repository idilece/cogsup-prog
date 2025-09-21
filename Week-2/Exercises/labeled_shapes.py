from expyriment import design, control, stimuli
from expyriment.misc import geometry
import math

# Create an object of class Experiment
exp = design.Experiment("Triangle and hexagon")

# Start experiment
control.initialize(exp)

def polygon_generating_function(sides, radius, colour, position):
    return stimuli.Shape(
        vertex_list = geometry.vertices_regular_polygon(sides, radius),
        colour=colour,
        position=position
    )

#side length in regular polygons: 2R*sin(pi/n)
#drawing the triangle (R=side/sqrt(3))
triangle = polygon_generating_function(3, 50, (128, 0, 128), (-150, 0)) #radius = side length / sqrt(3)

#drawing the hexagon
Radius_hexagon = 50 / math.sqrt(3) #h of hexagon = radius
hexagon = polygon_generating_function(6, Radius_hexagon, (255, 255, 0), (150, 0))

#labels
label_triangle = stimuli.TextLine("triangle", text_colour=(255, 255, 255))
label_hexagon = stimuli.TextLine("hexagon", text_colour=(255, 255, 255))
label_triangle.position = (-150, 100)
label_hexagon.position = (150, 100)

# the vertical lines
line1 = stimuli.Line((0, -25), (0, 25), line_width=3, colour=(255, 255, 255))
line2 = stimuli.Line((0, -25), (0, 25), line_width=3, colour=(255, 255, 255))
line1.position = (-150, 50)
line2.position = (150, 50)

# Start experiment
control.start(subject_id=1)

# present elements (shapes, lines, labels)
triangle.present(clear=True, update=False)
hexagon.present(clear=False, update=False)
line1.present(clear=False, update=False)
line2.present(clear=False, update=False)
label_triangle.present(clear=False, update=False)
label_hexagon.present(clear=False, update=True)

exp.keyboard.wait()
control.end()
