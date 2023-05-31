# how to update release notes
currently it is a manual process:

1. Have a git clone of this repo 

2. Have python 3 (no additional libraries needed)

3. Github access: The script expects a Github token in the `GITHUB_TOKEN` environment variable. You can create such a token in github.com: "Settings"/"Developer settings"/"Personal access tokens"/"Tokens (classic)". It requires the `repo` scope to access the releases of the private repository.

4. S3 access: For access to our S3-provider "Wasabi" the script uses the AWS CLI tools (https://github.com/aws/aws-cli, Debian package `awscli`, command binary `aws`). Before using the script the tools must be configured (`aws configure`). Use the "AWS Access Key ID" and "AWS Secret Access Key" of an authorized user and use `eu-central-1` as the "Default region name".
* For storing the release assets, the bucket `fylr-releases` is used.

5. execute `make` in the root directory of this repo. 

* A python3 script reads the release notes from fylr's releases on GitHub.
* The files (release artifacts/products) are copied to S3 (Wasabi). Files are only added when they are not present yet.
* Files will be updated:  `SUMMARY.md`, `releases/*.md`, `releases/*/*.md`

* If a release artifact is removed later, it is not removed from s3 but from the releases/...md files.
* If an artifact is changed later, a manual cleanup of the S3 files is required.
* if you change the relase notes later then it is being recognized by the next run with `make`.
* Drafts and PreReleases are ignored.

6. Do e.g. `git status` to see what was changed and then add, commit, push

