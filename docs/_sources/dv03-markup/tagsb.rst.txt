**3.3** Block Tags
===================

*Block** tags are denoted with _[[**TAG**]] on the first line. They evaluate a
multi-line text block and end with _[[**Q**]] on the last line of the block
(note: some tags only format pdf and html output).

____________________________________________
KEY
----
**tag**: description

::

    syntax 
    
    function scope
    output type

____________________________________________



**_[[V]]** :  numbered values format block 
------------------------------------------------

::

    _[[V]] Block Title
    value1
    value2
    ...
    _[[Q]]

    rv.I, rv.V
    text, pdf, html




**_[[Q]]** : end block
------------------------------------------------




**_[[T]]** : indent block
------------------------------------------------


**_[[C]]**

**_[[L]]**

**_[[O]]**

**_[[B]]**

**_[[I]]**


rv.I          **_[[S]]**       indent block
rv.I          **_[[C]]**       code (literal) block
rv.I          **_[[L]]**       latex block (lpdf, html)
rv.I          **_[[O]]**       italic (oblique) block (lpdf, html)
rv.I          **_[[B]]**       bold block  (lpdf, html)
rv.I          **_[[I]]**       indent italic block (lpdf, html)

  
    