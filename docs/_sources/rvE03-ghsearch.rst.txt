**E.3 - GitHub Search**
=========================

.. raw:: html

    <p id="api">&lt;t&gt;</p>

**[1]** GitHub Global Search
--------------------------------

.. raw:: html

    <hr>

This page is a search interface for **rivt** files on GitHub. The search covers
the full text of the **rivt** README.txt file in the *repo* directory. The
README file contains the *rivt report*. 

For advanced searching use the `GitHub interface <https://github.com/search>`_.


.. topic:: Buttons

    **[S]** Search GitHub <Ctrl+Enter>
    
    **[C]** Clear input <Ctrl+R>


**Example**: solar+steel+frame is passed to GitHub as rivt+solar+steel+frame

.. raw:: html

    <head>
    
    <style>
    .button {
    background-color: #6f6968; border: 3 px solid white; color: white; padding: 4px 10px; 
    text-align: center; text-decoration: none; display: inline-block; font-size: 16px; 
    margin: 4px 2px; cursor: pointer;} </style>

    <script> 
    function searchRivt(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

    <script> function searchOrg(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

    <script> function clearRivt(){document.getElementById("terms").value="";
    document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 82) && e.ctrlKey){document.getElementById("clearBtn").click();}})};</script>
    
    </head>

    <button class="button" id="searchBtn" onclick="searchRivt()">S</button><button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal"><br>

    <br>

    <br>

.. raw:: html

    <p id="api">&lt;t&gt;</p>

**[2]** GitHub Organization Search
---------------------------------------

.. raw:: html

    <hr>
    
Restrict search to the following comma separated GitHub organizations: 

.. raw:: html    
    
    <input type="text" id="terms" name="terms" size=40 style="height:38px;font-size:14pt; font-weight: normal">

    <br>
    <br>

    <b>Organization(s) Search Terms</b><br>
    <button class="button" id="searchBtn" onclick="searchOrg()">S</button> <button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal">

