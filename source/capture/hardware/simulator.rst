
Camera simulator
================

General
-------

The camera simulator is a special type of test camera that is entirely implemented in Kinovea's software. 
This camera can be used to evaluate the expected performances of real hardware on a particular computer.

In order to add a camera simulator use the "Manual connection" button on the camera tab of the explorer panel.

.. image:: /images/capture/manualconnection.png

In the manual connection dialog, use the Camera type drop down and select Camera simulator.

.. image:: /images/capture/addsimulator.png

Configuration
-------------

.. image:: /images/capture/config-simulator.png


Stream format
*************

The following stream formats are available:

- RGB24: the images are not compressed.
- JPEG: the images are compressed.

When using the JPEG format, a set of images is compressed in advance and images are rotated to the output.
This is to avoid any computer slow downs due to compression when using the simulator to evaluate if a particular camera configuration would be sustainable; as the JPEG compression would be done in the camera.

When using the RGB24 format, the current time and image sequence number is stamped on the image.

.. tip:: You can use the sequential numbers on the images in the recorded video to verify if any frames were dropped during the recording process.

Width
*****
The width of the images.

Height
******
The height of the images.

Framerate
*********
The target framerate of the stream.


