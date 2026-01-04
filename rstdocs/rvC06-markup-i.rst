**C.6 Insert - rv.I**
========================

**[1t]** rv.I Markup
-------------------------------------

.. raw:: html

    <hr>

The *Insert* API function inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

**[2t]** Format line of text
-------------------------------------

=========================================== =======================================
        Line Tags                                 Description 
=========================================== =======================================
    latex math _[L]                                  :ref:`latextag` 
    ascii math _[M]                                  :ref:`asciitag`
          text _[#] text                             :ref:`notetag`  
          text _[C]                                  :ref:`centertag` 
          text _[R]                                  :ref:`righttag` 
equation label _[E]                                  :ref:`equatag`
         title _[T]                                  :ref:`tabletag`
section anchor _[A]                                  :ref:`anchortag`
          text _[N] anchor_name link                 :ref:`linktag`
          text _[G] glossary link term               :ref:`termtag`
          text _[D] doc link                         :ref:`doctag`
          text _[U] external url                     :ref:`urltag`   
=========================================== =======================================
   
**[3t]** Format text blocks
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
 _[[NEWPAGE]]                               :ref:`pageblk`
========================================= ==============================

**[4t]** Read, Write Files
-------------------------------------

============================================================== =====================
         | Command | path | parameters                          Description
============================================================== =====================
\| IMAGE | relative path |  scale, caption, figure              :ref:`imgcmd`
\| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2   :ref:`img2cmd`
\| TABLE | relative path | width, align, title, number          :ref:`tablecmd`     
\| TEXT | relative path |  language                             :ref:`textcmd`
============================================================== =====================


