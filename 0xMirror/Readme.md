# 0xMirror

Creates a zero byte mirror of a folder at another folder.

![Properties](/0xMirror/Screenshot.png)

__Why?__

My laptop conked out once, and I had no idea of _what_ exactly I would lose if it never booted up again. 

__Shout-outs:__

[@iCHAIT](http://github.com/ichait/) for https://github.com/iCHAIT/0xMirror/

[@kwikadi](https://github.com/kwikadi/) for https://github.com/kwikadi/Raid-X/

[@nickedes](https://github.com/nickedes/) for https://gist.github.com/nickedes/751a971019da869008e6/

## <a name="todo"></a>Todo

* Use `scandir` instead of `os.walk`

* Support for multiple drives

* Remove the bug that wants destination not be a part of source

* Create a zip file (while mirroring) and copy the file to the Dropbox folder on completion. 

* A Progress Bar? (OH YEAH!!)

* Display Stats?
  * Number of files/folders mirrored. 
  * ~~Errors, if any?~~

* Output the filepaths to a text file?
