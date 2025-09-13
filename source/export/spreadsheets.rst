Exporting spreadsheet documents
===============================

Save annotations
----------------
To save annotations use :kbd:`CTRL` + :kbd:`S` or the menus :menuselection:`Save` or :menuselection:`Save as…`. This saves annotations to a KVA file, the native annotation format of Kinovea.

Export measurements from kinematics dialogs
-------------------------------------------
To export measurements such as point positions, linear velocities, or angular accelerations, use the kinematics dialogs.
The kinematics dialogs are found under the :menuselection:`Tools` menu: :menuselection:`Scatter diagram`, :menuselection:`Linear kinematics`, :menuselection:`Angular kinematics`, :menuselection:`Angle-angle diagram`.

To export data use the export options at the bottom right of the dialogs.

.. image:: /images/export/exportdata.png

This will export the data in CSV format, either to the clipboard or to a file. 
The first column is the time, either in milliseconds or normalized, and the other columns are the data sources.

The measurements displayed and exported from the kinematics dialog use the filtered coordinates. 
The filtering process is described in the About box of the :guilabel:`Linear kinematics` dialog.
You can control filtering from the preferences at :menuselection:`Options --> Preferences --> Drawings --> General --> Enable coordinates filtering`.

Export data to spreadsheet
--------------------------
Another option to export data is to use the converters menus under :menuselection:`File --> Export to spreadsheet`.

The following options are available:

- :guilabel:`LibreOffice (.odf)`
- :guilabel:`Microsoft Excel (.xml)`
- :guilabel:`Web (.html)`
- :guilabel:`Gnuplot (.txt)`

The underlying mechanism for these menus is to **convert** the annotation data into the output format: it does not perform any higher level computations.
This approach has the following differences with the export from the kinematics dialogs:

- The coordinates do not use filtering. 
- Only the coordinates are exported, not any higher level measurements like speed or acceleration.
- Each object is exported independently in its own table.
- Key images times are exported.
- Stopwatches are exported.
- The time column uses the configured timecode format and may not be numerical in nature.

To use Gnuplot to plot the trajectory data on a 3D graph with time as the third dimensions, you can use the following commands:

.. code-block::

    gnuplot> set xlabel "Time"
    gnuplot> set ylabel "X-AXIS"
    gnuplot> set zlabel "Y-AXIS"
    gnuplot> set ticslevel 0
    gnuplot> splot "weightlift.txt" using 1:2:3 with lines

.. image:: /images/export/gnuplot.png


Citation examples
-----------------
If you used Kinovea in your research we would very much appreciate it if you included it in your bibliography.

You can find examples of formatted citations in the About dialog under the Citation tab.

.. note:: Kinovea is an open source project and is not published by a company,
    thus there is no meaningful "city" or "country" of origin as is sometimes requested by journals for software references.
