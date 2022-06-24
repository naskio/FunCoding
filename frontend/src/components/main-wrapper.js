import * as React from "react";
import PropTypes from "prop-types";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import ChallengeBody from "./challenge-body";
import challenges from "../utils/create-challenges";
import styled from "@emotion/styled";

const useStyles = styled({
  tabPanelRoot: {
    backgroundColor: "red",
  },
});
function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      id={`vertical-tabpanel-${index}`}
      aria-labelledby={`vertical-tab-${index}`}
      {...other}
    >
      {value === index && <Box sx={{ p: 3 }}>{children}</Box>}
    </div>
  );
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.number.isRequired,
  value: PropTypes.number.isRequired,
};

function a11yProps(index) {
  return {
    id: `vertical-tab-${index}`,
    "aria-controls": `vertical-tabpanel-${index}`,
  };
}

export default function ChallengeNavigator() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Box
      sx={{
        bgcolor: "background.paper",
        display: "flex",
      }}
    >
      <Tabs
        orientation="vertical"
        variant="scrollable"
        value={value}
        onChange={handleChange}
        aria-label="Vertical tabs example"
        sx={{ borderRight: 1, borderColor: "divider", minWidth: "10%" }}
      >
        <Tab label={challenges[0].name} {...a11yProps(0)} />
        <Tab label={challenges[1].name} {...a11yProps(1)} />
        <Tab label={challenges[2].name} {...a11yProps(2)} />
      </Tabs>

      <TabPanel
        value={value}
        index={0}
        sx={{}}
        classes={{ root: classes.tabPanelRoot }}
      >
        <ChallengeBody
          name={challenges[0].name}
          description={challenges[0].description}
          problem_id={challenges[0].problem_id}
          stdin={challenges[0].stdin}
          stdout={challenges[0].stdout}
        />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <ChallengeBody
          name={challenges[1].name}
          description={challenges[1].description}
          problem_id={challenges[1].problem_id}
          stdin={challenges[1].stdin}
          stdout={challenges[1].stdout}
        />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <ChallengeBody
          name={challenges[2].name}
          description={challenges[2].description}
          problem_id={challenges[2].problem_id}
          stdin={challenges[2].stdin}
          stdout={challenges[2].stdout}
        />
      </TabPanel>
    </Box>
  );
}
