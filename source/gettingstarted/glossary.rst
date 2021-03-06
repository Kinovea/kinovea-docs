





real time speed
---------------
The speed at which the action physically occurred.
When the capture framerate is correctly configured the speed slider will show a percentage based on the real time speed. 

capture framerate
-----------------
The framerate of the camera while capturing the action.
Several framerates are distinguished:
- The framerate configured in the camera settins.
- The framerate at which Kinovea really receives frames from the camera. (Some camera do not send frames at the configured value for various reasons).

resulting framerate
-------------------
This is a framerate that is sometimes displayed in the camera configuration page when the combination of settings do not allow for the configured framerate to be honored.
For example we can set a camera to use a very long exposure duration and simultaneously ask for an incompatibly high framerate.
In this case the resulting framerate is the framerate that the camera will actually try to send images at.

output framerate
----------------
This is the framerate saved in the metadata of the file.
For high speed cameras with very high framerate the output file is modified to use a more typical framerate.
For example the camera is sending 1000 fps but the output video is set to be at 30 fps. This cause the action in the resulting video to appear in slow motion.

image aspect ratio
------------------
Width of image divided by height of image.

pixel aspect ratio
------------------
This is a metadata contained in the file used to change the aspect ratio.
Nowadays this is mostly found on files from DV camcorders.

working zone
------------

image sequence
--------------
A collection of images in a single folder with a naming pattern that contains consecutive numbers for the consecutive frames.

time origin
chronometer
stopwatch
clock
line calibration
plane calibration
perspective plane calibration




