**C.1 |** Publish
======================

.. _rivt-publish:

**[1]** Docs
-------------------------------------------------------------------------------


.. image:: _static/img/process2.png
    :class: dark-light
    :width: 75%
    :align: center
    :alt: rivt flow chart 

.. rst-class:: center

    **rivt Doc Processing**

A :term:`rivt file` is a Python plain text file ( *.py* ) that includes API
functions and imports the :term:`rivtlib` package into the *rv*
:term:`namespace`:

.. code-block:: python

    import rivtlib.rvapi as rv

*rivt files* are stored in either a *rivt* or *rivtbk* folder. Each *rivt file*
and corresponding *rivt doc* has a prefix used for document organization. The

Each :term:`rivt file` outputs a corresponding :term:`doc` of the format
specified in PUBLISH command of the *rv.D()* API. A rivt file number has the
form:

.. code-block:: text

    rvAnn-filename.py

where rvAnn is a required file number prefix with A an alphanumeric character and nn a two
digit non-negative integer. Corresponding rivt docs are output as:

.. code-block:: text

    rvAnn-filename.txt, pdf or html

---------------------------

.. _rivt-report:

**[2]** Report
-------------------------------------------------------------------------------

A *rivt report* is organized using the *file numbers*. The file numbers are
used to organize reports into divisions and subdivisions. Each *rivt file* or
*doc* is a report subdivision. If the *rivt filenames* are:

.. code-block:: bash

    rvA01-filename.py
    rv105-filename.py
    rv212-filename.py  

the corresponding *doc numbers* in a report would be: 

- A.1 (division A, subdivision 1)
- 1.5 (division 1, subdivision 5)
- 2.12 (division 2, subdivision 12)

----------------------------------------

.. _comment-settings:

**[3]** Comment Settings (.py)
--------------------------------

Comment settings are specified in the *rivt file* immediately following the
import statement and before API methods, and are used to override default
settings for the entire *rivt doc*. The *rv private* setting may be changed at
the section level. If default settings shown in parenthesis are acceptable the
comment settings are not needed.

.. code-block:: python

    import rivtlib.rvapi as rv

    # rv set_width = 80  ; character width of text output (80)
    # rv no_tag = true ; if false, the API type is added to section number (true)
    # rv private = true ; if false, default section heading changed to public (private)

See :ref:`rivt markup <rivt-markup>` for further details.

------------------------------

.. _publish-settings:

**[4]** Publish Settings
------------------------------

    Settings for *doc* publishing are specified using the PUBLISH command and
    METADA block in the *rv.D()* API. An example is shown below.

.. code-block:: python

    rv.D("""Publish Doc 
    
    A rivt file may be published as a text, PDF or HTML doc by specifying the
    PUBLISH type parameter as txt, pdf or html. 
    
    Published files are found in sub-folders of the _published folder. A text
    version of the doc or report is is always written to the rivt and
    _rivt-public folders as a README.txt file. READMEs are formatted and
    displayed on the first page of a GitHub repo.
    
    | PUBLISH | Pier and Ramp Design | pdf
    
    _[[METADATA]] 
    [doc]
    ;-----------------------------------------
    authors = rodhholland
    version = 1.0.0a20
    repo = https://github.com/rivt-info/rivt-example-01
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/
    [layout]
    ;----------------------- cover page and runner settings
    ; put logo files in rvsrc/image folder
    subtitle =  Structural Design
    copyright = --
    client = Zach Kahn, Verissimo Dr., Novato CA
    coverpage = true
    coverlogo = rivt-design2.png
    ; size in percent page width
    coverlogo_size = 30 
    runninglogo = rivt-design2.png
    ; size in pixels
    runninglogo_size = 175
    runninglabel = Rivt Design
    project_ref = proj. 1001
    ;------------------------ PDF settings
    ; colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
    pdf_link_color = brown
    pdf_link_underline = false
    ; page sizes: letter, legal, A4    
    pdf_pagesize = letter 
    ; margin order: top, right, bottom, left
    pdf_margins = 1in, 1in, 1in, 1in 
    ; start new page for each section
    pdf_page = false 
    ;----------------------- TOC levels
    ;--- 1: include subdivisions   2: include subdivisions and sections
    toc_level = 2
    [process]
    ;-----------------------------------------
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]    
    """)
     
.. _report-script:

**[5]** rivt-report.py
----------------------------------------------------------

The Python *report script* includes settings that specify assembly parameters
and override defaults. These include:

- *Docs* to be included in the report
- Division names
- recompiling *docs*
- report cover page and title

provides the option to either regenerate all *docs* or to
assemble the report from previously generated *docs*.  Most aspects of
the *report* appearance are determined at when generating *docs*.

An example rivt-report.py script is shown below.

.. code-block:: python

    #! python
    """generate rivt report

    Run this Python script in the rivt-report folder to write reports to the
    _published folder. Copy and rename this file to save custom report settings
    (e.g. rivt-folder-new.py).

    The script does not regenerate individual PDF docs unless specified in the
    settings. Regenerating individual PDF docs adds execution time. HTML and text
    docs are always regenerated. See https://www.rivt.info for more details.
    """

    # ========= Modify report settings between the double lines ==============
    iniS = """
    [settings]
    ;----- file name for report including extension (pdf, html, txt)
    rept_filename = rivt-treehouse-report.txt
    ;----- comma separated list of excluded doc numbers eg. rv102, rv204
    exclude = -- 
    ;-----  update settings and configuration files from rivt 
    rivt_cfg = true
    ;----- regenerate pdf doc files 
    regen_pdf = false

    [format]
    title = Treehouse Design 
    subtitle =rivt report
    client = Example
    project_ref = Proj. 0001
    authors = R Holland 
    copyright = StL
    version = 1.0.0a12
    ;----- logo files are stored in rvsrc/page folder, size is % page width
    coverlogo = tree1.png
    coverlogo_size = 50
    ;----- header and footer logos and labels
    running_logo = rivt02.png 
    running_label = rivt
    ;----- underline links in PDF - true or false
    pdf_link = true 
    ;----- page size letter, legal, A4 - margins top, right, bottom and left
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    """
    # ============================================================================
    # the following line is required after settings
    import rivtlib.rvreport

------------------------------------------------

.. _default-folders:

**[6]** Command Defaults
------------------------------------------------------------------------------

Files are opened using default paths relative to the *rivt-report* folder for
*reports* and *doc folders* for *rivtbooks*. They have the form:

| COMMAND | filename | parameters

For example, to read and insert an image file the command would be:

| IMAGE | image1.png | parameters 

If a different file path is needed it needs to be specified relative to
the *rivt-report* folder for *reports* and the *doc folder* for
*rivtbooks*. A unique path is triggered by including at least one folder 
separator "/" in the path specification. 

See :ref:`command summary <command-summary>` for further details.

**Default Paths for Commands**

================= ========================= =============================
    Command        Default Report Paths     Default rivtbook Paths  
================= ========================= =============================
\| SHELL |          **rvsrc/script**         **script/**     
\| IMAGE |          **rvsrc/image**          **image/** 
\| IMAGE2 |         **rvsrc/image**          **image/**   
\| PYTHON |         **rvsrc/script**         **script/**  
\| TABLE |          **rvsrc/data**           **data/**  
\| TEXT |           **rvsrc/script**         **script/**  
\| VALTABLE |       **rvsrc/data**           **data/**   
\| VALDATA |        **_rvstor/data**         **_rvstor/** 
\| ATTACHPDF |      **rvsrc/image**          **image/**  
\| PUBLISH | [1]    **/_published/**         **rivtbook/_published/**  
================= ========================= =============================

[1] *docs* are written to subdirectories of *_published*


.. raw:: html

    <p style="border-width:2px; border-style:solid; 
    border-color:#49b2c3;padding: 1em;">

    <b>Folder Naming</b><br>
    <br>

    A report project folder can contain any file or folder but the following structure
    is required for <i>doc</i> processing. <i>report folders</i> include at least
    the folders and files shown in brackets[] below. Folders with an underscore
    contain rivt generated files. Files and folders are organized under
    a rivt root folder with the prefix <i>rivt-</i> followed by the report
    label, e.g. <i>rivt-Report-Label</i>. <br> <br>

--------------------


**[7]** HTML and PDF Config (.py)
--------------------------------------------------------------------- 

The *conf.py* configuration file contains default configuration settings for 
*rivt docs* and reports. A typical *conf.py* file looks like this:

.. code-block:: python

    #! python

    from rivtlib.rvconfig import *  # noqa: F403

    """ configuration settings for rivt docs and reports

    This file is stored in /src/Tools. Settings for both HTML and PDF docs are
    included anc cover:

    - metadata 
    - formatting 

    """

    import sys
    import os
    from pathlib import Path

    sys.path.append(str(Path(".").resolve()))

    project = "rivt doc"
    copyright = "2023 StructureLabs LLC"
    author = "rholland"
    release = "0.3.8a7"

    #
    # -- Options for HTML and PDF output --------------------------------------
    #

    extensions = [
        "sphinx.ext.githubpages",
        "sphinx_togglebutton",
        "sphinxcontrib.jquery",
        "sphinx_copybutton",
        "sphinx_favicon",
        "sphinx.ext.duration",
        "sphinx.ext.doctest",
        "sphinx.ext.autodoc",
        "sphinx_design",
        "sphinx_new_tab_link",
        "rst2pdf.pdfbuilder",
    ]
    root_doc = "index"
    duration_write_json = ""
    html_show_sourcelink = False
    exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
    source_suffix = [".rst", ".md"]
    templates_path = ["_templates"]
    locale_dirs = ["_locale"]
    html_title = "rivt"
    html_theme = "pydata_sphinx_theme"
    html_context = {"default_mode": "dark"}
    html_sidebars = {"**": ["sidebar-nav-bs.html"]}
    html_static_path = ["_static", "_static/img"]
    html_css_files = ["css/custom.css"]
    html_theme_options = {
        "pygments_light_style": "tango",
        "pygments_dark_style": "github-dark",
        "navbar_start": ["navbar-logo"],
        "collapse_navigation": True,
        "header_links_before_dropdown": 6,
        "navbar_align": "left",
        "show_toc_level": 1,
        "navigation_depth": 1,
        "footer_start": ["copyright"],
        "footer_end": [],
        "logo": {
            "text": "rivt",
            "image_dark": "rivhome11c.png",
            "image_light": "rivhome11c.png",
        },
    }
    favicons = [
        {
            "rel": "icon",
            "sizes": "16x16",
            "href": "favicon-16x16.png",
        },
        {
            "rel": "icon",
            "sizes": "32x32",
            "href": "favicon-32x32.png",
        },
    ]

    #
    # -- Options for PDF output -----------------------------------------------
    #
    # source start file, target name, title, author, options
    # options: ('index', 'MyProject', 'My Project', 'Author Name', {'pdf_compressed': True})
    # More than one author : \\r'Guido van Rossum\\Fred L. Drake, Jr., editor'
    pdf_documents = [("rv001-single-doc", "rv001-single-doc", "rivt", "r holland")]
    # Label to use as a prefix for the subtitle on the cover page
    subtitle_prefix = "User Manual"
    # A list of folders to search for stylesheets. Example:
    pdf_style_path = ["./rstdocs/_static/pdfstyle"]
    # A colon-separated list of folders to search for fonts. Example:
    pdf_font_path = ["./rstdocs/_staticfonts"]
    # A comma-separated list of custom stylesheets. Example:
    pdf_stylesheets = ["./rstdocs/_static/pdfstyle/stylepdf1.yaml"]
    # Example: compressed=True
    pdf_compressed = False
    # Language to be used for hyphenation support
    pdf_language = "en_US"
    # literal blocks wider than the frame overflow, shrink or truncate
    pdf_fit_mode = "shrink"
    # 1 means top-level sections start in a new page 0 disabled
    pdf_break_level = 0
    # When a section starts in a new page, force it to be 'even', 'odd',
    # or just use 'any'
    pdf_breakside = "any"
    # If false, no coverpage is generated.
    pdf_use_coverpage = True
    # Name of the cover page template to use
    pdf_cover_template = "pdfcover.rst"
    # Page template name for "regular" pages
    # pdf_page_template = 'cutePage'
    # Documents to append as an appendix to all manuals.
    # pdf_appendices = []
    # Enable experimental feature to split table cells. Use it
    # if you get "DelayedTable too big" errors
    # pdf_splittables = False
    # Set the default DPI for images
    # pdf_default_dpi = 72
    # Enable rst2pdf extension modules
    # pdf_extensions = []
    # Show Table Of Contents at the beginning?
    pdf_use_toc = True
    # How many levels deep should the table of contents be?
    pdf_toc_depth = 9999
    # Insert footnotes where they are defined instead of
    # at the end.
    pdf_inline_footnotes = True
    # verbosity level. 0 1 or 2
    # pdf_verbosity = 0
    # If false, no index is generated.
    pdf_use_index = True
    # If false, no modindex is generated.
    pdf_use_modindex = False
    # Add section number to section references
    pdf_use_numbered_links = False
    # Background images fitting mode
    pdf_fit_background_mode = "scale"
    # Repeat table header on tables that cross a page boundary?
    pdf_repeat_table_rows = True
    # Enable smart quotes (1, 2 or 3) or disable by setting to 0
    pdf_smartquotes = 0


----------------------------------


**[8]** PDF Style File (.yaml)
--------------------------------------------------------------------- 

The *rivtstyle.yaml* file contains default formats for PDF files.

 .. code-block:: yaml

    fontsAlias:
    fontSerif: DejaVuSans
    fontSerifBold: DejaVuSans-Bold
    fontSerifBoldItalic: DejaVuSans-BoldOblique
    fontSerifItalic: DejaVuSans-Oblique
    fontMono: DejaVuSansMono
    fontMonoBold: DejaVuSansMono-Bold
    fontMonoBoldItalic: DejaVuSansMono-BoldOblique
    fontMonoItalic: DejaVuSansMono-Oblique
    fontSans: DejaVuSans
    fontSansBold: DejaVuSans-Bold
    fontSansBoldItalic: DejaVuSans-BoldOblique
    fontSansItalic: DejaVuSans-Oblique
    pageSetup:
    firstTemplate: coverPage
    height: null
    margin-bottom: 4mm
    margin-gutter: 1mm
    margin-left: 1.5cm
    margin-right: 1.5cm
    margin-top: 4mm
    size: letter
    spacing-footer: 10mm
    spacing-header: 10mm
    width: null
    pageTemplates:
    coverPage:
        showFooter: true
        showHeader: false
        underline: false
    noHead:
        frames: [[0%,0%,100%,100%]]
        showFooter: true
        showHeader: false
        underline: false
    mainPage:
        frames: [[0%,0%,100%,110%]]
        showFooter: True
        showHeader: True
    styles:
    base:
        allowWidows: 1
        allowOrphans: 1 
        alignment: TA_LEFT
        allowOrphans: false
        allowWidows: false
        backColor: null
        borderColor: null
        borderPadding: 5
        borderRadius: null
        borderWidth: 0
        bulletFontName: fontMono
        bulletFontSize: 10
        bulletIndent: 0
        commands: []
        firstLineIndent: 0
        fontName: fontSans
        fontSize: 9
        hyphenation: false
        leading: 12
        leftIndent: 0
        parent: null
        rightIndent: 0
        spaceAfter: 1
        spaceBefore: 1
        strike: false
        textColor: black
        wordWrap: null
        linkUnderline: true
        linkColor: blue
    tableofcontents:
        parent: normal
    big-text:
        fontSize: 175%
        parent: base
        fontName: fontSans
    medium-text:
        fontSize: 125%
        parent: base
        fontName: fontSans
    small-text:
        fontSize: 125%
        parent: base
        fontName: fontSans 
    blockquote:
        leftIndent: 20
        parent: bodytext
    bodytext:
        alignment: TA_JUSTIFY
        hyphenation: true
        parent: normal
        spaceBefore: 6
    align-center:
        alignment: TA_CENTER
        parent: bodytext
    align-right:
        alignment: TA_RIGHT
        parent: bodytext
    code:
        spaceBefore: 6
        spaceAfter: 6
        backColor: "#d1dede"
        borderColor: darkgray
        borderPadding: 6
        borderWidth: 0.5
        leftIndent: 0
        parent: literal
        fontName: fontMonoBold
    compgreen:
        textColor: green
        alignment: TA_RIGHT
        fontName: fontSansBold
    compred:
        textColor: red
        alignment: TA_RIGHT
        fontName: fontSansBold
    contents:
        parent: normal
    figure:
        spaceBefore: 18
        spaceAfter: 12
        alignment: TA_CENTER
        colWidths:
        - 100%
        commands:
        - - VALIGN
            - - 0
            - 0
            - - -1
            - -1
            - TOP
        - - ALIGN
            - - 0
            - 0
            - - -1
            - -1
            - CENTER
        parent: bodytext
    figure-caption:
        alignment: TA_CENTER
        fontName: fontSans
        parent: bodytext
    figure-legend:
        parent: bodytext
    footer-box:
        alignment: TA_CENTER
        fontName: fontSans
        commands:
        - - BOX
            - - 0
            - 0
            - - -1
            - -1
            - 0.25
            - white
    header-box:
        alignment: TA_RIGHT
        fontName: fontSans
        commands:
        - - BOX
            - - 0
            - 0
            - - -1
            - -1
            - 0.25
            - white
    heading:
        keepWithNext: true
        parent: normal
        spaceAfter: 1
        spaceBefore: 10
        fontName: fontSerif
        textColor: "#222222"
    heading1:
        fontSize: 120%
        parent: heading
        fontName: fontSansBold
        underlineColor: black
        underlineWidth: 1
        underlineOffset: 5
    heading2:
        fontSize: 110%
        parent: heading
        fontName: fontSansBold
        underlineColor: black
        underlineWidth: 1
        underlineOffset: 5
    heading3:
        fontSize: 100%
        parent: heading
    heading4:
        parent: heading
    heading5:
        parent: heading
    heading6:
        parent: heading
    hint:
        parent: admonition
    hint-heading:
        parent: admonition-heading
    image:
        spaceBefore: 5
        spaceAfter: 5
        alignment: TA_CENTER
        parent: bodytext
    important:
        parent: admonition
    important-heading:
        parent: admonition-heading
    italic:
        fontName: fontSansItalic
        parent: bodytext
    line:
        parent: lineblock
        spaceBefore: 0
    lineblock:
        parent: bodytext
    linenumber:
        parent: code
    literal:
        firstLineIndent: 0
        fontName: fontMono
        hyphenation: false
        parent: normal
        wordWrap: null
    normal:
        parent: base
    note:
        parent: admonition
    note-heading:
        parent: admonition-heading
    option-list:
        colWidths:
        - null
        - null
        commands:
        - - VALIGN
            - - 0
            - 0
            - - -1
            - -1
            - TOP
        - - TOPPADDING
            - - 0
            - 0
            - - -1
            - -1
            - 0
    rubric:
        alignment: TA_CENTER
        parent: bodytext
        textColor: darkred
    separation:
        parent: normal
    sidebar:
        backColor: cornsilk
        borderColor: darkgray
        borderPadding: 8
        borderWidth: 0.5
        float: none
        parent: normal
        width: 100%
    sidebar-subtitle:
        parent: heading4
    sidebar-title:
        parent: heading3
    subtitle:
        fontSize: 85%
        parent: title
        spaceBefore: 12
    table:
        alignment: TA_LEFT
        spaceBefore: 1
        spaceAfter: 1
        borderPadding: 5
        leftPadding: 6
        rightPadding: 6
        topPadding: 5
        bottomPadding: 5
        background-color: white
        alternate-row-background-color: lightgray
        commands:
        - - ROWBACKGROUNDS
            - - 0
            - 0
            - - -1
            - -1
            - - white
            - "#E0E0E0"
        - - BOX
            - - 0
            - 0
            - - -1
            - -1
            - 0.25
            - black        
    admonition:
        borderWidth: 0
        borderPadding: 0
    table-heading:
        alignment: TA_LEFT
        borderWidth: 0
        borderPadding: 0
        backColor: "#c5d1c5"
        borderColor: darkgray
        fontName: fontMonoBold
    tip-heading:
        parent: admonition-heading
    title:
        alignment: TA_CENTER
        fontSize: 120%
        keepWithNext: false
        parent: heading
        fontName: fontSansBold
        spaceAfter: 36
    title-reference:
        fontName: fontSansItalic
        parent: normal
    toc:
        parent: normal
        fontSize: 100%
    toc1:
        fontName: fontSansBold
        parent: toc
    toc10:
        leftIndent: 100
        parent: toc
    toc11:
        leftIndent: 100
        parent: toc
    toc12:
        leftIndent: 100
        parent: toc
    toc13:
        leftIndent: 100
        parent: toc
    toc14:
        leftIndent: 100
        parent: toc
    toc15:
        leftIndent: 100
        parent: toc
    toc2:
        leftIndent: 20
        parent: toc
    toc3:
        leftIndent: 40
        parent: toc
    toc4:
        leftIndent: 60
        parent: toc
    toc5:
        leftIndent: 80
        parent: toc
    toc6:
        leftIndent: 100
        parent: toc
    toc7:
        leftIndent: 100
        parent: toc
    toc8:
        leftIndent: 100
        parent: toc
    toc9:
        leftIndent: 100
        parent: toc
    topic-title:
        parent: heading3
    warning:
        parent: admonition
    warning-heading:
        parent: admonition-heading


.. toctree::
    :maxdepth: 1
    :hidden:
    
    rvC02-files.rst
    rvC03-folders.rst    