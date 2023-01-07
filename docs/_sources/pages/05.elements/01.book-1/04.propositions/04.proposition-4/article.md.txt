---
title:  Proposition I.4
subtitle: Triangles with Equal Sides have equal angles
author:
routes:
  aliases:
    - /elem.1.4
    - /I.4
taxonomy:
  tag:
  category:
    - proof
    - triangles
mermaid: true
---

If two triangles have the two sides equal to two sides respectively, and have the angles contained by the equal straight lines equal, they will also have the base [^I.4:3] equal to the base, the triangle will be equal to the triangle, and the remaining angles [^I.4:1] will be equal to the remaining angles respectively, [^I.4:2] namely those which the equal sides subtend. [^I.4:4]


===

Let `ABC`, `DEF` be two triangles having the two sides `AB`, `AC` equal to the two sides `DE`, `DF` respectively, namely `AB` to `DE` and `AC` to `DF`, and the angle `BAC` [^I.4:5]  equal to the angle `EDF`.

I say that the base `BC` is also equal to the base `EF`, the triangle `ABC` will be equal to the triangle `DEF`, and the remaining angles will be equal to the remaining angles respectively, namely those which the equal sides subtend, that is, the angle `ABC` to the angle `DEF`, and the angle `ACB` to the angle `DFE`.

For, if the triangle `ABC` be applied to the triangle `DEF`, 

- and if the point `A` be placed on the point `D` and the straight line `AB` on `DE`,

then the point `B` will also coincide [^I.4:6] with `E`, because `AB` is equal to `DE`.

Again, `AB` coinciding with `DE`, the straight line `AC` will also coincide with `DF`, because the angle `BAC` is equal to the angle `EDF`; 

- hence the point `C` will also coincide with the point `F`, because `AC` is again equal to `DF`.

But `B` also coincided with `E`; hence the base `BC` will coincide with the base `EF`.

[For if, when `B` coincides with `E` and `C` with `F`, the base `BC` does not coincide with the base `EF`, two straight lines will enclose a space: which is impossible. 

- Therefore the base `BC` will coincide with `EF`] [^I.4:7] and will be equal to it. [I.c.n.4]

Thus the whole triangle `ABC` will coincide with the whole triangle `DEF`, 

- and will be equal to it.

And the remaining angles will also coincide with the remaining angles and will be equal to them, the angle `ABC` to the angle `DEF`, and the angle `ACB` to the angle `DFE`.

Therefore etc. [^I.4:8]

- (Being) what it was required to prove.


[I.c.n.4]: /elem.1.c.n.4 "Book 1 - Common Notion 4"

[references]
graph BT

I_4[ I.4 ]:::prop;
click I_4 "/elem.1.4" "Book I Proposition 4";

%%%% dependencies


I_cn4( I.cn.4 ):::cn;
click I_cn4 "/elem.1.c.n.4" "Book I Common Notion 4";

%%%% links

I_4 --> I_cn4

[/references]

## Footnotes

[^I.4:1]: enunciation
    It is a fact that Euclid's enunciations not infrequently leave something to be desired in point of clearness and precision. Here he speaks of the triangles having <quote>the angle equal to the angle, namely the angle contained by the equal straight lines</quote> (<foreign lang="greek">τὴν γωνίαν τῇ γωνίᾳ ἴσην ἔχῃ τὴν ὑπὸ τῶν ἴσων εὐθειῶν περιεχομένην</foreign>), only one of the two angles being described in the latter expression (in the accusative), and a similar expression in the dative being left to be understood of the other angle. It is curious too that, after mentioning two <quote><em>sides</em>,</quote> he speaks of the angles contained by the equal <quote><em>straight lines</em>,</quote> not <quote><em>sides</em>.</quote>
It may be that he wished to adhere scrupulously, at the outset, to the phraseology of the definitions, where the angle is the inclination to one another of two <em>lines</em> or <em>straight lines</em>. Similarly in the enunciation of [<a href="/elem.1.5">I. 5</a>] he speaks of producing the equal <quote>straight lines</quote> as if to keep strictly to the wording of [<a href="/elem.1.post.2">Postulate 2</a>.

[^I.4:2]: respectively.
    I agree with Mr H. M. Taylor (<title>Euclid</title>, p. ix) that it is best to abandon the traditional translation of <quote>each to each,</quote>
which would naturally seem to imply that all the four magnitudes are equal rather than (as the Greek <foreign lang="greek">ὲκατέρα ὲκατέρᾳ</foreign> does) that one is equal to one and the other to the other.

[^I.4:3]: the base.
    Here we have the word <em>base</em> used for the first time in the <title>Elements</title>. Proclus explains it (<xref n="Proc. p. 236, 12-15" from="ROOT" to="DITTO">p. 236, 12-15</xref>) as meaning (1), when no side of a triangle has been mentioned before, the side <quote>which is on a level with the sight</quote> (<foreign lang="greek">τὴν πρὸς τῇ ὄψει κειμένην</foreign>), and (2), when two sides have already been mentioned, the third side. Proclus thus avoids the mistake made by some modern editors who explain the term exclusively with reference to the case where two sides have been mentioned before. That this is an error is proved (1) by the occurrence of the term in the enunciations of <a href="/elem.1.37">I. 37</a> etc. about triangles on the same base and equal bases, (2) by the application of the same term to the bases of parallelograms in <a href="/elem.1.35">I. 35</a> etc. The truth is that the use of the term must have been suggested by the practice of drawing the particular side horizontally, as it were, and the rest of the figure above it. The <em>base</em> of a figure was therefore spoken of, primarily, in the same sense as the base of anything <pb n="249"/>else, e.g. of a pedestal or column; but when, as in <a href="/elem.1.5">I. 5</a>, two triangles were compared occupying other than the normal positions which gave rise to the name, and when two sides had been previously mentioned, the base was, as Proclus says, necessarily the third side.

[^I.4:4]: subtend.
    <foreign lang="greek">ὑποτείνειν ὑπό</foreign>, <quote>to stretch under,</quote>
with accusative.

[^I.4:5]: the angle BAC.
    The full Greek expression would be <foreign lang="greek">ἡ ὑπὸ τῶν ΒΑ, ΑΓ περιεχομένη γωνία</foreign>, <quote>the angle contained by the (straight lines) `BA`, `AC`.</quote>
But it was a common practice of Greek geometers, e.g. of Archimedes and Apollonius (and Euclid too in Books X.—XIII.), to use the abbreviation <foreign lang="greek">αἱ ΒΑΓ</foreign> for <foreign lang="greek">αἱ ΒΑ, ΑΓ</foreign>, <quote>the (straight lines) `BA`, `AC`.</quote>
Thus, on <foreign lang="greek">περιεχομένη</foreign> being dropped, the expression would become first <foreign lang="greek">ἡ ὑπὸ τῶν ΒΑΓ γωνία</foreign>, then <foreign lang="greek">ἡ ὑπὸ ΒΑΓ γωνία</foreign>, and finally <foreign lang="greek">ἡ ὑπὸ ΒΑΓ</foreign>, without <foreign lang="greek">γωνία</foreign>, as we regularly find it in Euclid.

[^I.4:6]: if the triangle be applied to...coincide.
    The difference between the technical use of the passive <foreign lang="greek">ἐφαρμόζεσθαι</foreign> <quote>to be <em>applied</em> (to),</quote> and of the active <foreign lang="greek">ἐφαρμόζειν</foreign> <quote>to <em>coincide</em> (with)</quote>
has been noticed above (note on <title>Common Notion</title> 4, pp. 224-5).

[^I.4:7]: [For if, when B coincides...36. coincide with EF].
    Heiberg (<title>Paralipomena su Euklid</title> in <title>Hermes</title>, XXXVIII., 1903, p. 56) has pointed out, as a conclusive reason for regarding these words as an early interpolation, that the text of an-Nairīzī (<title>Codex Leidensis</title> 399, 1, ed. Besthorn-Heiberg, p. 55) does not give the words in this place but after the conclusion Q.E.D., which shows that they constitute a <em>scholium</em> only. They were doubtless added by some commentator who thought it necessary to explain the immediate inference that, since `B` coincides with `E` and `C` with `F`, the straight line `BC` coincides with the straight line `EF`, an inference which really follows from the definition of a straight line and <a href="/elem.1.post.1">Post. 1</a>; and no doubt the Postulate that <quote>Two straight lines cannot enclose a space</quote> (afterwards placed among the <title>Common Notions</title>) was interpolated at the same time.
[^I.4:8]: Therefore etc.
    Where (as here) Euclid's <em>conclusion</em> merely repeats the enunciation word for word, I shall avoid the repetition and write <quote>Therefore etc.</quote>
simply.

