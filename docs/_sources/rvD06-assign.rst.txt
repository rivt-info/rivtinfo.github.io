**D.4 |** Assignment
========================


.. _assign-summary:

**[1]** Summary
-------------------------------------

**Assign values to expressions**

========== =============================================================== ========================
API Scope           Command                                                        Description
========== =============================================================== ========================
rv.V         a **==:** 1*IN  | unit1, unit2, decimal | label                 :ref:`Define value`
rv.V         c **<=:** expression | unit1, unit2, decimal | label            :ref:`Assign value`
rv.V         c **:=:** func(x,y) | unit1, unit2, decimal | label             :ref:`Assign function`
rv.V         a **<=** c | unit, decimal, text1, text2 | label                :ref:`Compare value`
========== =============================================================== ========================


.. _Define value:

**[2]** Define values | **==:**
-------------------------------------------

Defines a value and writes it to the file *vdocnum-s.csv* where *num* is the 
*docnumber* and *s* is the section number. The file is written to the folder
*stored/vals* unless *singledocB* is set to *True* in the comment variable.

The stored values can read and defined in other rivt files using the VALUES
command.

.. code-block:: text

    Syntax:
        c ==: 5*unit | unit1, unit2, decimals | label, *num,nonum*

    Example:
        D_1 ==: 10*IN | IN, M, 3 | beam depth, num
  
=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================


.. _Assign value:

**[3]** Assign expression values | **<=:**
-------------------------------------------

Assigns a value to an equation and writes the values to a file *vdocnum-s.csv*
where *num* is the *doc number* and *s* is the section number. The file is
written to the folder *stored/vals* unless *rv single doc* is set to *True* 
in which case values are stored in the rivt file folder (root).

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

.. code-block:: text

    Syntax:
        b <=: a * 10*FT | unit1, unit2, decimals | label, num;nonum

    Example:
        b_1 <=: E_1 * 12.1*IN^2 | KIP, KN, 2 | Std. 123, num


=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================


.. _Assign function:

**[4]** Assign function values | **:=:**
-------------------------------------------

Assigns a value to an equation and writes the values to a file *vdocnum-s.csv*
where *num* is the *doc number* and *s* is the section number. The file is
written to the folder *stored/vals* unless *rv single doc* is set to *True* 
in which case values are stored in the rivt file folder (root).

The label is a reference printed with the equation. The units specify the
result expressed in two different units. The integer specifies the number of
places after the decimals.

.. code-block:: text

    Syntax:
        c :=: function name() | unit1, unit2, decimals | label, num;nonum

    Example:

        c_1 :=: func1(a,b) | KIP, KN, 2 | ACI 318-19 Table 22.5.5.1, num 


=========== ==========================
API Scope     rv.V
File Types    .csv
Doc Types     text, PDF, HTML
=========== ==========================


.. _Compare value:

**[5]** Compare values | **<=**
-----------------------------------------

Format to text1 if comparison is true and text2 if false. 

Comparison operators:

.. code-block:: text

    ==	  Equal	x == y	
    !=	  Not equal	x != y	
    >	  Greater than	x > y	
    <	  Less than	x < y	
    >=	  Greater than or equal to x >= y	
    <=	  Less than or equal to x <= y

.. topic:: <> 

    .. code-block:: text

        Syntax:  
            a < b | unit, decimal, text1, text2
        
        Example:
           a < b | ft, 2, OK, NOT OK
  
=========== ==========================
API Scope     rv.V
Doc Types     text, PDF, HTML
=========== ==========================
