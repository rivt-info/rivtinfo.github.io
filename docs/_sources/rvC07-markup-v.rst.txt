**C.7 Values - rv.V**
========================


**[1i]** rv.V Markup
-------------------------

.. raw:: html

    <hr>

The *Values* API function defines values and evaluates equations and functions.


**[2i]** Line Tags
-------------------------

.. raw:: html

    <hr>

**Format a line of text**

======================================== ==============================
       Line Tag                                         Description 
======================================== ==============================
         text **_[V] var_name** | text      :ref:`Variable value`
        **label _[E]**                      :ref:`Number equation`
        **title _[T]**                      :ref:`Number table`
      **caption _[F]**                      :ref:`Number figure`                              
======================================== ==============================

**[3i]** Block Tags
-------------------------

.. raw:: html

    <hr>

**Format or execute a block of text**

========================================= ==============================
       Block Tag                               Description 
========================================= ==============================
**_[[PYTHON]]** namespace                       :ref:`Python block`
**_[[END]]**                                    :ref:`End Block`
========================================= ==============================

**[2i]** Commands
-------------------------

.. raw:: html

    <hr>

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
