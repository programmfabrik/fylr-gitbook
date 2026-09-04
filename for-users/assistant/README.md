---
description: the assistant pane — asking for what you want instead of building it
---

# The assistant

**From version 6.36.0.** The assistant is a pane at the right edge of the window, opened with the **Assistant** handle. It pushes the content aside rather than covering it, and it stays where it is while you navigate.

It is not a second search box. It works the app you are already in: what you ask for happens on the screen next to it — the search bar fills with tokens you can take out, boxes tick themselves in the filter tree, the view switches when what you asked for lives somewhere else. Anything it does you could have done by hand, and anything it does you can undo by hand.

## Asking for records

Type what you are looking for. The assistant turns it into a search and runs it in the app:

> _"show me pictures of mountains"_

The search bar then carries an **AI** token, and the records are an ordinary result set — facets, sorting, saving, export, all of it. Click the token to see what it searched for and to change the words.

It searches two ways at once and fuses the results:

* **by meaning** — your phrase is turned into a vector and compared with the vector of every record, which finds records that mean what you asked for even when they never use your words: _"ein kleiner Vogel"_ finds _House Sparrow on Wooden Surface_.
* **by words** — the ordinary full text search, which reaches inside the files as well: the text layer of a PDF, what OCR read off a scan. A record can be found by a word printed on page forty and written nowhere else.

## When your request means two things

Some requests genuinely say two things. _"landscape images"_ can mean pictures **of** landscapes or pictures **in** landscape format — and those are different searches over different records.

The assistant asks, once, with both readings as buttons, and then acts on the answer. It does not ask when one reading is plainly meant.

## Narrowing what you got

Ask what you can narrow by and it reads the filters of the result: which keywords, which pool, how many records behind each. Ask it to narrow and it ticks the box in the filter tree, the way you would — the search you had stays, and you can untick it yourself.

Asking it to drop a filter drops it. A filter left over from an earlier question is mentioned rather than silently applied.

## More like this

A record's 3-dot menu offers **Find similar pictures**: the records whose picture looks like the one you are looking at, compared picture to picture. Nothing written about them plays any part, which is why it finds things a description never mentions.

The reference is the picture the asset browser is showing, so a record with several files answers for the one in front of you.

## Working on a record

Open a record in the editor and the assistant can work on it as well as search.

* **Ask about it.** _"what is in the video?"_, _"is there text in this picture?"_ — the answer is yours to read and to put where you want it.
* **Fill fields.** Mark fields with the star next to the field name and ask for what you want in them. The answer comes back as values you apply with a click; nothing is saved until you press Save, and languages the answer did not touch keep what they had.

The files go along with your question when **Send the object's files along** is ticked. They are sent at a small rendition to begin with; if the answer turns on detail the assistant asks for a larger one and says so.

## What it will not do

It says what it cannot do rather than doing something else:

> _"sortier nach dateigröße"_ → **Eine Sortierung nach Dateigröße ist leider nicht möglich.**

It tells you what is actually on screen, using the numbers the app gave it — so an answer claiming five records is five records. And it will not claim to have opened, collected, shared or filtered anything that did not happen.

## The Debug switch

The switch in the pane's header shows the working: every tool the assistant called, what each answered, which model replied and what the turn cost in tokens. Off by default, remembered per user, and worth turning on when an answer surprises you.

## What it needs

An administrator has to connect a provider and switch the parts on — see [AI Configuration](../../for-administrators/ai/configuration.md). Without a search assistant model the pane still searches, it simply searches the words you typed. Everything the assistant does runs **in your own session**, with your rights and your masks: it cannot see or change anything you could not.
