There is a script to generate the release notes from the Github releases. The files are copied to S3 (Wasabi). Run `make` to generate the release notes and commit the changes and new files:

* `SUMMARY.md`
* `releases/*.md`
* `releases/*/*.md`

The script is written in Python 3 without using any additional libraries. For S3 access another command line tool is required (see below).

## Github access

The script expects a Github token in the `GITHUB_TOKEN` environment variable. You can create such a token in
"Settings"/"Developer settings"/"Personal access tokens"/"Tokens (classic)". It requires the `repo` scope to access the releases of the private repository. Whether the token is set is checked by the `Makefile`.

## S3 access

For access to Wasabi the script uses the AWS CLI tools (https://github.com/aws/aws-cli, Debian package `awscli`). Before using the script the tools must be configured (`aws configure`). Use the "AWS Access Key ID" and "AWS Secret Access Key" of an authorized user and use `eu-central-1` as the "Default region name".

For storing the release assets, the bucket `fylr-releases` is used. Files are only added when they are not present yet, so in case a release is changed later, a manual cleanup of the mirrored files is required.
