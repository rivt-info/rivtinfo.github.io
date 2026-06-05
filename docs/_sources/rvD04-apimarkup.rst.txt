**D.4 | API Scopes**
==========================

.. _markup-api:

**[1]** rv.R Markup
------------------------------------


The *Run* API function executes markup and scripts.


**[1-1]** rv.R Block Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


========================================= ==============================
       Block Tag                            Description 
========================================= ==============================
**_[[PYTHON]]** namespace                       :ref:`Python block`
**_[[MARKUP]]** type                            :ref:`Markup block`
**_[[END]]**                                    :ref:`End Block`
========================================= ==============================

------------------------------------------

**[1-2]** rv.R Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
============================================================== =====================
      Command                                                      Description
============================================================== =====================
 **| PYTHON |** relative path | namespace                        :ref:`Python file`
 **| MARKUP |** relative path | type                             :ref:`Markup file`
============================================================== =====================

-------------------------------------------


**[2]** rv.I Markup
-------------------------------------------------------------------------------

 
The *Insert* API function inserts and formats static sources into the *doc*,
including images, tables, links and formatted text.

-------------------------------------------------


**[2-1]** rv.I Line Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================================================= ============================
     Line Tag                                       Description 
================================================= ============================
                text **_[C]**                     :ref:`Bold center text` 
           **text math _[M]** description         :ref:`Text math` 
          **LaTeX math _[L]** description         :ref:`LaTeX math` 
                text **_[#]** text                :ref:`Endnote number`  
                text **_[G] text, term**          :ref:`Term link`
                text **_[S] text, section link**  :ref:`Section link`
                text **_[U] text, label**         :ref:`URL link`   
                text **_[V] var_name** text       :ref:`Variable value`
               **title _[T]**                     :ref:`Number table`
             **caption _[F]**                     :ref:`Number figure`
================================================= ============================

--------------------------------------------


**[2-2]** rv.I Block Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


========================================= ==============================
       Block Tag                               Description 
========================================= ==============================
 **_[[BOX]]** optional label                  :ref:`Box block`
 **_[[TOPIC]]** topic                         :ref:`Topic block`
 **_[[END]]**                                 :ref:`End block`
========================================= ==============================


-----------------------------------------


**[2-3]** rv.I Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


==================================================================== =========================
         Command                                                          Description
==================================================================== =========================
 **| IMAGE |** relative path |  scale, caption, figure                 :ref:`Image file`
 **| IMAGE2 |** rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2      :ref:`Adjacent images`
 **| TEXT |** relative path |  language                                :ref:`Text file`
 **| TABLE |** rel path | title, width, rows, align, head              :ref:`Table file`     
==================================================================== =========================


 
**[3]** rv.V Markup
---------------------------------------------

 

The *Values* API function defines values and evaluates equations and functions.


---------------------------------------------

**[3-1]** Line Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Format a line of text**

======================================== ==============================
       Line Tag                                         Description 
======================================== ==============================
         text **_[V] var_name** | text      :ref:`Variable value`
        **title _[]**                       :ref:`Number table`
      **caption _[F]**                      :ref:`Number figure`                              
======================================== ==============================


---------------------------------------------


**[3-2]** Block Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

**Format or execute a block of text**

========================================= ==============================
       Block Tag                               Description 
========================================= ==============================
**_[[PYTHON]]** namespace                       :ref:`Python block`
**_[[END]]**                                    :ref:`End Block`
========================================= ==============================


---------------------------------------------

**[3-3]** Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Format files and calculations**

================================================================= ========================
        Command                                                      Description
================================================================= ========================
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


**[4]** rv.T Markup
------------------------------------------------

 

The *Tool* API function executes shell commands. 


---------------------------------------

**[4-1]** Block Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

======================================= ==============================
       Block Tag                              Description
======================================= ==============================
 **_[[SHELL]]** process parameters            :ref:`Shell script`
 **_[[END]]**                                 :ref:`End block`
======================================= ==============================


---------------------------------------

**[4-2]** Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

========================================= ====================
   Command                                    Description
========================================= ====================
**| SHELL |** relative path | os, wait     :ref:`Shell File`
========================================= ====================

---------------------------------------

**[5]** rv.D Markup
--------------------------------


The *Doc API* publishes formatted *docs* from the rivt API strings.

---------------------------------------


**[5-1]** Block Tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

======================================= ==============================
       Block Tag                         Description 
======================================= ==============================
 **_[[METADATA]]** label                     :ref:`Meta block` 
 **_[[END]]**                                :ref:`End block`
======================================= ==============================


**[5-2]** Commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 

========================================================= ==================== 
       Command                                                   Description
========================================================= ==================== 
**| PDFATTACH |** relative path | place, cover              :ref:`Attach PDF`   
**| PUBLISH |** ini rel. path | type                        :ref:`Publish Doc`
========================================================= ==================== 
