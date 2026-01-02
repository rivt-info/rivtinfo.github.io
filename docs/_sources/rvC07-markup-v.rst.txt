**C.7 Values - rv.V**
========================


**[1t]** rv.V Markup
-------------------------

.. raw:: html

    <hr>

The *Value* API function inserts static sources including images, tables and
formatted text.


**[2t]** Format line
-------------------------------------

========================================= =======================
       Line Tags                            Description 
========================================= =======================            
            text _[#] text                 :ref:`notetag`  
            text _[C]                      :ref:`centertag` 
            text _[R]                      :ref:`righttag` 
  equation label _[E]                      :ref:`equatag`
     table title _[T]                      :ref:`tabletag` 
     anchor_name _[A]                      :ref:`anchortag`
            text _[N] anchor_name link     :ref:`linktag`
            text _[G] glossary link term   :ref:`termtag`
            text _[D] doc link             :ref:`doctag`
            text _[U] external url         :ref:`urltag`   
  \-\-\-\-\-                               :ref:`linetag` [1]
  \=\=\=\=\=                               :ref:`pagetag` [1]
========================================= ======================= 

.. highlight:: none

::

    [1] must start in first indented column (absolute column 4)



**[3t]** Format block
-------------------------------------

========================================= ==============================
       Block Tags                           Description 
========================================= ==============================
 _[[INDENT]] spaces (4 default)             :ref:`indenttag`
 _[[ITALIC]] spaces (4 default)             :ref:`italictag`
 _[[NOTES]] optional label                  :ref:`notestag`
 _[[TEXT]] optional language                :ref:`codetag`
 _[[TOPIC]] topic                           :ref:`topictag`
 _[[END]]                                   :ref:`endblk`
========================================= ==============================


**[4t]** Read, Write Files
-------------------------------------

============================================================== =====================
         | Command | path | parameters                          Description
============================================================== =====================
\| IMAGE | relative path |  scale, caption, figure              :ref:`imgcmd`
\| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2   :ref:`img2cmd`
\| TABLE | relative path | width, align, title                  :ref:`tablecmd`     
\| TEXT | relative path |  language                             :ref:`textcmd`
\| VALUES | relative path | title, rows                         :ref:`valtablecmd` 
a := 1*IN  | unit1, unit2, decimal | label                      :ref:`defcmd`
c <= expression | unit1, unit2, decimal | label                 :ref:`asscmd`
\| PYTHON | relative path | namespace                           :ref:`pycmd`
============================================================== =====================

