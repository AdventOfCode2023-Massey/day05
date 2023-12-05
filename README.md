# Advent of Code 2023: Day 5
GitHub Copilot and Bart Massey

---

Part 1 took a tedious one-hour walk with Copilot. The cycle
at that point essentially involved debugging Copilot's code,
feeding the bug hints back to it, and looking at the
"corrected" output. it was not fun.

The moment when it was discovered that `input.txt` maps were
too large to materialize was predictably devastating. (I
*hate hate hate* the misleading example trick.) Fortunately,
Copilot adapted to this performance fix reasonably quickly
and well.

Part 2, where the seeds were also too many to materialize,
broke both Copilot and I. There's fancy interval arithmetic
to be done here; I would guess two hours minimum for me to
hand-code this, given Copilot's nice input parser.

I think the fun has stopped.

---

Solution to [this problem](https://adventofcode.com/2023/day/5).

Save your problem input to `input.txt` and run as appropriate.

---

This program is licensed under the "MIT License".
Please see the file LICENSE in this distribution
for license terms.
