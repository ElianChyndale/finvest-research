# FinVEST 科研设计 + 执行计划

> **Design & Execution Plan based on [FINVEST_RESEARCH_REFERENCE.md](FINVEST_RESEARCH_REFERENCE.md)**
>
> 本文件把参考文件中的判断转化为**可执行的架构设计与按周计划**。核心目标：在 90 天内获得第一张**完全无 target leakage、可复现、能区分方法优劣的主实验表**。
>
> 状态基准：`finvest-research@97ddb4c`，`ecoquant@6493165`，2026-08-07。

---

## 一、设计原则

1. **先修证明链，再跑数字**。任何 P0 修复之前跑出的 routing/selector/review 数字一律 `INVALIDATED_PENDING_GOLD_ISOLATION_FIX`。
2. **生产与评价物理分离**。生产路径中 `ProductionCase` 不含任何 gold 字段；gold 只存在于隔离的 `EvaluationLabel`。
3. **每个新工具的入场券**（五问）：减少哪个真实误差 / 提高哪个正式指标 / 产生哪个论文表格 / 服务哪个真实用户 / 删除后结论是否变化。
4. **工程治理服务于科学问题**，不替代它。
5. **所有数字可复现**：commit、config hash、dataset hash、seed、split 全部入档。

---

## 二、目标系统架构

### 2.1 生产流水线（gold-free）

```text
ProductionCase { question, issuer, target_period, source_cutoff, target_fiscal_year }
        ↓
[I] Requirement Induction       从问题推断: metric, periods, documents, operation,
                                version constraints, supporting concepts
        ↓                        (绝不读 gold requirement graph)
[R] Hierarchical Retrieval      entity → filing-family → accession/version
                                → section/table → fact
        ↓                       (R1 BM25 / R2 dense / R3 RRF / R4 concept-temporal
                                 / R5 label-definition-enriched / R6 hierarchical)
[S] Learned Set Selector        question repr + predicted requirements + candidates
        ↓                       + temporal/version features → subset + scores
[V] Joint Verifier              P(answer correct & supported | q, E, t, v)
        ↓                       (temporal/version + numerical executability)
[Risk] Risk Control             conformal / CRC over defined loss → threshold
        ↓
ANSWER / REVIEW / ABSTAIN
        ↓
audit / dossier / evidence package
```

### 2.2 隔离的 Evaluator

```text
EvaluationLabel { gold_answer, acceptable_evidence_sets, gold_route,
                  conflict_labels, minimal_evidence_sets }
        ↓
prediction + hidden label → correctness, review precision, false-review rate,
abstain precision/recall, coverage, expected utility
```

### 2.3 强制回归测试（新增，全部纳入 CI）

| 测试 | 拦截什么 |
|---|---|
| `test_route_invariant_to_gold_answer_mutation` | 改 gold_answer 不影响 route |
| `test_selector_invariant_to_gold_evidence_mutation` | 改 gold evidence 不影响 selector |
| `test_production_schema_contains_no_gold_fields` | ProductionCase 无 gold 字段 |
| `test_review_metric_not_tautological` | REVIEW 不再恒真 |
| `test_heldout_issuer_never_used_in_training` | LOIO 训练/测试分离 |
| `test_evidence_id_requirement_space_alignment` | coverage/requirement 同空间 |
| `test_no_gold_import_in_production_modules` | 生产模块无 gold import |
| `test_a11_set_selection_nondegenerate` | S2/S3/S4 不再空集（新） |

---

## 三、模块级设计

### 3.1 Requirement Induction（新增模块）

```text
question
  → parse metric entity (概念/别名)
  → parse period (target FY, duration/instant)
  → parse documents (10-K / 10-Q / 8-K / 10-K/A)
  → infer operation (sum/avg/delta/pct — 从语义)
  → infer version constraints (as-of / latest / as-filed)
  → output RequirementGraph { mandatory nodes, optional nodes }
```

实现路线：先规则 + 概念字典增强（2-4 周），再小模型微调（FinanceBench/FinDER 训练 + FinVEST 验证）。**与 gold requirement graph 物理隔离**。

### 3.2 统一 Requirement/Evidence 空间（P0-3 修复）

当前 bug：`CoverageModel({evidence_id: {evidence_id}})` 与 `requirements = {concept}` 语义不同空间。

修复：定义**统一概念空间**，两种映射都进概念空间：
```python
coverage: concept_id -> {concept_id}            # 概念级覆盖
evidence_concept_map: evidence_id -> concept_id # 每个 evidence 属于一个概念
# selector 输入用 concepts，输出映射回 evidence_id
```

或者直接用 evidence_id 空间 + 概念标签作为 evidence 的特征。**二选一，测试锁定。**

### 3.3 Learned Set Selector（替换 scaffold）

```text
Input:  question embedding, predicted RequirementGraph embedding,
        candidate evidence embeddings (含 temporal/version features)
Architecture: set scoring head (e.g., small transformer/graph)
Loss:  set-level sufficiency (coverage of requirements) + minimality
       + conflicts, 用 oracle 上界做 upper-bound 对照
```

先跑通 **non-gold oracle**（真 gold coverage，仅作上界），再训练 learned。**VISTA-Fin 名字保留给 learned 版本**，scaffold 阶段不对外宣称 novelty。

### 3.4 真正的 LOIO（P0-5 修复）

```text
for fold in 6 issuers:
    train/calibrate on other 5 issuers
    test ONLY on held-out issuer
report: held-out Recall@K, completeness, routing risk,
        macro mean ± CI (issuer-cluster bootstrap), per-fold table
```

### 3.5 Risk Control（Paper 3 前置）

**当前真实状态（recon 验证）**：仓库已有真正的 Platt calibrator + 嵌套 LOIO 校准协议 + split-conformal quantile gate（`src/ecoquant/uncertainty/`）。但：
- 从未在 held-out 数据上**验证有限样本 coverage**（无 coverage-vs-alpha 检查）；
- `max_selective_error` 阈值选择是**校准启发式**，不是风险保证；
- **没有决策损失/效用目标**（grep 全库 `expected_utility|decision_loss|review_cost|abstain_cost` 只在文档字符串中）——abstain-vs-answer 是固定阈值 gate，不是 expected-utility argmax；
- `finvest/calibration/leak_free.py` 的 A6-A8（leak-free 特征、robustness、transfer）**实现但从未在数据上执行**。

**升级方向**：定义损失并用 conformal/RCPS-style 构造提供已验证的 coverage：

```python
L = w1 * L_wrong_answer        # 错误答案
  + w2 * L_unsupported_answer  # 无证据支持却回答
  + w3 * L_wrong_version       # 版本错误
  + w4 * L_numerical_inconsistency
  + w5 * L_unnecessary_review  # 过度 REVIEW 成本
```
用独立 calibration split 拟合 threshold，CRC 提供有限样本保证 [12]。并增加 `test_conformal_heldout_coverage_meets_alpha`。

### 3.6 治理 CI（G-2，hub 新增）

```yaml
verify every submodule commit exists
verify .gitmodules and lock file agree
verify no dirty submodule
verify referenced experiment artifacts exist
verify claim matrix references valid SHAs
verify core and integration CI status
verify generated docs are current
```

---

## 四、按周执行计划（90 天）

### Phase 0：修复科研有效性（第 1-2 周）

**第 1 周**
- [x] 建立本文档与参考文件（本任务产出）
- [ ] 作废 A11 routing/review/selector 数字（状态文件更新）
- [ ] 重写 routing：删 `run.py:315` 的 gold 读取 → 键 `sufficiency_label`/`answer_type`（sealed case 已有这些非 gold 字段，见参考 §3.1 关键新发现）
- [ ] 修复 REVIEW 恒真：`run.py:509` 定义真实正确性
- [ ] **修复数值验证 `subtract` bug**：`calculate.py:135` 增加 `subtract` 操作（及派生所需 op），否则真实 cashflow 案例恒 REVIEW（参考 N-1）
- [ ] 统一 requirement/coverage 空间 + 修复 S4 退化（S4 必须用真 gold coverage 作上界，见参考 §3.3）
- [ ] 新增 8 个回归测试（§2.3）

**第 2 周**
- [ ] 重写 LOIO：真 held-out fold（train 5 → test 1，报 held-out 指标）
- [ ] **AMENDS 接入生产验证**：`latest_valid_version` 在 A11 管线中调用（参考 N-2）
- [ ] 对抗 mutation 改造为字段级 + 接入实验（参考 N-3）
- [ ] 修复 Integration CI 失败（根因：hardcoded git+https 安装 financial-ai-contracts@4b232218；lock 三处复制无校验）；为 hub 增加 G-2 governance CI
- [ ] 修复 E0 测试（cache 缺失 → 正确 skip）
- [ ] **修复标注 hash**：SOLO_ANNOTATIONS 更新为全包 SHA-256（参考 N-4）
- [ ] **清除 E5 过期 claim 残留**：`RESEARCH_PROGRAMME_OVERVIEW.md:51`、`E5_CALIBRATION_SELECTIVE.md` 删除 0.923、写入 0.719 基线（参考 N-5）
- [ ] 全量测试通过 + 本地重跑 A11 确认新路径 gold-free
- [ ] 更新 claim-evidence matrix 与 status.json

**验收（Phase 0）**：一条 gold-free 生产路径 + 回归测试全部绿 + 旧数字全部标记 INVALIDATED_PENDING_GOLD_ISOLATION_FIX。

### Phase 1：FinVEST-Pilot（第 3-6 周）

**第 3 周**
- [ ] 定义 15 类问题分类 schema + 生成器扩展
- [ ] 从 6 issuer → 20-30 issuer 扩展（10-K/10-Q/8-K/10-K/A/amended/restated）
- [ ] annotation guide + qualification test 第一版

**第 4 周**
- [ ] 300 challenge-rich cases 生成（覆盖 15 类）
- [ ] 表示增强：evidence unit 加 human label / taxonomy definition / statement type / table context（§参考 8.3）
- [ ] 双标协议：20-30% 双标 + high-risk 100% 双标 + adjudication

**第 5 周**
- [ ] 强检索基线：BM25、dense bi-encoder、cross-encoder、ColBERT、RRF、taxonomy-expanded
- [ ] flat vs hierarchical ablation 框架
- [ ] R5 label-definition-enriched、R6 hierarchical 实现

**第 6 周**
- [ ] Pilot 冻结（FinVEST-Pilot v1）
- [ ] 报告 IRR（双标一致性、confusion matrix、adjudication 原因）
- [ ] 集成 adapter 扩展（contracts schema v2）

**验收（Phase 1）**：300+ 案例、20-30 issuer、双标子集、6+ 检索基线、表示增强。

### Phase 2：方法实现（第 7-10 周）

**第 7-8 周**
- [ ] Requirement Induction v1（规则 + 字典增强），gold-free
- [ ] Learned set selector v1（small head），与 scaffold 对照
- [ ] 统一空间 selector 上线，S4 用真 gold coverage 作上界

**第 9 周**
- [ ] No-oracle verifier：联合 `P(correct & supported | q,E,t,v)`
- [ ] CRC risk control v1（定义 loss + calibration split）

**第 10 周**
- [ ] FinVEST-Pilot 冻结 v2
- [ ] 初版统计协议：issuer-cluster bootstrap、seeds、Holm
- [ ] 论文表格模板（Paper 1 所需）

**验收（Phase 2）**：gold-free 全链路；learned selector 有初步结果；CRC 有 coverage/risk 曲线。

### Phase 3：正式实验（第 11-13 周）

**第 11 周**
- [ ] 五个 seeds + 多重 holdout（issuer/time/filing-family/template/concept-family/amendment/cross-market）
- [ ] 全基线重跑（flat vs hierarchical、有无 reranker、有无表示增强）

**第 12 周**
- [ ] 统计分析完整：bootstrap CI、per-issuer macro、paired tests、Holm correction
- [ ] 主实验表生成（retrieval / set / verification / routing / utility 五层）

**第 13 周**
- [ ] Paper 1 第一版（FinVEST benchmark）
- [ ] annotation guide + qualification test 发布给第二标注者
- [ ] 90 天复盘 + 更新参考文件

**验收（Phase 3）**：主实验表无泄漏、可复现、能区分方法优劣。

---

## 五、90 天后的路线

| 时间 | 里程碑 | 产出 |
|---|---|---|
| 90 天 | 主实验表 + Paper 1 初稿 | ICAIF / SIGIR dataset track 投稿 |
| 6 个月 | VISTA-Fin learned selector + hierarchical retrieval 完整 | Paper 2 投稿（SIGIR/WWW/ACL/KDD） |
| 8 个月 | CRC risk control + 跨域验证（法律/医疗 pilot） | Paper 3 投稿（NeurIPS/ICLR/UAI） |
| 10 个月 | E6 preregistered human study | Paper 4 投稿（CHI/FAccT/CSCW） |
| 12-24 个月 | Financial Evidence Verification API wedge product | 产品化（retrieve/verify/route/audit 四 API） |

---

## 六、资源与依赖

- **算力**：ColBERT/cross-encoder 需要 GPU 或云端（见 `_research_program/planning/COMPUTE_AND_COST_PLAN.md`）。
- **数据**：SEC companyfacts + full 10-K（公开，cache-only）；FinanceBench 公开样本（需 cache）；I/B/E/S 等机构数据（后期，需许可）。
- **人力**：第二标注者（annotation guide + qualification test 先行）；金融领域顾问（UCD/Trinity 导师或 CFA 同行）。
- **风险缓解**：见参考文件 §12.2 风险登记。

---

## 七、与现有工作区计划的衔接

`_research_program/planning/` 的 E0-E8 计划在**测量完整性与 claim 治理**上很强（cluster bootstrap、≥3 seeds、Holm、E5 自查作废），但**方法创新面与论文拆解**需按本计划重建：

| 现有计划项 | 本计划动作 |
|---|---|
| E1 flat hybrid retrieval | 升级为 hierarchical retrieval（新增） |
| E5 经验校准（被作废） | 改为 leak-free CRC risk control（§3.5） |
| 单一 workshop-paper 目标 | 拆为 4 篇论文（参考 §9） |
| IMPLEMENTATION_ROADMAP（milestone 非 deadline） | 叠加 90 天时间盒（本计划 §四） |
| E6 人类研究（仅协议） | Phase 4 执行（24-30 reviewer 需外部招募） |
| claim 治理（强） | **保留**，并加 hub governance CI（G-2）收口 |

## 八、验证来源

本设计与计划中的每个判断均可追溯到：

| 判断 | 来源 |
|---|---|
| P0-1..P0-6（路由 gold、REVIEW 恒真、gold requirements、VISTA scaffold、LOIO、CI） | [FINVEST_RESEARCH_REFERENCE.md](FINVEST_RESEARCH_REFERENCE.md) §3.1-3.6（代码行号） |
| N-1..N-5（`subtract` bug、AMENDS 未执行、对抗 mutation、hash 缺陷、E5 残留） | 参考 §3.7（recon 验证） |
| 现有工作区计划差距 | 参考 §8.7（workspace recon） |
| 校准层真实状态 | 参考 §5.2 + 计划 §3.5（recon 验证） |

> 首次运行本计划 Phase 0 之前，请先阅读参考文件 §3（已验证科研状态）以确认修复目标的代码位置。

---

*本文档与 FINVEST_RESEARCH_REFERENCE.md 配套使用。计划以周为粒度，可按实际进度调整，但 Phase 0 → Phase 1 → Phase 2 → Phase 3 的顺序不变。*
