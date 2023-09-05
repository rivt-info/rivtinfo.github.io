
```{image} _static/img/riv02.png
:alt: rivt logo
:target: index.html
:width: 125px
:align: left
```

**<p style="text-align: left;"><a href="index.html"> HOME </a></p>**

# **rivt**

**rivt** is an engineering document markdown language processed by **rivtlib**,
a Python library. They are both open source and run on any platform that
supports Python 3.8 or above. The language and library are designed to write,
assemble and share engineering documents in a way that prioritizes clarity,
efficiency, extension and universal access. **rivt-doc**, is a complete open
source editing system with installers and a number open source library and
application dependencies.


## rivt files

A rivt file is a utf-8 text (Python) file that begins with the import statement:

*import rivtlib.rivtapi as rv*
 
which in turn provides four single letter API functions referred to as Repo,
Insert, Values and Tools. Each function takes a single, triple quoted string
as argument.

rv.R(rmS) - repository and report information 
rv.I(rmS) - static text, images, tables and math
rv.V(rmS) - equations
rv.T(rmS) - Python functions and scripts

When running in an IDE (e.g. VSCode), each method may be run interactively
using the standard cell decorator (# %%). Interactive output is formatted as
utf-8 text. The rv.writemd() and rv.writepdf() functions generate documents and
compilations in GitHub Markdown (ghmd) and PDF formats. 

rivt works with both single file documents as well as extensive reports
with hundreds of files. Multi-file reports are structured in an efficient
folder based framework.

