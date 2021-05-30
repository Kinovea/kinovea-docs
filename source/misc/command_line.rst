
Command line options
====================

Kinovea can be started from the command line.

Usage
-----

kinovea.exe 

    [-name <string>] [-hideExplorer] [-workspace <path>] [-video <path>] [-speed <0-200>] [-stretch]

Options
-------

- -name <string>: name of this instance of Kinovea. Used in the window title and to select a preference file.
- -hideExplorer: the explorer panel will not be visible. Default: false.
- -workspace <path>: path to a Kinovea workspace XML file. This overrides other video options. To create a workspace file use the menu Option > Workspace > Export workspace.
- -video <path>: path to a video to load.
- -speed <0-200>: playback speed to play the video, as a percentage of its original framerate. Default: 100.
- -stretch: The video will be expanded to fit the viewport. Default: false.

Examples
--------

.. code-block::

    > kinovea.exe -video test.mp4 -stretch
    > kinovea.exe -video test.mp4 -speed 50
    > kinovea.exe -name Replay -workspace myReplayWorkspace.xml

