%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    Kinovea |release| user guide
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

Welcome to the official user guide for Kinovea.

(Intro paragraph about the program.)


Getting started
===============

    - Features overview
    - Frequently asked questions
    - Terms of use
    - Installation (.zip vs .exe, .NET compat, min. requirements)

Sections
========

.. toctree::
   :maxdepth: 2

   userinterface/index

.. toctree::
   :maxdepth: 2

   observation/index

.. toctree::
   :maxdepth: 2

   comparison/index




Manual toc
==========

- User interface
    - User interface basics (explorer panels, browser panel, full screen)
    - Changing the language of the user interface.
    - Running multiple instances of Kinovea (+ preferences)
    - Workspaces.
    - Preferences.
    - Command line options.
    - Control from other applications. (WM_COPYDATA).

- Observation 
    - Loading videos (videos, images, image sequences)
    - Playback screen user interface. (toolbar)
    - Navigating the video (speed control, frame by frame, pagination)
    - Establishing a working zone (memory buffer)
    - Image geometry (rotation, aspect ratio, mirroring, deinterlacing, debayering).
    - Zoom and magnification.
    - Time display.
    - Capture framerate.
    - Broken framerate.
    - Overview function.
    - Reverse function.
    
- Comparison
    - Synchronization mechanisms (time origin, time independent).
    - Joint controls (navigation).
    - Superposition.
    - Linked speed

- Annotation
    - Time origin
    - Annotation tools (labels, numbers, pencil, arrows, lines, markers, etc. = any tool that can be used to annotate.)
    - Annotation style and opacity mechanism.
    - Keyframe comments
    - Importing images and vector drawings (copy & paste between screens, from explorer)
    - KVA file format (saving & loading.)
    - Importing subtitles, openPose.

- Measurement
    - The coordinate system.
    - Calibration mechanisms (Line, grid.)
    - Lens distortion calibration and compensation.
    - Measuring time. (origin, units, capture framerate)
    - Measuring distances (units).
    - Measuring angles.
    - Measuring linear and angular speed.
    - Tracking objects or body joints. (trajectory, objects, default params)
    - Scatter diagram.
    - Linear kinematics diagram.
    - Angular kinematics diagram.
    - Angle-angle diagram.
    - Coordinates filtering.
    - Exporting data.

- Live capture
    - Listing cameras.
    - Supported hardware. (Webcams, IP cameras + smartphones, Machine vision cameras.)
    - Configuring cameras (+ forgetting camera configuration).
    - Capture screen user interface.
    - Live delay mechanism. (memory buffer)
    - Recording (compressed/uncompressed, display fps). 
    - Recording modes (+ fps replacement).
    - Output file naming.
    - Recording automation. (duration + command line)
    - Replay folder observer.

- Export 
    - Exporting data (KVA, measurement, spreadsheet).
    - Exporting video.
    - Exporting images.
    - Exporting slideshow and paused video.
    - Citation.
    
- Maintenance
    - Checking for updates.
    - Logs.
    - Reporting bugs.
    - Getting more help + communication channels.
