---
myst:
    substitutions:
        "key4": |
            ```{image} _static/img/search01.png
            :alt: rivt-search logo
            :target: https://github.com/search
            :width: 60px
            ```
---

# {{ key4 }} **GitHub Search** 

<head>
<style>
.button {
  background-color: #cfdde2; 
  border: 3 px solid black;
  color: black;
  padding: 10px 20px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<script> function searchRivt(){var strng1 = document.getElementById("terms"); var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});
</script>

<script> function searchOrg(){var strng1 = document.getElementById("terms");var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});
</script>

<script> function clearRivt(){var strng1 = document.getElementById("terms");var strng2 = document.getElementById("terms").value="";document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 82) && e.ctrlKey){document.getElementById("clearBtn").click();}});
</script>

</head>


Full text **rivt** document search across GitHub README files

Example: solar+steel+frame

<input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal"><br>

<button class="button" id="searchBtn" onclick="searchRivt()">Search [ Ctrl+Enter ]</button>
<button class="button" id="clearBtn" onclick="clearRivt()">Clear [ Ctrl+R ]</button>
<hr>

## **Organizations**
<hr>

Full text **rivt** document search across GitHub README files in Organizations

<input type="text" id="terms" name="terms" size=30 style="height:40px;font-size:14pt; font-weight: normal"> Enter Organizations (comma separated)<br>


<input type="text" id="terms" name="terms" size=60 style="height:40px;font-size:14pt; font-weight: normal"> Search Terms<br>

<button class="button" id="searchBtn" onclick="searchOrg()">Search [ Ctrl+Enter ]</button>
<button class="button" id="clearBtn" onclick="clearRivt()">Clear [ Ctrl+R ]</button>

## **Search Tips**

Some text.