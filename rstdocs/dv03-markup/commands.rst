**3.4** Commands
===================

Commands read and write files and assign values to variables. They typically
start in the first column with double vertical bars. The command bar is
followed by the command name, the relative file path and any applicable
parameters.There are two exceptions to this pattern - the assignment (=) and
definition (:=) commands.

In the syntax descriptoin below, parameters are separated by commas and
parameter options are separated by colons.

**KEY**  
--------------------------------------------

||command | : description

.. raw:: html

    <hr>

.. topic::  command syntax

    - function scope
    - applicable output types


||APPEND| :  append a PDF file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: ||APPEND| rel. pth | num; nonum 

    - rv.D
    - PDF, HTML

||DOC| :  write a doc file
-------------------------------------------

.. raw:: html

    <hr>

.. topic:: ||DOC| rel. pth | rpdf; txt; html; tpdf

    - rv.D
    - PDF, HTML




rv.V         a := 1+1 | reference | units | decimals         := a command tag







========== ========================================================= ================
Scope                      Read Commands                              File Types
========== ========================================================= ================
rv.V       **|VALUES|** rel. pth | title, [rows], -;_[V]              .csv
rv.I, rv.V **|IMG|** rel. pth | caption, scale, -;_[F]                .png,.jpg
rv.I, rv.V **|IMG2|** rel. pth | c1, c2, s1, s2, -;_[F]               .png,.jpg
rv.I       **|TABLE|** rel. pth | title, col w, l;c;r, [r], -;_[T]    .csv,.txt,.xlsx
rv.I       **|TEXT|** rel. pth | [[block tag]]                        .txt,.tex
========== ========================================================= ================



  
