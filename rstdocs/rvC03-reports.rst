
C.3 Reports
============================================

.. _rivt-report:

**[2]** rivt-report.py
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