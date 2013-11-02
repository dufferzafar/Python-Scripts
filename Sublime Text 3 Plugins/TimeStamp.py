import sublime, sublime_plugin
from datetime import datetime

class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    stamp = datetime.now().strftime("%d/%m/%Y-%H:%M")
    for r in self.view.sel():
      if r.empty():
        self.view.insert (edit, r.a, stamp)
      else:
        self.view.replace(edit, r,   stamp)
