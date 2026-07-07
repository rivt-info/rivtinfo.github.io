
```mermaid
%%{init: {"theme": "neutral"}}%% 
kanban
  [<span style="font-size: 20px"><b>rivt file</span>]
    [Start a **.py** file with <br> **import rivtlib.api as rv**]
    ["Include **rivt API** <br> **methods of the form** <br> **rv.X(r)**  where **X** is an <br> **API method** and **(r)** is <br>a rivt string."]
    [Nonprinting comments <br> may be added as <br> triple-quoted strings <br> between **API methods**.]
  [<span style="font-size: 20px"><b>rivt markup</span>]
    ["API methods include: <br> **R(r) I(r) V(r) T(r) D(r)** <br>  They write to **STDOUT** <br> and may be run <br> interactively."]
    ["**(r)** is a triple-quoted <br> rivt string composed of <br> a header and content <br> substring (indented <br> 4 spaces)."]
    ["Content substrings <br> include **line** and **block** <br> **tags**, **commands** and <br> **assignments**."]
    ["**_[L]**, **_[[BLOCK]]** <br> **Line and block tags** <br> format content."]
    ["**| CMD | params** <br> **Commands** read and <br> format files."]
    ["x **<=:** 2 + y <br> **Assignments** assign <br> values to expressions"]
  [<span style="font-size: 20px"><b>publish rivt doc</span>]
    ["The **Doc API method** is <br> **rv.D(r)**"]
    ["The **| PUBLISH |** <br> command  writes docs <br> as **.txt .html** or **.pdf** <br> files and writes a <br> **README.txt**."]
    ["The **_[[METADATA]]** <br> block  specifies layout <br> and metadata settings."]


