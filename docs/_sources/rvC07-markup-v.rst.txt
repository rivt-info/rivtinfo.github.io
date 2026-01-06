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
text _[V] var_name text                         :ref:`Variable value`
assign command or label _[E]                    :ref:`Equation label`
valtable command or table title _[T]            :ref:`Table title`                              
========================================= ==============================

========================================= ==============================
       Block Tags                           Description 
 [[PYTHON]] namespace                       :ref:`Python block`
_[[END]]                                    :ref:`End Block`
_[[NEWPAGE]]                                :ref:`Start new page`
========================================= ==============================

================================================================= =====================
         | Command | path | parameters                               Description
================================================================= =====================
   \| IMAGE | relative path |  scale, caption, figure              :ref:`Image file`
   \| IMAGE2 | rel path1, rel path2 | s1, s2, c1, c2, fig1, fig2   :ref:`Adjacent images`
   \| VALTABLE | rel path | title, width, rows                     :ref:`Values file`     
   a =: 1*IN  | unit1, unit2, decimal | label                      :ref:`Define variable`
   c <=: expression | unit1, unit2, decimal | label                :ref:`Assign value`
   a < c  | decimal | text, align, color                           :ref:`Compare values`
   \| PYTHON | relative path | namespace                           :ref:`Python file`
================================================================= =====================
