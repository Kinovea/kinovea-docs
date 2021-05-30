
Control from other applications
===============================

While Kinovea is running it is possible to send it commands from a third party application or script.
For example this can be used to trigger recording based on a software event.

The commands use the Windows messaging system and the WM_COPYDATA message.
The exact way to create these Windows messages depends on the programming language or platform used to write the third party application.
Each command has to be sent separately. There is no return value.

The general format of the messages is the following:

.. code-block::

    Kinovea:<Category>.<Command>

The list of categories and commands is available under Options > Preferences > Keyboard. 

For example:

.. code-block::

    Kinovea:CaptureScreen.ToggleRecording

    Kinovea:PlayerScreen.TogglePlay

.. tip:: This mechanism works even if Kinovea is not in the foreground. 
    If there are multiple instances of Kinovea running you will need to send the message to the correct instance based on its name.

