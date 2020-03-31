# Write your code here :-)
from adafruit_circuitplayground import cp
import time
import random

class NeoPixels(object):

    def __init__(self):
        self.pixel_amount = 10
        self.pixel_off_state = (0, 0, 0) # pixels are turned off if black.
        self.count = 0
        cp.pixels.brightness = 0.1

    def everyThirdPixel(self):
        red = (255, 0, 0)
        blue = (0, 0, 255)
        cp.pixels[::3] = [red] * (int(self.pixel_amount/3)+1)
        cp.pixels[1::3] = [blue] * (int(self.pixel_amount/3))
        cp.pixels[2::3] = [blue] * (int(self.pixel_amount/3))

    def movingPixel(self):
        pixel_color = (255, 0, 0)
        cp.pixels[self.count] = pixel_color
        cp.pixels[(self.count-1) % self.pixel_amount] = self.pixel_off_state
        time.sleep(0.5)
        self.count = self.count + 1
        if self.count >= self.pixel_amount:
            self.count = 0

    def alternateLights(self):
        if self.count % 2 == 0:
            cp.pixels.fill((255, 0, 0))
        else:
            cp.pixels.fill((50, 0, 50))
        self.count = self.count + 1
        if self.count >= 4:
            self.count = 0
        time.sleep(0.5)
        #print(self.pixel_amount // 2, [pixel_colour] * (self.pixel_amount // 2))


    def wheel(self):
        if self.count >= self.pixel_amount:
            self.count = 0
            cp.pixels.fill(self.pixel_off_state)
            time.sleep(0.5)
        pixel_color = (255 - (25 * self.count), 0, 25 * self.count)
        cp.pixels[self.count] = pixel_color
        self.count = self.count + 1

    def meetHalfWay(self):
        pixel_color = (255 - (50 * self.count), 0, 50 * self.count)
        cp.pixels[self.count] = pixel_color
        cp.pixels[(self.pixel_amount - 1) - self.count] = pixel_color
        self.count = self.count + 1
        if self.count >= (self.pixel_amount//2):
            self.count = 0
            time.sleep(0.5) # remove jitter on last pixel
            cp.pixels.fill(self.pixel_off_state)

    def chaser(self, child_limit): # snake like movement through the pixels
        pixel_color = (255, 9, 255)
        for i in range(0, self.pixel_amount):
            if i < child_limit:
                cp.pixels[(i + self.count) % self.pixel_amount] = pixel_color
            else:
                cp.pixels[(i + self.count) % self.pixel_amount] = self.pixel_off_state
            print(i)
        #cp.pixels[pos] = pixel_color
        self.count = self.count + 1
        if self.count >= self.pixel_amount:
            self.count = 0
            #time.sleep(0.1) # remove jitter on last pixel
        time.sleep(0.2)

