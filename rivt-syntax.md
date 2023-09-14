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

**rivt** markup is based on
[restructuredText](https://docutils.sourceforge.io/docs/user/rst/quickref.html).
and includes arbitrary unicode text, rivt commands and rivt tags. Any text that
is not part of the defined syntax is processed as plain text, formatted and
output.

<hr>

## commands
<hr>

Commands read or write external files and are marked by double bars (||) at the
beginning of a line. Command parameters are separated by single bars (|). In the summary
below, parameter options are separated with semi-colons, parameter list
elements are separated with commas and optoins are in parenthesis.

```{list-table} example
:header-rows: 1
:name: test

* - [command syntax](rivt-syntax.md#tags)                                          
  - API 
* - || text | rel file path | rivt; plain                     
  - R I V
```


|| init | rel file path,                                      R

|| append | rel file path,                                    R

|| image  | rel file path \, (2nd image) | width \, (width),      I

|| table  | rel file path | max col width \, align,             I

|| declare | rel file path |  print; noprint,                 V


<hr>

## tags
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

