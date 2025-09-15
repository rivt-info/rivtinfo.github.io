4.2 - Publish Docs
========================


**[01]** rivt files and folders
--------------------------------

folder aliases

A *rivt file* is the basic unit of a rivt report. Its output is a *rivt doc*
which is a subdivision in the report heirarchy. Each *rivt file* is
identified with a *doc* prefix number of the form: 

    rvddss-file-name.py 
    
where dd is a two digit division number and ss is a two digit subdivision
number e.g., rv0203-loads.py. Editing the doc number changes the report
organization.

Resource files used in *rivt files* are organized in the *source* folder.

An example *rivt folder structure* for reports is shown below. *rivt files* are
organized into numbered division folders of the form:

    dvdd-division-name

where dd is the two digit division number.

*Docs* are written to the *reports* folder. A *report* is an organized assembly
of *docs*.

Report and document titles are taken from folder and file names unless
over-rides are specified in the rivt-config.ini file.


**[03]** Report folder structure
---------------------------------

An example folder structure is shown below. 


publish x



