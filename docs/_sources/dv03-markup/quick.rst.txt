3.5 Quick Look-up
=======================


=========== ===================================================== ==============
Scope                      Commands                                File Types
=========== ===================================================== ==============
rv.D         ||APPEND| rel. pth | num; nonum                       pdf,html,txt
rv.D         ||DOC| rel. pth | pdf; txt; html; pdf2                pdf, html,txt
rv.I, rv.V   || IMG | rel. pth | caption _[F], scale               png,.jpg
rv.I, rv.V   || IMG2 | rel. pth | c1 _[F], c2 _[F], s1, s2         png,.jpg
rv.I         || TABLE | rel. pth | title _[T], width, l;c;r, [r]   csv,txt,xlsx
rv.I         ||TEXT| rel. pth | _[[block tag]]                     txt,tex
rv.V         || VALUES | rel. pth | title _[V], [rows]             csv
rv.V         a = 1 + 1 | units | description                       assign value 
rv.V         b := a + 3 | units | decimals                         define value
=========== ===================================================== ==============

================ ========================== ====================================
Scope             Line Tags                    Description (doc scope)
================ ========================== ====================================
rv.I, rv.V               *text* _[B]          center bold text (pdf, html)
rv.I, rv.V               *text* _[C]          center text (all)
rv.I              *description* _[D]          footnote description (all)
rv.I, rv.V              *label* _[E]          equation label (all)
rv.I, rv.V            *caption* _[F]          autonumber image (all) [1]
rv.I              text _[LD] *doc link*       doc link (all)
rv.I              text _[LR] *report link*    report link (all)
rv.I              text _[LU] *url*            url link (all)
rv.I, rv.V                      _[P]          new page (all)
rv.I                 *equation* _[S]          format symbol math (all) 
rv.I                    *title* _[T]          table label (all) [1]
rv.V                    *label* _[V]          values table label (all) [1]
rv.I                   text _[#] text         footnote (all)
rv.I, rv.V                  --------          horizontal line (5 or more -)
================ ========================== ====================================

[1] tag may be added to the command parameter

=========== ===================== ==============================================
Scope        Block Tags              Description (doc scope)
=========== ===================== ==============================================
rv.I          _[[B]]                bold (pdf, html)
rv.I, rv.     _[[C]] *lang*         code, literal (all)
rv.I          _[[I]]                indent italic (pdf, html)
rv.I          _[[L]]                latex (pdf, html)
rv.I, rv.V    _[[S]]                indent (all)
rv.I          _[[O]]                italic, oblique (pdf, html)
rv.I, rv.V    _[[Q]]                quit (all)
rv.I, rv.V    _[[T]]                topic (all)
rv.V          _[[V]] *title*        values label (all)
=========== ===================== ==============================================
  
