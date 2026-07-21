**F.1 |** AI
=====================

.. raw:: html

   <hr>

.. figure::  _static/img/rivt-ai1.png
    :class: dark-light
    :scale: 20%
    :align: center
    :alt: rivt logo
    
.. raw:: html

   <hr>

.. _rivt-context:

**[1]** *rivt* and AI
------------------------------------------------------------------------ 

*AI* can be used to generate *rivt* content including scripts and tables. It
can assist in converting PDFs into text and ASCII math used by *rivt files*.
Since *rivtlib* is built on Python and rivt files are Python files, many
existing *AI* tools are availale for interacting with and extending *rivt*.

For context regarding future *rivt* development, a summary of current relevant AI
models and tools is provided :ref:`here <aiback>`. In brief, *AI* outputs are
based on a few large foundational models which provide in turn provide input to
agents, tools and UI's. This agent layer is then used to generate relevant
responses to user queries and prompts.

Agents that generate complete *rivt files* for specific project requirements
baed on scripts is currently being explored. If successful, *rivt* AI agents
will be offered as a software service in the latter part of 2026.  Services for 

------------------------------------


**[2]**  AI Use Cases
----------------------------------------------------------------------- 

The *VSCode IDE* has been used to develop *rivt* and *VSCode* is integrated with
*Microsoft Copilot*, an AI coding assistant powered by the *OpenAI*
:ref:`foundation model <aiback>`. *Copilot*  recognizes *rivt markdown* and is
able to make editing and content suggestions. 

*Claude* is effective in converting existing documents from PDF format into
ASCII text formats compatible with *rivt*. *AI* can also be used to generate
tables, equations and models that can be incorporated into *rivt* documents.

A conversion example is here.

A function and data example is here.

A model example is here.

.. toctree::
   :maxdepth: 1
   :hidden:

   rvF02-convert.rst
   rvF03-models.rst
   rvF04-aibackgrnd.rst
   rvF05-scripts.rst