# followme
_followme_ is for recording live tracking from [Locus Map](http://locusmap.eu/) and displaying the tracked position on a map.

# Features
* Record differently named live trackings
* Display the position on a fullscreen map

# Documentation
## Setup live tracking in Locus Map
1. Settings
2. Live Tracking
3. Add latitude (`lat`), longitude (`lon`)
4. Add a text input called `name`, set the value as desired
5. (_Optional_) Add speed (`speed`), altitude (`alt`) and/or time (`time`)
6. Enter update interval (time and/or distance)
7. Enter URL: `<your host and path>/rec.php`
8. Start recording

## Follow a tracked position
Open `<your host and path>/#<name of live tracking parameter 'name'>`
