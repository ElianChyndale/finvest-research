# AGENTS.md — Navigation for AI agents

This file tells an AI (or a new reader) how to understand the FinVEST research
programme from this hub. Read it before exploring.

## 1. What this repo is

A **coordination hub**. The research code lives in submodules and linked
repos. If you clone only this repo, you have the narrative, the experiment
status, and the map; the code is one `git submodule update --init` away.

## 2. Read order

1. [README.md](README.md) — the programme at a glance + research spine.
2. [docs/research-spine.md](docs/research-spine.md) — the evidence chain in
   depth: data → labels → experiments → claims, and how leakage is prevented
   at each step.
3. [docs/experiments.md](docs/experiments.md) — which experiments exist
   (E0–E8, A10, A11), their honest status, and where the artifacts live.
4. [docs/governance.md](docs/governance.md) — the claim-evidence matrix, the
   evidence-status legend, and the honesty rules every claim must obey.
5. [docs/tools/](docs/tools/) — one page per tool: purpose, status, spine role.

## 3. Submodule map (all 13 programme repos)

| Path | Repo | Spine role |
|---|---|---|
| `submodules/ecoquant` | EcoQuant-Financial-Intelligence | Main implementation: corpus, retrieval, verification, experiments, annotations |
| `submodules/contracts` | financial-ai-contracts | Data contracts + canonical hashing |
| `submodules/verification-kit` | financial-systems-verification-kit | Dual-implementation numerical verification |
| `submodules/paper-repro` | paper-reproduction-lab | Reproduction-study manifests |
| `submodules/dossiers` | project-evidence-dossiers | Evidence dossiers / claim matrices |
| `submodules/pdf-manager` | pdf-manager | Document rendering for evidence packages |
| `submodules/auralynq` | Auralynq | Event-stream / review-scheduling patterns |
| `submodules/defence-lab` | research-defence-lab | Oral-defence preparation |
| `submodules/application-gen` | academic-application-generator | Evidence-constrained application drafts |
| `submodules/portfolio` | chen-ai-systems-portfolio | Publication surface |
| `submodules/green-bond` | Green-Bond-Market-Infrastructure | Downstream application (risk attestation) |
| `submodules/reconciliation` | repo-reconciliation-toolkit | Repo-state audit / migration planning |
| `submodules/research-lab` | ai-research-engineering-lab | ML/IR foundations lab |

If a submodule is empty (not initialized):

```bash
git submodule update --init --recursive
```

## 4. Where the current research state lives

- **Experiments:** `submodules/ecoquant/research/results/*.json` (e.g.
  `a11_two_stage.json` for the two-stage experiment) and
  `submodules/ecoquant/research/corpus/` (frozen leak-free corpus).
- **Annotations:** `submodules/ecoquant/human_review/day1/v0.2-draft/` and
  `submodules/ecoquant/human_review/evidence_packages/` (frozen packages).
- **Registry:** `submodules/ecoquant/../_research_program/planning/` — note this
  lives in the D:/Aireland coordination workspace, not in a submodule; the hub
  mirrors its key content into `docs/`.
- **Honest status:** this hub's `docs/experiments.md` is the summary; the
  authoritative per-repo record is each experiment's result JSON with its
  `markers` (`EXPLORATORY_PILOT` / `SMALL_SAMPLE` / `SOLO_PROVISIONAL` /
  `NOT_PAPER_HEADLINE`).

## 5. Leakage rules (do not violate)

- The corpus builder must never read gold sources (annotations, sealed case
  gold, minimal sets). Tests rename gold files away and assert the corpus_id
  is unchanged.
- The production verifier must never receive the gold answer
  (`expected_value=None`); gold is consumed only by the offline evaluator.
- Public claims must carry an evidence status
  (implemented / harness-validated / solo-provisional / experimentally-
  supported / invalidated) and trace to the claim-evidence matrix.

## 6. Reproducing the main experiment

See `submodules/ecoquant/README.md` and `docs/research-spine.md §Reproduction`.
Quick path (from `submodules/ecoquant/`):

```bash
python experiments/a11_retrieval/run.py --top-k 20   # real two-stage run
python -m pytest tests/ -q                            # full suite
```

## 7. Syncing this hub

`scripts/sync_status.py` regenerates `docs/experiments.md` and
`docs/status.json` from the submodules' result artifacts. Run it after
experiments change, or rely on CI.
