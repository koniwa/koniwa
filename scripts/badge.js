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

function get_color(rate) {
  const red = parseInt(151 * rate);
  const green = parseInt((202 - 126) * rate) + 126;
  const blue = parseInt(198 * (1.0 - rate));
  return `rgb(${red},${green},${blue})`;
}

function generate_badges(prefix, substat, use_label) {
  const rate = substat.duration_done / substat.duration;
  const percent = (rate * 100).toFixed(2);

  {
    const arg = {
      message: `${percent}%`,
      color: get_color(rate),
    }
    if (use_label) {
      arg.label = 'Progress' ;
    }

    fs.writeFile(path.join(output_dir, `${prefix}.progress.svg`),
      makeBadge(arg),
      () => {},
    );
  }

  {
    const arg = {
      message: `${sec2pretty(substat.duration_done)} / ${sec2pretty(substat.duration)}`,
      color: get_color(rate),
    };
    if (use_label) {
      arg.label = 'Duration' ;
    }

    fs.writeFile(path.join(output_dir, `${prefix}.duration.svg`),
      makeBadge(arg),
      () => {},
    );
  }
}

generate_badges('total', stat.total);
Object.keys(stat.serieses).forEach(function(name) {
  generate_badges(name, stat.serieses[name]);
});
