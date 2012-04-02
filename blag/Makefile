conf = conf

define sed-rules
	$(shell cat $(conf) | egrep -v "^\s*#")
endef

all: conf.py templates/_tracking.html 

templates/_tracking.html: templates/_tracking.html.template conf Makefile
	@echo Создаем иноформацию для трэкинга
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < templates/_tracking.html.template > templates/_tracking.html

conf.py: conf.py.template conf Makefile
	@echo Создаем conf.py
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < conf.py.template > conf.py

.PHONY: clean
clean:
	rm -f templates/_tracking.html
