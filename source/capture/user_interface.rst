Capture screen user interface
=============================

The capture screen is divided in the following areas:

.. image:: /images/capture/capture-screen-ui3.jpg
    

At the top:

- The :ref:`Infobar <infobar>` contains information about the connected camera and streaming performances.
- The :ref:`Context bar <contextbar>` has drop downs of context variables to tag the captured files.
- The :ref:`Quick status band <quickstatusband>` gives a visual indication of the current status for recording.


In the middle:

- The :ref:`Camera viewport <cameraviewport>` is where the camera image and drawings are visible.

At the bottom:

- The :ref:`Annotation toolbar <annotationstoolbar>` contains drawing tools usable on the capture screen.
- The :ref:`List of recently captured files <capturedfiles>` displays thumbnails of the files recorded in the session.
- The :ref:`Capture controls <capturecontrols>` area has buttons to configure the camera, pause or restart the stream, switch between live and delayed view, arm and disarm the capture trigger, save an image, and start/stop recording.
- The :ref:`Delay and duration <delayduration>` area controls the delay of the stream and the duration of recordings.
- The :ref:`Output folder and file name <outputfolder>` area lets you pick the output folder and define the file naming pattern of recorded files.


.. _infobar:

Infobar
----------
The infobar contains information about the connected camera and streaming performances.

.. image:: /images/capture/infobar1.png

The first part of the infobar displays the alias of the camera and the current configuration for image size, frame rate and image format.
Clicking in this area of the infobar will bring up the camera configuration dialog.

The frame rate indicated is the one configured, the actual frame rate sent by the camera might be different for various reasons like low light levels or hardware limitations.

The second part of the infobar displays the following live statistics:

.. image:: /images/capture/infobar2.png

Signal (fps) 
************
This is the frequency at which Kinovea is receiving images from the camera. The value is in frames per second.

Many cameras will reduce their frame rate based on various external factors. 
For example, when a camera uses auto-exposure and the exposure duration computed by the device is incompatible with the selected frame rate.

Throughput (MB/s)
*****************
This is the amount of data that passes through Kinovea as it processes the stream. The value is in megabytes per second, with the convention of one megabyte as 1024 kilobytes.

This value is related to the the image size, frame rate and format, possible on-camera image compression, link bandwidth, and possible post-processing done at the driver level.

You can use this value to estimate the necessary speed for your storage medium to write the uncompressed stream.

In the case of a non-compressed stream in RGB24 format, the value is calculated as follows:

``Throughput = (width × height × 3 × frame rate) / (1024*1024)``

Load (%)
********
This value describes how much Kinovea is struggling to keep up with the camera framerate. 
It is computed as the time taken to process one frame divided by the interval between frames.

When this value is near 100% it means it takes Kinovea the same amount of time to process one frame as the time budget it has for that frame, if it goes over 100% dropped frames may occur.

Drops
*****
This is the number of frames that could not be processed by Kinovea during the current or last recording session.

If this value is non-zero, some frames are missing from the output video and any measurements involving time will not be perfectly accurate.

.. _contextbar:

Context bar
---------------

.. image:: /images/capture/contextbar.png


The context bar contains drop down lists of context variables. It is only visible if any variables have been configured. 

Context variables are used to tag the captured files with information like the name of the person being filmed, the type of exercise being performed, the equipment being used or any other relevant context.

The variables are configured from :menuselection:`Options --> Context`.

These variables can be used in the naming of the captured files and in the path of the capture folder to create a self-structuring file hierarchy. See :doc:`/recording/context_variables`.

To disable the context bar and ignore the context variables, click the identity card icon in the top right corner of the capture screen.

.. image:: /images/capture/context-disable.png
    
    
If the context bar is disabled but the path or name of the captured files contains context variables, the recording will be cancelled and a warning message will be displayed.
    

.. _quickstatusband:

Quick status band
---------------------

The quick status band is a colored band at the top of the viewport that gives a quick visual indication of the current status of the capture screen.


.. image:: /images/capture/recording-progress2.png

The color codes are as follows:

================    ========================
Color                   Status
================    ========================
Purple                  The camera is not connected or there is no camera selected
Yellow                  The camera is connected but the stream is paused
Blue                    The camera is streaming, but the capture trigger is disarmed or in the idle period
Green                   The camera is streaming, and the capture trigger is armed
Red                     Recording is in progress
================    ========================

If the recording has a maximum duration the quick status bar will progressively reduce in size as the recording approaches the maximum duration.


.. _cameraviewport:

Camera viewport
------------------
The camera viewport is the main area where the camera image is visible. 

The image itself can be moved around by dragging with the mouse and resized using the manipulators at the corners of the image or by using :kbd:`CTRL` + **mouse scroll**. 
Drawings on the capture screen can go outside the image area.

If the image stays black, there might be a problem with the available USB bandwidth or power, or the exposure duration might be too short.

If nothing is visible at all, not even the black image rectangle, the camera did not connect correctly; for example, the camera might be in use in another application at the same time.



.. _annotationstoolbar:

Annotation toolbar
------------------------------

.. image:: /images/capture/toolbar.png

The annotation toolbar contains drawing tools usable on the capture screen. Some tools available in the playback screen are not available in the capture screen.

Some buttons may give access to multiple tools. To access the other tools, right click the button or perform a long press on the button.


.. _capturedfiles:

List of recently captured files
----------------------------------

.. image:: /images/capture/capturedfiles.png

This area displays thumbnails of the recently captured files. 

.. tip:: This area can be folded down to save space by clicking the down arrow button in the right corner of the area.

Double clicking on a thumbnail opens the file in a playback screen. The close button removes the thumbnail from the list without deleting the file.

Right-clicking on a thumbnails brings a context menu with the following options:

================================================    ========================
|Open| Open                                         Opens the video in a playback screen.
|Locate| Locate in Windows Explorer                 Opens the Windows Explorer on the parent folder of the video.
|Rename| Rename                                     Make the file name label editable and save the new file name.
|Hide| Hide                                         Removes this thumbnail from the list without deleting the file.
|Delete| Delete                                     Sends the file to the Windows trash.
================================================    ========================

.. |Open| image:: /images/capture/icons/television.png
.. |Locate| image:: /images/capture/icons/folder_new.png
.. |Rename| image:: /images/capture/icons/rename.png
.. |Hide| image:: /images/capture/icons/hide.png
.. |Delete| image:: /images/capture/icons/delete.png

.. _capturecontrols:

Capture controls
-------------------

.. image:: /images/capture/capture-controls.png

|Configure| *Configure camera*

.. |Configure| image:: /images/capture/icons/settings.png

Displays the camera configuration dialog to change options like the image size or frame rate.

|Pause| *Pause camera* / |Restart| *Start camera*

.. |Pause| image:: /images/capture/icons/stream-pause.png
.. |Restart| image:: /images/capture/icons/stream-play.png

Pauses or restarts the camera stream. 

When the camera stream is paused it is possible to review the last few seconds of action by adjusting the delay slider.

|Live| *The view is live* / |Delayed| *The view is delayed*

.. |Live| image:: /images/capture/icons/live-live.png
.. |Delayed| image:: /images/capture/icons/live-delayed.png
    
Sets the camera view to live or delayed. This is independent from the recording it only affects the view.


|Armed| *The capture trigger is armed* / |Disarmed| *The capture trigger is disarmed*

.. |Armed| image:: /images/capture/icons/armed-armed.png
.. |Disarmed| image:: /images/capture/icons/armed-disarmed.png

Arms or disarms the capture trigger. 

If capture by trigger is disabled globally this will always show as disarmed. 
If capture by trigger is enabled globally but it is disarmed here, trigger events will be ignored.

The trigger options can be configured in :menuselection:`Options --> Preferences --> Capture --> Trigger`.


|SaveImage| *Save image*

.. |SaveImage| image:: /images/capture/icons/capture-screenshot.png

Saves the image currently displayed to an image file in the selected capture folder and with the defined file name.

|RecordStart| *Start recording video* / |RecordStop| *Stop recording video*

.. |RecordStart| image:: /images/capture/icons/recording-start.png
.. |RecordStop| image:: /images/capture/icons/recording-stop.png

Starts or stops recording the video. The video is recorded based on the global format and recording mode options.
It is saved in the selected capture folder with the defined file name.

See :doc:`userinterface/preferences/capture` for more information.


.. _delayduration:

Delay and duration
----------------------

.. image:: /images/capture/capture-delay-controls.png

The delay numerical field and slider let you adjust the amount of delay, in seconds, of the camera stream.

The delay setting can be ignored for the viewport image by using the |Live| Live view button in the capture controls. In this case the delay is still taken into account when recording if the recording mode is set to Delayed or Retroactive.

The maximum amount of delay depends on the camera configuration — hardware compression, image format, image size, frame rate — and the memory allocated in the delay cache under :menuselection:`Options --> Preferences --> Capture --> Memory`.


The duration numerical field let you set a maximum duration for the recording. This is the total duration of the resulting file. 

.. note:: For example if delay is set to 2 seconds and maximum duration is set to 3 seconds, the resulting file will be 3 seconds and contain 2 seconds of action before the recording button was pressed or triggered, and 1 second of action after the recording button was pressed or triggered.



.. _outputfolder:

Output folder and file name
-------------------------------

.. image:: /images/capture/capture-folder-file.png


Capture folder
***************

The capture folder drop down list let you select the folder where captured images and videos will be saved. 

This list of folders can be configured from :menuselection:`Options --> Preferences --> Capture --> Folders`. This preference page can be accessed by clicking on the folder button to the left of the drop down list.

The file name and capture folder path can use variables that are replaced by their current value when creating the file. 
This can be used to create self-structuring folder hierarchies for example by automatically saving in sub-folders by date and name.

Hover the mouse over the capture folder drop down to see a tooltip with the actual path target.

See :doc:`/recording/capture_folders`, :doc:`/recording/context_variables` and :doc:`/userinterface/preferences/capture` preferences for more information.

File name
*************

The file name field lets you define either a plain file name or a file name pattern using variables. 

When using a plain file name a number will be automatically appended before the next recording to avoid overwriting existing files.

When using a file name pattern with variables, the recorded files will be named according to the pattern and the variables will be replaced by their current value.

You can configure the global default file name and insert variables in a graphical way in the preference pages :menuselection:`Options --> Preferences --> Capture --> Files`.


