---
title:  Proposition I.11
subtitle: construct a perpendicular from a point on a line
author:
routes:
aliases:
  - /elem.1.11
  - /I.11
taxonomy:
    tag:
    category:
      - construction
      - perpendicular
mermaid: true
---

To draw a straight line at right angles to a given straight line from a given point on it.

===

Let `AB` be the given straight line, and `C` the given point on it. 

Thus it is required to draw from the point `C` a straight line at right angles to the straight line `AB`.

Let a point `D` be taken at random on `AC`; [^I.11:1] let `CE` be made equal to `CD`; [I.3] on `DE` let the equilateral triangle `FDE` be constructed, [I.1] and let `FC` be joined; 

I say that the straight line `FC` has been drawn at right angles to the given straight line `AB` from `C` the given point on it.

For, since `DC` is equal to `CE`, and `CF` is common, 

- the two sides `DC`, `CF` are equal to the two sides `EC`, `CF` respectively;

and the base `DF` is equal to the base `FE`; 

- therefore the angle `DCF` is equal to the angle `ECF`; [I.8]

 and they are adjacent angles.

But, when a straight line set up on a straight line makes the adjacent angles equal to one another, each of the equal angles is right; [I.def.10] 

- therefore each of the angles `DCF`, `FCE` is right.

Therefore the straight line `CF` has been drawn at right angles to the given straight line `AB` from the given point `C` on it.

- Q. E. F.

## References

[I.def.10]: /elem.1.def.10 "Book I - Definition 10"
[I.1]: /elem.1.1 "Book I - Proposition 1"
[I.3]: /elem.1.3 "Book I - Proposition 3"
[I.8]: /elem.1.8 "Book I - Proposition 8"


[mermaid]
graph BT

I_11[ I.11 ]:::prop; 
click I_11 "/elem.1.11" "Book I Proposition 11";

%%%% dependencies

I_def10[ I.def.10 ]:::def;
click I_def10 "/elem.1.def.10" "Book I Definition 10";

I_1[ I.1 ]:::prop; 
click I_1 "/elem.1.1" "Book I Proposition 1";

I_3[ I.3 ]:::prop; 
click I_3 "/elem.1.3" "Book I Proposition 3";

I_8[ I.8 ]:::def; 
click I_8 "/elem.1.8" "Book I Proposition 8";

%%%% links

I_11 --> I_def10
I_11 --> I_1
I_11 --> I_3
I_11 --> I_8


%%%% I_3 dependencies

I_2[ I.2 ]:::prop;
click I_2 "/elem.1.2" "Book I Proposition 2";

I_post3[ I.ax.3 ]:::post;
click I_post3 "/elem.1.post.3" "Book I Postulate 3";

I_def15[ I.def.15 ]:::def;
click I_def15 "/elem.1.def.15" "Book I Definition 15";

I_cn1[ I.cn.1 ]:::cn;
click I_cn1 "/elem.1.c.n.1" "Book I Common Notion 1";

%%%% links

I_3 --> I_2
I_3 --> I_post3
I_3 --> I_def15
I_3 --> I_cn1

%%%% dependencies

I_1[ I.1 ]:::prop; 
click I_1 "/elem.1.1" "Book I Proposition 1";

I_post1[ 1.post.1 ]:::post;
click I_post1 "/elem.1.post.1" "Book I Postulate 1";

I_post2[ 1.post.2 ]:::post;
click I_post2 "/elem.1.post.2" "Book I Postulate 2";

I_post3[ 1.post.3 ]:::post;
click I_post3 "/elem.1.post.3" "Book I Postulate 3";

I_def15[ 1.def.15 ]:::def;
click I_def15 "/elem.1.def.15" "Book I Definition 15";

%%%% links

I_2 --> I_1
I_2 --> I_post1
I_2 --> I_post2
I_2 --> I_post3
I_2 --> I_def15

[/mermaid]

## Footnotes 

[^I.11:1]: let CE be made equal to CD.
    The verb is <foreign lang="greek">κείσθω</foreign> which, as well as the other parts of <foreign lang="greek">κεῖμαι</foreign>, is constantly used for the passive of <foreign lang="greek">τίθημι</foreign> <quote>to <em>place</em></quote> ; and the latter word is constantly used in the sense of <em>making</em>, e.g., one straight line equal to another straight line.

