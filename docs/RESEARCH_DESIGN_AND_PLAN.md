# FinVEST 科研设计 + 执行计划

> **Design & Execution Plan based on [FINVEST_RESEARCH_REFERENCE.md](FINVEST_RESEARCH_REFERENCE.md) + [FINVEST_RESEARCH_REFERENCE_2.md](FINVEST_RESEARCH_REFERENCE_2.md) + [FINVEST_RESEARCH_REFERENCE_3.md](FINVEST_RESEARCH_REFERENCE_3.md)**
>
> 本文件把参考文件中的判断转化为**可执行的架构设计与按周计划**。核心目标：在 90 天内获得第一张**完全无 target leakage、可复现、能区分方法优劣的主实验表**。
>
> **战略定位（文件 2）**：`Risk-Controlled, Version-Aware Minimum Sufficient Evidence Systems`。首篇论文收缩为 `When Is Evidence Enough? Version-Aware Minimum Evidence Sets and Risk-Controlled Abstention for Long Financial Documents`——只做金融文档。
>
> **方向升级（文件 3）**：`Risk-Controlled Sequential Evidence Acquisition and Certification`。文件 2 的 Evidence Entitlement 是序贯决策的静态特例；文件 3 把 `继续检索 / 请求人 / 停止` 作为一等动作（见 §3.7-3.9）。
>
> 状态基准：`finvest-research` 主分支，`ecoquant@6465fff`（P0-1..N-8 修复后），2026-08-07。P0 阶段已完成。

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
| `test_verify_never_reads_calculation_program` | **P0-9**：`_verify` 不再读 `calculation_program`（AST 扫描） |
| `test_production_path_never_reads_gold_adjacent_fields` | **P0-9**：生产路径不读 `requirement_graph/answer_type/sufficiency_label/decision_label` |
| `test_verify_decision_invariant_to_calculation_program_mutation` | **P0-9 Gate 0**：改变/删除 `calculation_program`，decision 不变 |
| `test_induce_program_subtract_cashflow` | **P0-9**：问题 → subtract(OCF, CAPEX) |
| `test_induce_program_extractive_no_op` | **P0-9**：抽取式问题无 operation |
| `test_induce_program_gold_free_contract` | **P0-9**：归纳模块只消费 question 字符串 |

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

### 3.7 Program Induction（P0-9，参考文件 3 §3-4）

**问题（新方向 Gate 0）**：production verifier 曾从 sealed case payload 读取 `calculation_program`（`run.py:492`）。该字段与 `gold_answer` 同处一个 payload，属于 oracle assistance。生产路径必须自己从问题归纳程序。

**已修复（2026-08-07）**：

```text
question
  → induce_program(question)                    # 仅消费问题字符串
  → { operation: subtract|sum|average|...,
      required_metrics: [OCF, CAPEX], ... }     # 可执行 symbolic program
  → verify_calculation(operation, evidence, required_concepts)
```

- 新增 `finvest/program_induction/induction.py`：复用公开概念字典 `_concepts_for` + finance-operators 词典（与 `calculate.FUNCTIONS` 对齐）+ FCFF 派生规则。
- 对 sealed 39 个 case 的行为等价性已验证：9 个 cashflow 归纳为 `subtract`、30 个抽取式无 operation，与 gold `calculation_program` **0 不一致**。
- 回归测试 9 项（§2.3），核心是 **mutation invariance**：改变/删除 `calculation_program`，production decision 不变。

**下一步**：规则基线已落地；小模型微调（FinanceBench/FinDER 训练 + FinVEST 验证）是 P3 里程碑，必须遵守同一 gold-free 契约。

### 3.8 Sequential Evidence Acquisition（参考文件 3 §5-6）

把一次性的 `retrieve → select → verify` 泛化为**序贯决策问题**：

```text
s_t = (q, E_t, G_t, V_t, B_t, H_t)
a_t ∈ { Retrieve, QueryExpand, FindVersion, FindAmendment,
        ReadTable, Calculate, Verify, AskHuman, Answer, Abstain }
```

- 目前 `run.py` 是**单步**路径（R1-R4 一次检索 → S 选择 → V 验证 → 路由）。后续把 `Answer` 之外的动作接到真正的"下一步证据"循环。
- 最小可行序贯：从 `FindVersion / FindAmendment` 开始（对应 §9.4 的版本冲突 pilot），再逐步引入 `Calculate / AskHuman`。
- 需要 trajectory 数据（state, action, next evidence, cost, review, outcome）；第一阶段用 synthetic action environment + oracle trajectories + heuristic policy，产品未来产生 real trajectories。

### 3.9 VOI Review Allocation（参考文件 3 §5.6）

把"人工复核成本"显式放进决策目标：

```python
max_π E[ U_correct − C_retrieval − C_compute − C_human − C_abstain − L_unsafe ]
s.t.  R_accepted(π) ≤ α
```

- 当前 `route_decision`（`has_evidence, joint_valid`）是确定性 gate，**没有成本项**。
- 升级路径：对 REVIEW 候选，按 **Value of Information**（`a* = argmax_a E(ΔU|a) − Cost(a)`）判断"补哪一条证据 / 谁审"信息价值最高，而不是一律 REVIEW。
- 直接服务当前 `18/19 REVIEW`（automation utility 极低）问题的 **Price of Safety / Price of Review** 研究。

---

## 四、按周执行计划（90 天）

### Phase 0：修复科研有效性（第 1-2 周）

**第 1 周**
- [x] 建立本文档与参考文件（本任务产出）
- [x] **P0-9 程序归纳**：新增 `finvest/program_induction/induction.py`；`_verify` 删除 `calculation_program` 读取，改用 `induce_program`（参考文件 3 §3-4）
- [x] **P0-9 回归测试**：mutation invariance + AST 扫描 + 归纳单元测试（§2.3 追加 9 项；全绿）
- [ ] 作废 A11 routing/review/selector 数字（状态文件更新）
- [ ] 重写 routing：删 `run.py:315` 的 gold 读取 → 键 `sufficiency_label`/`answer_type`（sealed case 已有这些非 gold 字段，见参考 §3.1 关键新发现）
- [ ] 修复 REVIEW 恒真：`run.py:509` 定义真实正确性
- [ ] **修复数值验证 `subtract` bug**：`calculate.py:135` 增加 `subtract` 操作（及派生所需 op），否则真实 cashflow 案例恒 REVIEW（参考 N-1）
- [ ] 统一 requirement/coverage 空间 + 修复 S4 退化（S4 必须用真 gold coverage 作上界，见参考 §3.3）

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
| N-1..N-8（`subtract`、AMENDS、对抗 mutation、hash、E5、camelCase、日期数字、输入概念） | 参考 §3.7 + reconciliation §二 |
| 现有工作区计划差距 | 参考 §8.7（workspace recon） |
| 校准层真实状态 | 参考 §5.2 + 计划 §3.5（recon 验证） |
| 战略方向、go/no-go、文献矩阵、仓库战略 | [FINVEST_RESEARCH_REFERENCE_2.md](FINVEST_RESEARCH_REFERENCE_2.md) + [RESEARCH_REFERENCE_RECONCILIATION.md](RESEARCH_REFERENCE_RECONCILIATION.md) |

> 首次运行本计划 Phase 0 之前，请先阅读参考文件 §3（已验证科研状态）以确认修复目标的代码位置。

---

## 九、文件 2 战略优化（POST-CFA 执行路线）

> 本节整合 [FINVEST_RESEARCH_REFERENCE_2.md](FINVEST_RESEARCH_REFERENCE_2.md) 的关键判断。完整差异见 [RESEARCH_REFERENCE_RECONCILIATION.md](RESEARCH_REFERENCE_RECONCILIATION.md)。

### 9.1 方向纪律（必须遵守）

1. **首篇论文收缩**为 `When Is Evidence Enough? ... Long Financial Documents`——**只做金融**，工业文档作为后续 external validity 或商业产品。
2. **撤销**以下表述：`"RAG + Verifier" 是创新`、`"拒答更安全" 是创新`、`set-level sufficiency 首次提出`（SURE-RAG 已做）。
3. 正确 gap：**版本约束 + 最小证据集 + 数值可执行 + 检索遗漏 + 人工复核成本统一到一个风险受控决策问题**。
4. **检索优先**：先解决 Recall@20，再开发 Verifier。当前 Recall@5≈0.08，是最大瓶颈。

### 9.2 Go/No-Go 门槛（10 个月，量化验收）

| 时间 | 门槛 | 未达成动作 |
|---|---|---|
| Month 2 | ≥50 个可复核 case | 停止算法开发，修 Benchmark |
| Month 3 | 第二标注者确定 | 无则降级 pilot |
| Month 4 | IAA ≥ 0.70 | 重写定义/界面 |
| Month 5 | **Recall@20 ≥ 0.70** | 论文转向 retrieval |
| Month 6 | all-required set recall ≥ 0.55 | 停止 calibration 主张 |
| Month 7 | coverage ≥ 20% @ ≤5% risk | 不得宣称自动化效用 |
| Month 8 | version holdout gain 成立 | 移除 version novelty |
| Month 9 | ≥1 显著且有实质效应 | 转 Benchmark/failure paper |
| Month 10 | 可独立复现 | 不投稿主会 |

**90 天计划与本表的衔接**：Phase 1（检索基线 + 300 case）对应 Month 2-5；Phase 2（方法）对应 Month 5-8；Phase 3（统计+论文）对应 Month 8-10。**Month 5 的 Recall@20≥0.70 是 Phase 1 的硬性验收**。

### 9.3 数据集目标（采用文件 2 的现实版）

| 维度 | 文件 1（V1） | 文件 2（现实） | 采用 |
|---|---|---|---|
| Issuers | 20-30 | 36-50 | 文件 2（分阶段：Phase 1 先 20-30，V1 到 36-50） |
| Cases | 2,000-5,000 | ~600（360 base + 120 multi + 120 conflict/insufficient） | **文件 2 优先**（人工可复核） |
| 双标 | 20-30% | 100-150 cases | 文件 2 |
| 版本冲突 | 15 类问题 | 50 版本冲突 pilot 先行 | 文件 2 |

### 9.4 50 个版本冲突 pilot（Phase 1 前置，文件 2 §1.10）

现有 challenge cases 已有 6 类 mutation（wrong-period/future-source/amendment/scale-sign/duplicate/insufficient）。按文件 2 扩展：
- **amended filing**（10-K vs 10-K/A 数值差异）；
- **restatement**（2024 原始 vs 2025 重述的 2024 比较值）；
- **point-in-time cutoff 语义**（"截至 2024-11-01" vs "最新已知值"）；
- **comparative figure from later filing**；
- **cross-version conflict**（同一事实不同版本数字矛盾）。

这 50 个 pilot 直接服务 Recall@20 与 version holdout 的验收。

### 9.5 仓库战略（三个月后目标，不打断当前）

文件 2 §3.5：公开 portfolio 只保留 4 个一线入口（`finvest-research` / `finvest-core` / `pdf-manager` / `auralynq`），内部工具合并为 `finvest-tooling/`。当前**不执行**（避免打断 Phase 1），作为 2026-10 的治理任务登记。

### 9.6 CFA 重置纪律

文件 2 §1.10：未来 15 天**不启动重大科研开发**，专注 CFA。只允许修复阻止 CI 运行的极小问题。**当前状态已满足**：P0/N 修复完成、4 个 CI 全绿、UPS 数据对齐。今天可建 `POST-CFA RESEARCH RESET` GitHub issue 记录 go/no-go 门槛。

---

*本文档与两份参考文件配套使用。计划以周为粒度，可按实际进度调整，但 Phase 0 → Phase 1 → Phase 2 → Phase 3 的顺序不变；go/no-go 门槛（§9.2）是硬性验收。*
