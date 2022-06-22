import * as React from "react";
import Markdown from "marked-react";
import { TextEditor } from "./text-editor";
import Stack from "@mui/material/Stack";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
export default function ChallengeBody(challenge) {
  return (
    <Stack direction="row" spacing={2}>
      <Card>
        <CardContent>
          <Markdown>{challenge.description}</Markdown>
        </CardContent>
      </Card>
      <TextEditor />
    </Stack>
  );
}
