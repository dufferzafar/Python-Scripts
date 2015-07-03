import re
import os
import time
from itertools import groupby


def pretty_epoch(epoch, format_):
    """ Convert timestamp to a pretty format. """
    return time.strftime(format_, time.localtime(epoch))


def is_in_last_days(stamp, n):
    """
    Check whether the timestamp was created in the last n days.

    I guess the 'right' way to do this would be by using timedelta
    from the datetime module, but this felt 'ok' to me.
    """
    return stamp - time.time() < n * (24 * 60 * 60)

# History contains tuples - (timestamp, command)
history = []

# Read ZSH History
with open(os.path.expanduser("~/.zsh_history")) as inp:
    for line in inp.readlines():
        m = re.match(r":\s(\d+):\d+;(.*)", line)
        if m:
            history.append((int(m.group(1)), m.group(2)))

# Read Fish History
with open(os.path.expanduser("~/.config/fish/fish_history")) as inp:
    for line in inp.readlines():
        if line.startswith("- cmd:"):
            cmd = line[7:]
        elif line.startswith("  when:"):
            when = line[8:]
            history.append((int(when), cmd.strip()))

# Filter out unwanted entries
history = [item for item in history if is_in_last_days(item, 7)]

# Sort history by timestamp
history.sort(key=lambda x: x[0])

# Group history entries by date
groups = groupby(history, lambda item: pretty_epoch(item[0], "%a, %d %b"))

# Print!
for date, items in groups:
    print(date)

    for item in items:
        print(pretty_epoch(item[0], "%I:%M %p"), item[1])
