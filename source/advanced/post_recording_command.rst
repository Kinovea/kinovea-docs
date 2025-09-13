Post-recording commands 
=========================

Post-recording commands let you execute external programs right after a recording is finalized. 
The created file can be passed as an argument to the external program. 

Some use cases include:

- copying the file to a backup location.
- converting the recorded file to a different format.
- running a post-processing application to transform the video in some way or extract images.

Command editor
----------------

To enable post-recording commands right click the background of a capture screen and choose the menu :menuselection:`Post-recording command…`. Check the :guilabel:`Enable post-recording command` checkbox and enter the command line to execute.

You can call multiple programs, add each command on its own line. The commands are executed sequentially and the whole thing runs in a background thread.

Lines starting with ``#`` are treated as comments and ignored.

.. image:: /images/advanced/prc3.png


Variables
---------

Use the button :guilabel:`Insert a variable` to insert context variables that will be replaced with actual values when the command is executed. In addition to the user-defined variables and the date and time built-in variables, the following are available in this context:

=====================   ============= 
Variable                Meaning
=====================   =============
``%filepath%``          The full path to the video file.
``%folderpath%``        The full path to the capture folder containing the video file.
``%filename.ext%``      The name of the recorded file including the extension.
``%filename%``          The name of the recorded file without the extension.
``%ext%``               The extension by itself, without the leading dot.
``%kva%``               The name of the KVA file created alongside the recording.
=====================   =============


.. image:: /images/advanced/prc-insert-variable2.png
    
    
FFmpeg
---------

Kinovea ships with the ffmpeg executable that can be used for video conversion and compression. 

See the documentation of ffmpeg at `https://ffmpeg.org/ <https://ffmpeg.org/>`_ for usage instructions.

Example command that encodes the recorded video using the H.264 codec:

.. code-block:: none

    ffmpeg -i "%filepath%" -vcodec libx264 "%folderpath%\%filename%_compressed.mp4"
    

