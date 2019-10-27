# watermoccasin
Convert a NPR ONE news feed for offline listening with options for speed up and timed playlist

LICENSE: [CC By SA](https://creativecommons.org/licenses/by-sa/4.0/legalcode) [in Plain Text](
https://creativecommons.org/licenses/by-sa/4.0/legalcode.txt)

## Why
* Named after snakes who swim on top of the water. 
* Running out the door w/the latest news and swimming laps w/an mp3 player.
* Change to give back and [money for coffee](https://paypal.me/teachingstudent)

## Features
* Grabs NPR feed for offline listening
* Option to speed up playback for any device
* Will obtain a playlist by length (even if sped up)

## How do **I** use it?
`watermoccasin.py -s 1.85 -w 45`

## Installation

1. Obtain an [NPR developer account](https://dev.npr.org/).
2. Create an [application](https://dev.npr.org/console) to use.
3. Copy the "Application Secret" for use later in the app.
4. Ensure [ffmpeg](https://www.ffmpeg.org/download.html) is in the path.
5. `pip install watermoccasin`.