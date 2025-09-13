Synchronization
==============================

Synchronization mechanism
-------------------------
Two videos can be synchronized by setting their time origin to a common event visible on both videos.
When the videos are synchronized they will pass through their time origin at the same time.

To set the time origin in a video move to that point in the video 
and click the :guilabel:`Mark current time as time origin` button or right click the background of the video and choose the :menuselection:`Mark current time as time origin` menu.
Alternatively you can move each video to the correct point independently and use the :guilabel:`Synchronize videos on the current frames` button in the joint controls area.

.. image:: /images/observation/compare-syncpoint.png

During joint-playback, the synchronization mechanism means one video may start and/or end playing before the other.

To perform joint frame-by-frame navigation, move the cursor in the joint timeline or use the joint controls buttons.

.. image:: /images/observation/compare-synched.png

Joint controls
--------------
.. image:: /images/observation/joint-controls.png

The playback controls are the same as for individual playback screens but act on both videos at the same time.

The other buttons have the following functions:

- |JointOrigin| Set the time origin in both videos to their respective current time.
- |Merge| Enable or disable superposition of the videos into one another.
- |Swap| Swap the playback screens.

.. |JointOrigin| image:: /images/observation/icons/jointorigin.png
.. |Merge| image:: /images/observation/icons/syncmerge.png
.. |Swap| image:: /images/observation/icons/swap.png

Linked speed controls
---------------------
By default the speed controls in each playback screen are linked with each other:
lowering the playback speed in one video lowers it in the other.

The speed controls are independent of the frame rate of the video files so
this should apply a similar slow motion factor to both videos and keep the comparison meaningful.

.. tip:: If one of the video was captured with a high speed camera and has a different capture frame rate,
    this frame rate should be configured for this video via menu :menuselection:`Video --> Configure video timing`.
    Once this configuration is done both controls will still be coherent with each other.

If you are confident that you do not want the speed sliders to be linked together you may change the option in :menuselection:`Options --> Preferences --> Playback --> General --> Link speed sliders when comparing videos`.

