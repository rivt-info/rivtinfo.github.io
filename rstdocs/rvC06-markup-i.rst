**C.6 Insert - rv.I**
========================

**[1t]** rv.I Markup
-------------------------------------

.. raw:: html

    <hr>

The *Insert* API function inserts static sources into the *doc*, including
images, tables, links and formatted text.

**Format a line of text**

=========================================== =======================================
        Line Tags                                 Description 
=========================================== =======================================
    latex math _[L]                                  :ref:`latextag` 
    ascii math _[M]                                  :ref:`asciitag`
          text _[#] text                             :ref:`notetag`  
          text _[C]                                  :ref:`centertag` 
          text _[R]                                  :ref:`righttag` 
equation label _[E]                                  :ref:`equatag`
         title _[T]                                  :ref:`tabletag` [1]
section anchor _[A]                                  :ref:`anchortag`
          text _[N] anchor_name link                 :ref:`linktag`
          text _[G] glossary link term               :ref:`termtag`
          text _[D] doc link                         :ref:`doctag`
          text _[U] external url                     :ref:`urltag`   
    \-\-\-\-\-                                       :ref:`linetag` [2]
    \=\=\=\=\=                                       :ref:`pagetag` [2]
=========================================== =======================================

.. highlight:: none

::

    [1] tag may be added to the label parameter in the TABLE commands
    [2] must start in first indented column (absolute column 4)

    
**Format a block of text**

======================================= ==============================
       Block Tags                        Description (doc scope)
======================================= ==============================
 _[[INDENT]] spaces (4 default)          :ref:`indenttag`
 _[[ITALIC]] spaces (4 default)          :ref:`italictag`
 _[[ENDNOTES]] optional label            Endnote descriptions (all)
 _[[TEXT]] optional language             *literal*, code language (all)
 _[[TERMS]] label                        Glossary of terms
 _[[TOPIC]] topic                        Topic (all)
 _[[END]]                                End block (all)
======================================= ==============================

**Read, Write and Format Files**

======================================================== ===== ==================
         | Command | path | parameters                    R/W   input types
======================================================== ===== ==================
 \| IMAGE | relative path |  scale, caption (_[I])        R     *.png, .jpg*
 \| IMAGE2 | relative path | s1, s2, c1, c2 (_[I])        R     *.png, jpg*
 \| TABLE | relative path | width, l;c;r, title           R     *csv, txt, xlsx*
 \| TEXT | relative path |  *normal;literal* ;code        R     *txt, code*
======================================================== ===== ==================

