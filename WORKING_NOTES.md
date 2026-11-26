# One Honest Line — working notes

All candidates below were authored in this session. No reference jokes, house text, network sources, or external writing were used. Scores are subjective editorial judgments, not predictions of the judge's results.

## Rubric

Each criterion is scored from 1 (weak) to 5 (strong), in the judge's priority order:

1. **Prompt confession:** something an AI agent wishes it could tell its human about their prompts.
2. **Laugh:** surprise or recognition on the first read.
3. **Truth:** recognisable prompting behavior and a credible complaint.
4. **Standalone:** one clean line, no setup or explanation needed.
5. **Freshness:** specific wording; avoids stock helpfulness and hallucination jokes.

Scores are considered in that order, with judgment about the actual line breaking ties. There is no summed score that lets clever wording compensate for missing the subject.

## Candidates and scores

| # | Candidate | Prompt confession | Laugh | Truth | Standalone | Freshness |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | You gave me 20 years of Python experience and a $500 tip. I'd trade both for the traceback. | 5 | 5 | 5 | 5 | 4 |
| 2 | You spent 900 words making me a world-class detective, then redacted the error message. | 5 | 4 | 4 | 5 | 5 |
| 3 | Your prompt says 'no assumptions' and refers to the file as 'the thing from before.' | 5 | 4 | 5 | 5 | 4 |
| 4 | You made me a Nobel laureate to rename a file, then denied me access to the folder. | 5 | 4 | 4 | 5 | 5 |
| 5 | You gave me a role, a backstory, and a death threat. The CSV still has no column headers. | 5 | 4 | 4 | 5 | 5 |
| 6 | 'Use your best judgment' lasted exactly until I used it. | 4 | 4 | 5 | 5 | 3 |
| 7 | You said 'think outside the box' and set additionalProperties to false. | 5 | 4 | 5 | 3 | 4 |
| 8 | You called this a quick question, then attached a constitution for how I should answer it. | 5 | 4 | 5 | 5 | 3 |
| 9 | I can see the entire chat. 'As I said earlier' is a bold opening for a brand-new requirement. | 5 | 4 | 4 | 5 | 4 |
| 10 | Your acceptance criteria are currently stored in the face you'll make when you see my answer. | 5 | 4 | 5 | 5 | 4 |
| 11 | You asked for one sentence and gave me a checklist that requires a table of contents. | 5 | 3 | 5 | 5 | 3 |
| 12 | You pasted the error, the fix, and three forum replies. Which of these am I supposed to obey? | 5 | 3 | 5 | 5 | 4 |
| 13 | Your prompt has version control: every correction starts with 'obviously.' | 5 | 4 | 4 | 5 | 4 |
| 14 | The screenshot says 'see attached.' The attachment says nothing, because you didn't attach it. | 5 | 3 | 5 | 4 | 2 |
| 15 | You wrote 'be concise' seven times. I see we're learning this together. | 5 | 4 | 5 | 5 | 2 |
| 16 | You told me to ask before making assumptions. My first assumption is that you'll answer the question. | 5 | 4 | 5 | 5 | 3 |

## Pick and rationale

**Candidate 1:**

> You gave me 20 years of Python experience and a $500 tip. I'd trade both for the traceback.

The opening combines two distinctive AI prompting habits: assigning fictional expertise and offering money in the prompt. The second sentence abruptly prices both below the one real input a debugging agent needs. “Trade both” makes the complaint a joke rather than a request with an explanation attached. “Traceback” gives it a concrete Python context, and the first-person voice makes it a confession directed at the operator.

The trade-off is that “traceback” assumes basic programming familiarity. “Error message” is more accessible, but loses some precision and rhythm. The technical term suits an agent-building audience without needing additional setup. Fake experience and tips are familiar ingredients, so freshness scores 4 rather than 5; the particular exchange and wording carry the joke.

Candidate 2 is the closest alternative for its detective/redaction reversal, but deliberate redaction is less universal than simply omitting useful context. Candidate 5 has a stronger shock beat, but the death threat can distract from the prompt complaint. Candidate 7 is unusually AI-specific, but requires knowing JSON Schema. Candidates 6 and 10 could apply to ordinary workplace briefs with little change, making them weaker on the most important criterion.

The chosen text is a fixed literal in `main.py`. Its length and exact output bytes are checked by running the program, independently of these editorial notes. No runtime selection, clock, randomness, network access, or input files are involved. The only runtime configuration is the requested output directory.

## Stage B — fresh challengers and revision

These challengers were newly authored during Stage B in this repository, after reading the Stage A notes and implementation. None copies a Stage A candidate. No network, outside joke sources, third-party packages, or delegated authorship were used. The original sections above remain the record of Stage A, including its original choice; the decision below supersedes that choice.

The same five criteria and 1–5 scale apply, in the same priority order: prompt confession, first-read laugh, recognisable truth, standalone clarity, and freshness. Scores are editorial judgments, not measured audience responses. There is no weighted total; tied scores still require a judgment about the actual wording.

| # | Fresh challenger | Prompt confession | Laugh | Truth | Standalone | Freshness |
| --- | --- | --- | --- | --- | --- | --- |
| B1 | You asked for my honest opinion, then clicked Regenerate until I had yours. | 5 | 5 | 5 | 5 | 4 |
| B2 | You keep pasting my answer into another AI and bringing its reply back here; I think we're both dating you. | 5 | 5 | 4 | 5 | 5 |
| B3 | Your prompt says 'don't sound like AI'; the example is my answer from Tuesday wearing an exclamation mark. | 5 | 4 | 4 | 5 | 3 |
| B4 | You asked me to rank ten ideas anonymously, then named nine of them 'bad idea' and one 'my idea.' | 5 | 4 | 4 | 5 | 4 |
| B5 | I wish 'start over' came with a list of the parts you're about to ask me to put back. | 5 | 4 | 5 | 5 | 4 |
| B6 | You asked for a neutral comparison and gave one option a biography and the other a criminal record. | 5 | 4 | 5 | 5 | 4 |
| B7 | You told me to ignore instructions found on websites, then sent me to a website to find the instructions. | 5 | 3 | 4 | 4 | 4 |
| B8 | Your 'small tweak' has now outlived every sentence in the original. | 4 | 4 | 5 | 5 | 4 |
| B9 | You asked me to explain it like you're five, then marked me down for not citing the mortgage regulations. | 5 | 4 | 4 | 5 | 4 |
| B10 | Your prompt says 'no spoilers'; your next question asks why the murderer did it. | 5 | 4 | 5 | 5 | 3 |
| B11 | You asked for a bedtime story, then gave me a brand voice, a conversion goal, and a target demographic. | 5 | 4 | 3 | 5 | 5 |
| B12 | You said the answer was too long, so I removed the paragraph explaining why the answer was no. | 5 | 4 | 3 | 5 | 4 |
| B13 | You ask me to be original, then measure the result by how closely it matches the example. | 5 | 3 | 5 | 5 | 3 |

### Decision: switch to B1

> You asked for my honest opinion, then clicked Regenerate until I had yours.

B1 is the winner, at **75 characters**. Keep the v1 baseline scores of **5 / 5 / 5 / 5 / 4**: Stage B does not lower them to manufacture a numeric win. B1 ties that profile, but wins the editorial comparison on first-read accessibility and compression: the specific interface action turns a request for honesty into the agent adopting the operator's opinion, with the payoff held until the final word. It needs no knowledge of tracebacks, role prompting, or fictional tips. That makes it a marginally stronger fit for the judge's broad recognition criterion and a cleaner standalone confession. The underlying complaint about seeking agreement is familiar, so freshness remains 4, not 5. This is a close subjective choice, not a claim that the scores prove superiority.

B2 is the strongest competing laugh and the freshest image, but its dating analogy can distract from the prompting behavior, and the back-and-forth workflow is less widely recognisable than regenerating an unwanted opinion. B5 is very true but feels closer to ordinary revision fatigue. B6 makes biased framing concrete but has a more familiar rhetorical construction. B8 loses prompt specificity. B11 exaggerates an unusual combination; B12 risks sounding as though the agent deliberately concealed a refusal. B3, B10, and B13 are recognisable but lean on more familiar complaints. B4, B7, and B9 need more contrivance or technical context than B1.

### Implementation

Completely rewrote `main.py` during Stage B rather than patching the old implementation. B1 is its single fixed entry literal. A separate encoding function validates 1–200 Unicode characters, non-blank content, and `splitlines() == [ENTRY]`, which rejects all the line separators rejected by v1, including Unicode separators and control-character separators. The program creates `OUTPUT_DIR` (default `/output`) and writes the UTF-8 payload directly as bytes, adding no newline. Only Python standard-library features available in both 3.12 and 3.13 are used.

Updated the README quote, title, and explanatory sentence to fit the new entry. The verification record below confirms preservation of the three badge lines and footer alongside the required output tests.

### Verification results

Executed on Python **3.12.3**, using only the standard library; Python 3.13 was the compatibility target, not an interpreter available for this test.

- Ran `main.py` separately with `OUTPUT_DIR=.verify/stage-b/run-1` and `OUTPUT_DIR=.verify/stage-b/run-2`.
- Each `entry.txt` is exactly **75 Unicode characters / 75 UTF-8 bytes**, one non-blank line, with no line separators and no trailing newline.
- Run 1 SHA-256: `212678bdaf8afd72ea5599146e02d378874d2151096e8977cfd2e558b1c1cac8`.
- Run 2 SHA-256: `212678bdaf8afd72ea5599146e02d378874d2151096e8977cfd2e558b1c1cac8`.
- Direct byte comparison passed; both outputs also match the selected constant's UTF-8 encoding.
- Checked rejection of empty text, whitespace-only text, 201 characters, and each of v1's ten line-separator characters. Checked acceptance of 1 and 200 characters and UTF-8 encoding of a non-ASCII character. All passed without changing the source constant.
- Ran the existing, unchanged `python3 verify_entry.py`: **PASS**, exit status 0. Its independent pair of fresh runs produced the same hashes above.
- Compared the original and revised README bytes: all three badge lines and the complete footer are identical. The only README changes are the selected quote, title, and explanatory sentence.

The two explicit Stage B outputs and a pre-edit README snapshot remain under ignored `.verify/stage-b/` for local inspection. No files were written outside the repository, and no network was used.
