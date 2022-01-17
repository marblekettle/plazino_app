NAME=Plazino
DIR=venv

$(NAME): $(DIR)
	echo "Type \"bash run.sh\" to start."

$(DIR):
	python3 -m venv $(DIR)
	. $(DIR)/bin/activate && \
	pip install -e . && \
	pip list

remove:
	rm -rf $(NAME).egg-info
	rm -rf instance
	rm -rf __pycache__
	rm -rf $(DIR)
