---
description: >-
  The /inspect/datamodel tool — the objecttype/mask/field dump, and the model
  explorer that draws the objecttypes of a datamodel and what links them.
---

# Datamodel

The **Datamodel** page (`/inspect/datamodel/`) lists the datamodels of the instance and, for each, its objecttypes with their columns, masks and fields.

**From version 6.35.0** it also has a **model explorer** — `/inspect/datamodel/<id>/model/`, linked from the datamodel page — which draws the objecttypes of one datamodel and what links them. The net is on the left; picking an objecttype fills a panel on the right without leaving the picture. It answers the question the table cannot: how the objecttypes hang together.

## Reading the net

Every chip is a **top-level objecttype**. A nested table is not something you navigate to, so it contributes its *links* to the objecttype that owns it, and is counted in the chip's "nested".

**Lines.** One line per relationship — not per column — with exactly **one arrowhead**, at the objecttype the column **points at**, the way the column list reads it: `work.lk_keyword` puts the head at `keyword`. A reverse link is the owned objecttype's link column read from the master, so its head stays at the master: `photo.lk_person` puts it at `person`.

A grey line is read at its head only. What else a line is, it says with its colour, and the line's tooltip names the columns:

* **orange** reads from either end: a **reverse link** (the master surfaces the records that link to it) or a **hierarchy** (an objecttype that owns its own records, `reverse_hierarchical`);
* **purple** is a **bidirectional** pair: two link columns of a relation objecttype, pointing at another objecttype, written on one record and read on both. A pair whose columns point at the objecttype that holds them is refused when the schema is saved;
* **dashed purple** is the **reverse marker** (`bidirectional_reverse`): the self link of a relation kind that names the kind seen from the other end (father of / son of). It is a marker on a vocabulary, not a bidirectional link.

**Boxes.** A master and the objecttypes it owns are drawn as **one box**, not as arrows between them: an arrow says "points at", and what this says is "is part of". Clicking anywhere in a box opens its master. An owned objecttype also keeps a chip of its own outside every box — it is still an objecttype in its own right, and its other links are drawn from there.

**Marks.** Each chip carries the facts that decide what an objecttype is for, as letters in its corner:

| Mark | Means                                                       |
| ---- | ----------------------------------------------------------- |
| `S`  | in the main search                                          |
| `P`  | has pool management                                         |
| `T`  | has tags                                                    |
| `H`  | hierarchical                                                |
| `HR` | hierarchical **and** the parent owns its children           |

**Counts.** Each chip shows how many objects that objecttype actually holds — one grouped pass over the object table when the page loads. It is the difference between a model as designed and a model as used: which objecttypes carry the collection, and which ones were meant and never filled. The layout ranks by it, so the subjects of the model come first and the vocabularies after them.

## The panel

Picking a chip shows, for that objecttype: its flags, its comment, its **columns** as one list in schema order — a link names the objecttype it points at, a nested table, a reverse link and the hierarchy are blocks with their columns stepped in under them, the way the datamodel editor lists them — and its **masks**, each mask's fields with a matrix of the settings that decide where a field shows up at all (detail, text, list, expert search, fulltext, facet, nested search), a filled dot for on and a faint one for off. The nested-search mark sits on a nested table's own row, since that is where the setting lives. The head of the matrix stays in view while the fields scroll. What points at an objecttype from elsewhere is a line into its chip, not a column of it. Every objecttype named in the panel is a link back into the net, so the model can be walked without leaving the page. The current objecttype is in the URL as an anchor (`…/model/#work`), so a view can be linked to and the back button works.

## Controls

* **filter** — matches objecttype names, several words at once ("phot pers"); matching chips stay lit and the matched letters are marked in the name.
* **which objecttypes** — every one, only those in the main search, or everything but those.
* **hide unlinked** — drops the objecttypes nothing links to and that link to nothing.
* **hide links** — draws the objecttypes without the lines. On a model with hundreds of links the thicket buries what the lines are about; hovering a chip still lights what it links to.
* The zoom (**◎ ＋ −**) sits in the canvas. Dragging pans; the view is held over the model and cannot be carried off it.
* **Download SVG**, the button at the right of the page head — the whole model with the legend as a file, `fylr-datamodel-<id>-v<version>.svg`, unfiltered and with nothing highlighted, whatever the page shows at the moment. The head of the file is one line: the instance and the datamodel version with its commit time on the left, the download time and the user on the right. It is drawn in the browser, so it needs no `dot` service on the execserver, unlike the SVG the datamodel manager offers.

## JSON

Both halves answer with JSON for `Accept: application/json`:

* `/inspect/datamodel/<id>/model/` — the compiled net (`Graph.nodes`, `Graph.edges`) and the object counts.
* `/inspect/datamodel/<id>/model/<objecttype>/` — that objecttype's columns, masks and fields.

An edge carries `from`, `to`, the full api name of the column, its `kind` (`link`, `reverse` or `hierarchy`) and the `bidirectional` / `bidirectional_reverse` flags.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Objects](objects.md) — render one record against any datamodel version.
