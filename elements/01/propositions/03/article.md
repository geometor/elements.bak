---
title:  Proposition I.3
subtitle: Construct equal segments by section
author:
routes:
  aliases:
    - /elem.1.3
    - /I.3
taxonomy:
  tag:
    - proposition
  category:
    - construction
    - lines
mermaid: true
---

Given two unequal straight lines, to cut off from the greater a straight line equal to the less.


===

Let `AB`, `C` be the-two given unequal straight lines, and let `AB` be the greater of them.

Thus it is required to cut off from `AB` the greater a straight line equal to `C` the less.

At the point `A` let `AD` be placed equal to the straight line `C`; [I.2] and with centre `A` and distance `AD` let the circle `DEF` be described. [I.post.3] 

Now, since the point `A` is the centre of the circle `DEF`, `AE` is equal to `AD`. [I.def.15] But `C` is also equal to `AD`. 
- Therefore each of the straight lines `AE`, `C` is equal to `AD`; so that `AE` is also equal to `C`. [I.c.n.1]

Therefore, given the two straight lines `AB`, `C`, from `AB` the greater `AE` has been cut off equal to `C` the less.

- (Being) what it was required to do.


[I.def.15]: /elem.1.def.15 "Book I - Definition 15"
[I.2]: /elem.1.2 "Book I - Proposition 2"
[I.post.3]: /elem.1.post.3 "Book I - Postulate 3"
[I.c.n.1]: /elem.1.c.n.1 "Book I - Common Notion 1"


[references]
graph BT

I_3[ I.3 ]:::prop;
click I_3 "/elem.1.3" "Book I Proposition 3";

%%%% dependencies

I_2[ I.2 ]:::prop;
click I_2 "/elem.1.2" "Book I Proposition 2";

I_post3( I.ax.3 ):::post;
click I_post3 "/elem.1.post.3" "Book I Postulate 3";

I_def15( I.def.15 ):::def;
click I_def15 "/elem.1.def.15" "Book I Definition 15";

I_cn1( I.cn.1 ):::cn;
click I_cn1 "/elem.1.c.n.1" "Book I Common Notion 1";

%%%% links

I_3 --> I_2
I_3 --> I_post3
I_3 --> I_def15
I_3 --> I_cn1

%%%% I_2 dependencies

I_1[ I.1 ]:::prop; 
click I_1 "/elem.1.1" "Book I Proposition 1";

I_post1( I.post.1 ):::post;
click I_post1 "/elem.1.post.1" "Book I Postulate 1";

I_post2( I.post.2 ):::post;
click I_post2 "/elem.1.post.2" "Book I Postulate 2";

I_post3( I.post.3 ):::post;
click I_post3 "/elem.1.post.3" "Book I Postulate 3";

I_def15( I.def.15 ):::def;
click I_def15 "/elem.1.def.15" "Book I Definition 15";

%%%% I_2 links

I_2 --> I_1
I_2 --> I_post1
I_2 --> I_post2
I_2 --> I_post3
I_2 --> I_def15

%%%% I_1 dependencies

I_post1( I.post.1 ):::post;
click I_post1 "/elem.1.post.1" "Book I Postulate 1";

I_post3( I.post.3 ):::post
click I_post3 "/elem.1.post.3" "Book I Postulate 3";

I_def15( I.def.15 ):::def
click I_def15 "/elem.1.def.15" "Book I Definition 15";

I_cn1( I.c.n.1 ):::cn
click I_cn1 "/elem.1.c.n.1" "Book I Common Notion 1";

%%%% I_1 links

I_1 --> I_post1
I_1 --> I_post3
I_1 --> I_def15
I_1 --> I_cn1
[/references]
