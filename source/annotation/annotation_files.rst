
Saving and loading annotation files
===================================

Annotations are saved in KVA files. These are XML files with a .kva extension.

KVA files store data for key images, comments, drawings, trajectories, chronometers, time origin, tracked values, and the coordinate system calibration.

Saving annotations
------------------
To save the current annotations use the menu :menuselection:`File --> Save` or the shortcut :kbd:`CTRL` + :kbd:`S`.

.. tip:: Save the annotation file with the same name as the video to have it automatically loaded the next time you open the video in Kinovea.
    This is known as a "sidecar" file, for example :file:`video.mp4` and :file:`video.kva`. This is the default option when saving.

Loading annotations
-------------------
To load an annotation file into an opened video use the menu :menuselection:`File --> Load annotations`.

The imported annotations are merged together with the existing annotations you might have already added to the video.

If the imported annotations were created on a different video, a conversion step may take place to adapt the drawings dimensions and time codes to the new image size and frame rate.

Loading external annotations can be used to import calibration settings between videos filmed during the same session without having to perform the calibration for every video. 

Default annotation file
-----------------------
To automatically import a specific annotation file into every video, 
use :menuselection:`Options --> Preferences --> Playback --> General --> Default annotation file…`, and point it to the KVA file you want to be loaded.

