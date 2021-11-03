const {makeBadge, } = require('badge-maker')
const fs = require("fs");
const path = require('path');



function sec2pretty(second) {
  const hour = Math.floor(second / 3600);
  const min = Math.floor((second - hour * 3600) / 60);
  const p_second = Math.floor(second - hour * 3600 - min * 60);
  return `${hour.toString().padStart(3, "0")}:${min.toString().padStart(2, "0")}:${p_second.toString().padStart(2, "0")}`;
}


const fname = process.argv[2]
const stat = JSON.parse(fs.readFileSync(fname, 'utf8'));

const output_dir = process.argv[3]
fs.mkdirSync(output_dir, {
  recursive: true
})


function generate_badges(prefix, substat) {
  {
    const percent = (substat.duration_done / substat.duration * 100).toFixed(2);
    fs.writeFile(path.join(output_dir, `${prefix}.progress.svg`),
      makeBadge({
        label: 'Progress',
        message: `${percent}%`,
        color: 'blue',
      }),
      () => {},
    );
  }



  {
    fs.writeFile(path.join(output_dir, `${prefix}.duration.svg`),
      makeBadge({
        label: 'Duration',
        message: `${sec2pretty(substat.duration_done)} / ${sec2pretty(substat.duration)}`,
        color: 'blue',
      }),
      () => {},
    );
  }
}

generate_badges('total', stat.total);
Object.keys(stat.serieses).forEach(function(name) {
  generate_badges(name, stat.serieses[name]);
});
