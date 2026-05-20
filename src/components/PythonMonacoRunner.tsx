import React, { useEffect, useRef, useState } from "react";
import Editor from "@monaco-editor/react";

type PythonMonacoRunnerProps = {
  initialCode: string;
};

export default function PythonMonacoRunner({ initialCode }: PythonMonacoRunnerProps) {
  const iframeRef = useRef<HTMLIFrameElement>(null);
  const [editorCode, setEditorCode] = useState(initialCode);

  // Build iframe HTML content
  const iframeContent = `
<!DOCTYPE html>
<html>
<head>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.24.1/full/pyodide.js"></script>
  <style>
    body { font-family: monospace; margin: 0; padding: 8px; }
    #runBtn { margin-top: 4px; padding: 4px 8px; }
    #out { background: #0d1117; color: #58ff7a; padding: 8px; min-height: 100px; white-space: pre-wrap; }
  </style>
</head>
<body>
  <pre id="out">Loading Python...</pre>
  <script>
    let pyodide;

    async function init() {
      pyodide = await loadPyodide();
      document.getElementById('out').textContent = 'Python ready!';
    }

    async function runCode(code) {
      if (!pyodide) return;
      try {
        await pyodide.runPythonAsync(\`
import sys
from io import StringIO
sys.stdout = StringIO()
\`);
        await pyodide.runPythonAsync(code);
        const result = pyodide.runPython('sys.stdout.getvalue()');
        document.getElementById('out').textContent = result || "(no output)";
      } catch (e) {
        document.getElementById('out').textContent = e;
      }
    }

    // Listen for messages from parent
    window.addEventListener('message', (event) => {
      if (event.data.type === 'RUN_CODE') {
        runCode(event.data.code);
      }
    });

    init();
  </script>
</body>
</html>
`;

  const runCode = () => {
    if (iframeRef.current?.contentWindow) {
      iframeRef.current.contentWindow.postMessage(
        { type: "RUN_CODE", code: editorCode },
        "*"
      );
    }
  };

  return (
    <div style={{ border: "1px solid #444", borderRadius: 6, padding: 8 }}>
      <Editor
        height="250px"
        language="python"
        theme="vs-dark"
        value={editorCode}
        onChange={(v) => setEditorCode(v || "")}
        options={{
          fontSize: 14,
          minimap: { enabled: false },
          scrollBeyondLastLine: false,
        }}
      />
      <button
        onClick={runCode}
        style={{
          marginTop: 8,
          padding: "6px 12px",
          background: "#0f0",
          color: "#000",
          border: "none",
          borderRadius: 4,
          cursor: "pointer",
        }}
      >
        Run
      </button>
      <iframe
        ref={iframeRef}
        sandbox="allow-scripts"
        srcDoc={iframeContent}
        style={{ width: "100%", height: "200px", border: "1px solid #ccc", marginTop: 8 }}
      />
    </div>
  );
}
