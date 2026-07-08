---
description: Upload your own ICC color profiles for the file worker to use.
---

# Custom .icc Color Profiles

The file worker uses **ICC color profiles** when it converts images and generates preview versions. fylr already ships with a set of common built-in profiles (the default is `sRGB_IEC61966-2-1_black_scaled`). Here you can add your own `.icc` profiles on top of those, so they can be selected by name in the file worker / produce configuration.

### Name

A name for the profile. This is the name used to reference the profile in the file worker configuration.

### .icc File

Upload the color profile as an `.icc` file.
