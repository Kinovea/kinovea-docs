
Running multiple instances of Kinovea
=====================================

It is possible to run multiple Kinovea at the same time on the same computer. 
This can be used to record more than two cameras, play more than two videos at the same time, or create more advanced setups for capture and replay or instrumentation scenarios.


.. note:: By default each instance has its own set of preferences separate from the others.
    This behavior is controlled by the option under Preferences > General > Instances have their own preferences.
    This option can only be changed from the first instance of Kinovea.

Instance name
--------------
Each instance is assigned a number in sequential order of launch and by default this number becomes the name of the instance.

The name of the instance can be seen in the window title bar in square brackets.

.. image:: /images/ui/instancename2.png

It is possible to customize the name of instances by passing the new name in the -name argument on the command line.

.. code-block:: console

    >kinovea.exe -name "MyInstance"

.. image:: /images/ui/instancenamecustom.png

.. tip:: Command line arguments can also be specified by creating a Windows shortcut on Kinovea.exe and editing the Target field in the shortcut properties.




