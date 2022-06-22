import React from "react";
import { createRoot } from "react-dom/client";
import CodingArea from "./components/coding-area";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import "normalize.css";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
const darkTheme = createTheme({
  //todo make a switch to change between dark and light
  palette: {
    mode: "dark",
  },
});

const App = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <center>
        <h1>cool logo here</h1>
      </center>
      <Box
        sx={{
          width: "100%",
          backgroundColor: "red",
        }}
      >
        <CodingArea />
      </Box>
    </ThemeProvider>
  );
};
const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App tab="home" />);
