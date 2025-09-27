
Kinograms
=============

Introduction
-------------------

Kinograms show multiple frames of the video at the same time.

The two main use-cases for kinograms are 1. the full decomposition of the motion, typically using a large grid and regular intervals, 
and 2. the creation of reports highlighting the posture at standard key moments of the motion, 
using fewer images at non regular intervals.

Full decomposition:

.. image:: /images/observation/kinogram-mahuchikh.jpg


Key points:

.. image:: /images/observation/kinogram-baseball.jpg


To enter the Kinogram mode, use the menu :menuselection:`Video --> Kinogram`. 

.. tip:: The Kinogram mode is only enabled when the entire working zone is cached in memory. 
    To change the amount of memory used for the cache go to :menuselection:`Options --> Preferences --> Playback --> Memory`

To exit the Kinogram mode right click in the image background and use the menu :menuselection:`Exit Kinogram`. 
Alternatevely, use the exit button at the top right of the playback screen or select another video mode.


General 
--------------

When the Kinogram mode is activated the main viewport displays a collection of frames taken from the video, 
by default spaced at regular intervals. 

The playback controls are still active and the current frame is highlighted in blue. 
The drawing tools can be used to add annotations on top of the composite. 

.. image:: /images/observation/kinogram-furlani-annotations.jpg

.. tip:: The Kinogram mode viewport is at the same aspect ratio as the original video, 
    but the result can be saved at higher resolution and will not include the empty areas outside the Kinogram itself.


Adjusting the content of the cells
-------------------------------------

Using the left mouse button, drag the images around to select which area of the original video frame should be displayed inside a particular cell.

To adjust the *time* reference of a cell, use the :kbd:`ALT` key and scroll backward or forward with the mouse wheel while hovering above the cell.


Parameters
--------------
The parameters of the kinogram can be controlled from the context menu :menuselection:`Configuration…`.


.. image:: /images/observation/kinogram-configuration.png
   
- Table : The number of columns and rows of the kinogram.
- Crop size : the size of the area of the original images extracted into the cells of the kinogram.
- Border color : Color of the border between the cells.
- Label color: color used for the time or frame number labels.
- Label size: font size used for the time or frame number labels.

.. tip:: All options in this dialog change the kinogram in real time, except for the crop size. 
    Use the Apply button to integrate crop size changes without quiting the configuration dialog.

Toggles
----------------

Other options are available via the :menuselection:`Options` menu.

.. image:: /images/observation/kinogram-toggles2.png
    
- Right to left : Enable this if the athlete is moving right-to-left. This configures the kinogram to use the top-right cell as the first cell and progress right to left for each row.
- Show border: whether to show the outline of the cells.
- Auto-interpolate: when this option is enabled dragging the cell content will automatically interpolate the neighboring cells to match the motion. If this is disabled you can still trigger it manually by using the menu :menuselection:`Action --> Interpolate tiles`.

Information labels
----------------------

Small labels giving information about each cell can be shown by using the Labels menu.

.. image:: /images/observation/kinogram-labels2.png

- Clock: shows the time of the image in the cell, taking into account the time origin and scale if configured.
- Frame number: shows the cell index within the Kinogram.

The labels can be moved around by dragging. 
To move all the labels at once, use the :kbd:`SHIFT` key while dragging them. 
This is typically used to move all the labels to a particular corner of their cell.

To reset the labels to their default location use the menu :menuselection:`Action --> Reset label positions`.

.. tip:: The time shown uses the global time code format option, you can change this from the main menu :menuselection:`Options --> Time`.

Saving
----------------

The kinogram configuration is saved as part of the KVA file (menu :menuselection:`Save annotations…`) and will be restored when the video is opened again.

To save the kinogram image itself use the menu :menuselection:`Save image` in the context menu of the kinogram mode. 
This will ask for the output image size. 
Since the kinogram is a composite of images of the original video you may save it at a larger resolution without loosing quality.

.. image:: /images/observation/kinogram-save.png

