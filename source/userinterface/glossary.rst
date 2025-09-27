
Glossary
==============

A list of important concepts used in Kinovea and in this documentation. 


Annotations
**********************
Annotations in Kinovea combine all the pieces of information you add to the video. 
This includes drawings and comments but also image transforms like rotation or mirror, 
calibration data, tracking data, kinogram data, etc.
They are saved in KVA files.

Calibration
**************
Calibration is required to make measurements in real world units such as meters or seconds.
Kinovea has a number of calibration sub-systems:

- Spatial calibration by line for a perfectly frontal view.
- Spatial calibration by a rectangle in perspective for a non-frontal view.
- Lens distortion calibration.
- Time calibration (origin and "scale" from capture frame rate).


Camera motion estimation, Camera tracking
*******************************************
Camera motion estimation calculates the rotation and zoom of the camera between frames.
Drawings then take this motion into account when they are drawn 
so they appear fixed in the world even if the camera moves.

 
Capture folders
********************


Context, Context variables
****************************


Delay, Delay buffer
***********************


Demosaicing, Demosaicking, Debayering
**************************************




Drawing, Drawing tools
***********************
Kinovea drawings are vector based and their points can be moved after they are created.
Some drawings can be tracked over time.

Frame rate
************
Kinovea deals with multiple frame rates:

- camera frame rate: frame rate *configured* in the camera (ex: 200 fps)
- capture frame rate: frame rate actually *captured* by the camera (ex: 195 fps)
- capture screen "display frame rate": refresh rate of the capture screen (ex: 10 fps)
- video frame rate: nominal playback rate stored as a metadata in the video file (ex: 30 fps)
- playback frame rate: frame rate at which the video is being played back.

When capturing from a high speed camera (capture frame rate > 150 fps) 
it is customary to set the video frame rate to a lower value (ex: 30 fps) to allow for smooth playback.

Knowing the capture frame rate is important for time-based measurements such as speed and acceleration.

.. _intra-only:
Intra-only, Intra-frame, All-i, All-Intra
******************************************
Intra-only is an encoding strategy for video files where each frame is encoded independently from the others.
This is good for frame by frame navigation and Kinovea uses this by default when capturing and exporting videos.

It contrasts with Long-GOP encoding. 
Smartphones, action cameras and web videos typically use Long-GOP encoding to save space 
while high-end cameras and camcorders often have the option to use intra-only encoding.

Key frame, Key image
***************************

Kinematics
******************
Quantities such as position, velocity or acceleration.
These can be computed from the pixel coordinates of tracked points and are supported in Kinovea.
Acceleration values should not be used directly though as they are too sensitive to noise.

Kinetics, Dynamics
*********
Quantities such as force, torque, momentum or energy.
These require mass and inertia properties of the objects to be computed and are not supported in Kinovea.

Kinogram
*********
A composite image combining multiple frames from the video sequence.
The source frames can be taken at regular intervals or at specific events such as maximum extension of a joint.

KVA
*****************
KVA is the main file format used by Kinovea to save annotations. This is an XML based format.

Long-GOP
**********
Long-GOP is an encoding strategy for video files where most frames depend on other frames to be decoded.
This is good for compression but makes it more difficult to navigate frame by frame.
See :ref:`Intra-only <intra-only>`.

Markerless tracking, Human pose estimation
******************************************
When the subject does not wear any markers tracking often fails to follow the joint positions accurately.
In such cases we can use manual digitization by going over the video frame by frame, 
or we cane use markerless tracking using machine learning models.

Markerless tracking using machine learning models is not directly supported in Kinovea but you can 
use Sports2D to process videos and export a .TRC file that can be imported in Kinovea.


Plane of motion
********************
Kinovea is a 2D program and all measurements are done on a single plane. 
This plane can either be parallel to the camera sensor (frontal view) or in perspective.

Screen, Player screen, Capture screen
******************************************
The primary user interface elements where videos and camera streams are displayed.
Screens are loaded in windows. A window can have zero, one or two screens.

Stabilization, Image stabilization
******************************************
2D image stabilization based on a previously tracked point, to remove camera shake.
If the camera undergoes rotation or zoom use camera tracking instead.


Stream format, Pixel format
******************************************
The stream format describes the content of the video frames as delivered by the camera.
Camera vendors tend to use different names for the same thing 
but in the end there are only a few formats we are interested in:

- MJPEG, JPEG, etc. Good for frame by frame navigation, low bandwidth and low CPU usage.
- RGB, RGB8, RGB24, RGB32. Avoid this if possible. High bandwidth and high CPU.
- BayerRG8, BayerBG8, etc. Use this if available and check "Enable software demosaicing".
- Mono8, Y800, for monochrome cameras.

Synchronization
******************************************
When two videos are loaded side by side in the same Kinovea window they can be synchronized by aligning their time origin.
Synchronization works on videos with different length, frame rate, 
and even different capture frame rate (one video in slow motion not the other).
It supports video playback and frame by frame navigation using common controls.


Template matching
******************************************
The main algorithm used in object tracking. It looks for a patch of the image in the consecutive images.
This algorithm will not recognize the template if it rotates.
Thus it works best when using round markers of a single color contrasting with the background.


Time origin
****************
This is the "zero" time reference for time-based measurements.
It can be placed on any frame and is also used for synchronization between two videos.
When using capture by trigger the time origin is set to the trigger frame.

Tracking, Object tracking
******************************************
Also known as "digitisation". Tracking consists in following the position of a point or an object over time.
This can be done manually or automatically using various algorithms. 
It is supported for single points or for multi-point drawings such as lines, poly-lines or angles.
For full human models consider using markerless tracking.
This is what enable kinematics measurements.

There is also camera tracking which follows the motion of the camera itself.

Window
******************************************
A window is an instance of Kinovea that can be opened and closed independently.
Windows have names and remember their state between sessions.
Windows contain zero, one or two screens and can be referenced by workspaces.

Working zone
******************************************
A segment of the video defined by an in-point and an out-point. 
The playback and all operations are limited to this zone.
If the memory allows it, the working zone is cached in memory for faster frame by frame navigation.


Workspace
******************************************
A workspace in Kinovea is a collection of related windows that can be started together.
The workspace itself doesn't contain any data apart from the list of windows.

















