export default class {
  constructor(name, description, id, expectedOutput, stdin) {
    this.id = id;
    this.name = name;
    this.description = description;
    this.expectedOutput = expectedOutput;
    this.stdin = stdin;
  }
}
