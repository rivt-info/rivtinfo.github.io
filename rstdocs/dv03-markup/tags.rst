**3.2** Tags
================

**Line** tags format a line of text,are added at the end of the line and
are denoted with _[**TAG**]. **Block** tags are denoted with _[[**TAG**]] on
the first line. They evaluate a multi-line text block and end with _[[**Q**]]
on the last line of the block (note: some tags only format pdf and html output).


**_[V]**
---------
table title **_[V]**   :   autonumber values table 

**_[F]**
---------
figure caption **_[F]**   :  autonumber and label figure 

**_[E]**
---------
equation descroption **_[E]**  :    autonumber equation

**_[C]**
---------
text **_[C]**   :   center text 

**_[B]**
---------
text **_[B]**    :  center bold text (pdf, pdf2, html)

**_[P]**
---------
**_[P]**  :    new page

**_[T]**
---------
title **_[T]**  :    autonumber table [1]

**_[S]**
---------
equation **_[S]**   :   format symbol math 

**_[#]**
---------
text **_[#]**   :   autonumber footnote

**_[D]**
---------    
description **_[D]**  :    footnote description

**_[U]**
---------
url, label **_[U]**  :    url link (pdf, pdf2, html)

**line**
---------------------   
for horizontal line 4 or more dashes (----)


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
  
rv.V         

rv.I, rv.V   
rv.I, rv.V   
rv.I, rv.V   
rv.I, rv.V   
rv.I, rv.V   
rv.I, rv.V   
rv.I         
rv.I         
rv.I         
rv.I         
rv.I         