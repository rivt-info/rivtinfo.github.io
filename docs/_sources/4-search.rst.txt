
Search
=======

This page provides search of **rivt** files across GitHub.  It searches text in
**rivt** README files.

GitHub
------

Clear [ Ctrl+R ]

Search [ Ctrl+Enter ]

Example: solar+steel+frame


.. raw:: html

    <head>
    
    <style>
    .button {
    background-color: #6f6968; border: 3 px solid white; color: white; padding: 4px 10px; 
    text-align: center; text-decoration: none; display: inline-block; font-size: 16px; 
    margin: 4px 2px; cursor: pointer;
    }
    </style>

    <script> function searchRivt(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});
    </script>

    <script> function searchOrg(){var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;
    window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});
    </script>

    <script> function clearRivt(){document.getElementById("terms").value="";
    document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 82) && e.ctrlKey){document.getElementById("clearBtn").click();}})};
    </script>
    
    </head>

    <button class="button" id="searchBtn" onclick="searchRivt()">S</button><button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal"><br>


    <hr>

    <hr>



    GitHub Organizations
    ---------------------

    Full text **rivt** document search across GitHub Organization README files

    <input type="text" id="terms" name="terms" size=30 style="height:40px;font-size:14pt; font-weight: normal"> Organizations (comma separated)<br>

    <hr>

    <hr>

    <button class="button" id="searchBtn" onclick="searchOrg()">S</button> <button class="button" id="clearBtn" onclick="clearRivt()">C</button><input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal">





Search Tips
-----------

- The GitHub search interface is [here](https://github.com/search).

- GitHub README searches only index the root directory README. The rivt function <code> rv.readme() </code> writes every README in a project into the root README so rivt projects on GitHub can be fully searched.

- The rivt search box automatically adds the rivt search term.
