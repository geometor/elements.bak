---
title: The Beginning
subtitle: Developing a new presentation for Euclid's Elements
author:
collection:
  name: Post Details
  showCount: true
  showMenu: true
content:
  items: '@self.children'
child_type: article
figure:
  image:
  alt:
  title:
  caption:
taxonomy:
  tag:
  category:
date: 02/05/2020
---

- a fully traversable system of logic

===

The Perseus project from Tufts University has a public domain translations of Euclid's Elements by Thomas Heath.

Perseus allows for the download of XML files containing the content. These files are well formatted and fairly semantic making it an easy job to parse with `xmlstarlet` at the command line. A simple script converted the xml into over 600 markdown pages within Photon.

The goal is to create a fully linked and traversable system. Here are a few key objectives:

- dependency graph for each element
- animated demonstrations

Ultimately, I want to refactor the whole thing into a more code-like structure.
