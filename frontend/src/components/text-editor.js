import React from "react";
import Editor from "@monaco-editor/react";

export function TextEditor(props) {
  function handleEditorChange(value) {
    props.changeFromTextEditor(value);
  }
  const options = {
    automaticLayout: true,
  };
  return (
    <Editor
      options={options}
      height="70vh"
      theme="vs-dark"
      defaultLanguage="fsharp"
      defaultValue='printf "Hello World!"'
      onChange={handleEditorChange}
      value={props.code}
    />
  );
}
