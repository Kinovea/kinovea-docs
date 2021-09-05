
Playback screen user interface
==============================

The playback screen is divided in the following areas:

.. image:: /images/observation/ui-playback.png

1. Image viewport
-----------------
The image viewport is the main area where the video is played back.

Double clicking the image maximizes it in the viewport area.
The handles at the four corners of the image can be used to change its size.

2. Infobar
----------

The infobar contains the name of the file, the image size and the frame rate.

The file name can be clicked to access a context menu to switch between normal video mode and replay folder observer mode.

.. image:: /images/capture/menuobserver.png


3. Drawings toolbar
-------------------
The drawings toolbar contains buttons to create new key images, select the active tool and open the color profile.

.. image:: /images/observation/toolbar.png

The toolbar contains more tools than those immediately visible.
Buttons that host extra tools have a little black triangle in the top-left corner. 
The extra tools can be accessed by right-clicking or long-clicking the primary button.

.. image:: /images/observation/subtools.png

4. Working zone area
--------------------
The working zone defines the segment of the video that the player is working with. 
The play head loops within the working zone.

.. image:: /images/observation/workingzone.png

|TimeOrigin| Marks the current time as the time origin. This makes time values relative to this moment.

|WZLock| Locks the working zone start and end point to avoid changing them by mistake.

|WZStart| Sets the starting point of the working zone within the video.

|WZEnd| Sets the ending point of the working zone within the video.

|WZReset| Resets the working zone to the whole video.

.. |TimeOrigin| image:: /images/observation/icons/timeorigin.png
.. |WZLock| image:: /images/observation/icons/wz_lock.png
.. |WZStart| image:: /images/observation/icons/wz_left.png
.. |WZEnd| image:: /images/observation/icons/wz_right.png
.. |WZReset| image:: /images/observation/icons/wz_reset.png

You can also update the working zone boundaries by directly manipulating the blue end points.

.. tip:: If the amount of data fits in the cache memory, the working zone will be loaded in memory.

    This improves playback performances and enables the :menuselection:`Video --> Overview` and :menuselection:`Video --> Reverse` menus.
    The cache memory can be configured under :menuselection:`Options --> Preferences --> Playback --> Memory`.

5. Timeline area
----------------
The timeline area displays the current position within the video, time markers and the speed control.

.. image:: /images/observation/timeline.png

Time markers
**************************
Time markers are the colored rectangles inside the timeline gutter, they provide information about annotations.
They use the following color coding:

- Red: the time origin.
- Green: a key image.
- Blue: a chronometer.
- Purple: a trajectory.

Speed control
*************

The speed slider goes from 0 to twice the nominal speed of the video.

The displayed speed value takes into account the slow motion factor configured such that the speed is shown as a percentage of the real world action speed.
For example if a video is filmed at 240 fps and saved into a file as 24 fps, the video will normally play back at 10% of the real world speed. 
In this case the speed control will go from 0 to 20% with a mid-point at 10%.

.. warning:: If the video cannot be played back at its nominal speed for performance reasons the playback speed value will automatically be lowered down.

    Performance for playing back depends on the displayed image size, the frame rate and the file format.

6. Playback controls
--------------------

.. image:: /images/observation/playbackcontrols.png

From left to right the buttons provides the following functions:

- Returns to the start of the video or working zone.
- Goes back one frame.
- Starts playback.
- Goes forward one frame.
- Goes to the end of the video or working zone.

The playback loops to the start when it reaches the end of the video or working zone.

Navigation
**********

It is also possible to move in the video using the following shortcuts:

- Scroll with the mouse wheel to move forward and backward.
- Use the :kbd:`←` and :kbd:`→` arrow keys on the keyboard to move frame by frame.
- Use the :kbd:`↟` (Page up) and :kbd:`↡` (Page down) keys to jump 10% forward.
- Use the :kbd:`⇱` (Home) and :kbd:`⇲` (End) keys to jump to the start and end.

 
7. Export controls
------------------
The export controls provide ways to export videos and images of the current file.

.. image:: /images/observation/exportcontrols.png

See: Export > Exporting video and images

8. Context menu
---------------
The context menu provides quick access to more functions.

.. image:: /images/observation/contextmenu.png


