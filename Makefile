
all: lint_python lint_markdown

TARGET_DIRS:=./scripts

flake8:
	find $(TARGET_DIRS) | grep '\.py$$' | xargs flake8
black:
	find $(TARGET_DIRS) | grep '\.py$$' | xargs black --diff | diff /dev/null -
pyright:
	npx pyright
isort:
	find $(TARGET_DIRS) | grep '\.py$$' | xargs isort --diff | diff /dev/null -
pydocstyle:
	find $(TARGET_DIRS) | grep -v tests | xargs pydocstyle --ignore=D100,D101,D102,D103,D104,D105,D107,D203,D212
	

jsonlint:
	find .*json $(TARGET_DIRS) | grep '\.jsonl$$' | sort |xargs cat | python3 -c 'import sys,json; [json.loads(line) for line in sys.stdin]'
	find .*json $(TARGET_DIRS) | grep '\.json$$' | sort |xargs -n 1 -t python3 -m json.tool > /dev/null
	find .*json $(TARGET_DIRS) | grep '\.json$$' | sort |xargs -n 1 -t jsonlint
	python3 -c "import sys,json;print(json.dumps(json.loads(sys.stdin.read()),indent=4,ensure_ascii=False,sort_keys=True))" < .markdownlint.json | diff -q - .markdownlint.json

yamllint:
	find . \( -name node_modules -o -name .venv \) -prune -o -type f -name '*.yml' -print \
		| xargs yamllint --no-warnings
	

setup_node_module:
	npm install markdownlint-cli

lint_markdown:
	find . -type d \( -name node_modules -o -name .venv \) -prune -o -type f -name '*.md' -print \
	| xargs npx markdownlint --config ./.markdownlint.json

lint_python: flake8 black pyright isort yamllint pydocstyle
