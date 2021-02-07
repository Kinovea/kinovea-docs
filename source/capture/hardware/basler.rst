
Basler cameras
==============

More information about Basler cameras can be found on their website at: https://www.baslerweb.com

Installation 
------------

When installing the Basler runtime software "Pylon", it is necessary to use the "Custom" option in the installer, expand the "pylon Runtime" node and select "pylon C .NET Runtime" option.

.. image:: /images/capture/pylon-install.png

If you have already installed the software you can re-run the installer and choose "Modify the current installation" to access this option.

Configuration
-------------

.. image:: /images/capture/config-basler.png

Stream format
*************
The avalaible stream formats depend on the exact model of the camera.

Stream formats starting with the *Bayer* prefix transmit the raw sensor data and can be used to record raw videos. For other modes the color information is reconstructed in the camera.

Bayer format conversion 
***********************
When the selected stream format is a raw Bayer format, this option defines which reconstruction method, if any, is applied to the raw sensor data. The following options are available:

- Raw: No reconstruction is performed. Kinovea receives the images as-is.
- Mono: Monochromatic images are rebuilt by the Basler runtime before passing the images to Kinovea.
- Color: Color images are rebuilt by the Basler runtime before passing the images to Kinovea.

When using "Raw" and the video is recorded without compression, the raw sensor data is saved to the video file. 
It is then possible to rebuild the color at playback time by choosing the appropriate option under the menu Image > Demosaicing.

This approach can be interesting to limit the bandwidth required to transfer the camera stream and save it to storage.

Width
***********************
The width of the images. This usually has no effect on the maximum framerate possible as the cameras always read entire sensor rows.

Height
***********************
The height of the images. This usually impacts the maximum framerate possible as only the required rows are read from the sensor.

Framerate
***********************
The target framerate. Whether this framerate is actually reached or not depends on the image format, size, exposure and the camera hardware.
If the framerate cannot be sustain the *Resulting framerate* value will be displayed in red.

Exposure (µs)
***********************
The amount of time the sensor is exposed, in microseconds. This value can be used to find the tradeoff between motion blur and light requirements. 
Lowering this value reduces motion blur and increase the amount of light required to capture the scene.

This value is a limiting factor for the framerate. For example a value of 2000 µs or 2 ms implies that there cannot be more than 500 images per second.


Gain
***********************
Amplification of the signal captured on the sensor. Increasing this value increase the apparent light but can introduce noise in the image.

This value has no impact on the framerate.


Resulting framerate
***********************

This value is the actual framerate at which the camera will send images, based on the other values and the camera hardware capabilities.


Other options
-------------

Other options can be configured in "Pylon viewer" the software provided by Basler. 
Options that are not available in Kinovea will not be modified when opening the camera in Kinovea.




