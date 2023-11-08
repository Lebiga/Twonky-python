SCRIPT = main.py

BUILD_WIN = pyinstaller --onefile $(SCRIPT) -n game_win

HTML_TEMPLATE = index.html

HTML_OUTPUT = game.html
BUILD_LIN = pyinstaller --onefile $(SCRIPT) -n game_lin

all: win lin

win:
	mkdir -p win
	@echo "Сборка для Windows..."
	@if $(BUILD_WIN); then \
		mv dist/game_win.exe win/; \
		rm -rf build dist game_win.spec __pycache__; \
	else \
		echo "Ошибка при сборке для Windows"; \
	fi

lin:
	mkdir -p lin
	@echo "Сборка для Linux..."
	@if $(BUILD_LIN); then \
		mv dist/game_lin lin/; \
		rm -rf build dist game_lin.spec __pycache__; \
	else \
		echo "Ошибка при сборке для Linux"; \
	fi

all: game.html

web: main.py index.html
	@echo "Creating game.html..."
	@echo "<!DOCTYPE html>" > game.html
	@echo "<html lang=\"en\">" >> game.html
	@echo "<head>" >> game.html
	@echo "<meta charset=\"UTF-8\">" >> game.html
	@echo "<title>Title</title>" >> game.html
	@echo "<link rel=\"stylesheet\" href=\"https://pyscript.net/latest/pyscript.css\" />" >> game.html
	@echo "<script defer src=\"https://pyscript.net/latest/pyscript.js\"></script>" >> game.html
	@echo "</head>" >> game.html
	@echo "<body>" >> game.html
	@echo "<h1>game</h1>" >> game.html
	@echo "<py-script>" >> game.html
	cat main.py >> game.html
	@echo "</py-script>" >> game.html
	@echo "</body>" >> game.html
	@echo "</html>" >> game.html
	@echo "game.html created successfully."
	@echo "Removing index.html..."
	rm -f index.html
	@echo "index.html removed successfully."


clean:
	rm -rf win lin