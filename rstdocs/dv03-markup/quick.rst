**3.5** Quick Look-up
=======================


========== ========================================================= ================
Scope                      Read Commands                              File Types
========== ========================================================= ================
rv.V       **|VALUES|** rel. pth | title, [rows], -;_[V]              .csv
rv.I, rv.V **|IMG|** rel. pth | caption, scale, -;_[F]                .png,.jpg
rv.I, rv.V **|IMG2|** rel. pth | c1, c2, s1, s2, -;_[F]               .png,.jpg
rv.I       **|TABLE|** rel. pth | title, col w, l;c;r, [r], -;_[T]    .csv,.txt,.xlsx
rv.I       **|TEXT|** rel. pth | [[block tag]]                        .txt,.tex
========== ========================================================= ================

=========== =============================================== ====================
Scope                        Write Commands                         Notes 
=========== =============================================== ====================
rv.V         a := 1+1 | reference | units | decimals         := a command tag
rv.W         **||DOC|** rel. pth | pdf; txt; html; pdf2      pdf2 uses rst2pdf
rv.W         **||REPORT|** rel. pth | pdf; txt; html; pdf2   pdf uses latex
rv.W         **||APPEND|** rel. pth | num; nonum             .pdf,.txt
=========== =============================================== ====================

================ ======================= =======================================
Scope             Line Tags                    Description
================ ======================= =======================================
rv.V                    label **_[V]**      autonumber values table [1]
rv.I, rv.V            caption **_[F]**      autonumber image [1]
rv.I, rv.V              label **_[E]**      autonumber equation
rv.I, rv.V               text **_[C]**      center text 
rv.I, rv.V               text **_[B]**      center bold text (pdf, pdf2, html)
rv.I, rv.V                    **_[P]**      new page
rv.I, rv.V                  --------        horizontal line (4 or more - )
rv.I                    title **_[T]**      autonumber table [1]
rv.I                 equation **_[S]**      format symbol math 
rv.I                     text **_[#]**      autonumber footnote
rv.I                  descrip **_[D]**      footnote description
rv.I               url, label **_[U]**      url link (pdf, pdf2, html)
================ ======================= =======================================

[1] tags may be added to the command as a parameter

=========== =============== ====================================================
Scope        Block Tags      Description
=========== =============== ====================================================
rv.V          **_[[V]]**       values format block, autonumber
rv.I rv.V     **_[[Q]]**       end block
rv.I          **_[[S]]**       indent block
rv.I          **_[[C]]**       code (literal) block
rv.I          **_[[L]]**       latex block (lpdf, html)
rv.I          **_[[O]]**       italic (oblique) block (lpdf, html)
rv.I          **_[[B]]**       bold block  (lpdf, html)
rv.I          **_[[I]]**       indent italic block (lpdf, html)
=========== =============== ====================================================
  
