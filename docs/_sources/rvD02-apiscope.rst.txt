**D.5 | API Scopes**
==========================

.. _markup-R:

**[1]** rv.R Markup
------------------------------------

The *Run API*  executes shell commands. 

========================================= =====================
   Command                                    Description
========================================= =====================
**_[[SHELL]]** process parameters          :ref:`Shell script`
**_[[END]]**                               :ref:`End block`
**| SHELL |** relative path | os, wait     :ref:`Shell File`
========================================= =====================

------------------------------------------

.. _markup-I:

**[2]** rv.I Markup
-------------------------------------------------------------------------------
 
The *Insert API* inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

==================================================================== =========================
       Tags / Commands                                                   Description
==================================================================== =========================
text **_[C]**                                                          :ref:`Bold center text`  
text **_[#]** text                                                     :ref:`Endnote number` 
text **_[G] text, term |** text                                        :ref:`Term link`
text **_[S] text, section link |** text                                :ref:`Section link`
text **_[U] text, label |** text                                       :ref:`URL link`   
text **_[V] var_name |** text                                          :ref:`Substitute value`
**text math _[M]** description                                         :ref:`Text math` 
**LaTeX math _[L]** description                                        :ref:`LaTeX math` 
**title _[T]**                                                         :ref:`Number table`
**_[[ENDNOTES]]**                                                      :ref:`Endnotes block`
**_[[END]]**                                                           :ref:`End block`
**| IMAGE |** file | scale, caption, num, time                         :ref:`Image file`
**| IMAGE2 |** file | s1, s2, c1, c2, fig1, fig2, num1, num2,          :ref:`Adjacent images`
**| TABLE |** file | title, width, rows, align, head                   :ref:`Table file`     
==================================================================== =========================

-------------------------------------------------

.. _markup-V:
 
**[3]** rv.V Markup
---------------------------------------------

The *Values API* defines values and evaluates equations and functions.

================================================================= ========================
        Tags / Commands / Assignment                                      Description
================================================================= ========================
**_[[ENDNOTES]]**                                                  :ref:`Endnotes block`
**_[[END]]**                                                       :ref:`End Block`
| **TABLE** | file | title,width,rows,align,head,num               :ref:`Table file`     
| **IMAGE** | file |  scale, caption, figure                       :ref:`Image file`
| **IMAGE2** | file1, file2 | c1, c2, s1, s2, f1, f2               :ref:`Adjacent images`
| **VALTABLE** | file | title, width, rows                         :ref:`Values file`     
a **==:** 1*IN  | unit1, unit2, decimal, num | label               :ref:`Define value`
c **<=:** expression | unit1, unit2, decimal, num | label          :ref:`Assign value`
c **:=:** expression | unit1, unit2, decimal | label, number       :ref:`Function value`
a **<** c  | decimal | text1,text2,align, num                      :ref:`Compare value`
================================================================= ========================

---------------------------------------

.. _markup-T:

**[4]** rv.T Text
------------------------------------------------ 

The *Text API* processes text and scripts. It does not use markup. The
header substring takes an additional parameter that specifies the type of
text or script. The header substring has the form:

.. code-block:: python

    rv.(T"""Section title | script_type, file: filename""")

=========================== ====================================================
       script type                            Description 
=========================== ====================================================
   PYTHON                       run Python code   
   python                       Python code
   text                         literal text
   rst                          reStructuredText
   html                         HTML markup
   mermaid                      Mermaid diagram (requires mermaid installation)
   latex                        LaTeX (requires LaTeX installation)
=========================== ====================================================

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
