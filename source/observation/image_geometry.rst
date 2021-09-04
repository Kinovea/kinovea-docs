
Image transformation
====================

Image orientation
-----------------
To change the orientation of the image use the menus under :menuselection:`Image --> Image rotation`.

The following options are available:

- :guilabel:`No rotation`
- :guilabel:`90° clockwise`
- :guilabel:`90° counter-clockwise`
- :guilabel:`180°`

Videos filmed in portrait mode on a smartphone typically already have a flag embedded in the video file and don't need to be manually rotated.

Image mirroring
---------------
To mirror the image, that is to flip it along the vertical axis, use the menu Image mirror.

Zoom & magnification
--------------------
To zoom into the image use :kbd:`CTRL` + mouse wheel or :kbd:`CTRL` + :kbd:`Minus` and :kbd:`CTRL` + :kbd:`Plus`.

:kbd:`CTRL` + :kbd:`Numpad0` resets the zoom level.

The magnifier tool can also be used to create a picture in picture magnified area.

.. image:: /images/observation/magnifier.png

Image aspect ratio
------------------
To change the aspect ratio of the image use the menus under :menuselection:`Image --> Image format`.

Some devices use non-rectangular pixels and don't fill the corresponding pixel aspect ratio value in the file metadata. 
In these case it might be necessary to force the aspect ratio to a known value.

The following options are available:

- :guilabel:`Auto detection`
- :guilabel:`Force 4:3`
- :guilabel:`Force 16:9`

Deinterlacing
-------------
To deinterlace the video use the menu :menuselection:`Image --> Deinterlace`.

Some capture devices store video using an interlaced format.
Interlaced videos store half images at twice the frame rate, alternating odd and even rows.
This causes a combing artifact when the filmed motion is fast as objects or subjects move during the half frame interval.

The deinterlacing algorithm reconstructs full images by combining rows from adjacent frames.

.. image:: /images/observation/deinterlacing.png

Debayering
----------
Videos saved in Bayer mode contain the raw sensor data before color reconstruction. 
The color can be rebuilt using the menu under :menuselection:`Image --> Demosaicing`.

.. image:: /images/observation/debayering.png

The following options are available:

- :guilabel:`RGGB`
- :guilabel:`BGGR`
- :guilabel:`GRBG`
- :guilabel:`GBRG`

The appropriate option to select depends on the device and mode used during recording.

