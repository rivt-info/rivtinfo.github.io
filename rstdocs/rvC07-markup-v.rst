**C.7 Values - rv.V**
========================


**[1t]** rv.V Markup
-------------------------

.. raw:: html

    <hr>

The *Value* API function defines values and evaluates equations and functions.

========================================= ==============================
       Line Tags                             Description 
========================================= ==============================
equation or label _[E]                       :ref:`Equation label`
valtable command or title line _[T]          :ref:`Table title``                              
========================================= ==============================

========================================= ==============================
       Block Tags                           Description 
========================================= ==============================
 _[[PYTHON]] namespace                      :ref:`pyblk`                            
 _[[END]]                                   :ref:`endblk`
 _[[NEWPAGE]]                               :ref:`pageblk`
========================================= ==============================

============================================================== =====================
         | Command | path | parameters                          Description
============================================================== =====================
 \| IMAGE | relative path |  scale, caption, figure              :ref:`imgcmd`
 \| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, num1, num2   :ref:`img2cmd`
 \| VALTABLE | rel path | title, width, rows                     :ref:`valtablecmd`     
 \| PYTHON | relative path | namespace                           :ref:`pycmd`
 a =: 1*IN  | unit1, unit2, decimal | label                      :ref:`defcmd`
 c <=: expression | unit1, unit2, decimal | label                :ref:`asscmd`
 a < c  | decimal | stamp text, align, color                     :ref:`compcmd` 
============================================================== =====================
