#!/usr/bin/env python

import pygame as pg

kb_file = open("keyboard.txt", 'w')

pg.init()
screen = pg.display.set_mode((200, 200))

print("Press the 12 main keys you will use. Press Escape to exit.")
for i in range(24):
    event = pg.event.wait()
    if event.type is pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            break
        else:
            name = pg.key.name(event.key)
            print("Last key pressed: %s" % name)
            kb_file.write(name + '\n')

kb_file.close()
print("Done. you have a new keyboard configuration file: %s" % (kb_file.name))
pg.quit()
