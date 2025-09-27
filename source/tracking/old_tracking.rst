Tracking distances and angles
=======================================

Introduction
------------
To track a drawing object over time follow these steps:

* Right click the object and choose :menuselection:`Tracking --> Start tracking`.
* Move the video forward using the :guilabel:`Next frame` button, the **mouse wheel** or the :guilabel:`Play` button.
* Adjust the points position as necessary during the path creation.
* To finish tracking, right click inside the tracking window and choose :menuselection:`Stop tracking`.

.. image:: /images/measurement/tracking-start.png

Each tool type defines exactly which ones of its points are tracked or not. The following drawing can be tracked:

* Position: Marker.
* Distance: Line.
* Angles: Angle, Goniometer, Angle-to-horizontal, Angle-to-vertical.
* Grids: Flat grid, Perspective grid.
* Complex tools: Human model, Bike fit, Archery, Canis, Equus, etc.

Tracking parameters
-------------------
Unlike the trajectory tool the sizes of the search and object windows cannot be directly modified from the object configuration dialog.
In order to change the default sizes for these windows go to :menuselection:`Options --> Preferences --> Drawings --> Tracking`.

.. tip:: Use the trajectory tool configuration dialog to visually figure out the appropriate size of the object and search window, then enter these parameters in the preferences.

Tracked coordinate system
-------------------------------
The calibration mechanism uses a line object or a plane object to define a coordinate system and transform pixel coordinates into real world coordinates.

If the object defining the calibration is itself tracked, the calibration will be updated at every frame.
This can be used to compensate a moving camera.

It is also possible to track the coordinate system origin while keeping the calibration static.
This can be used to obtain coordinates of a point relatively to a moving reference.

.. note:: Tracking the calibration object and tracking the coordinate system are not compatible with each other. The tracked calibration object redefines the coordinate system.

