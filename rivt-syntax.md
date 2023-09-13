---
myst:
    substitutions:
        "key3a": |
            ```{image} _static/img/riv02.png
            :alt: rivt logo
            :target: https://github.com/rivt-doc.html
            :width: 50px
            ```
---

#  {{ key3a }} **rivt-syntax**

**rivt** markup includes arbitrary unicode text, rivt commands and rivt tags.
It uses [restructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html) as a base and some reST markup may be used. 

<hr>

## commands
<hr>

A command reads or writes external files and is denoted by || at the beginning
of a line. Command parameters are separated by |. In the summary below,
parameter options are separated with semi-colons and parameter list elements
are separated with commas.

<pre style="background:#dce8ef; color: #000000">
==================================================== ==============
    command syntax                                         API 
==================================================== ==============

|| text | rel file path | rivt; plain                     R I V

|| init | rel file path                                     R

|| append | rel file path                                   R

|| image  | rel file path, .. | .50, ..                     I

|| table  | rel file path | 60,r;l;c                        I

|| declare | rel file path |  print; noprint                V
</pre>

### tags

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

