
all: lint_node lint_python

TARGET_DIRS:=./koniwa
OUTPUT_STAT:=/dev/stdout
	
yamllint:
	find . \( -name node_modules -o -name .venv \) -prune -o -type f -name '*.yml' -print \
		| xargs yamllint --no-warnings
ruff:
	ruff format --respect-gitignore --check
	ruff check --respect-gitignore

check_json:
	python3 -m koniwa.check_json -i ./data -o $(OUTPUT_STAT)

lint_python: ruff yamllint check_json


pyright:
	npx pyright

markdownlint:
	find . -type d \( -name node_modules -o -name .venv \) -prune -o -type f -name '*.md' -print \
	| xargs npx markdownlint --config ./.markdownlint.json

lint_node: markdownlint pyright

