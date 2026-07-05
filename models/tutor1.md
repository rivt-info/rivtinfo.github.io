
```mermaid
%%{init: {"theme": "neutral"}}%% 

kanban
  ["**rivt file (.py)**"] 
    import rivtlib.api as rv
    include rivt API calls
    Nonprinting comments <br> may be added as <br> triple-quotes outside <br> of API calls
  ["**rivt markup (indent 4)**"]
    ["API calls include: <br> **R(r) I(r) V(r) T(r) D(r)**"]
    ["a rivt string **(r)** includes <br> header and content <br> substrings"]
    ["content substrings <br> include formatting <br> line tags **_[T]** and <br> block tags **_[[BLOCK]]**"]
    ["file commands read and <br> format files **| CMD |** "]
  **publish doc**
    ["doc API is **rv.D()**"]
    ["**| PUBLISH |** command <br> writes docs as .txt <br> .html or .pdf files and <br> writes a README.txt"]
    ["**_[[METADATA]]** block <br> specifies layout and <br> metadata settings  "]
    