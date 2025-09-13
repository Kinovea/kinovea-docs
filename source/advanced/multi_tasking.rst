
Multi-window system
=====================================

Kinovea implements a multi-window system where each opened window (instance of Kinovea) remembers its own content and state.

Multiple instances of Kinovea can run at the same time without interfering with each other. The core preferences are shared and synchronized between instances.

You can assign names to windows to associate them with specific tasks.

.. note:: We use the terms "Window" and "Instance" interchangeably in this documentation.

This system supports the following use cases:

- Associating windows with specific tasks or projects, for example one window is associated with a long term research project and another is used for quick review.

- Keeping track of a set of windows that are meant to work together at the same time, for example two windows for capture and one window for dual replay. Multiple such collections of windows can be stored in the system and reopened as needed. Individually these small groups of windows are known as workspaces.




Starting new windows
--------------------

To start a new window use the menu :menuselection:`Window --> Open new window`.


Reopening previous windows
--------------------------

When Kinovea is started it will reopen the last window that was open when it was last closed.

To reopen another window use the menu :menuselection:`Window --> Reopen window` and select the desired window from the list. Alternatively use the Window manager, :menuselection:`Window --> Window manager…`, and select from the list.

.. image:: /images/advanced/window-reopen2.png

The icon next to the window name or id indicates the type of content it is hosting.


Window name
-------------------------------

By default windows are assigned random Ids to identify them internally.

You can assign a custom name to each window by using the menu :menuselection:`Window --> Window properties…`.

.. image:: /images/advanced/window-props.png

The name of the Window can be seen in the window title bar in square brackets.

.. image:: /images/advanced/window-title.png
    

.. warning:: Do not use the same name for different windows. Even though windows have internal unique Ids, the name is used in certain functions like identifying windows in the command line options or for interprocess communication.



Startup options
----------------

Each window defines startup options that are used when the window is opened.

To edit the startup options of a window use the menu :menuselection:`Window --> Window properties…`.

The following options are available:

- :guilabel:`Open the file browser`: The window starts on the file browser, no video or camera is loaded. 

- :guilabel:`Continue where you left off`: The window restores its previous content and state. This is the default option.

- :guilabel:`Open specific content`: The window loads a specific video or camera, or two screens with videos and/or cameras. This option is useful if you want to create a stronger link between a window and a specific task or project. Even if you change the content or close the screens, the next time you open the window it will reload the specified content.

To assign the current content of a window to its startup option use the button :guilabel:`Import current screens`.


Deleting old windows
---------------------------

To delete old windows use the menu :menuselection:`Window --> Window manager…`, select the window to delete from the list, and click the :guilabel:`Delete` button.

.. image:: /images/advanced/window-delete.png



.. tip:: Window state is stored in XML files in the application data folder under the `Windows` subfolder.
    You can manually delete old window files from this folder if needed.



Global preferences vs window state
-----------------------------------

It can be helpful to understand what is saved in the core preferences and what is saved in the window state.

Everything that is modified via the menu :menuselection:`Options --> Preferences…` is saved in the core preferences and shared between all windows.

This include:

- The general behavior of Kinovea, language, time format, units, drawing defaults, keyboard shortcuts, etc.
- The central repository of capture folders that the capture screens and replay screens reference
- The list of recently opened files
- The list of known cameras and their configuration


Whereas the visual content of each window and the state of the player or capture screens are saved at the window level. 

This include:

- The layout of the panels and other UI elements
- In player screens: the speed slider and the image "stretch" state
- In capture screens: the selected capture folder, the output file name, the live delay and maximum duration, the post-recording command.




