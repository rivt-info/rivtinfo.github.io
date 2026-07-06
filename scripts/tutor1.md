
```mermaid
%%{init: {"theme": "neutral"}}%% 
kanban
  [<span style="font-size: 20px"><b>rivt file</span>]
    [Start a **.py** file with <br> **import rivtlib.api as rv**]
    ["Include **rivt API** <br> **methods of the form** <br> **rv.X(r)**  where **X** is an <br> **API method** and **(r)** is <br>a rivt string."]
    [Nonprinting comments <br> may be added as <br> triple-quoted strings <br> between **API methods**.]
  [<span style="font-size: 20px"><b>rivt markup</span>]
    ["API methods include: <br> **R(r) I(r) V(r) T(r) D(r)**"]
    ["**(r)** is a triple-quoted <br> rivt string composed of <br> a header and content <br> substring. Content <br> substrings are indented <br> 4 spaces."]
    ["Content substrings <br> are formatted with <br> line **_[T]** and block <br> tags **_[[BLOCK]]**, where <br> **T** and **BLOCK** are one <br> of two dozen tags."]
    ["Commands of the form <br> **| CMD | params** read <br> and format files, <br> where **CMD** is one of <br> a dozen commands."]
    ["**API methods** write to <br> **STD out** and may be <br> run interactively."]
  [<span style="font-size: 20px"><b>publish rivt doc</span>]
    ["The **Doc API method** is <br> **rv.D(r)**."]
    ["The **| PUBLISH |** <br> command  writes docs <br> as **.txt .html** or **.pdf** <br> files and writes a <br> **README.txt**."]
    ["The **_[[METADATA]]** <br> block  specifies layout <br> and metadata settings."]