**C.6 Insert - rv.I**
========================

**[1t]** rv.I Markup
-------------------------------------

.. raw:: html

    <hr>

The *Insert* API function inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

=============================================== ============================
        Line Tags                                 Description 
=============================================== ============================
              text **_[C]**                      :ref:`Center text` 
              text **_[R]**                      :ref:`Right justify text` 
        text  math **_[M]**                      :ref:`Text math` 
        LaTeX math **_[L]**                      :ref:`LaTeX math` 
              text **_[#]** more text            :ref:`Endnote number`
              text **_[G]** glossary term        :ref:`Term reference`
              text **_[S]** section label        :ref:`Section link` 
              text **_[D]** rivt_file text       :ref:`Doc link`
              text **_[U]** label, url           :ref:`URL link` 
              text **_[V]** var_name text        :ref:`Variable value`
   assign or label **_[E]**                      :ref:`Equation number`
             title **_[T]**                      :ref:`Table number`
           caption **_[F]**                      :ref:`Figure number`
=============================================== ============================


========================================= ==============================
       Block Tags                              Description 
========================================= ==============================
 **_[[INDENT]]** spaces (4 default)           :ref:`Indent text block`
 **_[[ITALIC]]** spaces (4 default)           :ref:`Indent italic block`
 **_[[ENDNOTES]]** optional label             :ref:`Endnotes block`
 **_[[TEXT]]** optional language              :ref:`Text block`
 **_[[TOPIC]]** topic                         :ref:`Topic block`
 **_[[END]]**                                 :ref:`End block`
========================================= ==============================

==================================================================== =========================
         Commands                                                         Description
==================================================================== =========================
 **| TEXT |** relative path |  language                                :ref:`Text file`
 **| TABLE |** rel path | title, width, rows, align, head              :ref:`Table file`     
 **| IMAGE |** relative path |  scale, caption, figure                 :ref:`Image file`
 **| IMAGE2 |** rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2      :ref:`Adjacent images`
==================================================================== =========================


 