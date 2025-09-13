
General annotation tools
========================

Text
-------------------

.. |Label| image:: /images/annotation/icons/label.png
    
- |Label| **Text**
    

The text tool can be used to create small labels. It has an optional "leg" with an arrow or circle at the end to point at things or circle them.

The width of the leg can be configured independently of the text size. The background can be transparent or filled.

To edit the text of an existing label, double click it and start typing. To change the font size visually you can drag the bottom right corner of the label.


.. image:: /images/annotation/text.png



Numbers 
------------------


.. |Number| image:: /images/annotation/icons/number.png

- |Number| **Numbers**

The number tool can be used to add consecutive numbers.

There is only one number sequence per video, all the numbers are using the same style and size and are part of the same sequence. Using the delete menu only removes that particular number.

.. image:: /images/annotation/numbers2.png



Stickers
------------------

Stickers are pre-defined emoji images that can be added to the video to quickly illustrate a point without the need to create a text object or attach a comment.

To change the emoji used by a sticker double click it to open the selection dialog.

.. image:: /images/annotation/stickers3.jpg
    

Stickers can also be used for anonymization purposes on static images.
    
.. image:: /images/annotation/stickers.jpg




Pencil
-------------------

.. |Pencil| image:: /images/annotation/icons/pencil.png

|Pencil| **Pencil tool**

The pencil tool is used to create free-hand drawings.
The width of the stroke can be modified afterwards but the path is fixed.


.. image:: /images/annotation/brush.jpg


Line family
-------------------

.. |Line| image:: /images/annotation/icons/line.png
.. |Curve| image:: /images/annotation/icons/polyline.png
.. |Polyline| image:: /images/annotation/icons/polyline.png
.. |Rectangle| image:: /images/annotation/icons/rectangle.png
.. |Circle| image:: /images/annotation/icons/circle.png
.. |DistanceHorizontal| image:: /images/annotation/icons/distancehorizontal.png

- |Line| **Line**
- |Curve| **Curve**
- |Polyline| **Polyline**
- |Rectangle| **Rectangle**
- |Circle| **Circle**
- |DistanceHorizontal| **Distance horizontal**

.. image:: /images/annotation/line.png

The line tool and the circle tool can also be used to measure segment lengths and the radius or circumference of circles, see :doc:`/measurement/measuring_distances` for more information.

Furthermore the line tool can be used as a calibration stick. See :doc:`/measurement/calibration_space` for more information.

The circle and rectangle tools have an option toggle to be drawn as filled shapes. The circle tool also has an option toggle to draw its center.

.. image:: /images/annotation/circle2.png 



Arrow family
-------------------

.. |Arrow| image:: /images/annotation/icons/arrow.png
.. |ArrowDash| image:: /images/annotation/icons/arrowdash.png
.. |ArrowSquiggly| image:: /images/annotation/icons/arrowsquiggly.png
.. |ArrowCurve| image:: /images/annotation/icons/arrowcurve.png
.. |ArrowPolyline| image:: /images/annotation/icons/arrowpolyline.png
.. |ArrowPolylineDash| image:: /images/annotation/icons/arrowpolylinedash.png
.. |ArrowPolylineSquiggly| image:: /images/annotation/icons/arrowsquiggly.png

- |Arrow| **Arrow**
- |ArrowDash| **Arrow - Dash**
- |ArrowSquiggly| **Arrow - Squiggly**
- |ArrowCurve| **Arrow - Curve**
- |ArrowPolyline| **Arrow - Polyline**
- |ArrowPolylineDash| **Arrow - Polyline dash**
- |ArrowPolylineSquiggly| **Arrow - Polyline squiggly**


.. image:: /images/annotation/arrows.png



Marker
-------------------

.. |Marker| image:: /images/annotation/icons/crossmark.png

- |Marker| **Marker tool**

The marker tool identifies the location of an object or joint. See also: :doc:`/measurement/measuring_distances`.

It has an option toggle to be displayed as a single-pixel dot.

.. image:: /images/annotation/marker.png



Angle family
-------------------

.. |Angle| image:: /images/annotation/icons/angle.png
.. |Goniometer| image:: /images/annotation/icons/goniometer.png
.. |AngleToHorizontal| image:: /images/annotation/icons/anglehorizontal.png
.. |AngleToVertical| image:: /images/annotation/icons/anglevertical.png

- |Angle| **Angle tool**
- |Goniometer| **Goniometer**
- |AngleToHorizontal| **Angle to horizontal**
- |AngleToVertical| **Angle to vertical**

Tools in the angle family measure angles on a particular plane.

The angle tool has options to choose the angle orientation. It also has an option to display the full circle instead of just the angle arc, in order to make it clearer that the measurement is sitting in a particular plane.

See also: :doc:`/measurement/measuring_angles`.

.. image:: /images/measurement/axesangles.png



Stopwatch family
-------------------

.. |Stopwatch| image:: /images/annotation/icons/time-16.png
.. |Clock| image:: /images/annotation/icons/clock-16.png

- |Stopwatch| **Stopwatch**
- |Clock| **Clock**

The stopwatch is used to measure one or more time intervals, can associate a label and a tag with each time segment.

The clock tool shows the video time relatively to a point and can be used as a simple count down.

See also: :doc:`/measurement/measuring_times`.

.. image:: /images/annotation/stopwatch.jpg



Counter
-------------------

.. |Counter| image:: /images/annotation/icons/counter-6.png
    
- |Counter| **Counter**

The counter tool is used to count occurrences of an event or cycle. It can be used to measure cadence or repetitions.

See also: :doc:`/measurement/measuring_cadences`.


.. image:: /images/annotation/cadence.jpg



Grid tools
-------------------

.. |Plane| image:: /images/annotation/icons/plane.png
.. |Grid| image:: /images/annotation/icons/grid.png

- |Plane| **Perspective grid**
- |Grid| **Grid**

The grid tools are used to materialize a plane of motion or are used for calibration purposes.

See also: :doc:`/measurement/calibration_space`.

.. image:: /images/annotation/grid.jpg




Spotlight tool
-------------------

.. |SpotlightTool| image:: /images/annotation/icons/spotlight.png

- |SpotlightTool| **Spotlight tool**

.. image:: /images/annotation/spotlight.jpg

The spotlight tool is used to highlight a particular area of the image by dimming the rest.
Multiple spotlights can be added throughout the video.

Magnifier
---------

.. |Magnifier| image:: /images/annotation/icons/magnifier.png

- |Magnifier| **Magnifier**

The magnifier function creates a picture-in-picture effect with an enlarged version of the current image displayed within the original image.
This is a display mode rather than a normal drawing tool, it is not saved in the KVA file.

.. image:: /images/observation/magnifier.png

