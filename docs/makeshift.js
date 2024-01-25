const textInput = document.getElementById("textInput");
const resultsArea = document.getElementById("results");
const counter = 1;

async function loadMakeshift(){
  let pyodide = await loadPyodide();
  await pyodide.loadPackage("micropip");
  const micropip = pyodide.pyimport("micropip");
  await micropip.install("makeshift");
  return pyodide;
}

let loadMakeshiftPromise = loadMakeshift();

async function runMakeshift(){
  let pyodide = await loadMakeshiftPromise;
  results = pyodide.runPython(`
    import js
    
    from makeshift.interpreter.lexer import Lexer
    from makeshift.interpreter.parser import Parser
    from makeshift.interpreter.interpreter import TreeWalkInterpreter
    
    text = js.textInput.value.replace("\\r\\n", "\\n")
    text = text.replace("   ", "\\t")
    
    s = Lexer(text)
    s.lexv2()
    pr = Parser(s.tokens)
    ast = pr.generator("sample")
    interp = TreeWalkInterpreter()
    output_list = set()

    while len(output_list) < 5:
      output_list.add(interp.visit_generator_node(ast))

    list(output_list)
  `);
  updateResults(results);
}

function updateResults(results) {
  resultsArea.value = results.join('\n')
}