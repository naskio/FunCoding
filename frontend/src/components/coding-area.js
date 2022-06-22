import * as React from "react";
import PropTypes from "prop-types";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import Box from "@mui/material/Box";
import ChallengeBody from "./challenge-body";
import challenges from "../utils/create-challenges";
function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
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

export default function VerticalTabs() {
  const [value, setValue] = React.useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  return (
    <Box
      sx={{
        flexGrow: 1,
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
        sx={{ borderRight: 1, borderColor: "divider" }}
      >
        <Tab label={challenges.name} {...a11yProps(0)} />
        <Tab label={challenges.name} {...a11yProps(1)} />
        <Tab label={challenges.name} {...a11yProps(2)} />
        <Tab label={challenges.name} {...a11yProps(3)} />
        <Tab label={challenges.name} {...a11yProps(4)} />
        <Tab label={challenges.name} {...a11yProps(5)} />
        <Tab label={challenges.name} {...a11yProps(6)} />
      </Tabs>

      <TabPanel value={value} index={0}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
      <TabPanel value={value} index={1}></TabPanel>
      <TabPanel value={value} index={2}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
      <TabPanel value={value} index={4}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
      <TabPanel value={value} index={5}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
      <TabPanel value={value} index={6}>
        <ChallengeBody
          name={challenges.name}
          description={challenges.description}
        />
      </TabPanel>
    </Box>
  );
}
