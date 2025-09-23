3.7 Quick Summary
=======================


**[01]** Line tags
----------------------

============= ========================== =======================================
Scope             Line Tags                    Description (doc scope)
============= ========================== =======================================
I, V              _____                    horizontal line, >4 underscores 
I, V              _[P]                     new page (all)
I              *description* _[D]          endnote description (all)
I              text _[#] text              endnote (all)
I              text _[L] *doc link*        doc link (all)
I              text _[R] *report link*     report link (all)
I, T           text _[U] *url*             url link (all)
I, V           *equation* _[S]             format symbol math (all) 
I              *text* _[B]                 center bold text (pdf, html)
I              *text* _[C]                 center text (all)
I, V           *label* _[E]                equation label (all)
I, V           *caption* _[F]              image label (all) [1]
I, V           *title* _[T]                table label (all) [1]
V              *title* _[V]                values table label (all) [1]
============= ========================== =======================================

[1] tag may be added to caption and title parameters in *commands*


**[02]** Block tags
----------------------

============ ============================= =====================================
Scope        Block Tags                    Description (doc scope)
============ ============================= =====================================
R             _[[WIN]] *description*          Windows command script (all)
R             _[[MACOS]] *description*        Mac shell script (all)
R             _[[LINUX]] *description*        Linux shell script (all)
I             _[[C]] *language*               code, literal (all)
I             _[[B]]                          bold (pdf, html)
I             _[[I]]                          indent italic (pdf, html)
I             _[[S]]                          indent (all)
I             _[[O]]                          italic, oblique (pdf, html)
I, V          _[[L]]                          LaTeX (pdf, html)
all           _[[Q]]                          quit (all)
all           _[[T]]                          topic (all)
V             _[[V]] *title*                  label values table (all)
T             _[[PYTHON]] *description*       Python functions (all)
T             _[[RUBY]] *description*         Ruby script (all)
T             _[[QCAD]] *description*         QCAD script (all)
T             _[[OPENSEES]] *description*     OpenSeesscript (all)
T             _[[LATEX]] *description*        LaTeX commands (all)
T             _[[HTML]] *description*         HTML commands (all)
M             _[[AUTH]] *description*         author data (all)
M             _[[FORK]] *description*         fork data (all)
============ ============================= =====================================


**[03]** Commands
-------------------

========= ==================================================== =================
Scope           (Read/Write)  | Command | parameters             file types
========= ==================================================== =================
R          (Rd) | LINUX | path | fname                                sh
R          (Rd) | MACOS | path | fname                                sh
R          (Rd) | WIN | path | fname                                  bat, cmd
I          (Rd) | TEXT | path | fname | title                    txt, tex, rst
I, V       (Rd) | TABLE | path | fname | title, width, l;c;r     csv, txt, xlsx
I, V       (Rd) | IMAGE | path | fname |  caption, scale              png, jpg
I, V       (Rd) | IMAGE2 | path | fname | c1, c2, s1, s2              png, jpg
V          (Rd) | VALUES | path | fname | title, [rows]               csv
V          (Wr)  a = 1 + 1  | unit1, unit2, decimal | descrip     assign value
V          (Wr)  b := a + 3 | unit1, unit2, decimal | ref         define value
T          (Rd) | HTML | path | fname                                 html
T          (Rd) | LATEX | path | fname                                tex
T          (Rd) | PYTHON | path | fname                               py
T          (Rd) | QCAD   | path | fname                               js
D          (Wr) | APPEND | path | fname                               pdf
D          (Wr) | DOCS | path | fname | rpdf; tpdf; txt; html    pdf, txt, html
========= ==================================================== =================
