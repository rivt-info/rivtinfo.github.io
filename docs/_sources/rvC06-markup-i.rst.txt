**C.6 Insert - rv.I**
========================

**[1t]** rv.I Markup
-------------------------------------

.. raw:: html

    <hr>

The *Insert* API function inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

=========================================== =======================================
        Line Tags                                 Description 
=========================================== =======================================
             text _[#] text                    :ref:`Endnote number`  
             text _[C]                         :ref:`Center text` 
             text _[R]                         :ref:`Right justify text`
       latex math _[L]                         :ref:`LaTeX math` 
       ascii math _[M]                         :ref:`ASCII math` 
             text _[S] section label           :ref:`Section link`
             text _[G] glossary link term      :ref:`Term reference`
             text _[D] doc number              :ref:`Doc link`
             text _[U] external url            :ref:`URL link`   
equation or label _[E]                         :ref:`Equation label`
  values or title _[T]                         :ref:`Table title`  
=========================================== =======================================

========================================= ==============================
       Block Tags                           Description 
========================================= ==============================
 _[[INDENT]] spaces (4 default)             :ref:`Indent text block`
 _[[ITALIC]] spaces (4 default)             :ref:`Indent italic block`
 _[[ENDNOTES]] optional label               :ref:`Endnotes block`
 _[[TEXT]] optional language                :ref:`Text block`
 _[[TOPIC]] topic                           :ref:`Topic block`
 _[[END]]                                   :ref:`End block`
========================================= ==============================

================================================================== ========================
         | Command | path | parameters                               Description
================================================================== ========================
 \| TEXT | relative path |  language                                :ref:`Text file`
 \| TABLE | rel path | title, width, rows, align, head              :ref:`Table file`     
 \| IMAGE | relative path |  scale, caption, figure                 :ref:`Image file`
 \| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2      :ref:`Adjacent images`
================================================================== ========================


 