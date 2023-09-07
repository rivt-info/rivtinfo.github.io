
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
  background-color: #005580; 
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

## Search GitHub 

Full text **rivt** search across README files on GitHub (**rivt** term is not required)

Enter search terms separated by a + sign

[ctrl+enter] to execute search
<br>
[ctrl+R or F5] to clear search terms
<br>
<input type="text" id="terms" name="terms" size=80 style="height:50px;font-size:14pt; font-weight: bold">
<br>
Example: concrete+beam+bridge

<button class="button" id="searchBtn" onclick="searchRivt()">Search [ ctrl+enter ]</button>

<hr>

## Search Organization

x


