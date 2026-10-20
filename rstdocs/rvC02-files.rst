**C.2 |** Files
============================

.. _file-types:

**[1]** File Types 
--------------------------------------------------------------------- 


rivt formatting *tags* and file *commands* have an :ref:`API scope <markup-R>`.
The *Insert and Values APIs* have a fixed set fo tags and commands. The Run and
Tools tags and command are extensible and function as a plugin-architecture.

`rivtlib <https://pypi.org/project/rivtlib/>`__ is the Python library that 
compiles a *rivt file* to a text, PDF or HTML doc. A *rivt file* is a 
Python file (.py) that imports the *rivtlib* Python package and includes 
*rivt markup*. *rivt* dependencies are listed `:ref:here <rivtstudio-settings>`. 

A *public rivt file* is a subset of a *rivt file*, made up of sections the
author chooses to share under an `Open Source license
<https://opensource.org/licenses>`__. *rivt* is designed to seamlessly extract
public files, allowing the author discretion in choosing which file 
sections to make public.

Groups of *rivt files* may be compiled and linked into a single 
:ref:`rivt report <rivt-report>`. Collections of *rivt files* with related 
subject matter may be grouped together as a :ref:`rivtbook <book-folder>`.

*rivt files* are generally edited and run in an IDE. The lightweight 
`Pyzo <https://pyzo.org/>`__ IDE is installed by rivtlib. The 
`VSCode IDE <https://code.visualstudio.com/>`__ is a full featured IDE 
with rivt profiles and extensions documented :ref:`here <rivtstudio-settings>`. 
*VSCode* is installed with the portable :ref:`rivtstudio <rivtstudio>` installation.

*rivt file* examples are illustrated :ref:`here <rivt-tutor>`. Additional  
*rivt files* may be downloaded from *Google Drive* at 
`OpenModels.info <https://www.openmodels.info/>`__.  An interface for searching 
*public rivt files* on *GitHub* is :ref:`here <search-interface>`. 

**rivt file**

A *rivt file* provides the formatting instructions and content that generate
*rivt docs*. Each *rivt file* has a *doc number* prefix that specifies the
*doc* division. The *doc number* prefix includes a single digit capital 
alphanumeric division label *D*, followed by a two digit subdivision 
number *ss*. For example:

.. code-block:: bash
    
    [rvDss-]file-name.py
    
    rvB02-Beam-Loads.py


project folders  or :ref:`rivtbook <book-folder>`
which work well as *GitHub* repositories. *rivt* also generates a *GitHub* 
README file from a *rivt report*. 

**Author provided source file inputs**

*rivt* reads and writes file types including:

================================  =================================================
description                         read file types   
================================  =================================================
Image files                         .png, .jpg, .jpeg
Data files                          .csv, xlsx, 
Pandas dataframes                   .dat, html, hdf5, .json, xml, feather, parquet 
Formatted text files                .txt, .tex, html, .md, .rst
Shell and terminal commands         .sh, .bat, .cmd
================================  =================================================

Files for use in a *rivt doc* are read and written to default folders that may
be changed by specifiying file paths relative to the *rivt file*. The

| IMAGE | filename.png | parameters



**Report files written by rivtlib**

*rivt* also generates and saves files that can be read by subsequent *rivt
files*.  When generating reports these are written to *rv_stor* folder and
subfolders and include:


================================  =================================================
description                         written file types   
================================  =================================================
Value files                         .csv
Stored sections                     .txt 
Log files                           .txt
Python output                       .png, .jpg, .csv, .dat, xlsx
Formatted text files                .txt, .tex, html, .md, .rst
Public rivt files                   .py
================================  =================================================

.. rst-class:: center

    **Value files**

A *value file* is a *csv* file that defines variable values. A values file 
is exported to rv_stor for each Values API call. The filename has the form:

.. code-block:: bash

    vDss-S-rivtfile.csv

where Dss is the doc number, S is the section number, and rivtfile.csv is the
original *rivt file* name. The file may be read using the VALUE command.

.. rst-class:: center``

    **Log files**


Log files include a backup of each rivt file and a record of most steps of
*rivt* file processing and are written to the */logs* subfolder of *rv_stor*.
They are written when the PUBLISH command is executed. Each log file has the
form:

.. code-block:: bash

    log-Dss-rivtfile.txt

.. rst-class:: center

    **Python scripts**

Python scripts can be run as a [[PYTHON]] block in the *Run* API or
as an imported file in the *Values* API.  The [[PYTHON]] block is written
to *rv_stor* with label name. For consistentcy, Python output should also be
directed to *rv_stor*.

.. rst-class:: center

    **Public rivt files**

A public rivt file is a copy of the *rivt file* that includes all of the
sections marked as *public* in the *header*. It has the same name as the *rivt
file* with an added hyphen between "rv" and the docnumber e.g.

.. code-block:: bash

    rv-Dss-filename.py


.. _public-files:  

**[3]** Public files
----------------------------------------

A feature of *rivt* is efficient control over public sharing of all or parts
of a rivt file. *Public rivt files* are generated by *rivtlib* on a section by
section basis defined by the API header substring. Each API function defines a
section and has a public/private setting in the header. Sections are private by
default (see `:doc: <rvF01-quickref>`).

.. code-block:: python

    rv._("""Section Label | doc;stored, private;public, section;merge

         Content substring indented 4 spaces
        
        ...
        
        """)

Sections are written to a rivt file in the */public* folder with a file name
composed as:

.. code-block:: text

    rivt file name

        rvAnn-filename.py

    modified with an additional hyphen

        rv-Ann-filename.py

The public folder may be uploaded to a GitHub repo for public sharing. When
files are downloaded for reuse the extra hyphens may be removed with a batch
remove command (e.g. in VSCode).

.. rst-class:: center

   **2. Contribute to rivt and rivtlib**

*rivtlib* can be improved by: 

  - providing pull requests.
  - submitting issues and bugs.
  - contributing to documentation and examples.
  
 *rivt* can be improved by:

  - contributing to packages and extensions used by *rivt*.