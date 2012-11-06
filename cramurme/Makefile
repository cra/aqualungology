conf = conf

define sed-rules
	$(shell cat $(conf) | egrep -v "^\s*#")
endef

all: conf.py templates/_tracking.html templates/_disqus.html

templates/_tracking.html: templates/_tracking.html.template conf Makefile
	@echo делаю шаблон для google-tracking
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < templates/_tracking.html.template > templates/_tracking.html

templates/_disqus.html: templates/_disqus.html.template conf Makefile
	@echo делаю шаблон для disqus
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < templates/_disqus.html.template > templates/_disqus.html


conf.py: conf.py.template conf Makefile
	@echo наполняю conf.py содержимым из conf
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < conf.py.template > conf.py

.PHONY: clean
clean:
	rm -f conf.py templates/_tracking.html template/_disqus.html
