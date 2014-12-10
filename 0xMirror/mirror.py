"""
Create a zero byte mirror of src_root at dest_root.

`ignore_dirs` are not traversed.
"""

import os
import time
import shutil

src_root = "D:\\Documents"
dest_root = "F:\\Mirror"

ignore_dirs = ['.git', 'env', "__pycache__", "node_modules"]

# Todo: Used only while debugging
if os.path.exists(dest_root):
    shutil.rmtree(dest_root)

# For files that errored
errors = []

# Use for execution time calculation
start_time = time.time()

# Todo: Replace walk with scandir?
for cur_dir, dirs, files in os.walk(src_root):

    # Removing entries from `dirs` results in those dirs
    # not being traversed.
    for ignore in ignore_dirs:
        if ignore in dirs:
            dirs.remove(ignore)

    dest_dir = cur_dir.replace(src_root, dest_root)

    # Create empty directories
    for dirname in dirs:
        destination = os.path.join(dest_dir, dirname)

        if not os.path.exists(destination):
            os.makedirs(destination)

    # Create empty files at destination
    for filename in files:
        destination = os.path.join(dest_dir, filename)

        try:
            # Pythonic way to `touch` a file?
            f = open(destination, "w")
            f.close()
        except:
            errors.append(os.path.join(cur_dir, filename))
        else:
            # Fix the timestamps of the files at destination
            stinfo = os.stat(os.path.join(cur_dir, filename))
            os.utime(destination, (stinfo.st_atime, stinfo.st_mtime))

# All Done!
print("Mirror completed in %.2f seconds with %d errors.\n" %
      ((time.time() - start_time), len(errors)))
print("Files that errored:\n\n", '\n'.join(errors))
