Post-recording commands 
=========================

Post-recording commands let you execute external programs right after a recording is finalized, using the created file as an argument to these programs. This can be used to automatically copy the file to a different location, perform compression or apply post-processing.

Command editor
----------------

To enable post-recording commands right click the background of a capture screen and choose the menu :menuselection:`Post-recording command…`. Check the :guilabel:`Enable post-recording command` checkbox and enter the command line to execute.

.. image:: /images/advanced/prc2.png

You can call multiple programs, add each command on its own line. The commands are executed sequentially and the whole thing runs in a background thread.

Lines starting with ``#`` are treated as comments and ignored.

Variables
---------

Use the button :guilabel:`Insert a variable` to insert context variables that will be replaced with actual values when the command is executed. In addition to the user-defined variables and the date and time built-in variables, the following are available in this context:

=================   ============= 
Variable               Meaning
=================   =============
``%filepath%``          The full path to the video file.
``%folderpath%``        The full path to the capture folder containing the video file.
``%filename%``          The name of the recorded file.
``%kva%``               The name of the KVA file created alongside the recording.
=================   =============


.. image:: /images/advanced/prc-insert-variable.png
