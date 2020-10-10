const apicalls = require("../../apicalls");
const SAMPLE = {
  aimed: false,
  apses: false,
  batch: false,
  calyx: false,
  donna: false,
  erase: false,
  genus: false,
  grade: false,
  holly: false,
  homer: false,
  homme: false,
  jihad: false,
  litho: false,
  media: false,
  papas: false,
  petty: false,
  plyer: false,
  ranch: false,
  scald: false,
  scent: false,
  shown: false,
  stint: false,
  wader: false,
  while: false,
  wrath: false,
};

export default function loadWords() {
  return new Promise((resolve, reject) => {
    const words = { data: SAMPLE };
    resolve(words);
  });
}
