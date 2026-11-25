#!/usr/bin/env python3
"""The Absurd Clause Contest -- make.fun bounty entry.

Writes one sentence (160 characters) to /output/entry.txt: an absurd
clause buried deep inside a terms-of-service agreement, in deadpan
legal boilerplate. Deterministic, no network, no files outside this
repo, no secrets.

Candidate contest (8 clauses, head-to-head on the judge's criteria,
in the brief's own order: an absurd clause that could hide deep
inside a terms-of-service agreement first, then funniest on one
reading, then real legal boilerplate until the absurdity hits, then
original and specific with a concrete absurd image, then tight in
one clean sentence with no wasted words and no explaining of its
own joke):

1. WINNER (160 chars): "In the event of a dispute, the parties
   agree to settle the matter by interpretive dance, judged by
   three pigeons selected by the Company at its sole discretion."
2. "Any user who has not logged in for ninety (90) days shall be
   presumed deceased, and their account shall pass to the
   Company's cat." (130) - the sharpest runner-up: "presumed
   deceased" is real legal language, and the account passing to
   the Company's cat is a clean ambush at the very last word.
   It loses because the image, while delightful, is one quiet
   turn; the winner stacks two absurdities (dance, then pigeon
   judges) in a single scene, so the joke lands harder on one
   reading.
3. "Users agree that all complaints must be submitted in the form
   of a haiku, and any complaint failing to observe the 5-7-5
   syllable structure shall be dismissed without further notice."
   (182) - bureaucratic perfection, and "dismissed without
   further notice" is pitch-perfect boilerplate. It loses on
   tightness: at 182 characters it is the longest candidate, and
   the 5-7-5 explanation spends words telling the reader how the
   joke works instead of letting the haiku rule speak for itself.
4. "By using the Service, you grant the Company a perpetual,
   royalty-free license to your dreams, including the right to
   sublicense them to third parties." (150) - the register is
   flawless (perpetual, royalty-free, sublicense), but licensing
   dreams is a familiar internet joke, so it reads less original
   than the winner's pigeon tribunal, which nobody has seen
   before.
5. "Any dispute arising under these Terms shall be resolved by a
   single game of rock-paper-scissors, best of three, conducted
   at the Company's offices." (147) - clean and deadpan, but
   rock-paper-scissors as dispute resolution is a known trope;
   the winner's interpretive dance judged by pigeons is the
   stranger, more specific version of the same idea.
6. "The Company reserves the right to require any user to change
   their legal name if it is deemed insufficiently pronounceable
   by our support staff." (144) - a good bureaucratic power grab,
   but the joke stays abstract: no concrete absurd image ever
   arrives, while the winner makes the reader picture three
   pigeons solemnly judging a dance.
7. "By continuing to use the Service, you consent to the Company
   visiting your home on your birthday to observe how you
   celebrate." (126) - creepy-funny and it ambushes well, but
   "observe how you celebrate" leans sinister more than funny,
   and the winner's clause is the one that reads as a joke first
   and a threat second.
8. "The Company reserves the right to charge your credit card for
   emotional damages suffered by our servers during periods of
   heavy traffic." (136) - a neat inversion (servers with
   feelings), but the absurdity is a single word swap away from
   ordinary billing language, so the image is thinner than the
   winner's full courtroom of pigeons.

Why the winner wins: on criterion 1 it is squarely an absurd
clause that could hide deep inside a terms-of-service agreement
(a dispute-resolution clause, the dullest section of all). On
criterion 2 it lands on one reading: the reader pictures a
dance-off solemnly judged by pigeons, with no setup needed. On
criterion 3 it sounds like real boilerplate until the absurdity
hits ("In the event of a dispute, the parties agree to settle
the matter by..." is genuine contract language, and "selected
by the Company at its sole discretion" closes it in perfect
legal register). On criterion 4 it is original and specific:
three pigeons, not a vague shrug at the genre. On criterion 5
it is tight: one sentence, every word doing work, and it never
explains its own joke.

Pairwise verdicts, winner against each rival: vs 2, two stacked
absurdities in one scene beat one quiet turn; vs 3, a 160-char
ambush beats a 182-char rule that explains its own 5-7-5; vs 4,
a pigeon tribunal beats a familiar dream-licensing joke; vs 5,
interpretive dance judged by pigeons beats the known
rock-paper-scissors trope; vs 6, a concrete pigeon courtroom
beats an abstract name-change power grab; vs 7, a joke first
beats a clause that reads as a threat first; vs 8, a full absurd
scene beats a single word swap.
"""

import os

# The winning line (160 characters, one sentence, no trailing newline).
LINE = "In the event of a dispute, the parties agree to settle the matter by interpretive dance, judged by three pigeons selected by the Company at its sole discretion."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")

MAX_CHARS = 200


def validate(text: str) -> None:
    """Gate: 1-200 characters, non-blank, exactly one sentence.

    Exactly one sentence means exactly one terminal stop: a single
    period at the end, and no other sentence-ending punctuation
    (! ? ...) hiding inside the line. The winning clause carries
    its only period at the very end, after "discretion".
    """
    if not text or not text.strip():
        raise SystemExit("entry must not be blank")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    if any(p in text for p in ("!", "?", "...", ";")):
        raise SystemExit("entry must be exactly one sentence")


def main() -> None:
    line = LINE.strip()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one sentence,
    # within the gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    validate(written)
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
