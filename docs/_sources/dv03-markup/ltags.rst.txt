**3.2** Line Tags
===================

**Line** tags format a line of text,are added at the end of the line and
are denoted with _[**TAG**]. Some tags only format pdf and html output.

KEY
----
::
    tag: description
    syntax 
    function scope


**_[B]** :  center, bold
------------------------------------------------
*text* **_[B]**  
rv.I, rv.V

**_[C]** :   center 
---------------------------
*text* **_[C]**  

**_[D]** :  footnote description
-----------------------------------    
*description* **_[D]** 

**_[E]** : number, label equation
-----------------------------------------
*equation description* **_[E]**  

**_[F]** : number, label figure 
-----------------------------------------
figure caption **_[F]**   

**_[P]** : new page
-----------------------
**_[P]**  

**_[S]**
---------
equation **_[S]**   :   format symbol math 

**_[T]**  number, label table
------------------------------------------
*table title* **_[T]** 

**_[#]** :  number footnote
------------------------------------
text **_[#]**   

**_[U]** :  url link 
------------------------
url, label **_[U]**  

**_[V]** : number, label values table 
-----------------------------------------------
*table title* **_[V]**   

**horizontal line**
---------------------   
4 or more dashes on empty line(----)
