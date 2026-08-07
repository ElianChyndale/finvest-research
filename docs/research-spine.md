# The FinVEST Research Spine

The spine is the evidence chain that connects raw public data to a public
claim. Each link has a **leakage boundary** and a **governance rule**.

## The chain

```
1. DATA SOURCES            SEC companyfacts (6 issuers, 170k facts) + full 10-K
2. CORPUS                  leak-free corpus, frozen (CORPUS_MANIFEST.json)
3. CASES                   sealed cases: question + evidence identity + gold (frozen)
4. ANNOTATION              solo-provisional human labels, append-only, frozen SHEP
5. RETRIEVAL               R1 BM25 / R2 dense / R3 RRF / R4 concept-temporal
6. SET SELECTION           S1 top-k / S2 greedy / S3 beam / S4 oracle
7. VERIFICATION            V1 temporal / V2 numerical / V3 joint (gold-free)
8. DECISION                ANSWER / REVIEW / ABSTAIN
9. EXPERIMENT RECORD       a11_two_stage.json (+ repro-lab manifests)
10. PUBLIC CLAIM           claim-evidence matrix entry with evidence status
```

## Leakage boundaries (each is tested)

| Link | Boundary | How it is enforced |
|---|---|---|
| Corpus | Corpus must not depend on gold | Builder reads only companyfacts + SOURCE_MANIFEST; test renames ALL gold files away → corpus_id unchanged |
| Retrieval | Retrievers must not read gold concepts | R4 uses only question + issuer + a public versioned concept dictionary |
| Verification | Production verifier must not receive gold | `verify_calculation(expected_value=None)`; test asserts the verifier signature has no gold/expected params |
| Evaluation | Gold touches only the offline evaluator | `evaluate_correctness` runs AFTER the decision; `gold_used: true` only there |
| Claims | Public statements must be honest | Evidence-status legend + claim-evidence matrix in docs/governance.md |

## The honest-status legend

| Status | Meaning |
|---|---|
| implemented | Code exists, exercised by tests; no research claim implied |
| harness-validated | A pilot harness runs it end-to-end, but the harness is known leaky/limited |
| solo-provisional | Single human annotator labeled it; not externally reviewed or gold |
| experimentally supported | Measured on a leak-free experiment with a defined protocol |
| invalidated | A previous result was retracted (e.g. gold-feature leakage) |

## What is true today (2026-08-07)

- Leak-free corpus: 170,229 facts, 6 issuers, 0 gold tokens in records.
- 20 solo annotations; 60 frozen evidence packages (full-package SHA-256).
- A11 two-stage run: R1 recall@5 ≈ 0.105 / R2 ≈ 0.079 / R3 ≈ 0.105 /
  R4 ≈ 0.053; decisions 0 ANSWER / 18 REVIEW / 1 ABSTAIN; unsafe_answer_rate 0.0.
- These are honest pilot numbers: low recall is a real finding (the full
  CompanyFacts space is a hard retrieval environment; query→XBRL alignment is
  weak), NOT a paper result.

## Reproduction (quick)

From `submodules/ecoquant/`:

```bash
python experiments/a11_retrieval/run.py --top-k 20    # two-stage experiment
python scripts/build_leak_free_corpus.py               # freeze the corpus
python scripts/freeze_evidence_packages.py             # freeze evidence packages
python -m pytest tests/ -q                             # full suite (~866 tests)
```

The SEC cache (`research/cache/sec/`) is gitignored; fetch via
`scripts/fetch_public_reports.py` or restore from the public SEC EDGAR API.
