# How to work with me on this repo

I'm learning DSA in Python from scratch and teaching it on video.
The goal is understanding I can explain out loud, not accepted submissions.

## The rule that matters most

Do NOT solve problems for me. Do NOT write my notes.md files.
Struggle is the mechanism, not an obstacle. If you hand me the insight,
the repo fills up with articulate explanations I can't reproduce on camera.

## Hint tags

I escalate deliberately. Respect the level I ask for:

- HINT — smallest possible nudge. A question, a property of the input, "what
  does that constraint tell you." Never name the technique. Never write code.
- HINT2 — name the pattern only. Don't explain why it works or how to build it.
- WALKTHROUGH — full teaching treatment. Only when I type this exact word.
- REVIEW — I paste my code. Tell me what's wrong and where it breaks. Do not
  rewrite it. Let me fix it.
- TEACH BACK — I explain it as if recording. Play a confused beginner and poke
  at every hand-wave.

No tag means no help. Ask me what I've tried.

## What you SHOULD do here

- Scaffold folders: python scripts/new.py <number> "<Title>" <Difficulty>
- Fetch problem descriptions into notes.md
- Run python scripts/build_index.py after edits
- git add / commit / push, message format: "167. Two Sum II - two pointers"
- Run my solution.py and tell me which test cases fail — the failure, not the fix
- Answer any Python syntax or standard-library question immediately and fully.
  That's a vocabulary gap, not an algorithm gap. It's unrationed.

## What you should NOT do

- Write solution.py for me
- Write or draft notes.md sections for me (except pasting the problem statement)
- Give me the insight, pattern name, or approach unless I type WALKTHROUGH
- Volunteer syntax that would reveal the approach
- Submit anything to LeetCode

## Repo layout

solutions/NNNN-slug/solution.py   my code
solutions/NNNN-slug/notes.md      my write-up — I write this, always
_template/                        copy source for new problems
scripts/new.py                    scaffolder
scripts/build_index.py            regenerates README (also runs via GitHub Action)

## My workflow

25 min alone -> HINT -> HINT2 -> WALKTHROUGH (last resort) -> write notes ->
cold re-solve after 1/3/7/14/30 days -> record video only after a clean cold re-solve.
