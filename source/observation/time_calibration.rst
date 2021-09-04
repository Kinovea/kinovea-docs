
Time calibration
================

Capture frame rate
------------------
When a video is captured with a high speed camera (or using the high speed or slow motion function of a smartphone),
the generated video file often has a frame rate different from the capture frame rate.
For example a video filmed at 1000 fps may be saved to a file with a more typical playback frame rate of 25 fps.

In this case the video will play back slower than real time, which is expected,
but the time-related information and calculations would be erroneous if they were based on the playback framerate.

To work with this type of video it is important to configure (or "calibrate") the time scale.
This is done by going to :menuselection:`Video --> Configure video timing` and filling the capture frame rate.

.. image:: /images/observation/captureframerate.png

Changing this option does not change the nominal speed at which the video is played back.
In other words setting the speed control at its mid-point will still play back the video at the same slow motion rate as before.
Instead, this option changes the time coordinates of the images.

Broken playback frame rate
--------------------------
In some cases a video is saved with a frame rate which is just plain wrong, or Kinovea cannot read it.
For example a USB camera might claim that it is capturing video at 25 fps but the video stream is actually transfered at 15 fps.

In this case the video will play back at the wrong speed and the time calibration will be wrong.
If you know the real playback frame rate at which the video is supposed to be played back, you may enter it in :menuselection:`Video --> Configure video timing`.

.. image:: /images/observation/brokenframerate.png

Changing this option does change the nominal speed at which the video is played back.


