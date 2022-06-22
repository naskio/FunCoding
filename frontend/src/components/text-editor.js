import React from "react";
import AceEditor from "react-ace";

import "ace-builds/src-noconflict/mode-java";
import "ace-builds/src-noconflict/theme-monokai";
import "ace-builds/src-noconflict/ext-language_tools";

export function TextEditor() {
  function onChange(newValue) {
    console.log("change", newValue);
  }
  return (
    <AceEditor
      mode="java"
      theme="monokai"
      value="//code your fizzbuzz solution here"
      onChange={onChange}
      name="UNIQUE_ID_OF_DIV"
      editorProps={{ $blockScrolling: true }}
    />
  );
}
