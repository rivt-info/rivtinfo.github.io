
```{image} _static/img/search01.png
:alt: rivt logo
:target: https://www.rivt-doc.net/index.html
:width: 125px
:align: left
```

# **rivt-search**

<head>
<style>
.button {
  background-color: #4CAF50; /* Green */
  border: 2 px solid black;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>

<script> function searchRivt(){var strng1 = document.getElementById("terms");var strng2 = document.getElementById("terms").value;URL = `https://github.com/search?q=rivt+${strng2}+in%3Areadme`;window.open(URL,'_self')};document.addEventListener("keydown", function(e) {if ((e.keyCode == 10 || e.keyCode == 13) && e.ctrlKey){document.getElementById("searchBtn").click();}});</script>

</head>

<p style= "font-size: 1.3em !important;"> Open Source Software for Composing and Sharing Engineering Documents </p>

<hr>

<div id="banner" style="overflow: visible; display: flex; justify-content:space-around;">
<div>
<a href="https://rivtdocs.net"><img src="./assets/img/rivtdocs03.png" width="75" height="75" /></a><a href="https://rivtdocs.net">rivtDocs</a>
</div>

<div>
<a href="https://rivtcode.net"><img src="./assets/img/rivt03.png" width="75" height="75"/></a><a href="https://rivtcode.net">rivt</a>
</div>

<div>
<a href="https://rivtdocs.net/search"><img src="./assets/img/search03.png" width="75" height="75"/></a><a href="https://rivtdocs.net/search"><b>rivtSearch</b></a>
</div>
</div>

<hr>


## Search GitHub 

Full text **rivt** search across README files on GitHub (**rivt** term is not required)

Enter search terms separated by a + sign

<br>
[ctrl+enter] to execute search
<br>
[ctrl+R or F5] to clear search terms
<br>
<input type="text" id="terms" name="terms" size=80 style="height:50px;font-size:14pt; font-weight: bold">
<br>
Example: concrete+beam+bridge

<button class="button" id="searchBtn" onclick="searchRivt()">Search [ ctrl+enter ]</button>


## Search Organization

x


