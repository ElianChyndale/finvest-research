# FinVEST 科研核心参考文件

> **FinVEST Research Core Reference — Financial Research Spine**
>
> 本文档是 FinVEST 研究纲领的**权威参考文件**：对 `finvest-research`（含 13 个 submodule，核心是 `submodules/ecoquant`）进行深度研究分析，覆盖 2026-08 科研审计提出的全部内容，并**逐一用代码与运行结果验证**，再给出提升路径与科研定位。
>
> **验证基准**：`finvest-research@97ddb4c`，`ecoquant@6493165`，2026-08-07。本文档中所有“已验证”的判断均标注了 `文件:行号` 或运行产物路径，可供复核。
>
> **用途**：金融科研方向的核心参考；撰写论文、博士申请、答辩、作品集时的单一事实来源。

---

## 目录

1. [文件定位与使用方式](#1-文件定位与使用方式)
2. [总判断：方向正确，证明链未追上工程](#2-总判断)
3. [已验证的真实科研状态（P0 问题逐条核对）](#3-已验证的真实科研状态)
4. [当前结果应如何重新分类](#4-当前结果应如何重新分类)
5. [仓库拓扑与各模块真实能力图](#5-仓库拓扑与各模块真实能力图)
6. [与审计文档的一致性核对（时间线）](#6-与审计文档的一致性核对)
7. [科研定位：Evidence Entitlement](#7-科研定位evidence-entitlement)
8. [与最新相关研究的差距分析](#8-与最新相关研究的差距分析)
9. [顶会路线与四篇论文策略](#9-顶会路线与四篇论文策略)
10. [金融科研部分：从技术系统到金融研究](#10-金融科研部分)
11. [个人发展与科研反馈环](#11-个人发展与科研反馈环)
12. [诚实规则与风险登记](#12-诚实规则与风险登记)
13. [设计建议（基于本参考文件）](#13-设计建议)
14. [90 天执行计划](#14-90-天执行计划)
15. [参考文献](#15-参考文献)

---

## 1. 文件定位与使用方式

**本文件回答四个问题：**

1. **我现在有什么？** —— 逐模块、逐行验证过的真实能力清单，区分 `IMPLEMENTED / PARTIAL / STUB / BROKEN / ABSENT`。
2. **审计说了什么，哪些是真的？** —— 对审计文档 P0-1..P0-6 及全部主张的代码级核对。
3. **我该往哪里走？** —— Evidence Entitlement 科研定位 + 四篇论文 + 金融研究维度。
4. **未来 90 天做什么？** —— 可执行到周的计划（见 [RESEARCH_DESIGN_AND_PLAN.md](RESEARCH_DESIGN_AND_PLAN.md)）。

**使用规则：**

- 任何对外 claim（论文、CV、PS、答辩）必须能回溯到本文档第 3/4 节的状态标签。
- 标为 `INVALIDATED_PENDING_GOLD_ISOLATION` 的数字**不得**对外使用。
- 标为 `EXPLORATORY_RETRIEVAL_DIAGNOSTIC` 的数字只能作为诊断，不能作为 benchmark 结论。
- 本文档与 `docs/governance.md` 的 evidence-status legend、`docs/experiments.md` 的机器同步状态、`_research_program/planning/CLAIM_EVIDENCE_MATRIX.md` 的 claim 矩阵保持一致；**冲突时以本文档第 3 节的代码验证为准**。

---

## 2. 总判断

### 2.1 分层评分（基于代码验证，2026-08-07）

| 层次 | 当前评分 | 判断依据（代码/产物证据） |
|---|---|---|
| **研究方向潜力** | **8/10** | Evidence Entitlement（时间有效 + 版本一致 + 数值可执行 + 最小充分证据集 + 选择性风险控制）交叉空间真实存在，尚无成熟工作完整组合七项（见 §8）。 |
| **科研工程与可审计性** | **8.5/10** | leak-free corpus（`build_leak_free_corpus.py`）、SHEP 冻结（60 packages + SHA-256）、denominator audit、claim-evidence matrix 均真实存在并测试覆盖。 |
| **当前实验可信度** | **3/10** | A11 routing 仍读 `gold_answer`（`run.py:315`）；REVIEW 指标恒真（`run.py:509`）；selector 用 gold concepts 做 requirements（`run.py:281`）。 |
| **当前方法创新** | **2.5/10** | R1-R4 检索（BM25/dense/RRF/concept-dict）；S1-S4 选择（greedy/beam/oracle）；V1-V3 验证（时间/数值/联合）。规则与已有检索器，无学习型方法。 |
| **当前 benchmark 成熟度** | **3/10** | 19 个评估案例、单人 provisional labels、6 个 issuer、无双标、无外源对照。170k 是 corpus 规模，不是 question 规模。 |
| **当前社会科学贡献** | **2/10** | 未研究真实人/组织/监管/市场后果；E6 human-in-the-loop 仅 `planned`。 |
| **当前顶会就绪度** | **2-3/10** | 现在投稿顶会，大概率因有效性、规模、novelty 被拒。 |
| **优化后潜力** | **7-8.5/10** | 有机会形成多篇较强论文（见 §9）。 |

### 2.2 核心结论

> **研究方向不是错误的；当前的问题是科研证明链还没有追上工程架构。**

- 工程层（corpus 冻结、SHEP、governance、CI 基建、13 repo 协调）**明显高于普通个人项目**。
- 但顶会审稿人只追问四件事：**你提出了什么以前没有的方法/数据/理论？实验是否真正无泄漏？相比最强方法提升了什么？对金融决策或社会产生了什么可测量价值？**
- 目前四个问题都还没有论文级答案。好消息是：**四个问题的答案都已经有了清晰的路线**（本文档 §8-§10）。

---

## 3. 已验证的真实科研状态

> 本节是审计 P0-1..P0-6 的**代码级验证结果**。每个结论都标注了证据位置。

### 3.1 P0-1：路由仍直接读取 `gold_answer` —— **CONFIRMED（问题仍存在）**

**证据**：[`experiments/a11_retrieval/run.py:315`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L315)

```python
case_answerable = (case.get("gold_answer") or {}).get("value") is not None
```

**分析**：系统在决定 `ANSWER/REVIEW/ABSTAIN` 之前，读取了隐藏 gold answer 是否存在。注释声称“answerability 是 case property，不是 gold answer”——但字段名就是 `gold_answer`，且正是 evaluator 用来评分的隐藏目标。

**影响**：以下主张**当前不能成立**：
- production routing is gold-free；
- routing result comes only from retrieved evidence；
- abstention behavior is independently evaluated。

**现状补充**：仓库的 gold-isolation 测试（`tests/finvest/test_verifier_gold_isolation.py`）只断言 `_verify`（V 层）签名无 gold、`expected_value=None`，**没有覆盖 routing 层的 gold 读取**。测试通过 ≠ 路由 gold-free。我本地运行了该测试（`17 passed`），确认测试通过但未覆盖此问题。

**修复方向**（已列入 90 天计划第 1-2 周）：
```python
class ProductionCase:      # 生产路径，禁止任何 gold 字段
    question; issuer; target_period; source_cutoff
class EvaluationLabel:     # 隔离 evaluator，只由离线评测读取
    gold_answer; acceptable_evidence_sets; gold_route; ...
```

**关键新发现（recon 验证，比审计更进一步）**：sealed case 里**已经存在非 gold 的 answerability 信号**——`sufficiency_label`（SUPPORTED/INSUFFICIENT/CONFLICTING）和 `answer_type`（derived/unanswerable/extractive）——但 A11 路由忽略了它们，改用 `gold_answer` 存在性。在 sealed manifest 中，`gold_answer` 为空 iff `sufficiency_label == INSUFFICIENT`，所以**用 gold 键路由实际上是在用一个 gold 代理表达一个本来就能无 gold 得到的属性**。修复应直接键 `sufficiency_label`/`answer_type`（若这些字段也被认为属“gold”类，则需在 case 构造时冻结为生产字段，evaluator 另存 `gold_route`）。

另外，**gold 在非 evaluator 位置被消费了不止一处**：除 `run.py:315` 路由外，`_summarize` 的 denominator audit（`run.py:535-542` 的 `n_answerable_gold`/`n_insufficient_gold`）也读取 sealed case 的 `gold_answer`。因此 docs 中“gold touches only the offline evaluator”是字面上不成立的（见 §3.8）。

### 3.2 P0-2：`REVIEW` 正确性指标恒真 —— **CONFIRMED（问题仍存在）**

**证据**：[`experiments/a11_retrieval/run.py:508-509`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L508)

```python
if decision == "REVIEW":
    return {"bucket": "review", "correct": gold_route != "ANSWER" or True, "gold_used": True}
```

`X or True` 恒为 `True`。**所有 REVIEW 决策自动判对**。

**影响（直接）**：
- `review_precision = 1.0`、`false_review_rate = 0.0`（`run.py:677-682` + A11 产物 `research/results/a11_two_stage.json`）**由代码逻辑保证，不是实验发现**。
- 当前 0 ANSWER / 18 REVIEW / 1 ABSTAIN 看起来“非常安全”，但一个永远输出 REVIEW 的系统同样能获得这些数字。

**必须同时衡量（utility-aware）**，不能只问“是否安全”：

```
U = B_correct_answer − C_review·(review cost) − C_abstain·(abstain cost) − L_unsafe_answer·(unsafe-answer loss)
```

### 3.3 P0-3：证据集合选择使用 gold requirements + CoverageModel 空间不匹配 —— **CONFIRMED，且比审计更严重**

**证据 A（gold requirements）**：[`experiments/a11_retrieval/run.py:236-237, 281`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L236)

```python
gold_concepts = {it.get("concept") for it in case.get("evidence_items", [])}   # 来自 sealed case 的 gold evidence
...
requirements = gold_concepts if ranked_ids else frozenset()                     # 直接作为 selector requirements
```

即 S2/S3/S4 的 requirements 直接读取了答案所需概念（gold），**不是**从自然语言问题推断。

**证据 B（CoverageModel 空间不匹配）**：[`run.py:282-284`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L282) + [`selectors.py:37-48`](../submodules/ecoquant/finvest/set_selection/selectors.py#L37)

```python
coverage = CoverageModel({uid: frozenset({uid}) for uid in ranked_ids})  # evidence_id -> {evidence_id}
```

而 `requirements` 是 `{concept_1, concept_2, ...}`。`evidence_id` 的格式是 `issuer:us-gaap:concept:unit:start:end:form:accession`（见 `run.py:163`），**绝不等于 concept**。

因此 greedy（`b2_greedy_set_cover`）中 `coverage.coverage.get(best) & remaining` 恒为空 → **S2/S3 永远输出空集**；`minimality_violation = 1.0`。**S4 oracle 在 A11 中传入的也不是 gold coverage，而是同一个 identity CoverageModel**——所以 S4 在 A11 里甚至不是真正的 oracle upper bound（审计说 S4 是 oracle-only，我验证后确认：A11 中它是退化的）。

**影响**：`set_selection` 层的全部数字（set precision/recall/exact match/minimal set recall）在 A11 中**无意义**。

**修复方向**：
1. requirement 空间与 coverage 空间必须统一（都用 concept 或都用 evidence_id）；
2. requirements 必须由 question-requirement induction 推断（非 gold）；
3. S4 oracle 必须使用真 gold coverage 才有 upper-bound 意义。

### 3.4 P0-4：VISTA-Fin 还不是学习方法 —— **CONFIRMED（代码自述）**

**证据**：[`finvest/set_selection/selectors.py:164-185`](../submodules/ecoquant/finvest/set_selection/selectors.py#L164)

```python
def vista_fin_selector(...):
    """P1: VISTA-Fin graph set selector (scaffold).
    Full implementation (requirement-graph encoder, candidate-evidence-graph
    encoder, cross-graph attention, set-level sufficiency head) is a later
    milestone with learned weights. This scaffold uses greedy set cover ..."""
```

**结论**：VISTA-Fin 明确标注为 scaffold，核心是 greedy proxy。**当前不能声称“我们提出了一个新的 evidence-set learning method”**。准确说法：方法框架、接口、oracle-aware evaluation harness 已实现；proposed learned model 未完成。

### 3.5 P0-5：所谓 leave-one-issuer-out 还不是泛化实验 —— **CONFIRMED，且比审计更严重**

**证据**：[`run.py:634-661`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L634)

```python
def _leave_one_issuer_out(per_case):
    ...
    for held_out, held_cases in sorted(groups.items()):
        train = [c for iss, cs in groups.items() if iss != held_out for c in cs]
        ...
        folds[held_out] = {
            "held_out_cases": len(held_cases),
            "train_cases": len(train),
            "macro_recall@5_train": {...},   # 只报告 train 侧 recall
        }
```

**分析**：该函数只聚合 **train 侧**案例的 recall，从不报告 held-out issuer 的真实测试结果。A11 产物 `research/results/a11_two_stage.json` 中 `leave_one_issuer_out.folds.*.macro_recall@5_train` 全部为 0.0。它既没有 train/calibrate 在 5 个 issuer 上再测第 6 个，也没有 held-out 侧任何指标。

真正的 LOIO：
```text
Fold A: train/calibrate on 5 issuers → test ONLY on held-out issuer 6
Fold B: train/calibrate on other 5   → test ONLY on held-out issuer 5
...
报告：held-out Recall@K、held-out completeness、held-out routing risk、6 折 macro mean + CI
```

### 3.6 P0-6：公开 CI 尚未完全闭环 —— **CONFIRMED（hub 无 CI + integration CI 失败）**

**证据（GitHub Actions 实际状态，2026-08-07）**：
- `EcoQuant` 最新提交 `fix(audit): gold-free production verifier...`：**CI = success**（31143553715），**human-workbench = success**（31143553723），但 **Integration CI (pinned tool repos) = FAILURE**（31143553708）。
- `finvest-research` hub **没有 `.github/` 目录 → 零 CI run**。
- 本地跑 `python -m pytest tests/ -q`：**405 passed / 1 failed / 6 skipped**。失败项 `tests/research/test_e0_integrity.py::test_e0_runner_writes_parseable_output`，因为 FinanceBench cache 是 cache-only 未提交，`run_e0_validate.py` 输出 `"all_gates_pass": false`（`financebench_sample.gate_pass=false, reason: cache absent`）。

**影响**：13 个 submodule 可手工 clone，但 submodule SHA、文档状态、integration lock、各子仓库 CI 状态未被总仓库持续自动验证。Meta-repo 应增加只做治理的 CI（见 §13 设计建议 G-2）。

### 3.7 新发现：三个此前未报告的实质问题（recon 验证）

> 这三点不在原审计的 P0 清单里，但对论文级结论同样致命。**数值验证在真实案例上恒失败**、**AMENDS 未在生产路径执行**、**对抗 mutation 未接入生产**。

**N-1：数值验证在真实案例上恒失败（`subtract` 操作未实现）**

- 真实 `calculation_program` 的 operation 是 `'subtract'`（cashflow proxy 案例）。
- 但 `src/ecoquant/research/table_eval/calculate.py` 只支持 6 个 GRI-QA 函数（`average/sum/increase_difference/reduction_difference/increase_percentage/reduction_percentage`），**没有 `subtract`**。
- 执行验证：`verify_calculation(operation='subtract', ...)` → `calculate()` 抛 `ValueError: unknown GRI-QA function: subtract` → 返回 `REVIEW_REQUIRED`（`numerical.py:45-47`）→ `numerical_ok=False` → **所有真实 cashflow 案例必然 REVIEW**。
- 这解释了 A11 的 0 ANSWER / 18 REVIEW：即使修复路由 gold 依赖，数值验证也会把几乎所有案例推向 REVIEW。
- 文档声称 `_extract_numbers` “scale-normalized via the E2 parser”，实际只是朴素 regex（`numerical.py:81-87`）；`parse_cell/extract_cells`（处理 %、括号、单位后缀）从未被 `verify_calculation` 调用。**无 unit/scale/sign 验证**。

**N-2：AMENDS 修订未在生产路径强制执行**

- `temporal_version.py:50` 的 `_superseded` 只认 `SUPERSEDES`，不认 `AMENDS`。
- 处理 AMENDS 的 `latest_valid_version`（`temporal_version.py:100-114`）**在 A11 管线中从未被调用**（只在测试里引用）。
- 因此“amendment-aware 验证”对真实修订场景不生效。

**N-3：对抗 mutation 未接入生产 + 字符串级缺陷**

- `finvest/verification/adversarial.py` 的 mutation 是**字符串级文本编辑**（如 wrong_number 破坏所有数字、wrong_scale 只匹配字面 'billion'），不是字段级（filing date / valid period / unit / scale / sign）。
- 该 harness **未接入任何生产实验**（只被 `tests/finvest/test_adversarial.py` 调用）。
- 指标 bug：per-type precision 硬编码（`adversarial.py:167-168` `'fp = ... if False else 0'`），per-type F1 被虚高。

**N-4：evidence-package hash 缺陷（第二标注者无法验证包回放）**

- 20 条 SOLO 记录的 `evidence_package_hash` 是**旧版 16-hex 截断 source-row hash**，不是 Phase-1.5 的全包 SHA-256（`package_freeze.package_hash_for_case()` 返回值）。
- 即 `package_freeze.py` 要修的正是这个问题，但**现有标注数据里仍是旧 hash** → 未来第二标注者无法按记录 hash 字节级验证包回放。

**N-5：E5 过期 claim 仍残留在两个活跃表面**

- `research/reports/RESEARCH_PROGRAMME_OVERVIEW.md:51` 仍引用 “AUROC 0.923; ECE 0.054”。
- `research/reports/E5_CALIBRATION_SELECTIVE.md` 仍把 0.923 当作 SUPPORTED 呈现，无 INVALIDATED 标记、无 0.719 基线。
- 审计声称已更新报告，但**当前报告文件既无 'INVALIDATED' 也无 '0.719' 也无 'leak'**。

**N-6：camelCase 概念拼写导致 requirement induction 失败（真实数据验证）**

- 真实 benchmark 问题用 camelCase 拼写 XBRL 概念（`AccruedLiabilitiesCurrent`），与字典空格分隔 key（`'accrued liabilities'`）不匹配 → 预测退化为更宽泛的 `Liabilities` → S2/S3/R4 选不出任何东西。
- 修复：`_concepts_for` 同时匹配 camelCase 边界加空格变体。真实 170k corpus 上 R1 S2_greedy 从 size 0.0 → 1.0，R4 recall@5 从 0.04 → 0.08。

**N-7：数值提取把日期/表单数字算进答案（真实数据验证，4/5 ANSWER 错误根因）**

- `_extract_numbers` 的 regex 把 `2024-09-29` 拆成 `2024, -9, -29`，`10-Q` 拆出 `10` → `subtract` 算出巨大负数 `-9947023532`，被 executability-only 判 SUPPORTED → 错误 ANSWER。
- 真实 170k run（路由修复后）产生 4/5 错误 ANSWER，全部 R1 recall@5=0.0（gold 未检索到，却用错误概念算出数）。
- 修复：排除日期形/表单形 token。

**N-8：数值验证不校验计算输入概念是否齐全（N-7 修复后仍 4/5 错）**

- 即使排除日期数字，`subtract` 对**只含 OCF、缺 capex** 的证据池仍算出荒谬值并 SUPPORTED。
- 修复：`verify_calculation(required_concepts=...)`，`_verify` 传 `_concepts_for(question)`（gold-free）。缺失任一输入概念 → REVIEW_REQUIRED。

**真实数据验证结果（修复后，冻结 170,229 corpus）**

| 指标 | 修复前（恒真） | 修复后 |
|---|---|---|
| decisions | 0 ANSWER / 18 REVIEW / 1 ABSTAIN | **1 ANSWER / 18 REVIEW / 0 ABSTAIN** |
| answer_precision | 0.0（无 ANSWER） | **1.0**（唯一 ANSWER 正确） |
| unsafe_answer_rate | 0.0（恒真假象） | **0.0**（真实） |
| coverage | 0.0 | **0.0526** |
| false_review_rate | 0（恒真假象） | 0.8333（诚实：大部分可答案例被 REVIEW） |
| leakage audit | clean | **clean**（`evidence_id_overlap_with_gold: 0`） |

**结论**：修复让系统从"恒真伪安全"变成**真实安全 + 诚实保守**——只在证据充分（gold recall@5=1.0）且输入概念齐全时 ANSWER，否则 REVIEW。`false_review_rate 0.83` 诚实地暴露了检索质量不足（recall@5 ~0.08）——这正是选择性风险控制论文要研究的问题。

### 3.7b 已确认为真实能力的部分（非 P0，但值得记录）

| 能力 | 状态 | 证据 |
|---|---|---|
| Leak-free corpus（170,229 facts，6 issuer，gold-blind 构造） | **IMPLEMENTED** | `finvest/benchmark/builders/leak_free_corpus.py`；`CORPUS_MANIFEST.json`；测试：改名全部 gold 文件后 corpus_id 不变 |
| 联合时间/版本验证（source-time, valid-time, period, supersession） | **IMPLEMENTED**（逻辑真实，但基于 rules） | `finvest/verification/temporal_version.py` |
| 数值可执行验证（expected_value=None，无 gold 进生产） | **IMPLEMENTED**（`_extract_numbers` 是朴素 regex） | `finvest/verification/numerical.py:41-52` |
| 确定性六函数计算引擎（GRI-QA 语义） | **IMPLEMENTED** | `src/ecoquant/research/table_eval/calculate.py`（161 行，六函数 + 单元解析） |
| SHEP 冻结 + 全包 SHA-256 + manifest | **IMPLEMENTED** | `human_review/evidence_packages/`（60 packages） |
| Leak-free calibration 特征 + issuer-grouped cross-fitting | **IMPLEMENTED**（经验型，无正式保证） | `finvest/calibration/leak_free.py`；E5 rerun AUROC 0.719（`PILOT_VALIDATED`） |
| 四类 challenge-case 生成（wrong-period/future-source/amendment/scale-sign/...） | **IMPLEMENTED** | `finvest/benchmark/builders/challenge_cases.py` |
| R4 concept 检索（gold-blind，公共概念字典） | **IMPLEMENTED 但字典仅 ~17 terms** | `finvest/retrieval/retrievers.py:36-54` |
| 集成适配器（contracts / verification-kit / paper-repro，INTEGRATION_LOCK 固定 commit） | **IMPLEMENTED**（集成报告 all_pass=true） | `integrations/INTEGRATION_LOCK.json`；`research/results/INTEGRATION_REPORT.json` |

### 3.8 审计提到但需要修正/注意的点

1. 审计说“S4 oracle = upper bound only”——验证后 **A11 中 S4 退化为 identity-coverage，连 oracle 都不是**。这是比审计更进一步的发现。
2. 审计说“retrieval Recall@5 数字未必需要作废”——同意。A11 的 R1-R4 候选确实来自独立 leak-free corpus（corpus 层无 gold token，`evidence_id_overlap_with_gold: 0`），可以作为**小样本诊断**，但不能作为正式 benchmark 结论。
3. `paper/report.md`（151 行）仍是**已作废的 green-bond temporal RAG 版本**（含 ORACLE_CONDITION 的 1.000 Recall@5），不应被当作当前论文草稿。

---

## 4. 当前结果应如何重新分类

> 下表是审计分类的**代码验证版**（状态列以代码为准）。

| 当前内容 | 正确科研身份 | 验证状态 |
|---|---|---|
| 170,229 CompanyFacts records | **Corpus engineering artifact** | 确认 |
| 19 个评估案例 | **Small exploratory evaluation subset** | 确认（`n_final_evaluated: 19`） |
| BM25/Dense/RRF/Concept Recall@5 | **Exploratory retrieval diagnostics**（A11 产物 R1≈0.08 / R2≈0.06 / R3≈0.08 / R4≈0.04 macro） | 确认，可用作诊断 |
| 0 ANSWER / 18 REVIEW / 1 ABSTAIN | **Invalid routing result until gold dependency removed** | 确认（`run.py:315`） |
| review precision = 1.0 | **Invalid metric**（恒真） | 确认（`run.py:509`） |
| false-review rate = 0 | **Invalid metric**（恒真） | 确认 |
| S2/S3 selectors | **Gold-conditioned + space-mismatched → 当前无意义** | 确认，比审计更严重 |
| S4 oracle | **A11 中退化，非 true upper bound** | 新发现 |
| mutation rejection | **Known-mutation test coverage** | 确认（challenge cases 测试 REJECTION 路径） |
| 13 submodules | **Research coordination infrastructure** | 确认 |
| E5 AUROC 0.923 / ECE 0.054 / Brier 0.085 | **INVALIDATED**（gold-feature leakage） | 确认（`docs/audits/E5_GOLD_LEAKAGE_AUDIT.md`） |
| E5 leak-free rerun AUROC 0.719 | **PILOT_VALIDATED**（小样本，非 headline） | 确认 |
| FinVEST paper claim | **Not yet experimentally supported** | 确认 |

### 4.1 三个必须立即处理的“非 P0 但致命”问题（并入 Phase 0）

| 问题 | 影响 | 证据 |
|---|---|---|
| **N-1 数值验证 `subtract` 未实现** | 真实 cashflow 案例必然 REVIEW → A11 的 0 ANSWER 部分由代码缺陷造成 | `numerical.py` 调 `calculate()`，`calculate.py:135-161` 无 `subtract` |
| **N-2 AMENDS 未在生产执行** | “amendment-aware 验证”名存实亡 | `_superseded` 只认 SUPERSEDES（`temporal_version.py:50`）；`latest_valid_version` 未接入 A11 |
| **N-3 对抗 mutation 字符串级 + 未接入** | verifier 的真实拒绝能力未被压力测试 | `adversarial.py:22-181`；无实验调用；per-type F1 虚高 |
| **N-4 标注 hash 是旧 16-hex** | 第二标注者无法验证包回放 | `SOLO_ANNOTATIONS.jsonl` 记录旧 hash ≠ 全包 SHA-256 |
| **N-5 E5 过期 claim 残留两处** | 活跃表面仍显示 0.923 | `RESEARCH_PROGRAMME_OVERVIEW.md:51`、`E5_CALIBRATION_SELECTIVE.md` |

---

## 5. 仓库拓扑与各模块真实能力图

### 5.1 13 个 submodule 的角色与真实状态

| Submodule | 角色 | 真实状态（基于代码/文档） |
|---|---|---|
| `ecoquant` | 主研究仓库（corpus/retrieval/verification/experiments/annotations） | 核心，见 §5.2 |
| `contracts` | 版本化数据契约（EvidenceUnit, BenchmarkCase, ExperimentRecord） | `v0.1.0`，`4b232218…`；集成报告 PASS |
| `verification-kit` | 独立 Decimal 金融验证 + mutation controls | `b0b1024…`；集成报告 PASS |
| `paper-repro` | 复现清单（claim→hypothesis→mechanics） | `9ca75082…`；集成报告 PASS |
| `dossiers` | 证据档案 / claim matrix | `v0.1.0` |
| `pdf-manager` | 证据包文档渲染 | `delivery-160-rc1~44` |
| `auralynq` | 事件流 / 复习调度（CFA 学习项目） | `heads/main` |
| `defence-lab` | 答辩准备 | `v0.1.0` |
| `application-gen` | 证据约束的应用草稿 | `v0.1.0` |
| `portfolio` | 出版表面 | `heads/main` |
| `green-bond` | 下游应用（风险认证） | `heads/main` |
| `reconciliation` | repo 状态审计 / 迁移 | `v0.1.0` |
| `research-lab` | ML/IR 基础实验室 | `heads/master` |

**关键判断**：科研主线（corpus→retrieval→selection→verification→routing）全部在 `ecoquant`。其他 12 个是协调/呈现/下游层。**未来 90 天科研工作应集中在 ecoquant**，其余仓库只在被真实使用时才改动。

### 5.2 ecoquant 模块能力矩阵

| 模块 | 能力 | 状态 | 论文级缺口 |
|---|---|---|---|
| `finvest/benchmark/` | 构建器、schemas、splitters、leakage audit、challenge cases | IMPLEMENTED | 19 案例太少；单人标签；无 cross-market |
| `finvest/retrieval/` | R1-R4 + metrics | IMPLEMENTED（弱表示） | 表示仅 raw XBRL 文本；无 label/definition/taxonomy 增强；概念字典 17 terms |
| `finvest/set_selection/` | S1-S4 + VISTA scaffold | PARTIAL（space mismatch, gold-conditioned, scaffold） | 无 learned selector；无 requirement induction |
| `finvest/verification/` | V1-V3 联合验证 | IMPLEMENTED（rules-based） | 无联合概率模型；数值提取朴素 |
| `finvest/calibration/` | Platt calibrator + 嵌套 LOIO + split-conformal gate | IMPLEMENTED（有真正的校准协议） | 无有限样本 coverage 验证；无决策损失/效用；A6-A8 特征集实现了但从未在数据上执行 |
| `human_review/` | 单人标注、SHEP、web workbench、60 packages | IMPLEMENTED | 无双标/adjudication/IRR（`DOUBLE_ANNOTATED/ADJUDICATED/HUMAN_VALIDATED_GOLD` 只是常量，无数代码路径进入）；E6 未跑；标注 hash 是旧版 |
| `integrations/` | 三工具适配器 | IMPLEMENTED（本地产物 PASS，但 Integration CI 红色） | lock 三处复制无一致校验；hardcoded git+https 安装正是 CI 失败根因 |
| `experiments/` | A0/A9/A10/A11 harness | IMPLEMENTED（A11 有 P0 问题） | 需修复后重跑 |

---

## 6. 与审计文档的一致性核对

| 审计主张 | 验证结论 |
|---|---|
| “方向有顶会潜力，但当前版本还没有顶会级可信结果” | ✅ 一致 |
| “科研工程与可审计性 8.5/10，高于普通个人项目” | ✅ 一致（corpus 冻结、SHEP、governance 真实） |
| P0-1 路由读 gold | ✅ 确认（`run.py:315`） |
| P0-2 REVIEW 恒真 | ✅ 确认（`run.py:509`） |
| P0-3 selector 用 gold requirements | ✅ 确认（`run.py:281`），**并发现 CoverageModel 空间不匹配 + S4 退化（审计未发现）** |
| P0-4 VISTA 是 scaffold | ✅ 确认（`selectors.py:171-185` 自述） |
| P0-5 LOIO 不是真泛化 | ✅ 确认（`run.py:634-661` 只报 train 侧），**并确认产物中全为 0.0（比审计更严重）** |
| P0-6 CI 未闭环 | ✅ 确认（hub 无 CI；Integration CI FAILURE；E0 本地失败） |
| “retrieval 表示过弱” | ✅ 确认（evidence unit 是 `concept value unit start end filed form accession`；`retrievers.py:36-54` 字典仅 17 条） |
| “17 万 facts 不能弥补 19 cases” | ✅ 确认（corpus 是 corpus，benchmark 是 question 规模） |
| “四篇论文拆分合理” | ✅ 采纳（见 §9） |
| “90 天目标 = 第一张无泄漏主实验表” | ✅ 采纳（见 §14） |

**审计时间线后仓库已做的改进**（截至 2026-08-07 `ecoquant@6493165`）：
- 新增 denominator audit（`run.py:525-563`）—— 每个分母显式可审计；
- 新增 per-issuer 检索统计与 macro average（`run.py:608-631`）；
- V 层明确 `expected_value=None` 的 executability 语义（`run.py:450-457`）；
- gold-isolation 测试扩展到签名/源码层面（`test_verifier_gold_isolation.py`）；
- Integration CI 使用 INTEGRATION_LOCK 固定 commit。

这些改进是真实的，但**都还没有解决 routing 层的 gold 依赖**。这是下一阶段最优先事项。

---

## 7. 科研定位：Evidence Entitlement

> **总研究问题：**
>
> **When is a financial AI system entitled to answer?**
>
> 形式版本：*Can a financial AI system determine whether it possesses a temporally valid, version-consistent, numerically executable and minimally sufficient evidence set, and selectively answer with finite-sample risk guarantees?*

**中文**：金融 AI 能否判断自己是否拥有时间有效、版本一致、数值可执行且最小充分的证据集合，并在有限样本风险保证下选择回答、复核或弃答？

这个定位比以下表述更强：
- 金融 RAG（无治理维度）；
- SEC QA（无时间/版本/风险维度）；
- evidence verification（无 set-level 充分性与选择性风险控制）。

**七项组合（目前无成熟工作完整覆盖，是真正机会）：**
1. **valid time**：事实属于哪个财务期间；
2. **source time**：何时公开；
3. **accession/version**：来自哪个 filing；
4. **amendment/restatement**：修订与重述；
5. **minimum sufficient evidence set**：最小充分证据集；
6. **numerical executability**：数值可执行；
7. **calibrated entitlement to answer**：校准的回答资格。

**与 SURE-RAG 的差异化**：SURE-RAG 已提出 sufficiency 是 set-level property、support/refute/insufficient 判断、no-oracle 与 counterfactual audit（[6]）。FinVEST 的差异化优势在于**金融域内七项组合**：版本/时间感知 + 数值可执行 + 选择性风险控制，且以 SEC filing 的真实结构（accession、amendment、restatement）为对象。

---

## 8. 与最新相关研究的差距分析

> 本节把审计引用的文献 [1]-[14] 转化为**可操作的差距清单**。每条都给出：他们有什么 → FinVEST 缺什么 → 怎么补。

### 8.1 Benchmark 规模差距（[1][2][3][4]）

| 文献 | 规模 | 对 FinVEST 的含义 |
|---|---|---|
| FinanceBench [1] | 10,231 问；2,400 个生成答案人工审查 | 顶会 benchmark 的规模下限。FinVEST-Pilot 300-500 是第一步，V1 需 2,000+ |
| FinAgentBench [2] | ~26,000 expert-annotated agentic retrieval examples；document-type selection + passage pinpointing | 表明“检索”应拆成 document-type 选择与 passage 定位两阶段——支持 FinVEST 的 hierarchical retrieval |
| FinDER [3] | 5,703 expert 构建的 query–evidence–answer triplets；强调用户问题模糊性/多样性 | FinVEST 问题分类应覆盖单事实/派生/跨期/跨文件/修订/版本冲突等 15 类 |
| HiREC/LOFin [4] | 145,897 份 SEC 标准化文档；1,595 QA；hierarchical retrieval + passage curation | 直接对标：document retrieval 与 passage curation 分离。FinVEST 的 evidence unit 应是 document→section→table→fact 层级 |

**行动**：FinVEST 的 benchmark 论文必须做到 (a) 2,000+ 高质量问题；(b) 15 类问题分类（见 §14 Phase 1）；(c) 至少 20-30% 双标；(d) 与 [1][3][4] 的对照实验。

### 8.2 方法 novelty 差距（[5][6]）

- **SURE-RAG [6]**：sufficiency set-level、no-oracle、counterfactual audit、指定 coverage 下报告 risk。
- **FinReflectKG [5]**：temporal KG + multi-hop 推理 + evidence efficiency。

**FinVEST 的差异化创新组合**（比“首次提出 set-level sufficiency”更站得住）：

> **Version- and transaction-time-aware evidence entitlement for financial QA under amendments, restatements, numerical executability and selective risk control.**

即同时处理 valid time + source time + accession/version + amendment/restatement + minimal sufficient set + numerical executability + calibrated entitlement。**目前没有成熟工作完整组合这七项**——这是真正的机会窗口。

### 8.3 表示差距（corpus representation）

当前 evidence unit：`concept value unit start end filed form accession`（[`run.py:163`](../submodules/ecoquant/experiments/a11_retrieval/run.py#L163)）。

自然语言问题 → XBRL concept 存在巨大语义断层：

```
"What was capital expenditure?"  →  PaymentsToAcquirePropertyPlantAndEquipment
```

简单 dense/BM25 在这种表示上失败，**不一定说明金融检索极难，也可能说明表示不合理**。真实 evidence unit 应包含：

```text
XBRL concept / human label / taxonomy definition / statement type /
calculation relationships / period type (instant/duration) /
issuer-specific aliases / table title / row label / surrounding rows /
filing section / version lineage
```

然后系统性比较：raw XBRL → label-enriched → definition-enriched → taxonomy-graph-expanded → full table context → hierarchical document/table/fact retrieval。**这本身就可形成一项扎实的研究（Paper 2 的 retrieval 组件）。**

### 8.4 风险控制差距（[12] Conformal Risk Control）

当前 calibration（`finvest/calibration/leak_free.py`）是经验型（AUROC/ECE/Brier/risk-coverage curve），**无有限样本保证**。Conformal Risk Control（CRC）为控制一般 monotone loss 提供有限样本框架 [12]。

**FinVEST 机会**：把 loss 定义成

```
L = w1·L_wrong_answer + w2·L_missing_evidence + w3·L_wrong_version + w4·L_numerical_inconsistency + w5·L_unnecessary_review
```

对 route threshold 提供统计保证。这是 Paper 3 的核心。

### 8.5 公平性与社会科学（[11] Fuster et al.）

[11] 表明某些 ML credit models 预测更强但可能扩大群体差异。FinVEST 当前未研究：谁更容易被 REVIEW、谁的文档更容易被检索、小公司是否覆盖更差、非标准 fiscal year 是否被系统性误判、非美国公司是否受 taxonomy disadvantage、新手是否过度信任 verifier。**这需要真实 human study（Paper 4）。**

### 8.6 系统性差距汇总表

| 维度 | 最强基线 | FinVEST 差距 | 补法 |
|---|---|---|---|
| Benchmark | FinanceBench 10k [1] | 19 cases | Phase 1 到 2,000+ |
| Retrieval | HiREC hierarchical [4] | flat + 弱表示 | hierarchical + 表示增强 |
| Set selection | SURE-RAG sufficiency [6] | scaffold + gold-conditioned + space mismatch | learned selector + requirement induction |
| Risk | CRC [12] | 经验型无保证 | conformal risk control over defined loss |
| Fairness | Fuster et al. [11] | 未研究 | human study + 分组分析 |
| Human | [10] Generative AI at Work | E6 planned only | preregistered workflow experiment |

### 8.7 与现有工作区计划的差距（workspace recon）

`_research_program/planning/` 的 E0-E8 计划**与审计的 4 篇论文策略/90 天计划存在结构性差距**：

| 维度 | 现有工作区计划 | 审计/参考文件要求 |
|---|---|---|
| 论文分解 | 单一 MSc 应用 + “eventually a workshop paper”（blueprint:14,162-168） | 4 篇独立论文，各自有数据集/方法/统计/验收 |
| hierarchical retrieval | **不存在**（E1 是 flat hybrid） | 核心方法贡献 |
| requirement induction | **不存在**（最接近的是 E7 的 facts/inferences 分离） | 核心方法贡献 |
| learned selector（VISTA） | **不存在**（只有可选 “learned or rule-based query routing”） | 核心方法贡献 |
| conformal risk control | 存在但 **E5 经验结果被 INVALIDATED**，leak-free rerun 只是小样本 pilot | 需 leak-free 重新建立证据 |
| 90 天时间盒 | **不存在**（IMPLEMENTATION_ROADMAP 是 milestone，非 deadline） | 需把 90 天计划叠加到 milestone 之上 |
| human study | 有完整协议（HUMAN_REVIEW_PROTOCOL.md）但 **未执行**；单一 primary reviewer | 需执行 + 外部第二 reviewer |
| 统计协议 | **很强**（cluster bootstrap 10k、≥3 seeds、Holm、BCa）—— 这是优势 | 保留 |
| claim 治理 | 很强（E5 泄漏被自查作废）—— 这是优势 | 保留 |

**结论**：工作区计划在**测量完整性与 claim 治理**上是罕见的强；但**方法创新面与论文拆解**需要按参考文件 §9 重建。90 天计划的起点正是把参考文件 Phase 0-3 叠加到现有 milestone 结构上。

---

## 9. 顶会路线与四篇论文策略

### 9.1 顶会准备度与潜力

| 目标 | 当前准备度 | 优化后潜力 | 关键条件 |
|---|---|---|---|
| ICAIF / FinNLP | 4/10 | **8/10** | P0 修复 + 300-500 高质量案例 |
| SIGIR / WWW | 2.5/10 | **8/10** | hierarchical retrieval + requirement induction + 大规模实验 |
| ACL / EMNLP | 2/10 | **7/10** | 2,000+ 问题 + 强语言模型/检索基线 + 对照 |
| KDD | 2/10 | **7/10** | 学习方法 + 大规模实验 + temporal/graph + ablation |
| NeurIPS / ICLR | 1/10 | **5-7/10** | 形成一般理论（risk-controlled entitlement）+ 跨域验证 |
| FAccT / CHI | 2/10 | **7/10** | 真实 human study |
| 顶级 Finance journal | 1/10 | **4-6/10** | 经济机制 + 真实结果变量（见 §10） |

### 9.2 四篇论文策略（采纳审计拆分，补充定位）

**Paper 1 — Benchmark**（目标 ICAIF / SIGIR / ACL dataset track）
> **FinVEST: A Version- and Time-Aware Benchmark for Minimum-Sufficient Financial Evidence Retrieval**
- 贡献：benchmark、evidence packages、version/amendment challenges、benchmark audit。
- 前置：P0 修复 → FinVEST-Pilot (300-500) → FinVEST-V1 (2,000+)。

**Paper 2 — Method**（目标 SIGIR / WWW / ACL / KDD）
> **VISTA-Fin: Version-Aware Minimum-Sufficient Evidence Set Selection for Financial QA**
- 贡献：requirement induction、hierarchical retrieval、learned set selector、version-aware graph。
- 前置：真正的 learned selector（非 scaffold）+ 统一 requirement/coverage 空间。

**Paper 3 — Risk**（目标 NeurIPS / ICLR / UAI）
> **Evidence Entitlement: Risk-Controlled Selective Answering for High-Stakes RAG**
- 贡献：entitlement 形式化、no-oracle verifier、finite-sample risk control、cross-domain evaluation。
- 前置：gold-free routing 重写 + CRC loss 定义 + 金融/法律/医疗跨域。

**Paper 4 — Human & Governance**（目标 CHI / FAccT / CSCW）
> **When Should Analysts Trust Financial AI? Evidence Presentation, Automation Bias and Selective Deferral**
- 贡献：human study、novice/expert 异质性、governance、社会后果。
- 前置：E6 真实 human study（preregistered）。

下游 green-bond / lending 系统 → 第五篇 systems/case-study，**不挤进第一篇**。

---

## 10. 金融科研部分

> 这是“金融科研部分核心参考”的重点章节：把技术系统升格为**真正的金融研究**。

### 10.1 现状判断

FinVEST 当前是**金融域内的可信 IR + 验证系统**，不是 finance research。缺三样：
1. **经济机制**：为什么信息错误会传导到估值/信贷/风险？
2. **真实结果变量**：valuation error、credit decision、analyst forecast、risk outcome。
3. **行为/组织后果**：人类分析师如何使用、是否过度依赖、组织是否采纳。

### 10.2 可证伪的金融研究问题（从技术误差映射到金融结果）

**研究问题族 A：信息质量 → 定价/估值**
- A1. 错误 filing version 导致多大的 **valuation error**？
- A2. stale evidence 如何改变 **credit decision** 与违约预测？
- A3. 缺失证据（非标准 fiscal year、小公司）是否系统性偏向特定公司类型？

**研究问题族 B：AI 辅助 → 分析师行为**
- B1. 更好的证据系统是否**降低 analyst dispersion**（分歧度）？
- B2. 是否**缩短 earnings analysis 时间**，且不损失准确率？
- B3. 自动 REVIEW 是否产生**过度保守**和资本配置延迟？
- B4. 分析师是否对 verifier 的 confidence 产生 **automation bias** / 校准失调？

**研究问题族 C：披露 → 战略行为**
- C1. 公司是否会**战略性改变披露结构**以适应 AI parsing（goodharting）？
- C2. 更透明的 evidence package 是否改变信息不对称结构？

**研究问题族 D：治理 → 责任**
- D1. 谁承担错误？哪些群体被 REVIEW/ABSTAIN 得更多（**公平性**）？
- D2. 机构采纳证据验证 API 的**责任边界与监管映射**（EU AI Act / financial regulation）？

### 10.3 经济模型链接（把 engineering metric 映射为 economics）

建议把 FinVEST 的指标映射到**标准金融变量**：

| FinVEST 技术指标 | 金融后果变量 | 数据来源 |
|---|---|---|
| wrong-version error rate | valuation error（相对 DCF/可比估值） | 分析师估值复现 |
| stale-evidence rate | credit decision 差异 | 贷款审批模拟 |
| evidence completeness | analyst forecast accuracy / dispersion | I/B/E/S |
| REVIEW rate × decision latency | capital allocation delay | 流程模拟 |
| REJECTION of amendment | restatement 冲击 | SEC RESTATED filings |

### 10.4 推荐的研究顺序

1. **先做技术上可证伪的**：错误版本/过期证据 → 估值误差（用可复现的 DCF 或可比公司估值）。
2. **再做行为研究**：E6 human study（学生 → CFA 考生 → 初级分析师 → 资深从业者）。
3. **最后做市场/组织**：需要数据合作（I/B/E/S、信贷数据、机构工作流）。

> 只有到这一步，项目才开始具备 **finance-journal 潜力**（4-6/10）。

---

## 11. 个人发展与科研反馈环

### 11.1 双向反馈

```text
金融学习（CFA、财务报表、XBRL、会计定义）
→ 更准确的问题定义与计算程序
→ 更高质量 benchmark
→ 更强 verifier
→ 更深入金融理解
→ 更好的研究问题
```

学习 CFA、财务模型、AI 与研究写作时，都可反向补充 FinVEST。对爱尔兰（UCD/Trinity/DCU）跨学科博士申请尤其合适：AI/CS 导师 + Finance/Business 导师 + Regulation/IS 导师三方。

### 11.2 最大个人风险（须持续自我检查）

> **用不断增加仓库、adapter、manifest 和 CI，代替真正困难的金融和科学问题。**

每个新工具/新仓库必须回答：
1. 它减少了哪个**真实研究误差**？
2. 它提高了哪个**正式指标**？
3. 它产生哪个**论文表格**？
4. 它服务哪个**真实用户**？
5. 删除它后，论文结论会不会变化？

若五个答案都是“不会”，**不应进入主研究路径**。

### 11.3 申请叙事（把“做了很多仓库”改写为研究问题）

> 一个清楚的研究问题、三个可证伪假设、一套逐步验证计划。

示例：
- **研究问题**：金融 AI 能否在有限样本风险保证下判断自己是否“有权回答”？
- **假设 H1**：版本/时间感知的层次化检索显著优于 flat 检索（held-out issuer 上 Recall@K）。
- **假设 H2**：learned set selector 在 no-oracle 设置下显著优于 greedy scaffold（set-level sufficiency）。
- **假设 H3**：conformal risk control 能在指定风险下提供有效覆盖（finite-sample guarantee）。
- **验证计划**：FinVEST-Pilot → V1 → 统计协议（issuer-cluster bootstrap + seeds + Holm）。

---

## 12. 诚实规则与风险登记

### 12.1 诚实规则（沿用 governance，强化）

1. 每个 claim 携带 evidence status。
2. 无 SOTA 声称（除非强神经基线公平对比）。
3. 无“eliminates hallucinations / production-ready / proven investment model”。
4. 无“reduces analyst workload”除非 E6 完成。
5. 无“statistically significant”除非写明方法（bootstrap、seeds、effect size）。
6. 无“generalises to finance”除非跨数据集证据。
7. 负结果也是 claim，有自己的证据文件。
8. 永远 REVIEW 的系统安全但无用——**报告 coverage 时必带 precision**（A11 selective 块已做）。
9. **生产 schema 与 evaluator 物理分离**（P0-1 修复后强制）。
10. **review/abstain 指标不得是恒真逻辑**（P0-2 修复后强制）。

### 12.2 风险登记（新增）

| 风险 | 等级 | 缓解 |
|---|---|---|
| 继续在错误的 routing/selector 上产出数字 | **高** | P0 修复先行，修复前所有相关数字 INVALIDATED |
| 把 corpus 规模当 benchmark 规模 | 高 | 明确定义 question-level benchmark |
| 过度投资仓库治理而荒废科学问题 | 中 | §11.2 五问 |
| 单一 issuer/模板上的假泛化 | 高 | issuer/time/template 多重 holdout |
| 人力标注质量不足 | 中 | 20-30% 双标 + adjudication + qualification test |
| 概念字典过小导致检索假阴性 | 中 | 表示增强（label/definition/taxonomy）而非只调检索 |

---

## 13. 设计建议

> 完整设计见 [RESEARCH_DESIGN_AND_PLAN.md](RESEARCH_DESIGN_AND_PLAN.md)。本节是**架构级**要点。

### 13.1 系统架构：生产与评价物理分离（P0-1 的强制结构）

```text
Production system:
  question + cutoff + corpus
  → retrieval (R1-R4, 增强表示)
  → requirement induction (从问题推断, 非 gold)
  → evidence selection (S1-S3 + learned VISTA, 统一空间)
  → verification (V1-V3)
  → route (ANSWER / REVIEW / ABSTAIN)
  → audit / dossier

Evaluator (完全隔离):
  prediction + hidden human label
  → metrics (correctness, review precision, false-review rate, utility)
```

强制测试：
```text
test_route_invariant_to_gold_answer_mutation
test_selector_invariant_to_gold_evidence_mutation
test_production_schema_contains_no_gold_fields
test_review_metric_not_tautological
test_heldout_issuer_never_used_in_training
test_evidence_id_requirement_space_alignment
test_no_gold_import_in_production_modules
```

### 13.2 数据层设计

- evidence unit 从 7 字段扩为 17+ 字段（§8.3）。
- 问题分类 15 类（§14 Phase 1）。
- 数据集冻结为**软件基础设施**（Data Cards 思想 [9]）：每个构建阶段留决策、来源、版本记录。

### 13.3 方法层设计

- **R 层**：hierarchical（entity → filing-family → accession/version → section/table → fact）；flat vs hierarchical ablation。
- **I 层（Requirement Induction）**：从问题预测 required metric/periods/documents/operation/version constraints/supporting concepts——**不读 gold requirement graph**。
- **S 层**：learned set selector（question repr + predicted requirements + candidate evidence + temporal/version features → evidence subset + completeness + minimality + conflict score）。
- **V 层**：联合 `P(answer correct and supported | q, E, t, v)` 而非堆叠二元规则。
- **Risks 层**：CRC over 定义好的 loss（§8.4）。

### 13.4 治理/CI 层设计

- hub 增加**治理专用 CI**（G-2）：
```text
verify every submodule commit exists
verify .gitmodules and lock file agree
verify no dirty submodule
verify referenced experiment artifacts exist
verify claim matrix references valid SHAs
verify core and integration CI status
verify generated docs are current
```
- 修复 Integration CI 失败（先看 pinned commit 是否可达/依赖是否安装）。

---

## 14. 90 天执行计划

> 目标不是“增加更多仓库”，而是：**获得第一张完全无 target leakage、可重复、能够区分方法优劣的主实验表。**

### Phase 0：立即修复科研有效性（第 1-2 周）—— 最高优先级

1. **作废** A11 的 routing/review metrics（标 `INVALIDATED_PENDING_GOLD_ISOLATION_FIX`）。
2. 重写 routing：`case_answerable` 不得读 `gold_answer`。answerability 改为从 requirement induction + verification 推断。
3. 修复 REVIEW 恒真：`correct = gold_route != "ANSWER" or True` → 定义真实正确性（REVIEW 正确 = 确实需要复核）。
4. 修复 selector：统一 requirement/coverage 空间；requirements 由问题推断。
5. 重写 LOIO：真 held-out issuer fold（train 5 → test 1，报 held-out 指标）。
6. 修复 Integration CI；为 hub 增加 governance CI（G-2）。
7. 增加 7 个回归测试（§13.1）。
8. 修复 E0 测试（FinanceBench cache 缺失 → 正确 skip 而非 fail）。

**产出**：一条 gold-free 的生产路径 + 一套能拦住回归的测试。

### Phase 1：FinVEST-Pilot benchmark（第 3-6 周）

1. 生成 **300 个 challenge-rich cases**（15 类问题覆盖）。
2. 扩展到 **20-30 issuers**（10-K / 10-Q / 8-K / 10-K/A / amended/restated）。
3. 完成强检索基线：BM25、dense bi-encoder、cross-encoder reranker、ColBERT/late-interaction、hybrid RRF、taxonomy-expanded、flat vs hierarchical。
4. 加入 label/definition/taxonomy context（表示增强）。
5. 全部 challenge/high-risk cases 双标 + adjudication；报告 IRR。

### Phase 2：方法实现（第 7-10 周）

1. question-to-requirement induction（非 gold）。
2. 非 gold set selector + 统一空间。
3. no-oracle verifier（routing 不读 gold）。
4. 冻结 benchmark pilot（FinVEST-Pilot 版本）。

### Phase 3：正式实验协议（第 11-13 周）

1. 五个 seeds + issuer/time/filing-family/template/concept-family 多重 holdout。
2. 统计分析：issuer-cluster bootstrap、per-issuer macro、paired tests、Holm、CI。
3. 写 Paper 1 第一版（benchmark）。
4. 招募第二标注者：annotation guide + qualification test。

**90 天验收标准**：主实验表包含（a）retrieval recall/MRR/nDCG（flat vs hierarchical）；(b) set-level sufficiency 指标；(c) routing 的 coverage/selective-risk/utility；(d) 统计检验；全部在无泄漏生产路径上、可复现、能区分方法优劣。

---

## 15. 参考文献

> 来自审计的 Consensus 核心文献，编号保留；补充 [15]-[17]。

[1] Islam P, et al. FinanceBench. *ArXiv*, 2023. 258 cites.
[2] Choi C, et al. FinAgentBench. *ACM ICAIF*, 2025. 26 cites.
[3] Choi C, et al. FinDER. *ACM ICAIF*, 2025. 23 cites.
[4] Choe J, et al. Hierarchical Retrieval with Evidence Curation for Open-Domain Financial QA. *ACL*, 2025, pp. 16663-16681.
[5] Arun A, et al. FinReflectKG-MultiHop. *ArXiv*, 2025.
[6] Qiu J, Han Z, Huang C. SURE-RAG. *ArXiv*, 2026.
[7] Kapoor S, Narayanan A. Leakage and the reproducibility crisis in ML-based science. *Patterns*, 2023. 762 cites.
[8] Hutchinson B, et al. Towards Accountability for ML Datasets. *FAccT*, 2020. 330 cites.
[9] Pushkarna M, et al. Data Cards. *FAccT*, 2022. 355 cites.
[10] Brynjolfsson E, Li D, Raymond L. Generative AI at Work. *SSRN*, 2023. 1,336 cites.
[11] Fuster A, et al. Predictably Unequal? *Journal of Finance*, 2020. 572 cites.
[12] Angelopoulos A N, et al. Conformal Risk Control. *ArXiv*, 2022. 303 cites.
[13] Capponi A, et al. Decentralized Finance: Protocols, Risks, and Governance. *Foundations and Trends*, 2023. 22 cites.
[14] Černevičienė J, Kabašinskas A. XAI in Finance: a systematic literature review. *Artificial Intelligence Review*, 2024. 226 cites.
[15] Fuster A, Goldsmith-Pinkham P, Ramadorai T, Walther A. Predictably Unequal? (peer-reviewed version) — credit ML 公平性。
[16] Bates S, et al. Distribution-Free, Risk-Controlling Prediction Sets. *JACM*, 2021 — CRC 的理论基础。
[17] Devlin J, et al. BERT（dense retriever 基础）/ Khattab & Zaharia. ColBERT（late interaction）。

---

*本参考文件由代码级验证生成。任何结论均可追溯到 `finvest-research`（含 submodules）中的文件与运行产物。*
