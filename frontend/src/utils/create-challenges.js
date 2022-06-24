//create array of challenges
const challenges = [
  {
    problem_id: 0,
    name: "Hello World",
    description: `
**Using F#**
 
*   Print a \`Hello World!\` message to the console.

**Example 1:**
**Output:** Hello World!
`,
    stdout: "Hello World!",
    stdin: 0,
  },
  {
    problem_id: 1,
    name: "FizzBuzz",
    description: `
Given an integer \`n\`, return _a string array_ \`answer\` _(**1-indexed**) where_:

*   \`answer[i] == "FizzBuzz"\` if \`i\` is divisible by \`3\` and \`5\`.
*   \`answer[i] == "Fizz"\` if \`i\` is divisible by \`3\`.
*   \`answer[i] == "Buzz"\` if \`i\` is divisible by \`5\`.
*   \`answer[i] == i\` (as a string) if none of the above conditions are true.

**Example 1:**

**Input:** n = 3
**Output:** ["1","2","Fizz"

**Example 2:**

**Input:** n = 5
**Output:** ["1","2","Fizz","4","Buzz"\

**Example 3:**

**Input:** n = 15
**Output:** ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

**Constraints:**

*   \`1 <= n <= 104\`
`,
    stdout: `1
    2
    Fizz
    4
    Buzz
    Fizz
    7
    8
    Fizz
    Buzz`,
    stdin: 5,
  },
  {
    problem_id: 2,
    name: "Anagram",
    description: `
    Given two strings s and t, return true if t is an anagram
    of s, and false otherwise.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**Example 1:**

**Input:** s = "anagram", t = "nagaram"
**Output:** true

**Example 2:**

**Input:** s = "rat", t = "car"
**Output:** false

**Constraints:**

*   \`1 <= s.length, t.length <= 5 * 104\`
*   \`s\` and \`t\` consist of lowercase English letters.

**Follow up:** What if the inputs contain Unicode characters? How would you adapt your solution to such a case?`,
    stdin: "rat,car",
    stdout: false,
  },
];

export default challenges;
