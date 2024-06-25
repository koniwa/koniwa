const { makeBadge } = require("badge-maker");
const fs = require("node:fs");
const path = require("node:path");

function sec2pretty(second) {
  const hour = Math.floor(second / 3600);
  const min = Math.floor((second - hour * 3600) / 60);
  const p_second = Math.floor(second - hour * 3600 - min * 60);
  return `${hour.toString().padStart(3, "0")}:${min.toString().padStart(2, "0")}:${p_second.toString().padStart(2, "0")}`;
}

const fname = process.argv[2];
const stat = JSON.parse(fs.readFileSync(fname, "utf8"));

const output_dir = process.argv[3];
fs.mkdirSync(output_dir, {
  recursive: true,
});

function get_color(rate) {
  const red = Number.parseInt(151 * rate);
  const green = Number.parseInt((202 - 126) * rate) + 126;
  const blue = Number.parseInt(198 * (1.0 - rate));
  return `rgb(${red},${green},${blue})`;
}

function generate_badges(prefix, substat, use_label) {
  const rate = substat.duration_done / substat.duration;
  const percent = (rate * 100).toFixed(2);

  {
    const arg = {
      message: `${percent}%`,
      color: get_color(rate),
    };
    if (use_label) {
      arg.label = "Progress";
    }

    fs.writeFile(path.join(output_dir, `${prefix}.progress.svg`), makeBadge(arg), () => {});
  }

  {
    const arg = {
      color: get_color(rate),
    };
    if (use_label) {
      arg.message = `${sec2pretty(substat.duration_done)} / ${sec2pretty(substat.duration)}`;
      arg.label = "Duration";
    } else {
      arg.message = `${sec2pretty(substat.duration_done)}`;
    }

    fs.writeFile(path.join(output_dir, `${prefix}.duration_done.svg`), makeBadge(arg), () => {});
  }
  fs.writeFile(
    path.join(output_dir, `${prefix}.duration_total.svg`),
    makeBadge({
      color: "gray",
      message: sec2pretty(substat.duration),
    }),
    () => {},
  );
}

generate_badges("total", stat.total, true);
for (const name of Object.keys(stat.series)) {
  generate_badges(name, stat.series[name], false);
}
