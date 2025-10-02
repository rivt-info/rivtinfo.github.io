3.7 Quick Lookup
=======================


**[01]** Line tags
----------------------

============= ========================== =======================================
Scope             Line Tags                    Description (doc output)
============= ========================== =======================================
I              *text*        _[B]          center bold text (pdf, html)
I              *description* _[D]          endnote description (all)
I              *text*        _[C]          center text (all)
I              text _[#] text              endnote (all)
I              text _[L] *doc link*        doc link (all)
I              text _[R] *report link*     report link (all)
I              text _[U] *url*             url link (all)
I, V           *equation*    _[S]          format symbol math (all) 
I, V           *label*       _[E]          equation label (all)
I, V           *caption*     _[F]          image label (all) [1]
I, V           *title*       _[T]          table label (all) [1]
I, V             _____   or  _[H]          horizontal line, >5 underscores (all)
I, V                         _[P]          new page (all)
============= ========================== =======================================

[1] tag may be added to parameter in IMG and TABLE commands


**[02]** Block tags
----------------------

============ ============================= =====================================
Scope          Block Tags                    Description (doc scope)
============ ============================= =====================================
I             _[[B]]                          indent bold (pdf, html)
I             _[[I]]                          indent italic (pdf, html)
I             _[[O]]                          italic, oblique (pdf, html)
I             _[[L]]                          LaTeX (pdf, html)
I             _[[N]]                          indent (all)
I             _[[C]] *language*               code, literal (all)
M             _[[AUTH]] *description*         author data (all)
M             _[[FORK]] *description*         fork data (all)
R             _[[WIN]] *description*          Windows command script (all)
R             _[[MACOS]] *description*        Mac shell script (all)
R             _[[LINUX]] *description*        Linux shell script (all)
T             _[[PYTHON]] *description*       Python functions (all)
T             _[[RUBY]] *description*         Ruby script (all)
T             _[[QCAD]] *description*         QCAD script (pdf,html)
T             _[[OPENSEES]] *description*     OpenSeesscript (all)
T             _[[LATEX]] *description*        LaTeX commands (all)
T             _[[HTML]] *description*         HTML commands (all)
all           _[[T]] *topic*                  topic (all)
all           _[[Q]]                          quit (all)
============ ============================= =====================================


**[03]** Commands
-------------------

========= ===================================================== =================
Scope           | Command | parameters                              file types
========= ===================================================== =================
D            | APPEND | rel path | fname | page;nopage               pdf, html
D            | DOCS | rel path | fname | rpdf; tpdf; txt; html    pdf, txt, html
I, V         | TEXT | rel path | fname | normal; literal          txt, tex, rst
I, V         | TABLE | rel path | fname | title, width, l;c;r     csv, txt, xlsx
I, V         | IMG | rel path | fname |  caption, scale              png, jpg
I, V         | IMG2 | rel path | fname | c1, c2, s1, s2              png, jpg
V            | VALUES | rel path | fname | title, [rows]               csv
V            a := 1*unit1 | unit1, unit2, decimal | descrip        define value
V            b <= a + 3 | unit1, unit2, decimal | ref              assign value
R            | LINUX | rel path | fname                                sh
R            | MACOS | rel path | fname                                sh
R            | WIN | rel path | fname                                  bat, cmd
T            | HTML | rel path | fname                                 html
T            | LATEX | rel path | fname                                tex
T            | PYTHON | rel path | fname                               py
T            | QCAD   | rel path | fname                               js
========= ===================================================== =================
