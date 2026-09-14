---
description: Holding several files in one file field — and what fylr does with them
---

# Variants

A file field in fylr does not hold a single file. Its value is a **list** of
files, and each file in that list is a **variant**. One field can therefore
carry several files at once — the front and back of a postcard, several scans
of one page, a video together with its subtitle track.

Exactly one variant is the **preferred** one. fylr uses the preferred variant
wherever it needs a single file to stand for the record: the thumbnail in a
result grid, the preview on the detail page, the poster of a video player. When
a field holds only one file, that file is the preferred variant automatically.

Each variant is a full file in its own right: an uploaded **original** together
with the renditions fylr derives from it (thumbnail, preview, poster frame, and
so on). Variants are not smaller copies of one file — for that, see
[Custom Renditions & Crop Tool](custom-renditions-and-crop-tool.md). Variants
are *different files* kept together in the same field.

## Contents

- [When to use variants](#when-to-use-variants)
- [Managing variants in the editor](#managing-variants-in-the-editor)
- [Matching files by name during upload](#matching-files-by-name-during-upload)
- [Displaying subtitles with videos](#displaying-subtitles-with-videos)
- [Feature overview](#feature-overview)

## When to use variants

Use variants when several files belong to **one** field of **one** record and
you want fylr to treat one of them as the representative file:

- **Multiple views of the same object** — front and back of a postcard, recto
  and verso of a sheet, several angles of a sculpture.
- **The same content in different formats** — a print-ready TIFF next to a JPEG
  for the web, both attached to the same field.
- **A media file with its sidecar** — a video together with its `.vtt`
  subtitle track (see [below](#displaying-subtitles-with-videos)).

When each file needs its **own descriptive metadata** (its own caption,
photographer, usage right), variants are the wrong tool — use a
[nested table](https://docs.fylr.io/for-developers/concepts/nested-and-reverse-nested.md)
instead, with one file field per row. Variants share the field; they carry no
per-file description beyond the file's own technical data.

## Managing variants in the editor

To add, remove or reorder the variants of a file field:

1. Open the record and switch it to **edit** mode.
2. Open the **variant editor** for the file field, either by
   **Alt + clicking** the file field, or through the **three-dot menu** on the
   field and choosing the variants entry.
3. Add a file with the **plus button** at the bottom left; remove a variant
   from its own menu.
4. **Order matters:** the file at the **top of the list is the preferred
   variant** — the one the viewer shows in the various outputs (grid preview,
   detail preview, player). Drag the file you want as the representative to the
   top.
5. Choose **Apply**, then **save** the record in the editor to persist the
   change.

Saving a record does not re-upload files that were already there; only the
variants you added or replaced are processed.

## Matching files by name during upload

When you upload several files at once, fylr can decide **on its own** whether a
new file is a fresh record or belongs to a record it is already building — by
comparing filenames. This lets you drop a whole folder of files in one go and
have related files land together as variants. Three relations are recognised:

| Relation | What fylr does | Example |
| --- | --- | --- |
| **Same file** | Same filename — treated as the same file. | `photo.jpg` uploaded twice |
| **Version** | Same name, different extension — added as another **variant** of the same field. | `scan.tif` and `scan.jpg` |
| **Series** | Same base name followed by a separator and a number — distributed as a numbered series. | `page_01.jpg`, `page_02.jpg`, … |

For the **series** relation the trailing counter must be separated by a space,
`_` or `-` and end the filename before the extension (`name_01.jpg`,
`name 2.png`, `name-003.tif`).

Version and series recognition are optional and controlled by the **"recognize
version"** and **"recognize series"** options in the upload dialog. If both are
off, every file becomes its own record.

## Displaying subtitles with videos

fylr can show a subtitle track on a video. The subtitle file must be a **WebVTT
(`.vtt`)** file, and it must sit as a **variant** of the video file.

### Add the subtitle to an existing video

1. Open the record carrying the video and switch it to **edit** mode.
2. Open the **variant editor** for the file field — **Alt + click** the field,
   or use the **three-dot menu** and open the variants.
3. Add the `.vtt` file with the **plus button** at the bottom left. **Leave the
   video at the top of the list** — the topmost file is the one the viewer
   displays.
4. Choose **Apply**, then **save** the record.

Play the video: a **CC button** now appears in the player, and the subtitle
track can be selected from it.

### Let fylr match the subtitle on upload

If you upload the video and its subtitle **together**, fylr can attach the
`.vtt` to the video's variants automatically, provided the subtitle filename
identifies the video it belongs to. The recognised form is:

```
<video-basename>--<label>.vtt
```

that is, the video's base name, a **double hyphen**, and a short label, e.g. a
video `interview.mp4` with subtitles `interview--en.vtt` and
`interview--de.vtt`. The part after the `--` becomes the **track label** shown
in the player's CC menu (here `en` and `de`).

The manual route in the [section above](#add-the-subtitle-to-an-existing-video)
works with any filename; only the automatic on-upload matching depends on the
`--<label>.vtt` naming.

## Feature overview

| Feature | How to use it |
| --- | --- |
| Hold several files in one field | Open the variant editor (Alt + click the field, or its three-dot menu), add files with the plus button. |
| Choose the representative file | Drag the file to the **top** of the variant list — the top file is the preferred variant. |
| Attach a subtitle track | Add a `.vtt` file as a variant of the video, keep the video on top. |
| Auto-group files on upload | Name related files with a shared base (`scan.tif`/`scan.jpg`) or a numbered series (`page_01.jpg`); enable *recognize version* / *recognize series*. |
| Auto-attach subtitles on upload | Name the subtitle `<video-basename>--<label>.vtt` and upload it together with the video. |

## See also

- [Files and assets](https://docs.fylr.io/for-developers/concepts/files-and-assets.md)
  — the concept behind records, files, variants, originals and renditions.
- [Custom Renditions & Crop Tool](custom-renditions-and-crop-tool.md) — deriving
  additional sized/cropped versions of a single file.
