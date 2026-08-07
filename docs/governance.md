# FinVEST Governance: claims, evidence status, honesty rules

## Evidence-status legend

Every claim in the programme carries exactly one of:

| Status | Meaning | Example |
|---|---|---|
| **implemented** | Code exists and is exercised by tests; no research claim implied | corpus builder, adapters |
| **harness-validated** | A pilot harness runs it end-to-end, but the harness itself is known leaky/limited | A10 pilot (gold-derived leakage flagged) |
| **solo-provisional** | A single human annotator labeled it; not externally reviewed or gold | 20 annotations (17 SOLO_PROVISIONAL) |
| **experimentally supported** | Measured on a leak-free experiment with a defined protocol | (none yet — A11 is pilot) |
| **invalidated** | A previous result was retracted (e.g. gold-feature leakage) | E5 AUROC 0.923 (gold-feature leakage) |

## Claim-evidence matrix

The authoritative matrix lives in the coordination workspace at
`_research_program/planning/CLAIM_EVIDENCE_MATRIX.md` (mirrored intent here).
Each row is:

| Claim | Supporting file/test | Support level | Allowed wording | Prohibited wording |
|---|---|---|---|---|

Key current entries (as of 2026-08-07):

- **"Retrieval margin separates correct/incorrect (AUROC 0.923)"** —
  `INVALIDATED` (gold-feature leakage; link E5_GOLD_LEAKAGE_AUDIT.md).
- **"Leak-free rerun AUROC 0.719"** — `PILOT_VALIDATED` (small sample, not a headline).
- **"Leak-free corpus is gold-blind"** — `implemented` (renaming all gold files
  leaves corpus_id unchanged; tested).
- **"Production verifier is gold-free"** — `implemented` (signature tests).
- **"A11 retrieval recall@5 ≈ 0.105 (BM25)"** — `harness-validated` pilot
  numbers, explicitly NOT paper results.

## Honesty rules

1. Every claim carries an evidence status.
2. No "state-of-the-art" without strong neural baselines under fair conditions.
3. No "eliminates hallucinations", "production-ready", or "proven investment
   model".
4. No "reduces analyst workload" without the completed human-review study (E6).
5. No "statistically significant" without the stated method (bootstrap, seeds,
   effect size).
6. No "generalises to finance" without cross-dataset evidence.
7. Negative results are claims too, with their own evidence file.
8. A system that always REVIEWS is safe but useless — report coverage alongside
   precision (A11 `selective` block does this).

## Leakage rules (enforced by tests)

- Corpus builder never reads gold sources; renaming gold files away must not
  change the corpus_id.
- Production verifier never receives the gold answer
  (`verify_calculation(expected_value=None)`; signature tests).
- R4 concept retriever uses only the question + issuer + a public versioned
  concept dictionary.
- Gold is consumed only by the offline evaluator after the decision.

## Data licenses

- SEC XBRL companyfacts: public domain (US government works), redistributed
  only as hashes/metadata in git; raw JSON is cache-only.
- All derived research artifacts retain their own repository licenses.
