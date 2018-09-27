.PHONY: all

all:
	docker build --no-cache --pull --rm -t lukaszimmermann/file-download-service:0.0.1 .

