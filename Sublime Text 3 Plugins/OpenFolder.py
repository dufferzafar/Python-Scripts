import os
import sublime, sublime_plugin
from subprocess import call

class openProjectFolderCommand(sublime_plugin.WindowCommand):
    def run( self ):

        call([ "explorer", self.window.folders()[0] ])

class openFileFolderCommand( sublime_plugin.WindowCommand ):
  def run( self ):
    if self.window.active_view() is None:
      return

    call([ "explorer", os.path.dirname(self.window.active_view().file_name()) ])
