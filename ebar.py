import curses
import time

def main(stdscr):
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()

    counter = 0
    while True:
        stdscr.clear()
        stdscr.addstr(h-1, 0,
            f" INFO | counter: {counter} ".ljust(w),
            curses.A_REVERSE
        )
        stdscr.refresh()
        counter += 1
        time.sleep(1)

curses.wrapper(main)
