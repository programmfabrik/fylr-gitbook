all: gen-release-notes

gen-release-notes:
	@if [ -z "${GITHUB_TOKEN}" ]; then \
		echo "GITHUB_TOKEN is unset"; \
		exit 1; \
	fi
	@echo './gen_release_notes.py $$GITHUB_TOKEN'
	@./gen_release_notes.py "${GITHUB_TOKEN}"

openapi:
	rm -rf for-developers/system-data-types
	cd for-developers && wget -q -R "*.html*" --cut-dirs=3 -nH -r -np http://localhost:8081/inspect/apidocs/gitbook/system-data-types/

.PHONY: gen-release-notes .gen-openapi-docs
