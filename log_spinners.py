import sys
import time
from threading import Thread, Lock
from spinners import Spinners

color_end = '\033[0;39m'

status_symbols = {
    'info': '{0}ℹ{1}'.format('\033[34m', color_end),
    'success': '{0}✔{1}'.format('\033[32m', color_end),
    'warning': '{0}⚠{1}'.format('\033[33m', color_end),
    'error': '{0}✖{1}'.format('\033[31m', color_end)
}

lock = Lock()


class LogSpinners(object):
    def __init__(self, options):
        super(LogSpinners, self).__init__()

        if type(options) is str:
            options = {
                'text': options
            }

        self.options = {**{
            'text': '',
            'color': 'cyan',
            'spinner': Spinners.dots
        }, **options}

        self.text = self.options['text']
        self.spinner = self.options['spinner']
        self.frames = self.spinner.value['frames']
        self.interval = self.spinner.value['interval']
        self.frame_index = 0
        self.enabled = False
        self.status = None

    def output_log(self):
        while self.enabled:
            frame = self.frames[self.frame_index]
            output = "\r{0} {1}".format(frame, self.text)
            sys.stdout.write(output)
            sys.stdout.flush()
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            time.sleep(0.001 * self.interval)
        if self.status in status_symbols:
            symbol = status_symbols[self.status]
            output = "\r{0} {1}\n".format(symbol, self.text)
            sys.stdout.write(output)
            # sys.stdout.flush()
        lock.release()

    def start(self):
        self.enabled = True
        lock.acquire()
        t = Thread(target=self.output_log)
        t.start()

    def stop(self, status=None):
        self.enabled = False
        self.status = status

    def update(self, text):
        self.text = text
