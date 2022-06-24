import React from "react";
import { createRoot } from "react-dom/client";
import MainWrapper from "./components/main-wrapper";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import "normalize.css";
import Box from "@mui/material/Box";
import CssBaseline from "@mui/material/CssBaseline";
//import my logo from resources
import logo from "./assets/logo.png";

const darkTheme = createTheme({
  //todo make a switch to change between dark and light
  palette: {
    mode: "dark",
  },
});
//add logo to <img>
const App = () => {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <center>
        <img src={logo} width="150px" alt="Page logo" />
      </center>
      <Box>
        <MainWrapper />
      </Box>
    </ThemeProvider>
  );
};
const container = document.getElementById("root");
const root = createRoot(container);
root.render(<App tab="home" />);
