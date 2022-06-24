import * as React from "react";
import MuiAccordion from "@mui/material/Accordion";
import Stack from "@mui/material/Stack";
import { styled } from "@mui/material/styles";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";
import MuiAccordionSummary from "@mui/material/AccordionSummary";
import MuiAccordionDetails from "@mui/material/AccordionDetails";
import ArrowForwardIosSharpIcon from "@mui/icons-material/ArrowForwardIosSharp";

// variable with value that changes
let consoleMessage = "Run the code to see the result";
const Accordion = styled((props) => (
  <MuiAccordion disableGutters elevation={0} square {...props} />
))(({ theme }) => ({
  border: `1px solid ${theme.palette.divider}`,
  "&:not(:last-child)": {
    borderBottom: 0,
  },
  "&:before": {
    display: "none",
  },
}));
const AccordionSummary = styled((props) => (
  <MuiAccordionSummary
    expandIcon={<ArrowForwardIosSharpIcon sx={{ fontSize: "0.9rem" }} />}
    {...props}
  />
))(({ theme }) => ({
  backgroundColor:
    theme.palette.mode === "dark"
      ? "rgba(255, 255, 255, .05)"
      : "rgba(0, 0, 0, .03)",
  flexDirection: "row-reverse",
  "& .MuiAccordionSummary-expandIconWrapper.Mui-expanded": {
    transform: "rotate(90deg)",
  },
  "& .MuiAccordionSummary-content": {
    marginLeft: theme.spacing(1),
  },
}));

const AccordionDetails = styled(MuiAccordionDetails)(({ theme }) => ({
  padding: theme.spacing(2),
  borderTop: "1px solid rgba(0, 0, 0, .125)",
}));
function getConsoleBody(success, message, props, memory, cpu_time) {
  if (success) {
    return (
      <div>
        <Typography
          sx={{
            color: "green",
          }}
        >
          Success. {message}
          <br />
          Input: {props.stdin}
          <br />
          Output: {props.stdout}
        </Typography>

        <Typography>
          <br />
          Memory usage: {memory}
          <br />
          CPU Time: {cpu_time}
          <br />
        </Typography>
      </div>
    );
  } else {
    return (
      <Typography
        sx={{
          color: "red",
        }}
      >
        Failed. {message}
        Input: {props.stdin}
        <br />
        Output: {props.stdout}
      </Typography>
    );
  }
}

const sendChallenge = async (props) => {
  var credentials = btoa("admin:admin");
  const body = {
    code: props.code,
    stdin: props.stdin,
    problem_id: props.problem_id,
  };

  const response = await fetch("https://funcoding.nask.io/api/run", {
    method: "POST",
    credentials: "include",
    headers: {
      Authorization: `Basic ${credentials}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  const executionResult = await response.json();
  if (executionResult) {
    consoleMessage = getConsoleBody(
      true,
      "Your response is correct.",
      props,
      executionResult.cpu_time,
      executionResult.memory
    );
  } else {
    consoleMessage = getConsoleBody(false, "", props);
  }
};
// make post request to server
const formatCode = async (props) => {
  var credentials = btoa("admin:admin");
  const response = await fetch("https://funcoding.nask.io/api/format", {
    method: "POST",
    credentials: "include",
    headers: {
      Authorization: `Basic ${credentials}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ code: props.code }),
  });
  const formattedCode = await response.json();
  if (formattedCode.code) {
    const replacedCode = formattedCode.code;
    handleEditorChange(replacedCode, props);
    sendChallenge(props);
  } else {
    consoleMessage = getConsoleBody(
      false,
      "Compilation error, please verify.",
      props
    );
  }
};

function handleEditorChange(code, props) {
  props.changeFromConsole(code);
}

export default function Console(props) {
  const [expanded, setExpanded] = React.useState("panel1");

  const handleChange = (panel) => (event, newExpanded) => {
    setExpanded(newExpanded ? panel : false);
  };

  return (
    <div>
      <Accordion
        expanded={expanded === "panel1"}
        onChange={handleChange("panel1")}
      >
        <AccordionSummary
          sx={{}}
          aria-controls="panel1d-content"
          id="panel1d-header"
        >
          <Stack
            direction={{ xs: "column", sm: "row" }}
            spacing={{ xs: 0, sm: 1, md: 60 }}
            sx={{
              width: "90%",
            }}
          >
            <Button variant="text">Console</Button>
            <Button
              variant="outlined"
              onClick={() => {
                formatCode(props);
              }}
            >
              Run
            </Button>
          </Stack>
        </AccordionSummary>
        <AccordionDetails>{consoleMessage}</AccordionDetails>
      </Accordion>
    </div>
  );
}
