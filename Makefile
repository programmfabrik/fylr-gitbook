all: gen-release-notes

gen-release-notes:
	@if [ -z "${GITHUB_TOKEN}" ]; then \
		echo "GITHUB_TOKEN is unset"; \
		exit 1; \
	fi
	@echo './gen_release_notes.py $$GITHUB_TOKEN'
	@./gen_release_notes.py "${GITHUB_TOKEN}"

openapi:
	# openapi docs live inside ".gitbook/includes"
	# the gitbook editor can be used to pull the prepared docs
	# into the articels
	rm -rf .gitbook/includes
	cd .gitbook && wget -q -R "*.html*" --cut-dirs=3 -nH -r -np http://localhost:8081/inspect/apidocs/gitbook/includes/

.PHONY: gen-release-notes .gen-openapi-docs
