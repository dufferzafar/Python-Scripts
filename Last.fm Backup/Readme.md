# Last.fm Backup

Backup Last fm data - scrobbles, loved/banned tracks, etc.

Modified the [original script](https://gitorious.org/fmthings/lasttolibre/blobs/master/lastexport.py) from the [lasttolibre](https://gitorious.org/fmthings/lasttolibre) project to suit my usecase.

## Todo

* Incremental Backups: Only backup *new* data. Use timestamps to figure out upto what moment we already have stuff and then stop.

* Only backs up scrobbles currently, but has support for other stuff too. Need to test it out.

* Data is currently saved as TSV. I think a SQL DB would be better coz I'd be able to run queries.

