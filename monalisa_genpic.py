from PIL import Image, ImageDraw, ImageFilter
import random

# Create a blank canvas
canvas_width = 800
canvas_height = 1000
canvas = Image.new('RGB', (canvas_width, canvas_height), 'white')
draw = ImageDraw.Draw(canvas)

# Define colors
colors = [
    (255, 240, 192),  # Light skin tone
    (162, 115, 89),   # Dark skin tone
    (42, 48, 103),    # Dark blue
    (242, 166, 115),  # Light orange
    (29, 112, 55),    # Dark green
    (255, 255, 255),  # White
    (0, 0, 0)         # Black
]

# Draw face
face_color = random.choice([0, 1])
draw.rectangle([(200, 200), (600, 700)], fill=colors[face_color])

# Draw eyes
eye_color = random.choice([5, 6])
draw.ellipse([(300, 300), (350, 350)], fill=colors[eye_color])
draw.ellipse([(450, 300), (500, 350)], fill=colors[eye_color])

# Draw mouth
mouth_color = random.choice([0, 1])
draw.arc([(300, 450), (500, 550)], start=30, end=150, fill=colors[mouth_color])

# Display the image
canvas.show()
