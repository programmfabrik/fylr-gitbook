all: gen-release-notes

gen-release-notes:
	@if [ -z "${GITHUB_TOKEN}" ]; then \
		echo "GITHUB_TOKEN is unset"; \
		exit 1; \
	fi
	@echo './gen_release_notes.py $$GITHUB_TOKEN'
	@./gen_release_notes.py "${GITHUB_TOKEN}"

.PHONY: gen-release-notes
