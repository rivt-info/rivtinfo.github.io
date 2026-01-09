
**F.1 Quick Ref**
================== 


**[1t]** API functions
--------------------------------------------------------------------- 

.. raw:: html

    <hr>

=============== =============== ===========================================
API Functions        Name             Purpose
=============== =============== ===========================================
rv.R(rS)           **R** un          Run shell commands
rv.I(rS)           **I** nsert       Insert static sources 
rv.V(rS)           **V** alues       Calculate values
rv.T(rS)           **T** ools        Python and markup scripts
rv.S(rS)           Skip              Skip section (comments and debugging)
rv.D(rS)           Doc               Publish docs 
rv.X(rS)           Exit              Exit rivt (debugging)
=============== =============== ===========================================

The first line of a *rivt string* (rS) is a *header substring*.

.. code-block:: python

    rv.I("""A New Section | private, doc, section

        Content text
        ...
        
        """)

Default settings in the *header substring* do not need to be specified. The
default setting for each API is listed first (**in bold**) in the table below.
 
========== ===================== ===================== =====================
API          private;public         doc;stored         section;merge         
========== ===================== ===================== ===================== 
rv.R        **private**;public     **stored**;doc       **merge**;section
rv.I        **private**;public     **doc**;stored       **section**;merge   
rv.V        **private**;public     **doc**;stored       **section**;merge    
rv.T        **private**;public     **stored**;doc       **merge**;section
rv.S        **private**;public     **stored**;doc       **merge**;section
rv.D        **private**;public     **stored**           **merge**
rv.X        **private**;public     **stored**           **merge**
========== ===================== ===================== =====================




**[2t]** Line Tag Summary
-------------------------------------

.. raw:: html

    <hr>

**Format a line or partial line of text**
  
========== ================================================= ===============================
API Scope             Line Tags                                     Description 
========== ================================================= ===============================
rv.I                          text **_[C]**                         :ref:`Center text` 
rv.I                          text **_[R]**                         :ref:`Right justify text`
rv.I                    text  math _[M]                         :ref:`Text math` 
rv.I                    LaTeX math _[L]                         :ref:`LaTeX math` 
rv.I                   label, url  _[U]                         :ref:`URL link`   
rv.I                          text _[G] glossary term           :ref:`Term reference`
rv.I                          text _[S] section label           :ref:`Section link`
rv.I                          text _[#] more text               :ref:`Endnote number`  
rv.I                text rivt_file _[D] more text               :ref:`Doc link`
rv.V, I              text var_name _[V] more text               :ref:`Variable value`
rv.V, I            assign or label _[E]                         :ref:`Equation label`
rv.V, I          valtable or title _[T]                         :ref:`Table title`
========== ================================================= ===============================


**[3t]** Block Tag Summary
-------------------------------------

.. raw:: html

    <hr>


**Format blocks of text**

========== ========================================= ===============================
API Scope         Block Tags                           Description 
========== ========================================= ===============================
rv.R        **_[[SHELL]]** process parameters              :ref:`Shell script`
rv.I        **_[[INDENT]]** spaces (4 default)             :ref:`Indent text block`
rv.I        _[[ITALIC]] spaces (4 default)             :ref:`Indent italic block`
rv.I        _[[ENDNOTES]] optional label               :ref:`Endnotes block`
rv.I        _[[TEXT]] optional language                :ref:`Text block`
rv.I        _[[TOPIC]] topic                           :ref:`Topic block`
rv.I        _[[BOX]] label                             :ref:`Box block`
rv.V, T     _[[PYTHON]] namespace                      :ref:`Python block`
rv.T        _[[MARKUP]] type                           :ref:`Markup block`
rv.T        _[[METADATA]] label                        :ref:`Meta block`
rv.D        _[[LAYOUT]] label                          :ref:`Layout block` 
all         _[[END]]                                   :ref:`End block`
all         _[[NEW PAGE]]                              :ref:`Start new page`
========== ========================================= ===============================


**[4t]** Command Summary
-------------------------------------

.. raw:: html

    <hr>

**Read, write and format files**

========== ============================================================== =====================
API Scope           | Command | path | parameters                          Description
========== ============================================================== =====================
rv.R       **| SHELL |** relative path | os, wait                             :ref:`Shell file`
rv.I       **| TEXT |** relative path |  language                             :ref:`Text file`
rv.V, I    \| TABLE | rel path | title, width, rows, align, head           :ref:`Table file`     
rv.V, I    \| IMAGE | relative path | caption, scale, number               :ref:`Image file`
rv.V, I    \| IMAGE2 | rel path1, rel path2 | caption, scale number        :ref:`Adjacent images`
rv.V       \| VALTABLE | rel path | title, rows, number                    :ref:`Values file`     
rv.V       a =: 1*IN  | unit1, unit2, decimal | label                      :ref:`Define variable`
rv.V       c <=: expression | unit1, unit2, decimal | label                :ref:`Assign value`
rv.V       a < c  | decimal | text, align, color                           :ref:`Compare values`
rv.T, V    \| PYTHON | relative path | namespace                           :ref:`Python file`
rv.T       \| MARKUP | relative path | type                                :ref:`Markup file`
rv.D       \| ATTACHPDF | relative path | place, title                     :ref:`Attach PDF`   
rv.D       \| PUBLISH | ini rel. path | type                               :ref:`Publish doc` 
========== ============================================================== =====================


**Default command paths**

See :ref:`here <report folders>` for the folder structure. If files
are in the default path only the file name needs to be provided.

================ =========================
   Command         Default Path
================ =========================
\| SHELL |          /src/shell/
\| TEXT |           /src/data/
\| TABLE |          /src/data/
\| IMAGE |          /src/image/
\| IMAGE2 |         /src/image/
\| VALTABLE |       /src/data/  [1]    
\| PYTHON |         /src/scripts/
\| MARKUP |         /src/scripts/
\| ATTACHPDF |      /src/gendocs/  
\| PUBLISH |        /src/gendocs/
================ =========================

[1]  use /stored/data/ to read values previously defined in the report

