# Extract Read-Only Embedded PDF

Automatically takes screenshots of PDF pages and converts them to a high-quality PDF book.

## Installation

1. Clone this repository
2. Install requirements:
```bash
pip install -r requirements.txt
```

## Configuration

Edit the variables at the top of `main.py`:

```python
# File paths
save_dir = r"C:\Users\YourName\Desktop\screenshots"
output_pdf = r"C:\Users\YourName\Desktop\output.pdf"

# Screenshot region position, See below how to obtain position
left = 596         # X1
top = 164          # Y1
right = 1311       # X2
bottom = 1150      # Y2

# Next button position (where to click)
next_button_x = 864
next_button_y = 1114

# Timing settings (in seconds)
delay_between_pages = 0.5
startup_delay = 3
```

### How to find position (coordinates):

1. **Screenshot region**: Open python interactive shell:
```python
import pyautogui
pyautogui.displayMousePosition()
```
2. Now you'll be able to see the coordinates of the mouse in the python shell
3. Move your mouse to the top-left corner of the area you want to capture → Note: X1, Y1
4. Then move it to the bottom-right corner → Note: X2, Y2
5. Set the left, top, right, bottom variables above
6. Press `Ctrl+C` to stop the coordinate display

**For next button:**
1. Hover over the "Next" button → note `next_button_x` and `next_button_y`

## Usage

1. Open your PDF
2. Edit the configuration variables at the top of `main.py`
3. Run the script:
```bash
python main.py
```
4. Enter number of pages when prompted
5. Focus your PDF viewer window within 3 seconds
6. The script will automatically screenshot each page and create a PDF

## Features

- **High-quality screenshots** using MSS library
- **Lossless PDF creation** with img2pdf
- **Configurable regions** and timing
- **Automatic page navigation**

## Notes

- Make sure your PDF viewer window is focused and visible
- Test with a few pages first to ensure coordinates are correct
- The script will create the output directory if it doesn't exist
