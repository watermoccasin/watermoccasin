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

## Useage
`watermoccasin.py [-h] [-w [WORKOUT]] [-s [SPEEDUP]]
                        [-l [{DEBUG,INFO,WARNING,ERROR,CRITICAL}]] [-v]
                        media`

## How do **I** use it?
`watermoccasin d:\ -s 1.85 -w 45`

## Installation
1. Obtain an [NPR developer account](https://dev.npr.org/).
2. Create an [application](https://dev.npr.org/console) to use.
3. Copy the "Application ID & Secret" for use later in the app.
4. `pip install watermoccasin`.
5. Ensure [ffmpeg](https://www.ffmpeg.org/download.html) is in the path.
6. The first time, you will be required to set up your NPR account, follow the instructions.
7. Test with you your local temp directory or removable drive.


Note: The destination directory is cleared of previous media.