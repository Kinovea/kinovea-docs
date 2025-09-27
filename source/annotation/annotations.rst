
Annotation user interface
==========================


Annotations are used to document key points, add commentary, drawings or insert reference images into the video. 
Certain tools can also be used to measure times, repetitions, angles or distances. 

The following screenshot describes the parts of the interface used for annotating videos.

.. image:: /images/annotation/annotations-ui.jpg

- The :ref:`annotation toolbar <annotationtoolbar>` has tools for adding drawings and key images.
- The :ref:`list of key images <keyimagelist>` shows thumbnails of the key images added to the video.
- The :ref:`drawings <drawings>` are added on top of the video.
- The :ref:`annotation pane <annotationpane>` has tabs for editing key images and drawings.

Some annotation features are not immediately visible in the screenshot

- :ref:`Other tools <othertools>` can be found in different places of the interface.
- :ref:`Big pointers <bigpointers>` can be used for presentation purposes.
- The :ref:`background layer <background>` sits between the video and the drawings.

Annotations can be saved and loaded using :doc:`annotation files <annotation_files>`. 

Certain external formats can be imported, see :doc:`importing data <importing_data>`.



.. _annotationtoolbar:

Annotation toolbar
---------------------

.. image:: /images/annotation/annotation-toolbar.png

The left part of the toolbar has the following general function buttons:

=======================    ========================
|Hand|                     Manipulates drawings or pans the image.
|KeyImage|                 Adds a key image at the current time.
|Commentary|               Toggles the annotation pane.
=======================    ========================

.. |Hand| image:: /images/annotation/icons/handtool.png
.. |KeyImage| image:: /images/annotation/icons/add-image-16.png
.. |Commentary| image:: /images/annotation/icons/sidepanel.png
    
The rest of the toolbar has the drawing tools.
 
There are more tools than those immediately visible. 
Buttons with a small arrowhead in the top-left corner contain other tools that can be accessed by doing a right click or a long click (click and hold) on the button.

.. image:: /images/annotation/tools_notch.png

A flying menu opens with the extra tools available.

.. image:: /images/observation/subtools.png
    
For a description of the individual drawing tools see :doc:`general_tools`, :doc:`posture_tools`, 
:doc:`/measurement/measuring_times`, :doc:`/measurement/measuring_cadences`, :doc:`/measurement/measuring_angles`, :doc:`/measurement/measuring_distances`.


To stop using a particular tool and come back to the hand tool you can also use the :kbd:`Escape` key.

.. tip:: You can use the middle mouse button to directly manipulate drawings without switching to the hand tool.


.. _keyimagelist:

List of key images
---------------------

.. image:: /images/annotation/keyimagelist.png

The list of key images presents an overview of all added key images.
It can be used to delete or move them in time using the context menu or dragging them to the timeline.

More about key images can be found in :doc:`key_image_management`.

.. tip:: You can close down this area by clicking the down arrow at the right of the annotation toolbar or by double-clicking the annotation toolbar.


.. _drawings:

Drawings
--------------------

Drawings are vector-based, they can be manipulated and resized after they have been added to the video.

They have a context menu that can be used to access tool-specific functions, copy and paste, and deletion.

For a description of the individual drawing tools see :doc:`general_tools`, :doc:`posture_tools`, 
:doc:`/measurement/measuring_times`, :doc:`/measurement/measuring_cadences`, :doc:`/measurement/measuring_angles`, :doc:`/measurement/measuring_distances`.

For editing style and opacity options see :doc:`style_and_opacity`.

The drawings can be attached to filmed objects even when the camera is moving, see :doc:`/tracking/camera_compensated_annotations`.

.. warning:: Drawings are created in key images. Deleting the key image deletes all the drawings in it.


.. _annotationpane:

Annotation pane
--------------------

The annotation pane has tabs to edit key images and drawings.

.. image:: /images/annotation/annotation-pane-tabs.png

=======================    ========================
|TabKF|                    :doc:`key_image_management`
|TabDrawings|              :doc:`style_and_opacity`
|TabTracking|              :doc:`/tracking/object_tracking`
=======================    ========================

.. |TabKF| image:: /images/annotation/icons/notes2-16.png
.. |TabDrawings| image:: /images/annotation/icons/editorcolor.png
.. |TabTracking| image:: /images/annotation/icons/trajectory6.png
    

.. _othertools:

Other tools 
---------------------

Some tools are not part of the annotation toolbar and can be found in other places in the interface.

- Trajectory objects are created by right clicking the video viewport and menu :menuselection:`Track path`
- The coordinate system is available in the main menu :menuselection:`Tools --> Coordinate System`
- The camera test grid is available in the main menu :menuselection:`Tools --> Camera Test Grid`
- Inserting an image or SVG as a reference is done using the main menu :menuselection:`Tools --> Import Image`


.. _bigpointers:

Big pointers
---------------------

For presentation purposes the hand tool can use a large image instead of the normal cursor. To enable this mode go to the main menu :menuselection:`Options --> Pointers` and select a pointer from there. This list of image-based pointers can be customized by adding new images to the "Pointers" directory under application data. 

.. image:: /images/annotation/pointer-big-hand.jpg
    
    
    
.. _background:
    
Background layer
----------------------

The background layer sits between the video image and the drawings. 
It can be used to make the drawings more visible against the video or, at full opacity, 
show only the annotations and trajectories on a plain background.

To change the background layer color and opacity right click in the background of the video and choose :menuselection:`Background…`. 
This option is also available in the main menu :menuselection:`Tools --> Background…`

.. image:: /images/annotation/background-opacity.jpg
    






