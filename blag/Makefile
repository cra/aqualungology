conf = conf

define sed-rules
	$(shell cat $(conf) | egrep -v "^\s*#")
endef

all: templates/base.html 
	@sed $(foreach rule, $(sed-rules), -e $(rule)) < templates/_tracking.html.template > templates/_tracking.html

.PHONY: clean
clean:
	rm -f templates/_tracking.html
