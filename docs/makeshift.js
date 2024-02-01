/*
Pyodide will always use the version of makeshift available on PyPI.
There may be changes on the github that are not yet released as a PyPI version.

Any changes to the python here must be compatable with the latest PyPI release
of Makeshift, not necessarily the code shown on GitHub.
*/

const textInput = document.getElementById("textInput");
const resultsArea = document.getElementById("results");
const counter = 1;

textInput.addEventListener('keydown', function(e) {
  if (e.key == 'Tab') {
    e.preventDefault();
    var start = this.selectionStart;
    var end = this.selectionEnd;
    this.value = this.value.substring(0, start) + '\t' + this.value.substring(end);
    this.selectionStart = this.selectionEnd = start + 1;
  }
});

function wrap(s) {
  return(s.replace(/(?![^\n]{1,40}$)([^\n]{1,40})\s/g, '$1\n  '));
}

async function loadMakeshift(){
  let pyodide = await loadPyodide();
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install("makeshift");
  return pyodide;
}

let loadMakeshiftPromise = loadMakeshift();

async function runMakeshift(){
  if (textInput.value.trim() == "") {
    resultsArea.value = ""
    return
  }
  let pyodide = await loadMakeshiftPromise;
  results = pyodide.runPython(`
    import js
    
    from makeshift.interpreter.lexer import Lexer
    from makeshift.interpreter.parser import Parser
    from makeshift.interpreter.interpreter import TreeWalkInterpreter
    
    text = js.textInput.value
    s = Lexer(text)
    s.lexv2()
    pr = Parser(s.tokens)
    ast = pr.generator("sample")
    interp = TreeWalkInterpreter()
    output_list = []

    while len(output_list) < 5:
      output_list.append(interp.visit_generator_node(ast))

    output_list
  `);
  updateResults(results);
}

function updateResults(results) {
  var formattedResults = ''
  for (let i = 0; i < results.length; i++) {
    formattedResults += (i+1) + '. ' + wrap(results[i]) + '\n'
  }
  resultsArea.value = formattedResults
}