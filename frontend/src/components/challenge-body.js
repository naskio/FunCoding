import * as React from "react";
import Markdown from "marked-react";
import { TextEditor } from "./text-editor";
import Stack from "@mui/material/Stack";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Console from "./console";

export default function ChallengeBody(challenge) {
  //set state for code
  const [code, setCode] = React.useState("");
  return (
    <Stack direction="row" spacing={2} sx={{}}>
      <Card
        sx={{
          width: "650px",
        }}
      >
        <CardContent
          sx={{
            padding: 4,
            wordwrap: "break-word",
          }}
        >
          <Markdown
            sx={{
              padding: 4,
              wordwrap: "break-word",
            }}
          >
            {challenge.description}
          </Markdown>
        </CardContent>
      </Card>
      <Card
        sx={{
          width: "50%",
        }}
      >
        <CardContent sx={{}}>
          <TextEditor changeFromTextEditor={setCode} code={code} />
          <Console
            changeFromConsole={setCode}
            code={code}
            problem_id={challenge.problem_id}
            stdin={challenge.stdin}
            stdout={challenge.stdout}
          />
        </CardContent>
      </Card>
    </Stack>
  );
}
