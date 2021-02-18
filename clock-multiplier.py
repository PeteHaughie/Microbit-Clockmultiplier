from microbit import *
# import time

# global vars
minute = 60000  # ms per second
bpm = 10  # an integer which represents the beats per minute
converted = minute / bpm  # converting the bpm to ms
off = 0
on = 9

# delta timers
sourceDelta = 50
doubleDelta = 100
tripleDelta = 150
quadDelta = 200
quintDelta = 250

# these values are the brightness of the LED 0 off, 9 full
s = 0  # source
d = 0  # source doubled
t = 0  # source tripled
q = 0  # source quadrupled
f = 0  # source quintupled

template_str = "dd0tt:ddstt:0sss0:ffsqq:ff0qq"
matrix_str = "00000:00000:00000:00000:00000"
matrix = Image(matrix_str)

def updateValues():
    global sourceDelta
    global doubleDelta
    global tripleDelta
    global quadDelta
    global quintDelta
    global s
    global d
    global t
    global q
    global f
    if sourceDelta <= 1:
        sourceDelta = 50
        s = on
    else:
        sourceDelta -= 1
        s = off
    if doubleDelta <= 1:
        doubleDelta = 100
        d = on
    else:
        doubleDelta -= 1
        d = off
    if tripleDelta <= 1:
        tripleDelta = 150
        t = on
    else:
        tripleDelta -= 1
        t = off
    if quadDelta <= 1:
        quadDelta = 200
        q = on
    else:
        quadDelta -= 1
        q = off
    if quintDelta <= 1:
        quintDelta = 250
        f = on
    else:
        quintDelta -= 1
        f = off

def changeMatrixState():
    global s
    global d
    global t
    global q
    global f
    global template_str
    global matrix_str
    x = template_str
    x = x.replace("s", str(s))
    x = x.replace("d", str(d))
    x = x.replace("t", str(t))
    x = x.replace("q", str(q))
    x = x.replace("f", str(f))
    matrix_str = x

def updateLED():
    global matrix_str
    global matrix
    matrix = Image(matrix_str)
    display.show(matrix)

# loop
while True:
    # clear the display
    display.clear()
    # decrement the counters
    updateValues()
    # change the values in the display matrix
    changeMatrixState()
    # paint the new state to the display
    updateLED()
    # 10ms tick - yeah right…
    sleep(10)