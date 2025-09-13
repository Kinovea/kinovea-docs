Spatial calibration
======================

In order to use Kinovea to make measurements on the video, it is necessary to calibrate the transformation of pixels in the image into real world units.
Kinovea supports two calibration mechanisms: calibration by line and calibration by plane.

All measurements in Kinovea must sit on a 2D plane.
If the motion you want to study is on a plane parallel to the image plane (orthogonal to the camera optical axis), you may use calibration by line.
Otherwise, if you are measuring points on the ground, for example, you should use the calibration by plane.
If the motion is happening in arbitrary 3D space you cannot measure it in Kinovea.

Line calibration
----------------
Line calibration is possible when the motion is sitting on a 2D plane parallel to the camera plane.

.. image:: /images/measurement/planeofmotion.png

To perform line calibration follow these steps:

- Have an object of known length visible in the video.
- Add a line object and place it on top of the object of known length.
- Right click the line and select the :menuselection:`Calibrate` menu.
- Enter the real-world length of the object.

.. image:: /images/measurement/calibrationline.png
    :align: center

.. note:: Modifying the calibration line after calibration already took place will update the calibration to use the new pixel length of the line
    and keep the real-world length as configured.

Plane calibration
-----------------
Plane calibration is possible when the motion is sitting on an arbitrary 2D plane visible in the video.

To perform plane calibration follow these steps:

- Have a rectangle of known dimensions visible in the video.
- Add a perspective grid object and move its corners to match the rectangle.
- Right click a corner and select the :menuselection:`Calibrate` menu.
- Enter the real-world width and height of the rectangle.

.. image:: /images/measurement/calibrationplane.png
    :align: center

.. note:: Modifying the calibration plane after calibration already took place will update the calibration to use the new pixel dimensions of the plane
    while keeping the real-world dimension as configured.




