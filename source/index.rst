%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Kinovea reference manual
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the manual for `Kinovea <https://www.kinovea.org>`__.

Kinovea is a video annotation tool designed for motion analysis in sport. Its main features revolve around the study and capture of short sport video sequences.

For a single-page overview of the features of Kinovea check the `Features <https://www.kinovea.org/features.html>`__ page on the website.

.. tip:: 
    This manual can be used offline: `download the manual (zipped web pages) <Kinovea-Manual-0.9.5.zip>`__.

The sections below and the table of content on the left side let you access the documentation for your topic of interest.
You can also use the search function in the top left corner.

    .. container:: tocdescr

        .. container:: descr

            .. figure:: /images/home/userinterface.jpg
                :target: userinterface/ui.html

            :doc:`User interface </userinterface/ui>`
                The main window, basic concepts and the preference pages.
                
        .. container:: descr

            .. figure:: /images/home/observation3.jpg
                :target: observation/introduction.html

            :doc:`Observation </observation/introduction>`
                Visual inspection, image adjustment, stabilization and kinograms.
                
        .. container:: descr

            .. figure:: /images/home/comparison.jpg
                :target: comparison/comparison.html

            :doc:`Comparison </comparison/comparison>` 
                Comparing and synchronizing two videos side by side.
                

        .. container:: descr

            .. figure:: /images/home/annotation.png
                :target: annotation/annotations.html

            :doc:`Annotation </annotation/annotations>`
                Tools to annotate videos, mark key moments and study posture.

        .. container:: descr

            .. figure:: /images/home/measurement.jpg
                :target: measurement/measurement.html

            :doc:`Measurement </measurement/measurement>`
                Calibration and measuring times, cadence, distances and angles.



        .. container:: descr

            .. figure:: /images/home/tracking2.jpg
                :target: tracking/tracking.html

            :doc:`Tracking </tracking/tracking>`
                Tracking joints and objects, and compensating for camera motion.


        .. container:: descr

            .. figure:: /images/home/kinematics.png
                :target: kinematics/kinematics.html

            :doc:`Kinematics </kinematics/kinematics>`
                Plotting and exporting kinematics diagrams.


        .. container:: descr

            .. figure:: /images/home/export.png
                :target: export/videos.html

            :doc:`Export </export/videos>`
                Exporting videos, images, reports and spreadsheets.


        .. container:: descr

            .. figure:: /images/home/cameras2.jpg
                :target: capture/capture.html

            :doc:`Capture </capture/capture>`
                Capture system, camera management and supported camera types.


        .. container:: descr

            .. figure:: /images/home/capture.jpg
                :target: recording/recording.html

            :doc:`Recording </recording/recording>`
                Recording options, capture folders, triggers and context variables.
                
                
        .. container:: descr

            .. figure:: /images/home/delay-replay.jpg
                :target: delay/live_delay.html

            :doc:`Delay & Replay </delay/live_delay>`
                Live delay and instant replay mechanism.

        .. container:: descr

            .. figure:: /images/home/advanced.jpg
                :target: advanced/multi_tasking.html

            :doc:`Advanced </advanced/multi_tasking>`
                Multi-tasking, automation, command line interface, programmatic control.


        .. container:: descr

            :doc:`Misc </misc/faq>`
                FAQ, updating and general information about the project.


This manual is maintained by volunteers.
If you find something that is confusing, wrong, or otherwise needs to be edited,
`let us know <https://github.com/Kinovea/kinovea-docs/issues>`__.


.. toctree::
    :titlesonly:
    :hidden:
    :caption: User interface

    userinterface/ui
    userinterface/main_menu
    userinterface/browser_view
    userinterface/preferences
    userinterface/glossary

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Observation

    observation/introduction
    observation/playback_ui
    observation/image_transformation
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

    annotation/annotations
    annotation/key_image_management
    annotation/general_tools
    annotation/posture_tools
    annotation/style_and_opacity
    annotation/importing_images
    annotation/annotation_files
    annotation/importing_data

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Measurement

    measurement/measurement
    measurement/calibration_space
    measurement/calibration_lens
    measurement/calibration_time
    measurement/calibration_validation
    measurement/guidelines
    measurement/coordinate_system
    measurement/measuring_times
    measurement/measuring_cadences
    measurement/measuring_distances
    measurement/measuring_angles
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Tracking

    tracking/tracking
    tracking/tracking_algorithms
    tracking/trajectory
    tracking/trackable_drawings
    tracking/markerless_tracking
    tracking/camera_motion_estimation
    tracking/camera_compensated_annotations
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Kinematics
    
    kinematics/kinematics
    kinematics/scatter
    kinematics/linear
    kinematics/angular
    kinematics/angle_angle

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Export
    
    export/export
    export/videos
    export/images
    export/documents
    export/spreadsheets
    
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Capture

    capture/capture
    capture/user_interface
    capture/hardware_directshow
    capture/hardware_machine_vision
    capture/hardware_network
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
    advanced/workspaces
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

