
Workspaces
=====================================

A workspace is a predefined set of windows that are meant to be opened together. 
Each window in the workspace has its own content and state.

Workspaces are built on top of the :doc:`/advanced/multi_tasking`.

To create and delete workspaces, use the menu :menuselection:`Window --> Manage workspaces…`.


Workspace manager
-------------------

.. image:: /images/advanced/workspace-manager.png
    
    
The workspace manager is divided in two areas. 
At the top, the workspace list shows the existing workspaces and lets you create, rename and delete them, 
or create a desktop shortcut to open a specific workspace. At the bottom, the window list shows the windows that are part of the selected workspace.


=============    ========================
|Add|             Creates a workspace referencing the currently active windows and prompts for a name.
|Rename|          Opens a dialog to rename the selected workspace.
|Shortcut|        Creates a shortcut on the desktop to open the selected workspace.
|Delete|          Deletes the selected workspace.
=============    ========================

.. |Add| image:: /images/advanced/icons/add-16.png
.. |Rename| image:: /images/advanced/icons/rename-16.png
.. |Shortcut| image:: /images/advanced/icons/shortcut2.png
.. |Delete| image:: /images/advanced/icons/bin_empty.png

Creating shortcuts
***************************

To create a shortcut to open a specific workspace, use the button :guilabel:`Create a desktop shortcut`. 
(Same function as the one next to the workspace list.)

The shortcut will automatically be created on the desktop.

When the shortcut is used, Kinovea will start and reopen all the windows defined in the workspace.

.. image:: /images/advanced/shortcut.png


Storage
****************

Workspace files are saved as XML files in the application data folder under the `Workspaces` subfolder.

A workspace only contains references to windows. It does not store any state by itself.

