# kinovea-docs

Kinovea user documentation project

**Goal**: Modernize and update Kinovea's user manual.

**Main website**: https://www.kinovea.org/


Introduction
------------
Kinovea is an open source video player and camera capture software with features tailored to sports applications such as comparison, annotation and measurement. It is a somewhat mature project, it has been in development since 2004, has been downloaded more than a million times and is cited in many scientific papers in the field of sports science. 

User manual update project
--------------------------
The user manual for Kinovea was last updated in 2011 for version 0.8.15. Since then multiple beta versions have been released. The current versions are now just as stable as the old version 0.8.15 and it is only this lack of an up-to-date manual that is preventing their release as an official stable version to replace the main download link.

This project is an effort to update the documentation to integrate all the changes that were made during the intervening years, as well as update the way the documentation is authored to make it easier to export it to HTML and PDF and translate it to other languages.

Contact
-------
Get in touch here: joan@kinovea.org

Plans
-----
The documentation will be moved to the ReadTheDocs platform where it will be easier to work with, easier to conform to modern documentation standards and will provide native export options and translation facilities.

A tentative table of content is provided below as a template. That being said topics pages can be merged, split or reorganized, they are just provided to give an overview of the kind of topics involved and the scale of the project. Many of these pages already have a corresponding entry in the old manual while others are new.

Resources
---------
The current documentation can be found here: https://www.kinovea.org/help/en/index.htm 

This documentation was authored via a Wiki and transformed to HTML using custom scripts.

List of successive release posts since the last update, containing descriptions of new features (some of the features have seen multiple updates over the course of these versions):
* [0.8.16](https://www.kinovea.org/en/forum/viewtopic.php?id=483)
* [0.8.17](https://www.kinovea.org/en/forum/viewtopic.php?id=598)
* [0.8.18](https://www.kinovea.org/en/forum/viewtopic.php?id=628)
* [0.8.19](https://www.kinovea.org/en/forum/viewtopic.php?id=638)
* [0.8.20](https://www.kinovea.org/en/forum/viewtopic.php?id=664)
* [0.8.21](https://www.kinovea.org/en/forum/viewtopic.php?id=700)
* [0.8.22](https://www.kinovea.org/en/forum/viewtopic.php?id=732)
* [0.8.23](https://www.kinovea.org/en/forum/viewtopic.php?id=745)
* [0.8.24](https://www.kinovea.org/en/forum/viewtopic.php?id=771)
* [0.8.25](https://www.kinovea.org/en/forum/viewtopic.php?id=816)
* [0.8.26](https://www.kinovea.org/en/forum/viewtopic.php?id=854)
* [0.8.27](https://www.kinovea.org/en/forum/viewtopic.php?id=886)
* [0.9.1](https://www.kinovea.org/en/forum/viewtopic.php?id=928)
* [0.9.2 / 0.9.3](https://www.kinovea.org/en/forum/viewtopic.php?id=953)


Tentative TOC
-------------

- User interface
    - User interface basics (explorer panels, browser panel, full screen)
    - Changing the language of the user interface.
    - Running multiple instances of Kinovea (+ preferences)
    - Command line options.
    - Workspaces.
    - Keyboard shortcuts.
    - Control from other applications.

- Observation 
    - Loading videos (videos, images, image sequences)
    - Playback screen user interface. (incl. +toolbar)
    - Navigating the video (speed control, frame by frame, pagination)
    - Establishing a working zone (incl. memory buffer)
    - Image geometry (rotation, aspect ratio, mirroring, deinterlacing, debayering).
    - Zoom and magnification.
    - Time display.
    - Capture framerate.
    - Fixing broken framerate.
    - Using the overview function.
    - Using the reverse function.
    
- Comparison
    - Synchronization mechanisms (time origin).
    - Joint controls (navigation).
    - Superposition.
    - Linked speed controls.

- Annotation
    - Time origin.
    - Annotation tools (labels, numbers, pencil, arrows, lines, markers, etc. = any tool that can be used to annotate. + copy & paste)
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

