---
myst:
    substitutions:
        "key3a": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: https://github.com/docs.html
            :width: 60px
            ```
---

:tocdepth: 1

<style type="text/css">
  table    { background:#dce8ef; color: #000000; }
</style>

#  {{ key3a }} rivt-syntax

**rivt** markup is based on
[restructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html)
and includes arbitrary unicode, rivt commands and rivt tags. Any text not
defined with commands or tags is processed as plain text, formatted and output.

<hr>

## **commands**
<hr>

Commands read and write external files and are marked by double bars (||) at
the beginning of a line. Command parameters are separated by a single bar (|).
In the summary below parameter options are separated with semi-colons,
parameter list elements are separated with commas, and options are in
parenthesis.

File locations are specified using shortened relative paths that include the
name of the file and the name of its containing folder. Further information on
the folder organization for a rivt project is [here](rdoc.md#folders)

```{list-table} Command Syntax
:header-rows: 1

* - **command syntax** 
  - **API** 
* - || [text](syntax.md#text) | relative path | rivt; plain                     
  - R I V
* - || [init](syntax.md#init) | relative path
  - R
* - || [append](syntax.md#append) | relative path | cover.pdf
  - R
* - || [image](syntax.md#image)  | relative path, (2nd path) | width, (width)
  - I
* - || [table](syntax.md#table)  | relative path | max col width, align
  - I
* - || [declare](syntax.md#declare) | relative path |  print; noprint
  - V
```


### **text**

The text command inserts and formats text from external files into the rivt
file. Text files may be plain text or text with rivt tags.

### **init**

The init command specifies the name of the configuration file which is read
from the rivt-doc folder. Report formatting can be easily modified by
specifying a different init file.

### **append**

The append command attaches PDF files to the end of the doc.

### **image**

The image command inserts and formats image data from png or jpg files.

### **table**

The table command inserts and formats tabular data from csv or xls files.

### **declare**

The declare command imports values from a csv file written by rivt when
processing assigned and declared values from another doc in the same
project.



<hr>

## **tags**
<hr>

Line tags format a line of text and are denoted with *_[tag]*, typically at the
end of a line. The *=* and *:=* tags used in the Value method are unique
exceptions. 

<pre style="background:#dce8ef; color: #000000">
============================ ================================= ==========
   line tags                        description                   API
============================ ================================ ===========
text _[b]                       bold                            R I V 
text _[c]                       center                          R I V  
text _[i]                       italic                          R I V  
text _[bc]                      bold center                     R I V  
text _[bi]                      bold italic                     R I V
text _[r]                       right justify                   R I V
text _[u]                       underline                       R I V   
text _[l]                       LaTeX math                        I V
text _[s]                       sympy math                        I V
text _[bs]                      bold sympy math                   I V
text _[e]                       equation label, autonumber        I V
text _[f]                       figure caption, autonumber        I V
text _[t]                       table title, autonumber           I V
text _[#]                       footnote, autonumber              I V
text _[d]                       footnote description              I V
_[page]                         new page                          I V
_[address, label]               url or internal reference         I V
a = 1.2 | unit, alt | descrip   declare =                           V
a := b + c | unit, alt | n,n    assign :=                           V
</pre>

Block tags format a text block and start a block with *_[[tag]]* and
end with *_[[q]]*.

<pre style="background:#dce8ef; color: #000000">
============================ ================================ ==========
   block tags                        description                 API
============================ ================================ ==========
_[[b]]                          bold                            R I V
_[[c]]                          center                          R I V
_[[i]]                          italic                          R I V
_[[p]]                          plain                           R I V
_[[q]]                          quit block                      R I V
_[[l]]                          LaTeX                             I V
</pre>

