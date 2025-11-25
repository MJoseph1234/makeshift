---
layout: page
title: MakeShift Lab
---

# MakeShift Lab

The lab runs MakeShift templates on the fly to make five random results. Enter your template text in the left box and hit the `make` button.

> ⚠️ The Lab is experimental and may be running an old version of MakeShift

<script src="https://cdn.jsdelivr.net/pyodide/v0.29.0/full/pyodide.js"></script>
<link rel="stylesheet" href="lab_styles.css">

<div>
  <input id="generateButton" type="button" onclick="runMakeshift()" value="Run MakeShift"/>
</div>
<div id="textareas">
  <textarea id="textInput" rows="24" cols="50" placeholder="add your MakeShift template here"></textarea>
  <textarea id="results" readonly rows="24" cols="40" placeholder="generated results will appear here"></textarea>
</div>

<script src="makeshift.js"></script>


The MakeShift Lab is built using [Pyodide](https://pyodide.org/en/stable/) running the [latest PyPI release of MakeShift](https://pypi.org/project/makeshift/). There may be features and bug fixes in the GitHub repository that are not yet published as a new release on PyPI.

Example templates are available in the `examples/` directory on the GitHub repository ([https://github.com/MJoseph1234/makeshift/tree/master/examples](https://github.com/MJoseph1234/makeshift/tree/master/examples)). You can copy and paste these into the template field above to run them.

