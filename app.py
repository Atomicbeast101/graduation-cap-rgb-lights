# Imports
import threading
import neopixel
import random
import flask
import board
import time

# Attributes
LED_SIZE = 51
SNAKE_SIZE = 5
SKIPPER_SIZE = 10
PIXELS = neopixel.NeoPixel(board.D18, LED_SIZE, brightness=0.4, auto_write=False)
rainbow_colors = [
    (148, 0, 211), # purple
    (0, 0, 255), # blue
    (0, 255, 0), # green
    (255, 255, 0), # yellow
    (255, 0, 0), # red
]
app = flask.Flask(__name__)
current_thread = None

# Class
class ColorRunner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.kill = threading.Event()

    def run(self):
        print('Launching program...')
        while not self.kill.is_set():
            print('Executing snake()')
            snake()
            if self.kill.is_set() : return
            print('Executing skipper()')
            skipper()
            if self.kill.is_set() : return
            print('Executing loading()')
            loading()
            if self.kill.is_set() : return
            print('Executing picker()')
            picker()
            if self.kill.is_set() : return
            print('Executing rit()')
            rit()
            if self.kill.is_set() : return
            print('Executing down_up()')
            down_up()
            if self.kill.is_set() : return
            print('Executing yt_loading()')
            yt_loading()
            if self.kill.is_set() : return
            print('Executing rainbow()')
            rainbow()
            if self.kill.is_set() : return
            print('Executing rotate()')
            rotate()
            if self.kill.is_set() : return

# Functions
def snake():
    for color in rainbow_colors:
        place = 0
        while place < LED_SIZE + SNAKE_SIZE:
            for i in range(0, SNAKE_SIZE):
                if place - i >= 0:
                    if place < LED_SIZE:
                        PIXELS[place - i] = color
            if place - SNAKE_SIZE >= 0:
                PIXELS[place - SNAKE_SIZE] = (0, 0, 0)
            PIXELS.show()
            place += 1
            time.sleep(.03)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def skipper():
    for color in rainbow_colors:
        count = 0
        step = 0
        while count < SKIPPER_SIZE:
            PIXELS.fill((0, 0, 0))
            PIXELS.show()
            if step == 0:
                for place in range(0, LED_SIZE, 2):
                    PIXELS[place] = color
                step = 1
            else:
                for place in range(1, LED_SIZE, 2):
                    PIXELS[place] = color
                step = 0
            PIXELS.show()
            count += 1
            time.sleep(0.04)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def loading():
    for color in rainbow_colors:
        PIXELS.fill((0, 0, 0))
        PIXELS.show()
        for place in range(0, LED_SIZE):
            PIXELS[place] = color
            time.sleep(0.02)
            PIXELS.show()
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def picker():
    places = list(range(0, LED_SIZE))
    random.shuffle(places)
    colors = []
    for place in places:
        ran_color = random.choice(rainbow_colors)
        PIXELS[place] = ran_color
        colors.append(ran_color)
        time.sleep(0.07)
        PIXELS.show()
    count = 0
    while count < 4:
        PIXELS.fill((0, 0, 0))
        PIXELS.show()
        time.sleep(0.2)
        for i in range(0, len(colors)):
            PIXELS[i] = colors[i]
        PIXELS.show()
        time.sleep(0.2)
        count += 1
    time.sleep(0.8)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def rit():
    rit_color = (247, 105, 2)
    count = 0
    while count < 12:
        PIXELS.fill((0, 0, 0))
        if count % 2 == 0:
            for i in range(0, 30):
                PIXELS[i] = rit_color
        else:
            for i in range(30, LED_SIZE):
                PIXELS[i] = rit_color
        PIXELS.show()
        time.sleep(0.25)
        count += 1
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def down_up():
    # Down
    count = 0
    while count < 2:
        PIXELS.fill((255, 255, 255))
        PIXELS.show()
        time.sleep(0.3)
        for i in range(0, 6):
            if i == 0:
                for x in range(0, 10):
                    PIXELS[x] = (0, 0, 0)
            elif i == 1:
                for x in range(44, 51):
                    PIXELS[x] = (0, 0, 0)
            elif i == 2:
                for x in range(10, 20):
                    PIXELS[x] = (0, 0, 0)
            elif i == 3:
                for x in range(30, 37):
                    PIXELS[x] = (0, 0, 0)
            elif i == 4:
                for x in range(20, 30):
                    PIXELS[x] = (0, 0, 0)
            elif i == 5:
                for x in range(37, 44):
                    PIXELS[x] = (0, 0, 0)
            PIXELS.show()
            time.sleep(0.2)
        PIXELS.fill((0, 0, 0))
        PIXELS.show()
        time.sleep(0.1)
        for i in range(0, 6):
            if i == 5:
                for x in range(0, 10):
                    PIXELS[x] = (255, 255, 255)
            elif i == 4:
                for x in range(44, 51):
                    PIXELS[x] = (255, 255, 255)
            elif i == 3:
                for x in range(10, 20):
                    PIXELS[x] = (255, 255, 255)
            elif i == 2:
                for x in range(30, 37):
                    PIXELS[x] = (255, 255, 255)
            elif i == 1:
                for x in range(20, 30):
                    PIXELS[x] = (255, 255, 255)
            elif i == 0:
                for x in range(37, 44):
                    PIXELS[x] = (255, 255, 255)
            PIXELS.show()
            time.sleep(0.2)
        count += 1
    PIXELS.fill((255, 255, 255))
    PIXELS.show()
    time.sleep(0.3)
    for i in range(0, 6):
        if i == 0:
            for x in range(0, 10):
                PIXELS[x] = (0, 0, 0)
        elif i == 1:
            for x in range(44, 51):
                PIXELS[x] = (0, 0, 0)
        elif i == 2:
            for x in range(10, 20):
                PIXELS[x] = (0, 0, 0)
        elif i == 3:
            for x in range(30, 37):
                PIXELS[x] = (0, 0, 0)
        elif i == 4:
            for x in range(20, 30):
                PIXELS[x] = (0, 0, 0)
        elif i == 5:
            for x in range(37, 44):
                PIXELS[x] = (0, 0, 0)
        PIXELS.show()
        time.sleep(0.2)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def yt_loading():
    color = (255, 0, 0)
    size = 4
    count = 0
    loop = 6
    place = 0
    start = True
    while count < loop:
        PIXELS.fill((0, 0, 0))
        if place < LED_SIZE:
            for i in range(0, size):
                if place - i >= 0:
                    PIXELS[place - i] = color
                else:
                    if not start:
                        PIXELS[LED_SIZE - i + place] = color
            if place >= size:
                start = False
            PIXELS.show()
            time.sleep(0.015)
            place += 1
        else:
            place = 0
            count += 1
    count = 0
    place = 51
    while count < size:
        PIXELS.fill((0, 0, 0))
        for i in range(0, size):
            if place - i < LED_SIZE:
                PIXELS[place - i] = color
        PIXELS.show()
        time.sleep(0.015)
        place += 1
        count += 1

def rainbow():
    count = 0
    while count < 8:
        for i in range(1, 256):
            if count == 0:
                PIXELS.fill((i, 0, 0))
            elif count == 1:
                PIXELS.fill((255, i, 0))
            elif count == 2:
                PIXELS.fill((255 - i, 255, 0))
            elif count == 3:
                PIXELS.fill((0, 255, i))
            elif count == 4:
                PIXELS.fill((0, 255 - i, 255))
            elif count == 5:
                PIXELS.fill((i, 0, 255))
            elif count == 6:
                PIXELS.fill((255, i, 255))
            elif count == 7:
                PIXELS.fill((255 - i, 255 - i, 255 - i))
            PIXELS.show()
        count += 1
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def rotate():
    color_1 = (255, 0, 0)
    color_2 = (0, 255, 0)
    color_3 = (0, 0, 255)
    count = 0
    while count < 2:
        for x in range(0, 6):
            PIXELS.fill((0, 0, 0))
            if x == 0:
                for i in range(0, 10):
                    PIXELS[i] = color_1
                for i in range(10, 20):
                    PIXELS[i] = color_2
                for i in range(20, 30):
                    PIXELS[i] = color_3
            elif x == 1:
                for i in range(37, 44):
                    PIXELS[i] = color_1
                for i in range(44, 51):
                    PIXELS[i] = color_2
                for i in range(30, 37):
                    PIXELS[i] = color_3
            elif x == 2:
                for i in range(20, 30):
                    PIXELS[i] = color_1
                for i in range(0, 10):
                    PIXELS[i] = color_2
                for i in range(10, 20):
                    PIXELS[i] = color_3
            elif x == 3:
                for i in range(30, 37):
                    PIXELS[i] = color_1
                for i in range(37, 44):
                    PIXELS[i] = color_2
                for i in range(44, 51):
                    PIXELS[i] = color_3
            elif x == 4:
                for i in range(10, 20):
                    PIXELS[i] = color_1
                for i in range(20, 30):
                    PIXELS[i] = color_2
                for i in range(0, 10):
                    PIXELS[i] = color_3
            elif x == 5:
                for i in range(44, 51):
                    PIXELS[i] = color_1
                for i in range(30, 37):
                    PIXELS[i] = color_2
                for i in range(37, 44):
                    PIXELS[i] = color_3
            time.sleep(0.6)
            PIXELS.show()
        count += 1
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

def online():
    PIXELS.fill((0, 255, 0))
    PIXELS.show()
    time.sleep(0.25)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()
    time.sleep(0.2)
    PIXELS.fill((0, 255, 0))
    PIXELS.show()
    time.sleep(0.25)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()
    time.sleep(0.2)
    PIXELS.fill((0, 255, 0))
    PIXELS.show()
    time.sleep(1)
    PIXELS.fill((0, 0, 0))
    PIXELS.show()

# Flask Calls
@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/start')
def start():
    global current_thread
    if not current_thread:
        try:
            current_thread = ColorRunner()
            current_thread.start()
            return flask.jsonify({
                'status': 'success'
            })
        except Exception:
            return flask.jsonify({
                'status': 'unexpected error detected'
            })
    else:
        return flask.jsonify({
            'status': 'already running'
        })

@app.route('/stop')
def stop():
    global current_thread
    current_thread.kill.set()
    current_thread = None
    return flask.jsonify({
        'status': 'success'
    })

# Main
if __name__ == '__main__':
    online()
    app.run(host='0.0.0.0', port='80')
