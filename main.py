#!/usr/bin/env python

import subprocess


if __name__ == "__main__":
    proc = subprocess.Popen(['ssh', '-f', 'sam@jenkins', '-L',
                             '8080:localhost:8080', '-N', '"tesvf"'])
    print proc