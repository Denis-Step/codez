const apicalls = require("../apicalls");
import axios from "axios";
jest.mock("../");

test("API Call Loads Words properly", () => {
  const resp = { data: SAMPLE };
  axios.mockResolvedValue(SAMPLE);
});
