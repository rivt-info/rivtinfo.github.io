**3.2** Tags
================

**Line** tags format a line of text,are added at the end of the line and
are denoted with _[**TAG**]. **Block** tags are denoted with _[[**TAG**]] on
the first line. They evaluate a multi-line text block and end with _[[**Q**]]
on the last line of the block (note: some tags only format pdf and html output).

**_[B]** :  center, bold
------------------------------------------------
*text* **_[B]**    

**_[C]** :   center 
---------------------------
*text* **_[C]**  

**_[D]** :  footnote description
-----------------------------------    
*description* **_[D]** 

**_[E]** : autonumber, label equation
-----------------------------------------
*equation description* **_[E]**  

**_[F]** : autonumber, label figure 
-----------------------------------------
figure caption **_[F]**   

**_[V]** : autonumber, label values table 
-----------------------------------------------
*table title* **_[V]**   


**_[P]** : new page
-----------------------
**_[P]**  


**_[S]**
---------
equation **_[S]**   :   format symbol math 

**_[T]**  autonumber, label table
------------------------------------------
*table title* **_[T]** 

**_[#]** :   autonumber footnote
------------------------------------
text **_[#]**   

**_[U]** :  url link 
------------------------
url, label **_[U]**  

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