%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Kinovea reference manual
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the manual for `Kinovea <https://www.kinovea.org>`__.

Kinovea is a video annotation tool designed for motion analysis in sport. Its main features revolve around the study and capture of short sport video sequences.

For a single-page overview of the features of Kinovea check the `Features <https://www.kinovea.org/features.html>`__ page on the website.

.. tip:: 
    This manual can be used offline: `download the manual (zipped web pages) <Kinovea-Manual-0.9.5.zip>`__.

The sections below and the table of content in the sidebar let you access the documentation for your topic of interest.
You can also use the search function in the top left corner.

    .. container:: tocdescr

        .. container:: descr

            .. figure:: /images/home/userinterface.jpg
                :target: userinterface/index.html

            :doc:`/userinterface/index`
                The main window, basic concepts and the preference pages.
                
                

        .. container:: descr

            .. figure:: /images/home/observation3.jpg
                :target: observation/index.html

            :doc:`/observation/index` 
                Visual inspection, image adjustment, stabilization and creating kinograms.
                
        .. container:: descr

            .. figure:: /images/home/comparison.jpg
                :target: comparison/index.html

            :doc:`/comparison/index` 
                Comparing and synchronizing two videos side by side.
                

        .. container:: descr

            .. figure:: /images/home/annotation.png
                :target: annotation/index.html

            :doc:`/annotation/index`
                Tools to annotate videos, mark key moments and study posture.

        .. container:: descr

            .. figure:: /images/home/measurement.jpg
                :target: measurement/index.html

            :doc:`/measurement/index`
                Calibration and measuring times, cadence, distances and angles.



        .. container:: descr

            .. figure:: /images/home/tracking2.jpg
                :target: tracking/index.html

            :doc:`/tracking/index`
                Tracking joints and objects, and compensating for camera motion.


        .. container:: descr

            .. figure:: /images/home/kinematics.png
                :target: kinematics/index.html

            :doc:`/kinematics/index`
                Plotting and exporting kinematics diagrams.


        .. container:: descr

            .. figure:: /images/home/export.png
                :target: export/index.html

            :doc:`/export/index`
                Exporting videos, images, reports and spreadsheets.


        .. container:: descr

            .. figure:: /images/home/cameras2.jpg
                :target: capture/index.html

            :doc:`/capture/index`
                Capture system, camera management and supported camera types.


        .. container:: descr

            .. figure:: /images/home/capture.jpg
                :target: recording/index.html

            :doc:`/recording/index`
                Recording options, capture folders, triggers and context variables.
                
                
        .. container:: descr

            .. figure:: /images/home/delay-replay.jpg
                :target: delay/index.html

            :doc:`/delay/index`
                Live delay and instant replay mechanism.



        .. container:: descr

            .. figure:: /images/home/advanced.jpg
                :target: advanced/index.html

            :doc:`/advanced/index`
                Multi-tasking, automation, command line interface, programmatic control.


        .. container:: descr

            :doc:`/misc/index`
                FAQ, updating and general information about the project.


This manual is maintained by volunteers.
If you find something that is confusing, wrong, or otherwise needs to be edited,
`let us know <https://github.com/Kinovea/kinovea-docs/issues>`__.


.. toctree::
    :titlesonly:
    :hidden:
    :caption: User interface

    userinterface/ui
    userinterface/concepts
    userinterface/preferences

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Observation

    observation/loading
    observation/playback_ui
    observation/image_geometry
    observation/stabilization
    observation/kinogram

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Comparison

    comparison/comparison
    comparison/synchronization
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Annotation

    annotation/general
    annotation/tools
    annotation/style_and_opacity
    annotation/importing_images
    annotation/annotation_files
    annotation/importing_data

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Measurement

    measurement/calibration_space
    measurement/calibration_lens
    observation/calibration_time
    measurement/guidelines
    measurement/coordinatesystem
    measurement/measuring_times
    measurement/measuring_cadences
    measurement/measuring_distances
    measurement/measuring_angles
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Tracking

    tracking/object_tracking
    tracking/tracking_algorithms
    tracking/trajectory
    tracking/camera_motion_estimation
    tracking/camera_compensated_annotations
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Kinematics
    
    kinematics/scatter
    kinematics/linear
    kinematics/angular
    kinematics/angle_angle

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Export
    
    export/videos
    export/images
    export/documents
    export/spreadsheets
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Capture

    capture/introduction
    capture/user_interface
    capture/listing
    capture/hardware_directshow
    capture/hardware_machine_vision
    capture/hardware_ipcameras
    capture/hardware_simulated
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Recording

    recording/recording
    recording/capture_folders
    recording/triggers
    recording/context_variables
    

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Delay and replay

    delay/live_delay
    delay/replay


.. toctree::
    :titlesonly:
    :hidden:
    :caption: Advanced

    advanced/multi_tasking
    advanced/post_recording_command
    advanced/command_line
    advanced/remote_control
    
        
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Miscellaneous topics

    misc/faq
    misc/update
    misc/comms

