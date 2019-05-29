#!/bin/python3

import GameOfLife as gol
import curses
import time
import random
import argparse
import sys

class Application(gol.GameOfLife):
    def __init__(self, speed, x=0, y=0, dynamic_size=False):
        self.speed = speed
        self.stdscr = curses.initscr()
        self.dynamic_size = dynamic_size
        self.stdscr.nodelay(1)
        curses.noecho()

        if x == 0:
            x = x = self.stdscr.getmaxyx()[1]
        if y == 0:
            y = self.stdscr.getmaxyx()[0]-1
        super(Application, self).__init__(x-2, y-2)



    def __del__(self):
        curses.echo()
        curses.endwin()


    def print(self):
        self.stdscr.clear()
        try:
           self.stdscr.addstr('+' + self.x*'-' + '+' + ' '*(self.stdscr.getmaxyx()[1]-self.x-2))
        except:
            print('Window is too wide! Please lower it using -x or use dynamic window size.', file=sys.stderr)
            sys.exit()
        for y in range(self.y):
            line = ''
            for x in range(self.x):
                if self.grid[x][y] == 1:
                    line += 'x'
                else:
                    line += ' '
            try:
                self.stdscr.addstr('|' + line + '|' + ' '*(self.stdscr.getmaxyx()[1]-self.x-2))
            except:
                print('Window is too wide! Please lower it using -y or use dynamic window size!', file=sys.stderr)
                sys.exit()
        try:
            self.stdscr.addstr('+' + self.x*'-' + '+')
        except:
            print('Window is too wide! Please lower it using -x or use dynamic window size!', file=sys.stderr)
            sys.exit()
        self.stdscr.refresh()

    def handleEvents(self):
        timetmp = time.process_time()
        while (time.process_time() - timetmp) < (1/self.speed):
            key = self.stdscr.getch()
            if key == curses.KEY_MOUSE:
                _, mx, my, _, _ = curses.getmouse()
                self.grid[my][mx] = 1
            elif (key == 114) or (key == 82):
              #  curses.endwin()
                self.grid = [[random.getrandbits(1) for i in range(self.y)] \
                for j in range(self.x)]
            elif key == curses.KEY_RESIZE:
                if (self.dynamic_size == True):
                    self.y = self.stdscr.getmaxyx()[0]-3
                    self.x = self.stdscr.getmaxyx()[1]-2
                    self.grid = [[random.getrandbits(1) for i in range(self.y)] \
                    for j in range(self.x)]
            elif key == 43:
                self.speed += self.speed*0.25
            elif key == 45:
            	self.speed -= self.speed*0.25


def main():

    parser = argparse.ArgumentParser(description='CLI Version of Game of Life.',epilog='Made By TheSeaOvStars')
    parser.add_argument('-d', '--dynamic', action='store_true', help='Dynamic window size')
    parser.add_argument('-s', '--speed', default=7, type=int, help='Initial speed')
    parser.add_argument('-x', default=0, type=int, help='Width of the window')
    parser.add_argument('-y', default=0, type=int, help='Height of the window')
    args = parser.parse_args()

    app = Application(args.speed, args.x, args.y, dynamic_size = args.dynamic)
    while True:
        app.print()
        app.handleEvents()
        app.step()

if __name__ == '__main__':
    main()
