# FinVEST Research Hub

Research coordination, reproducibility, and evidence governance for **FinVEST** —
evidence-grounded financial question answering (QA) with temporal, version, and
numerical verification plus calibrated selective abstention.

> **What is this repository?** This is the *hub* for the FinVEST research
> programme. It does not contain the research implementation itself — that
> lives in the submodules and linked sibling repositories. This hub exists so
> that a reader (human or AI) can clone ONE repository and understand the whole
> programme: what problem we study, how the evidence chain is built, which
> experiments exist and their honest status, and where each piece of code lives.

---

## The FinVEST Research Spine

The spine is the evidence chain that connects raw data to public claims:

```text
SEC companyfacts / full 10-K
        ↓  (leak-free corpus — gold-blind by construction)
Retrieval   R1 BM25 / R2 dense / R3 RRF / R4 concept-temporal
        ↓  top-K candidates
Set selection  S1 top-k / S2 greedy / S3 beam / S4 oracle
        ↓  minimum evidence set
Verification  V1 temporal / V2 numerical / V3 joint
        ↓
ANSWER / REVIEW / ABSTAIN
        ↓
Experiment record → evidence dossier → portfolio / application
```

Every link is governed: annotation is append-only with frozen evidence
packages; the corpus builder provably cannot read gold; the production verifier
never receives the gold answer; public claims must trace to a claim-evidence
matrix entry.

## How to read this hub

| Path | What it is |
|---|---|
| [README.md](README.md) | This file — the programme at a glance |
| [AGENTS.md](AGENTS.md) | Navigation for AI agents: read this first |
| [docs/FINVEST_RESEARCH_REFERENCE.md](docs/FINVEST_RESEARCH_REFERENCE.md) | Research core reference #1 — code-verified status audit |
| [docs/FINVEST_RESEARCH_REFERENCE_2.md](docs/FINVEST_RESEARCH_REFERENCE_2.md) | Research core reference #2 — strategic direction & literature |
| [docs/FINVEST_RESEARCH_REFERENCE_3.md](docs/FINVEST_RESEARCH_REFERENCE_3.md) | Research core reference #3 — sequential evidence acquisition & certification (P0-9) |
| [docs/RESEARCH_REFERENCE_RECONCILIATION.md](docs/RESEARCH_REFERENCE_RECONCILIATION.md) | Reconciliation of the three reference files |
| [docs/research-spine.md](docs/research-spine.md) | The evidence chain in depth (data → labels → experiments → claims) |
| [docs/experiments.md](docs/experiments.md) | Experiment registry E0–E8 + A10/A11 pilot status (machine-synced) |
| [docs/governance.md](docs/governance.md) | Claim-evidence matrix, evidence-status legend, honesty rules |
| [docs/tools/](docs/tools/) | One page per tool repo: purpose, status, where it fits |

## Where the code lives

**All 13 programme repositories are git submodules** — one clone brings the
whole codebase locally.

| Submodule | Role in the spine |
|---|---|
| `submodules/ecoquant` | Main research repo (corpus, retrieval, verification, experiments, annotations) |
| `submodules/contracts` | Versioned data contracts (EvidenceUnit, BenchmarkCase, ExperimentRecord) |
| `submodules/verification-kit` | Independent Decimal financial verification + mutation controls |
| `submodules/paper-repro` | Reproduction-study manifests (claim → hypothesis → mechanics) |
| `submodules/dossiers` | Evidence dossiers / claim matrices for external statements |
| `submodules/pdf-manager` | Document rendering for evidence packages |
| `submodules/auralynq` | Event-stream / review-scheduling patterns |
| `submodules/defence-lab` | Oral-defence preparation |
| `submodules/application-gen` | Evidence-constrained application drafts |
| `submodules/portfolio` | Publication surface |
| `submodules/green-bond` | Downstream application (risk attestation) |
| `submodules/reconciliation` | Repo-state audit / migration planning |
| `submodules/research-lab` | ML/IR foundations lab |

Clone with submodules:

```bash
git clone --recurse-submodules https://github.com/ElianChyndale/finvest-research.git
# or after a plain clone:
git submodule update --init --recursive
```

Each has its own remote (see [docs/tools/](docs/tools/) for links).

## Current status (honest)

**What is true today:**

- A leak-free SEC corpus of **170,229 facts** is built and frozen (gold-blind:
  renaming all gold/annotation files away leaves the corpus_id unchanged).
- 20 solo-provisional human annotations (17 SOLO_PROVISIONAL / 3 NEEDS_EXTERNAL_REVIEW);
  60 frozen evidence packages with full-package SHA-256.
- A11 two-stage experiment on the leak-free corpus runs end-to-end:
  R1 recall@5 ≈ 0.105, R2 ≈ 0.079, R3 ≈ 0.105, R4 ≈ 0.053 — real numbers,
  NOT paper headline results.
- The production verifier is gold-free by construction (tests enforce it):
  the executable program is **induced from the question text**
  (`finvest/program_induction/induction.py`, P0-9) — the sealed payload's
  calc-program field is never consumed (it lives beside the hidden answer).

**What is explicitly NOT true:**

- No experiment result here is a paper headline. Labels are solo-provisional;
  retrieval recall is low; the routing is conservative (reports coverage +
  precision so "18 REVIEW" is not presented as success).
- See [docs/experiments.md](docs/experiments.md) and
  [docs/governance.md](docs/governance.md) for per-experiment honest status.

## Reproducing the main experiment

```bash
# In submodules/ecoquant (requires the SEC cache under research/cache/):
python experiments/a11_retrieval/run.py --top-k 20
# Corpus freeze:
python scripts/build_leak_free_corpus.py
# Annotation freeze:
python scripts/freeze_evidence_packages.py
# Full test suite:
python -m pytest tests/ -q
```

See [submodules/ecoquant/README.md](submodules/ecoquant/README.md) for details.

## License

See [LICENSE](LICENSE). The SEC data used is public domain; all derived
research artifacts retain their own repository licenses.
