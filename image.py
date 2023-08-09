from PIL import Image, ImageDraw

# Canvas dimensions
canvas_width, canvas_height = 1280, 600

# Create a new canvas
canvas = Image.new("RGB", (canvas_width, canvas_height), "black")
draw = ImageDraw.Draw(canvas)

# Building dimensions
building_width, building_height = 400, 400
building_x = (canvas_width - building_width) //2
building_y = (canvas_height - building_height) // 2

# Draw the building
building_color = "lightgray"
building_coords = [(building_x, building_y), (building_x + building_width, building_y + building_height)]
draw.rectangle(building_coords, outline=building_color, width=2, fill=building_color)

# Window dimensions
window_color = "blue"
window_width, window_height = 40, 60
window_spacing_x, window_spacing_y = 30, 20
num_windows_horizontal, num_windows_vertical = 4, 4

# Calculate starting position for windows
start_x = building_x + (building_width - (num_windows_horizontal * (window_width + window_spacing_x) - window_spacing_x)) // 2
start_y = building_y + (building_height - (num_windows_vertical * (window_height + window_spacing_y) - window_spacing_y)) // 2

# Draw windows
for i in range(num_windows_horizontal):
    for j in range(num_windows_vertical):
        x = start_x + i * (window_width + window_spacing_x)
        y = start_y + j * (window_height + window_spacing_y)
        draw.rectangle([(x, y), (x + window_width, y + window_height)], outline=window_color, width=2, fill=window_color)

# Save the centered building with windows
canvas.save("centered_building_with_windows.png")
