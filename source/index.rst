%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Kinovea reference manual
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the manual for `Kinovea <https://www.kinovea.org>`__.

Kinovea is a video annotation tool designed for motion analysis.
It features utilities to capture, slow down, compare, annotate and measure motion in videos.

For a single-page overview of the features of Kinovea you may consult the `Features <https://www.kinovea.org/features.html>`__ page on the website.

.. tip:: 
    This manual can be used offline: `download the manual (zipped web pages) <Kinovea-Manual-0.9.5.zip>`__.

The sections below and the table of content in the sidebar should let you access the documentation for your topic of interest. 
You can also use the search function in the top left corner.

    .. container:: tocdescr

        .. container:: descr

            .. figure:: /images/home/userinterface.jpg
                :target: userinterface/index.html

            :doc:`/userinterface/index`
                Description of the main window, workspaces and the preference pages.

        .. container:: descr

            .. figure:: /images/home/observation.jpg
                :target: observation/index.html

            :doc:`/observation/index` 
                Functions to control video time, image aspect, and synchronize two videos.

        .. container:: descr

            .. figure:: /images/home/annotation.png
                :target: annotation/index.html

            :doc:`/annotation/index`
                Tools to annotate videos with drawings, text, highlight key moments and use posture references.

        .. container:: descr

            .. figure:: /images/home/measurement.png
                :target: measurement/index.html

            :doc:`/measurement/index`
                Functions to calibrate space and time, measure intervals, positions, distances, angles, and track kinematics.

        .. container:: descr

            .. figure:: /images/home/capture.jpg
                :target: capture/index.html

            :doc:`/capture/index`
                Subsystem to capture, delay, and record live cameras.

        .. container:: descr

            .. figure:: /images/home/export.png
                :target: export/index.html

            :doc:`/export/index`
                Functions to save videos and measurements for other applications.

        .. container:: descr

            :doc:`/misc/index`
                Various topics related to programmatically controlling Kinovea and general information about the project.


This manual is maintained by volunteers.
If you find something that is confusing, wrong, or otherwise needs to be edited,
`let us know <https://github.com/Kinovea/kinovea-docs/issues>`__.


.. toctree::
    :titlesonly:
    :hidden:
    :caption: User interface

    userinterface/overview
    userinterface/workspaces
    userinterface/instances
    userinterface/preferences

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Observation and comparison

    observation/loading
    observation/playback_ui
    observation/image_geometry
    observation/time_calibration
    observation/comparison
    observation/overview
    observation/reverse

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Annotation

    annotation/general
    annotation/tools
    annotation/style_and_opacity
    annotation/time_origin
    annotation/importing_images
    annotation/annotation_files
    annotation/importing_data

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Measurement

    measurement/calibration
    measurement/guidelines
    measurement/coordinatesystem
    measurement/lensdistortion
    measurement/time
    measurement/distance
    measurement/angle
    measurement/trajectory
    measurement/tracking
    measurement/kinematics
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Capture

    capture/listing
    capture/userinterface
    capture/hardware
    capture/livedelay
    capture/recording
    capture/replay

.. toctree::
    :titlesonly:
    :hidden:
    :caption: Export
    
    export/video
    export/data
    
.. toctree::
    :titlesonly:
    :hidden:
    :caption: Miscellaneous topics

    misc/faq
    misc/update
    misc/command_line
    misc/copydata
    misc/comms

