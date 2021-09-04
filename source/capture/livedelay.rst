Live delay
==========

Feature description
-------------------

The live delay function lets you delay the display of the live stream.

This function is very useful for self-coaching: set the delay to be approximately the total time of the exercise plus the time necessary to come back to the computer.
The camera and Kinovea can then be left unattended. 
By the time you complete your exercise and come back to the computer, you should see a replay of the action.
 
The same approach can be used with a group of students or athletes, forming an uninterrupted queue of intertwined feedback loops.

Applying delay 
--------------

To delay the display of the camera stream use the delay slider or the delay input box. 
The delay amount is in seconds.

.. image:: /images/capture/delaycontrols.png

The maximum amount of delay depends on the camera configuration — hardware compression, image format, image size, frame rate — and the memory allocated in the delay cache under :menuselection:`Options --> Preferences --> Capture --> Memory`.

If you wish to use a delay that is larger than the maximum that can be set using the slider, increase the size of the memory buffer under :menuselection:`Options --> Preferences --> Capture --> Memory`.
Note however that this buffer is always allocated, even if you do not use the delay function. 

.. note:: When using two capture screens at the same time the memory buffer is shared between the screens.

Recording modes
---------------

It is possible to record video while delay is active. The option selected for the recording mode impacts whether the delay is taken into account for the recording or not.


======================    ========================
Recording mode            Delay
======================    ========================
Camera                    No
Delayed                   Yes
Retroactive               Yes  
======================    ========================

Combining delay and recording can be used to record actions happening before the moment the record button is hit or triggered.

Time origin
-----------

When recording with delay, the time origin of the resulting video is set to the real moment the record button was hit or triggered.

For example we are filming a golf swing for a total duration of 2.5 seconds and a delay of 1.5 seconds.
The recording is started via audio trigger when the club hits the ball.

The first image of the video will correspond to what the camera was filming 1.5 seconds before the club hit the ball.

The time origin in the metadata file will be set to the club-ball impact. All of the action happening before the impact will be timestamped with negative numbers.

Pause and browse
----------------

Pausing the camera using the pause button |Pause| freezes the delay buffer.

This enables manually navigating the recent history of the camera stream using the delay slider.

.. |Pause| image:: /images/capture/icons/grab_pause.png
