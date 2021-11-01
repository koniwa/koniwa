const {makeBadge, } = require('badge-maker')
const fs = require("fs");
const path = require('path');



function sec2pretty(second) {
  const hour = Math.floor(second / 3600);
  const min = Math.floor((second - hour * 3600) / 60);
  const p_second = Math.floor(second - hour * 3600 - min * 60);
  return `${hour.toString().padStart(3, "0")}\
:${min.toString().padStart(2, "0")}\
:${p_second.toString().padStart(2, "0")}`;
}


const fname = process.argv[2]
const stat = JSON.parse(fs.readFileSync(fname, 'utf8'));

const output_dir = process.argv[3]
fs.mkdirSync(output_dir, {
  recursive: true
})

{
  const percent = (stat.total_duration_done / stat.total_duration * 100).toFixed(2);
  fs.writeFile(path.join(output_dir, 'progress.svg'),
    makeBadge({
      label: 'Progress',
      message: `${percent}%`,
      color: 'blue',
    }),
    () => {},
  );
}



{
  fs.writeFile(path.join(output_dir, 'duration.svg'),
    makeBadge({
      label: 'Duration',
      message: `${sec2pretty(stat.total_duration_done)} / ${sec2pretty(stat.total_duration)}`,
      color: 'blue',
    }),
    () => {},
  );
}
