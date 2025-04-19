from rembg import remove
from PIL import Image

input_path = "programmer.jpg"
output_path = "programmer.png"
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
