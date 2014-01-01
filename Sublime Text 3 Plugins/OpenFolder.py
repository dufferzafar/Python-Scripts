import os
import sublime, sublime_plugin
from subprocess import call

class openFolderCommand( sublime_plugin.WindowCommand ):
  def run( self ):
    if self.window.active_view() is None:
      return

    try:
      call([ "explorer", self.window.folders()[0] ])
    except:
      call([ "explorer", os.path.dirname(self.window.active_view().file_name()) ])
