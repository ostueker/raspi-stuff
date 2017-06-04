from sense_hat import SenseHat

sense = SenseHat()
sense.rotation = 180

for i in range(100):
    if i%3 == 1:
        r,g,b = 255, 0, 0
    elif i%3 == 2:
        r,g,b = 0, 255, 0
    else:
        r,g,b = 0, 0, 255

    sense.show_message("Hello Craig! Placentia is back up!!!", text_colour=(r, g, b))

