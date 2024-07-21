# Makefile

# Команда для установки зависимостей
install:
	poetry install

# Команда для запуска brain-games
brain-games:
	poetry run brain-games

# Команда для сборки пакета
build:
	poetry build

# Команда для публикации пакета (в тестовом режиме)
publish:
	poetry publish --dry-run

# Команда для установки пакета из локального дистрибутива
package-install:
	python3 -m pip install --user dist/*.whl

# Команда для линта с flake8
lint:
	poetry run flake8 brain_games