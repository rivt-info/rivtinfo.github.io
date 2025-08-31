**3.3** Block Tags
===================

*Block** tags are denoted with _[[**TAG**]] on
the first line. They evaluate a multi-line text block and end with _[[**Q**]]
on the last line of the block (note: some tags only format pdf and html output).



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
  
    