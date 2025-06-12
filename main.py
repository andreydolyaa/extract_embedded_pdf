import pyautogui
import os
import time
from PIL import Image
import mss
import img2pdf

# ================================
# USER CONFIGURATION - EDIT THESE
# ================================

# File paths
save_dir = r"C:\Users\John\Desktop\pdf_extract\screenshots"
output_pdf = r"C:\Users\John\Desktop\pdf_extract\output.pdf"

# Screenshot region coordinates
left = 596
top = 164
right = 1311
bottom = 1150

# Next button position (where to click)
next_button_x = 864
next_button_y = 1114

# Timing settings (in seconds)
delay_between_pages = 0.5
startup_delay = 3

# ================================
# DO NOT EDIT BELOW THIS LINE
# ================================

os.makedirs(save_dir, exist_ok=True)

width = right - left
height = bottom - top
screenshot_region = {"left": left, "top": top, "width": width, "height": height}
next_button_pos = (next_button_x, next_button_y)

def get_next_filename():
    i = 1
    while os.path.exists(os.path.join(save_dir, f"{i:03}.png")):
        i += 1
    return os.path.join(save_dir, f"{i:03}.png")

num_pages = int(input("How many pages to capture? "))

print(f"Starting in {startup_delay} seconds... focus the PDF viewer window")
time.sleep(startup_delay)

with mss.mss() as sct:
    for page in range(num_pages):
        filename = get_next_filename()
        screenshot = sct.grab(screenshot_region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        img.save(filename, "PNG")
        print(f"Saved {filename}")
        
        if page < num_pages - 1:
            pyautogui.moveTo(next_button_pos)
            pyautogui.click()
            time.sleep(delay_between_pages)

print("Creating PDF...")

images = [f for f in os.listdir(save_dir) if f.endswith(".png")]
images.sort()

if not images:
    print("No images found to create PDF.")
    exit()

image_paths = [os.path.join(save_dir, img) for img in images]

with open(output_pdf, "wb") as f:
    f.write(img2pdf.convert(image_paths))

print(f"PDF created successfully: {output_pdf}")