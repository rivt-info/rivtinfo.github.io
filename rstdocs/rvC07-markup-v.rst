**C.7 Values - rv.V**
========================


**[1t]** Summary
-------------------------

.. raw:: html

    <hr>

The *Value* API function inserts static sources including images, tables and
formatted text.

============================= =======================================
        Line Tags              Description (doc scope)
============================= =======================================
    text _[#] text             endnote number (all)
    text _[C]                  center text (all)
    text _[R]                  right justify text (all)
   label _[E]                  equation number and label (all)
   title _[T]                  table number and title (all)[1]
    text _[D] term link        link to defined term in report (all)
    text _[S] section link     link to section in doc (all)
    text _[R] report link      link to doc in report (all)
    text _[U] external url     external url link (all)
    \-\-\-\-\-                 >4 dashes inserts line (all)[2]
    \=\=\=\=\=                 >4 double dashes inserts page (all)[2]
============================= =======================================

[1] title tag may be added to TABLE command

[2] starts in first indented column (absolute column 4)

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
_[[INDENT]] spaces (4 default)           Indent (all)
_[[ITALIC]] spaces (4 default)           Italic indent - (all)
_[[NOTES]] optional label                Endnote descriptions (all)
_[[TEXT]] optional language              *literal*, code (all)
_[[TOPIC]] topic                         Topic (all)
_[[VALUES]] title, rows (_[T])           Define values(all)
_[[END]]                                 End block (all)
======================================= ==============================

======================================================== ===== ==================
         | Command | path | parameters                    R/W   input types
======================================================== ===== ==================
 \| FIGURE | relative path |  scale, caption              R     *.png, .jpg*
 \| FIGURE2 | relative path | s1, s2, c1, c2              R     *.png, jpg*
 \| IMAGE | relative path |  scale                        R     *.png, .jpg*
 \| IMAGE2 | relative path | scale1, scale2               R     *.png, jpg*
 \| TABLE | relative path | title, width, l;c;r,          R     *csv, txt, xlsx*
 \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
 \| VALUES | relative path | title, rows  (_[T])[1]       R     *csv*
a := 1*IN  | unit1, unit2, decimal | label (_[E])         W     define value
b <= a + 3*FT | unit1, unit2, decimal | label (_[E])      W     assign value
c <= func1(x,y) | unit1, unit2, decimal | label (_[E])    W     assign value
======================================================== ===== ==================

[1] The equation tag (_[E]) is ignored when values are defined in a block

