# Microbit Clock Multiplier

## How…

Just upload the hex file to your microbit and you'll see a pattern appear on the LED matrix. 

The pattern on the matrix represents five different rhythmic patterns.

The centre five are the base pulse. 

```
00000
00100
01110
00100
00000
```

The top left is the base pulse duration * 2.

```
11000
11000
00000
00000
00000
```

The top right is base pulse * 3.

```
00011
00011
00000
00000
00000
```

The bottom right is * 4. 

```
00000
00000
00000
00011
00011
```

The bottom left is * 5.

```
00000
00000
00000
11000
11000
```

The next steps are to send a pulse out of specific digital pins and take a clock signal in as the base pulse.
