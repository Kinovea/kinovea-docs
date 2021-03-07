Guidelines to minimize measurement errors
=========================================

The following guidelines are designed to minimize the systematic and random errors inherent to measuring spatial motion on 2D images.

Camera setup
----------------

Mount the camera on a tripod and avoid camera motion
****************************************************
The camera must remain stationary for the images to provide a stable frame of reference.
If the camera is moving relatively to the scene, the plane of motion will change over time
and the calibration from one video frame cannot be used on other frames.

.. tip:: If you do not control the camera and it is moving, you can try to track the calibration object itself.

Align the camera plane with the plane of motion
****************************************************
When using calibration by line the camera must be perfectly aligned with the plane of motion.
This means the camera optical axis must be orthogonal to the plane of motion.

.. tip:: If the camera is not in a controlled environment use the calibration by plane.

Maximize the camera distance to the scene
****************************************************
Place the camera as far as possible from the scene and zoom in, to minimize perspective distortion.
This will reduce errors due to points moving in and out of the plane of motion.

TODO: demo.

Camera and digitization
--------------------------------

Minimize or correct lens distortion
************************************
Use a lens with as little distortion as possible to minimize the curvature of the plane of motion in the images.

This distortion can be taken into account in Kinovea using the lens calibration dialog.

Use an appropriate exposure time
********************************
To minimize motion blur decrease the exposure time as much as possible (increase shutter speed).

Maximize image size and image quality
**************************************
Use the largest possible image resolution to improve the precision of the digitization process when locating points on the images.

Use the zoom function
*********************
Use the zoom function in Kinovea to position the points more precisely. 
Kinovea use fractional pixel coordinates for calibration and measurements.

Scene setup
-----------

Use a large reference object
******************************
The scaling object used for calibration should occupy a proportion of the image as large as possible.

Use a vertical or horizontal reference
***************************************
To align the axes of the coordinate system with the real world use a plumb line or other object of known direction as the calibration object.

Avoid measuring objects outside the plane of motion
****************************************************
The physical objects used to make the measurements must sit on the calibrated plane of motion.
Coordinates of and measurements using points outside the plane of motion will be inaccurate.

TODO: demo with angles.

Use small round markers
************************
Use small markers on the object or joints. 
The markers shape should not vary when rotated.














