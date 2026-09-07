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

**Lines.** One line per relationship — not per column — with exactly **one arrowhead**, at the objecttype that **holds the column**. A vocabulary is used by the things that name it, and that is the direction worth reading: `work.lk_keyword` puts the head at `work`.

A line marked **R** reads from either end. Three different schema constructs land there, and the line's tooltip names the columns and says which it is:

* a **reverse link** — the master surfaces the records that link to it;
* a **hierarchy** — an objecttype that owns its own records (`reverse_hierarchical`);
* a **bidirectional** column — set on one side, written on both.

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

Picking a chip shows, for that objecttype: its flags, its comment, its **links** (the column on the left, the objecttype at the other end on the right), its **columns** with their types, and its **masks** — each mask's fields with a matrix of the settings that decide where a field shows up at all (detail, text, list, expert search, fulltext, facet, nested search), a filled dot for on and a faint one for off. Every objecttype named in the panel is a link back into the net, so the model can be walked without leaving the page. The current objecttype is in the URL as an anchor (`…/model/#work`), so a view can be linked to and the back button works.

## Controls

* **filter** — matches objecttype names, several words at once ("phot pers"); matching chips stay lit and the matched letters are marked in the name.
* **which objecttypes** — every one, only those in the main search, or everything but those.
* **hide unlinked** — drops the objecttypes nothing links to and that link to nothing.
* **hide links** — draws the objecttypes without the lines. On a model with hundreds of links the thicket buries what the lines are about; hovering a chip still lights what it links to.
* The zoom (**◎ ＋ −**) sits in the canvas. Dragging pans; the view is held over the model and cannot be carried off it.

## JSON

Both halves answer with JSON for `Accept: application/json`:

* `/inspect/datamodel/<id>/model/` — the compiled net (`Graph.nodes`, `Graph.edges`) and the object counts.
* `/inspect/datamodel/<id>/model/<objecttype>/` — that objecttype's columns, masks and fields.

An edge carries `from`, `to`, the full api name of the column, its `kind` (`link`, `reverse` or `hierarchy`) and the `bidirectional` / `bidirectional_reverse` flags.

## See also

* [The /inspect Backend](README.md) — the console overview and auth model.
* [Objects](objects.md) — render one record against any datamodel version.
