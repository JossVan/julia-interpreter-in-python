// referencia a codemirror: https://codemirror.net/doc/manual.html
CodeMirror.fromTextArea(document.getElementById("entrada"),{
    lineNumbers : true,
    theme:'dracula',
    matchBrackets: true
});