install: 
	./install_modules.sh

clean:
	-rm -rf image/store/vendored/*
	find . \( -name "*.pyc" -o -name __pycache__ \) -exec rm -f {} \;
