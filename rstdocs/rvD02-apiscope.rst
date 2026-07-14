**D.5 | API Scopes**
==========================

.. _markup-R:

**[1]** rv.R Markup
------------------------------------

The *Run API* processes text and scripts. It does not use markup. The
header substring takes an additional parameter that specifies the type of
text or script. The header substring has the form:

.. code-block:: python

    rv.R("""Section title | script_type, other parameters""")

=========================== ====================================================
       script type                            Description 
=========================== ====================================================
   endnotes                     Footnotes separated by blank line, in order   
   python                       Python script
   literal                      literal text
   rst                          reStructuredText
   html                         HTML markup
   mermaid                      Mermaid diagram (requires mermaid installation)
   latex                        LaTeX (requires LaTeX installation)
=========================== ====================================================

------------------------------------------

.. _markup-I:

**[2]** rv.I Markup
-------------------------------------------------------------------------------
 
The *Insert API* inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

==================================================================== =========================
       Tags / Commands / Assignment                                           Description
==================================================================== =========================
  text **_[C]**                                                        :ref:`Bold center text` 
**text math _[M]** description                                         :ref:`Text math` 
**LaTeX math _[L]** description                                        :ref:`LaTeX math` 
text **_[#]** text                                                     :ref:`Endnote number`  
text **_[G] text, term**                                               :ref:`Term link`
text **_[S] text, section link**                                       :ref:`Section link`
text **_[U] text, label**                                              :ref:`URL link`   
text **_[V] var_name** text                                            :ref:`Substitute value`
**title _[T]**                                                         :ref:`Number table`
 **_[[TEXT]]** type                                                    :ref:`Text block`
 **_[[END]]**                                                          :ref:`End block`
 **| IMAGE |** relative path |  scale, caption, figure                 :ref:`Image file`
 **| IMAGE2 |** rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2      :ref:`Adjacent images`
 **| TEXT |** relative path |  language                                :ref:`Text file`
 **| TABLE |** rel path | title, width, rows, align, head              :ref:`Table file`     
==================================================================== =========================

-------------------------------------------------

.. _markup-V:
 
**[3]** rv.V Markup
---------------------------------------------

The *Values API* defines values and evaluates equations and functions.

================================================================= ========================
        Tags / Commands / Assignment                                      Description
================================================================= ========================
**_[[TEXT]]** optional label                                       :ref:`Text block`
**_[[PYTHON]]** namespace                                          :ref:`Python block`
**_[[END]]**                                                       :ref:`End Block`
| **TABLE** | rel path | title,width,rows,align,head,num           :ref:`Table file`     
| **IMAGE** | relative path |  scale, caption, figure              :ref:`Image file`
| **IMAGE2** | rel path1, rel path2 | c1, c2, s1, s2, f1, f2       :ref:`Adjacent images`
| **VALTABLE** | rel path | title, width, rows                     :ref:`Values file`     
| **PYTHON** | relative path | namespace                           :ref:`Python file`
a **==:** 1*IN  | unit1, unit2, decimal, num | label               :ref:`Define value`
c **<=:** expression | unit1, unit2, decimal, num | label          :ref:`Assign value`
c **:=:** expression | unit1, unit2, decimal | label, number       :ref:`Function value`
a **<** c  | decimal | text1,text2,align, num                      :ref:`Compare value`
================================================================= ========================

---------------------------------------

.. _markup-T:

**[4]** rv.T Markup
------------------------------------------------ 

The *Tool API*  executes shell commands. 

========================================= ====================
   Command                                    Description
========================================= ====================
**_[[SHELL]]** process parameters         :ref:`Shell script`
**_[[END]]**                              :ref:`End block`
**| SHELL |** relative path | os, wait     :ref:`Shell File`
========================================= ====================

---------------------------------------

.. _markup-D:

**[5]** rv.D Markup
--------------------------------

The *Doc API* publishes formatted *docs* from the rivt API strings.

========================================================= ==================== 
   Tags / Commands / Assignment                              Description
========================================================= ==================== 
 **_[[METADATA]]** label                                    :ref:`Meta block` 
 **_[[END]]**                                               :ref:`End block`
**| PDFATTACH |** relative path | place, cover              :ref:`Attach PDF`   
**| PUBLISH |** doc title | type                            :ref:`Publish Doc`
========================================================= ==================== 
