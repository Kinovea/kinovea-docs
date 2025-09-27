
Playback screen user interface
==============================

The playback screen is divided in the following areas:

.. image:: /images/observation/ui-playback.png


- :ref:`videoviewport`
- :ref:`infobar`
- :ref:`annotation_toolbar`
- :ref:`working_zone`
- :ref:`timeline`
- :ref:`playback_controls`
- :ref:`export_controls`

Some functions are not directly visible in the screenshot

- :ref:`keyboard`
- :ref:`mouse`
- :ref:`context_menu`



.. _videoviewport:

Video viewport
-----------------
The image viewport is the main area where the video is played back.

Double clicking the image maximizes it in the viewport area.
The handles at the four corners of the image can be used to change its size.

.. _infobar:

Infobar
----------

The infobar contains the name of the file, the image size and the frame rate.

The file name can be clicked to access a context menu to switch between normal video mode and replay folder observer mode.

.. image:: /images/capture/menuobserver.png

.. _annotation_toolbar:

Annotation toolbar
-------------------
The annotation toolbar contains buttons to create new key images, select the active tool and open the color profile.

.. image:: /images/observation/toolbar.png

The toolbar contains more tools than those immediately visible.
Buttons that host extra tools have a little black triangle in the top-left corner. 
The extra tools can be accessed by right-clicking or long-clicking the primary button.

.. image:: /images/observation/subtools.png

.. _working_zone:

Working zone area
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

.. _timeline:

Timeline area
----------------
The timeline area displays the current position within the video, time markers and the speed control.

.. image:: /images/observation/timeline.png

Time markers
**************************

Time markers are the colored rectangles inside the timeline gutter, they provide information about annotations.

The red marker is the time origin.

The other markers are key images, chronometers or trajectories. Their color corresponds to the color of the drawing.


.. _playback_controls:

Playback controls
--------------------

.. image:: /images/observation/playbackcontrols.png

From left to right the buttons provides the following functions:

- Returns to the start of the video or working zone.
- Goes back one frame.
- Starts playback.
- Goes forward one frame.
- Goes to the end of the video or working zone.

The playback loops to the start when it reaches the end of the video or working zone.

Speed slider
*************

The speed slider goes from 0 to twice the nominal speed of the video.

The displayed speed value takes into account the slow motion factor configured such that the speed is shown as a percentage of the real world action speed.
For example if a video is filmed at 240 fps and saved into a file as 24 fps, the video will normally play back at 10% of the real world speed. 
In this case the speed control will go from 0 to 20% with a mid-point at 10%.

.. warning:: If the video cannot be played back at its nominal speed for performance reasons the playback speed value will automatically be lowered down.

    Performance for playing back depends on the displayed image size, the frame rate and the file format.

.. _export_controls:


Export controls
------------------
The export controls provide ways to export videos and images of the current file.

.. image:: /images/observation/exportcontrols.png

See also: :doc:`/export/videos`.


.. _keyboard:

Keyboard navigation
-------------------------

The following keyboard shortcuts are defined by default:

===========================================         =============================================================
:kbd:`←` Left arrow                                 Step backward one frame
:kbd:`→` Right arrow                                Step forward one frame
:kbd:`↟` Page up                                    Big jump backward
:kbd:`↡` Page down                                  Big jump forward
:kbd:`SHIFT` + :kbd:`↟` Page up                     Small jump backward
:kbd:`SHIFT` + :kbd:`↡` Page down                   Small jump forward
:kbd:`⇱` Home                                       Jump to the start
:kbd:`⇲` End                                        Jump to the end
:kbd:`SHIFT` + :kbd:`←` Left arrow                  At the start, will force jump back to the end
===========================================         =============================================================

- The big jump is 10% of the video length
- The small jump is 1% of the video length


.. _mouse:

Mouse navigation
----------------------

There are two modalities to use the mouse to navigate in time:

- Use the **mouse wheel** to move forward and backward.
- Hold the :kbd:`ALT` key and drag the image left or right to move backward or forward.

.. _context_menu:

Context menu
---------------
The context menu provides quick access to more functions.

.. image:: /images/observation/contextmenu.png


