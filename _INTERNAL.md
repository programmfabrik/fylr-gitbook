# how to update release notes
currently it is a manual process:

1. Have a git clone of this repo 

2. Have python 3 (no additional libraries needed)

3. Github access: The script expects a Github token in the `GITHUB_TOKEN` environment variable. You can create such a token in github.com: "Settings"/"Developer settings"/"Personal access tokens"/"Tokens (classic)". It requires the `repo` scope to access the releases of the private repository.

4. S3 access: For access to our S3-provider "Wasabi" the script uses the AWS CLI tools (https://github.com/aws/aws-cli, Debian package `awscli`, command binary `aws`, uses `~/.aws/credentials`). Before using the script the tools must be configured (`aws configure`). Use the "AWS Access Key ID" and "AWS Secret Access Key" of an authorized user and use `eu-central-1` as the "Default region name".
* For storing the release assets, the bucket `fylr-releases` is used.

5. execute `make` in the root directory of this repo. 

* A python3 script reads the release notes from fylr's releases on GitHub.
* The files (release artifacts/products) are copied to S3 (Wasabi). Files are only added when they are not present yet.
* Files will be updated:  `SUMMARY.md`, `releases/*.md`, `releases/*/*.md`

* If a release artifact is removed later, it is not removed from s3 but from the releases/...md files.
* If an artifact is changed later (e.g. release re-done on github), manually delete its file(s) in S3 bucket fylr-releases and `make`.
* if you change the relase notes later then it is being recognized by the next run with `make`.
* Drafts and PreReleases are ignored.

6. Do e.g. `git status` to see what was changed and then add, commit, push


# how the plugin sheets are updated

The plugin marketplace is fed by two Google sheets. Everything in them is generated except three curation columns and one hand-kept tab.

The chain is: the `programmfabrik` GitHub org → the private "easydb + fylr plugins" sheet, tab "fylr plugins" → the published marketplace catalog sheet → the fylr servers.

* `make google-plugins-sheet` (fylr repo, `utils/plugins_sheet.py`) rebuilds the private sheet's "fylr plugins" and "easydb plugins" tabs from the org: every repo carrying a plugin manifest becomes a row, read from the manifest on the default branch, from `releases/latest` and from the release/Pages workflows. The split criterion is the repo name — `fylr-plugin-*` is a fylr plugin, everything else lands on the easydb tab. The run is non-destructive: label row, header, dropdowns, checkbox formatting and the human columns survive it.
* `make google-marketplace` (`utils/marketplace_catalog_sheet.py`) copies the rows with a `fylr marketplace` tick, plus the rows they transitively depend on (hidden libraries such as `commons-library`), into the published catalog sheet, keeping the same column layout.
* the servers pull that sheet's CSV export at runtime (`plugin.marketplace.catalog.url`), cached for 15 minutes. Nothing is compiled into the binary since 6.35, so the offer changes without a fylr release. The full picture is in `internal/pluginmarketplace/doc.go` in the fylr repo.

Both targets are run by hand — there is no cron and no CI job. Run them:

* when a plugin repo is added or renamed (sweep, so the row exists at all),
* after a GitHub release: `release tag` and `release date` are what the plugin manager shows as version and date. The download URL resolves to `releases/latest`, so installs keep working — a stale row breaks nothing, it just never advertises the new version,
* after a curation change (a tick or a category): the transfer alone is enough,
* a changed shop description is a manifest change: edit `plugin.info`, commit, and the next sweep picks it up — no release needed.

Always sweep first, then transfer. The private tab is the master, so a fix made directly in the catalog sheet is silently reverted by the next transfer.

## what humans fill in

Three columns of the "fylr plugins" tab:

* `fylr marketplace` (checkbox) — the only criterion for what the shop offers.
* `fylr licensed` (checkbox) — a paid plugin: installable by anyone, but enabling it needs an instance license that grants the plugin by name.
* `category` — the group slug (authority, geo, editor, media, integration, ai; empty = "other"). The script seeds a default for a new row, after that the value in the sheet wins.

Everything else in that tab is regenerated on every run, so a correction typed there is gone after the next sweep. Fix the source instead: the manifest (`plugin.name`, `plugin.info`, `custom_types`, dependencies), the GitHub repo (description, license, visibility, release) or the script (the developer company override table).

The "easydb plugins" tab has no human columns at all, and the published catalog sheet has none either — it is a copy. Only its header row is protected (the service account is not an editor there): if the master layout ever changes, a human has to fix that header once.

## the migration tab

"Plugin Migration Disk -> URL" is the one hand-curated tab. The script never adds rows to it, it only maintains two columns and the red marking.

* `disk name` and `url` are hand-kept: the disk plugin, and the manifest name of the marketplace plugin that succeeds it. `-` means deliberately not migrated (the plugin is deleted), empty means undecided.
* `target url` and `marketplace` are script-written: the target's install artifact, and whether the target currently has a marketplace entry.
* `remarks` is free text, except for the `[red: <reason>]` suffix the script appends and removes.

A red row means the target has no marketplace entry, i.e. the migration would delete the plugin. The red markings on the other two tabs (shop-ticked without a release; an easydb plugin with no fylr successor) are the run's audit as well.

Two traps when the steps are run separately: `push` writes from the cache of the previous `build`, so a tick set by hand in between must be followed by a `build` before the next `push` or it is reverted. And the `preserved N marketplace ...` line is the guard — if N drops against the previous run, human decisions were lost and the push must not go out.

# how to refresh plugins/overview.md

The "In the marketplace" tables are a snapshot of the **published marketplace
catalog** — the same sheet fylr pulls at runtime, mirrored in the fylr repo at
`internal/pluginmarketplace/testdata/catalog_sheet.csv` (refresh it there first,
see that directory's README). Take from each row: the manifest plugin name, the
`fylr licensed` / `custom data type` / `dependencies` / `visibility` flags, the
category, the repository URL and the one-line repo description. Rows without the
`fylr marketplace` tick are not offered and do not belong in those tables —
`commons-library` is one of them and is described in prose instead.

Two rules the page follows:

* A **private** repository (`visibility` other than `PUBLIC`) answers 404 to a
  reader without access — name it, do not link it.
* The catalog's repo descriptions are written for GitHub. Rewrite the ones that
  open with "This plugin …" or "fylr plugin that …" rather than pasting them.

The "Not in the marketplace" section is maintained by hand: plugins that exist
but are not offered in the shop. Link the repository, not a release URL — the
install URL belongs in the plugin's own README, which the plugin manager now
displays.
