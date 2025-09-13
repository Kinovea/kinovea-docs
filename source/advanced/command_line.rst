
Command line options
====================

Kinovea can be started from the command line. There are essentially two modalities of operation:

* Starting Kinovea with a specific video file, with some extra options.
* Starting a specific Kinovea window or group of windows, which can contain their own content and settings.

Usage
-----

.. code-block::

    > kinovea.exe 
        [-video <path>] [-speed <0..200>] [-stretch] [-hideExplorer]
        [-name <string>]
        [-id <string>]


Options
-------

``-video`` ``<path>``
    Path to the video or image to load.

``-speed`` ``<0..200>``
    Playback speed to play the video, as a percentage of its original playback framerate. 
    
    Default: ``100``.

``-stretch``
    The video will be expanded to fit the viewport. Default: ``false``.

``-hideExplorer``
    The navigation pane on the left of the main area will be closed. Default: ``false``.

``-name`` ``<string>``
    Name of the Kinovea window to load. 
    
    The name of a window is set from the window properties dialog: :menuselection:`Window --> Window properties…`.

``-id`` ``<string>``
    Id of a Kinovea window to load. This option is meant to be used internally between instances of Kinovea.

Examples
--------

.. code-block::

    > kinovea.exe -video test.mp4 -stretch
    > kinovea.exe -video test.mp4 -speed 50
    > kinovea.exe -name Replay

