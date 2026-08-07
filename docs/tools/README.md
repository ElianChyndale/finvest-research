# Tool Repositories — One Page Each

Every repository that the FinVEST research programme uses, with its purpose,
its role in the [research spine](../research-spine.md), and its honest status.
**All 13 are git submodules of this hub** — `git submodule update --init --recursive`
brings the whole programme's code locally.

| Tool | Submodule | Spine role |
|---|---|---|
| [EcoQuant-Financial-Intelligence](ecoquant.md) | `submodules/ecoquant` | Main research implementation |
| [financial-ai-contracts](contracts.md) | `submodules/contracts` | Versioned data contracts |
| [financial-systems-verification-kit](verification-kit.md) | `submodules/verification-kit` | Dual-implementation numerical verification |
| [paper-reproduction-lab](paper-repro.md) | `submodules/paper-repro` | Reproduction-study manifests |
| [project-evidence-dossiers](dossiers.md) | `submodules/dossiers` | Evidence dossiers / claim matrices |
| [pdf-manager](pdf-manager.md) | `submodules/pdf-manager` | Document rendering for evidence packages |
| [Auralynq](auralynq.md) | `submodules/auralynq` | Event-stream / review-scheduling patterns |
| [research-defence-lab](defence-lab.md) | `submodules/defence-lab` | Oral-defence preparation |
| [academic-application-generator](application-gen.md) | `submodules/application-gen` | Evidence-constrained application drafts |
| [chen-ai-systems-portfolio](portfolio.md) | `submodules/portfolio` | Publication surface |
| [Green-Bond-Market-Infrastructure](green-bond.md) | `submodules/green-bond` | Downstream application (risk attestation) |
| [repo-reconciliation-toolkit](reconciliation.md) | `submodules/reconciliation` | Repo-state audit / migration planning |
| [ai-research-engineering-lab](research-lab.md) | `submodules/research-lab` | ML/IR foundations lab |

Status legend: **implemented** (code + tests, no claim) · **harness-validated**
(pilot harness runs it, may be leaky) · **solo-provisional** (single-annotator
labels) · **experimentally supported** (measured on leak-free experiment) ·
**invalidated** (retracted).
