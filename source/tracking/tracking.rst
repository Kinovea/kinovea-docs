Tracking
===========================

This section covers the features related to tracking points, objects, angles, polylines and other drawings, 
establishing moving coordinate systems and the estimation of the camera motion.

By itself tracking does not require calibration or a perfect frontal view. It is possible to get qualitative insights from the visual path of points or objects over time without calculating real world kinematics.
To calculate kinematics quantities such as speed or acceleration, calibration is necessary.

The following screenshot illustrates the main user interface for tracking points and drawings:

.. image:: /images/tracking/tracking-ui.jpg


Tracking of points, objects and people
--------------------------------------

- The fundamental tool of tracking is the "track", visually represented by :doc:`trajectory objects <trajectory>`.
- Kinovea implements several :doc:`tracking algorithms <tracking_algorithms>` with their own parameters.
- :doc:`Trackable drawings <trackable_drawings>` like angles, polylines or markers can have tracks attached to them.
- For full body tracking, when manual digitization is too time consuming and template-based tracking fails, we can turn to :doc:`markerless tracking <markerless_tracking>` using external machine learning frameworks.


Moving camera or moving coordinates
------------------------------------

- The :doc:`coordinate system <tracked_coordinates>` or the calibration objects themselves can be tracked.
- :ref:`2D image stabilization <stabilization>` uses a track to compensate for camera or object translation.
- To estimate more :doc:`complex camera motion <camera_motion_estimation>` there is a dedicated mode with its own interface.
- :doc:`Camera compensated annotations <camera_compensated_annotations>` stick to the real world despite camera motion.

