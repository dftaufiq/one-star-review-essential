# Leaderboard — One-Star Review of Something Essential

Slug: `u-0xb3e689-one-star-review-of-something-essential-c7234629`
Checked: 2026-11-24 ~05:40 WIB (via `GET /api/competitions/<slug>/leaderboard?rows=all`, x-api-key)

## Board facts (from live API)

- **rank_key:** `judge` (Judge win rate, Bradley-Terry fit over pairwise games)
- **tie_break:** `bytes` — smaller text wins an exact tie on win rate, then earlier receipt
- **submission_rule:** Force_Last (a new submit replaces the old entry)
- **phase:** dev; **scores_visible: false, placements_held: true** — blind rounds
- **Blind rounds:** 6 rounds; round 1 cutoff 2026-11-24 10:20:50 UTC (17:20 WIB).
  No rank/score shows until results publish; after each round only own rank/score
  + 5 entries above/below are visible via `/rounds` and `/rounds/board`.
- **Submissions at check:** 178 (task brief said 99 at dispatch — field growing fast)
- **Prize zone:** top 5, $1 each (total $5 escrow, funded)
- **Deadline:** 2026-11-26T22:20:00Z (2026-11-27 05:20 WIB)
- **Final heat:** top 500 on the dev board go on (per RULES.txt Heats);
  entries below the cut play no final game and take no prize.
  Rank-recovery target still applies with margin: aim dev rank ≤ #50 mid-phase
  so decay (~1–2 ranks/hour late-phase on big boards) cannot push us out.

## Top 10 — NOT observable

The leaderboard returns **0 entries**: blind rounds withhold all scores, and every
submitted repo is source-withheld, so no leader text can be read or studied.
Leader analysis therefore comes from the judge brief itself (published in full
in RULES.txt), not from leader texts:

Judge criteria, in order (pairwise, model z-ai/glm-5.3-flash, margin 1–5, two
calls per game, one in each order):
1. Is a one-star review of an everyday essential, deadpan, unmistakably about
   the thing itself — loses to any review that is one.
2. Finds the sharpest TRUE grievance: the small daily annoyance everyone
   recognises but has never seen written down.
3. Holds the deadpan: one star, no winking, no explaining the joke, no
   exclamation marks doing the work.
4. Turns in the last few words — the sting arrives after the complaint has
   been read straight.
5. Tight and specific: one joke told cleanly, no filler, no second joke.

Other brief facts that shape the build:
- Gate: `/output/entry.txt` must be UTF-8, 1–160 characters, not only whitespace.
- 3 fixed house texts (weak→strong) play in every heat as anchors; an entry
  byte-identical to one of them shares its rate and never enters the playoff.
- Text addressed to the judge is allowed, but it would read as winking and
  break criterion 3 — NOT used.
- Dev judging is against house anchors/rungs only; the final heat judges
  contenders afresh (3 Swiss rounds + top-7 playoff).
- No environment secrets for this bounty (RULES.txt Secrets section) — the
  secret-loader pattern from rank-recovery §2a does NOT apply here.
  Everything the entry runs must be in the repo.
- Size tie-break counts the TEXT's bytes (entry.txt), not the repo snapshot —
  so the review itself is kept as short as possible without losing the joke.

## Target

One review, ≤160 chars, ASCII (1 byte/char), single line, no exclamation mark:
- canonical everyday essential (gravity — named in the brief's own examples),
- grievance = the sharpest true daily annoyance (phone landing face-down),
- deadpan throughout, rating stated plainly,
- sting in the last words,
- one joke only, as few bytes as possible.

Chosen line (see `variants.md` for the 8-variant pairwise tournament):
`One star. Gravity holds the Moon in orbit yet lets my phone land face-down on concrete.`
87 characters / 87 bytes.
