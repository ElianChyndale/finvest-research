# FinVEST 科研核心参考文件 3 — 序贯证据获取与认证（终极方向升级）

> **FinVEST Research Core Reference #3 — Risk-Controlled Sequential Evidence Acquisition and Certification**
>
> 本文档是 FinVEST 研究纲领的**方向升级参考文件**：把参考文件 2 确定的 `Risk-Controlled, Version-Aware Minimum Sufficient Evidence Systems` 再提升一层为 **Risk-Controlled Sequential Evidence Acquisition and Certification（风险受控的序贯证据获取与认证）**，并对新方向自带的新 P0 风险（`calculation_program` oracle dependency）做代码级审计与修复。
>
> **与参考文件 1/2 的关系**：
> - 文件 1（`FINVEST_RESEARCH_REFERENCE.md`）是**代码级现状审计**：回答"我现在是什么"。
> - 文件 2（`FINVEST_RESEARCH_REFERENCE_2.md`）是**战略决策**：回答"我应该成为什么"（minimum sufficient evidence + version + risk）。
> - **文件 3（本文）是方向升级 + 可执行落地**：回答"更高一层的研究问题是什么，且把上一个方向暴露出的新 P0 当场修掉"。文件 2 的 `Evidence Entitlement` 是文件 3 的一阶段特例（无主动获取动作、证据集合一次性给出）；文件 3 把它泛化为**序贯决策问题**。
>
> **验证基准**：`finvest-research` 主分支，`ecoquant@6465fff`（P0-1..N-8 修复后），2026-08-07。本文档中所有"已验证"判断标注 `文件:行号` 或产物路径。
>
> **配套文件**：
> - [FINVEST_RESEARCH_REFERENCE_2.md](FINVEST_RESEARCH_REFERENCE_2.md) — 战略决策版（唯一方向、103-source 文献矩阵、go/no-go 门槛）。
> - [RESEARCH_REFERENCE_RECONCILIATION.md](RESEARCH_REFERENCE_RECONCILIATION.md) — 三份文件的差异协调。
> - [RESEARCH_DESIGN_AND_PLAN.md](RESEARCH_DESIGN_AND_PLAN.md) — 可执行设计（已追加 §3.7 程序归纳 / §3.8 序贯获取 / §3.9 VOI 复核）。

---

## 目录

1. [文件定位与使用方式](#1-文件定位与使用方式)
2. [总判断：方向升级，且自带上一个方向的新 P0](#2-总判断)
3. [P0-9 代码级审计：`calculation_program` 仍是 oracle assistance](#3-p0-9-代码级审计)
4. [P0-9 修复：程序归纳（question → induced program）](#4-p0-9-修复程序归纳)
5. [新终极方向的形式化定义](#5-新终极方向的形式化定义)
6. [为什么这个方向比 Financial RAG 更能活 5 年以上](#6-为什么这个方向比-financial-rag-更能活-5-年以上)
7. [与参考文件 1/2 的一致性核对](#7-与参考文件-12-的一致性核对)
8. [五篇论文树与顶会路线](#8-五篇论文树与顶会路线)
9. [Go/No-Go 门槛（文件 2 的扩展）](#9-gono-go-门槛)
10. [十五大弱点与自我批评](#10-十五大弱点与自我批评)
11. [90 天执行计划（追加 P0-9 后）](#11-90-天执行计划)
12. [参考文献与文献信号](#12-参考文献与文献信号)

---

## 1. 文件定位与使用方式

**本文件回答四个问题：**

1. **上一方向（Evidence Entitlement）有哪些尚未解决的 P0 风险？** —— 代码级逐条核对。
2. **新方向的正式问题是什么？** —— 用状态、动作、证据证书、目标函数形式化（§5）。
3. **新方向相对旧方向增加了什么科学价值？** —— 从"静态选择充分证据集"升级为"序贯决定下一步查什么、何时停止、何时请求人"（§6）。
4. **未来 90 天做什么？** —— 已落地的 P0-9 + 检索优先级（§11）。

**使用规则（与文件 1 相同）：**

- 任何对外 claim 必须能回溯到文件 1 第 3/4 节的状态标签。
- 标为 `EXPLORATORY_PILOT / SMALL_SAMPLE / NOT_PAPER_HEADLINE / SOLO_PROVISIONAL` 的数字不得作为论文 headline。
- **新方向涉及的 `calculation_program` 相关数字，在 P0-9 修复前一律视为 `INVALIDATED_PENDING_PROGRAM_INDUCTION`。** 修复后生产路径不再读取该字段（§3/§4）。
- 冲突时以本文档 §3/§4 的代码验证为准。

---

## 2. 总判断

### 2.1 一句话

> 参考文件 2 的方向（Risk-Controlled, Version-Aware Minimum Sufficient Evidence Systems）**仍然正确，但它是序贯决策问题的一个静态特例**。把证据获取本身动作化（`Retrieve / FindVersion / FindAmendment / Calculate / Verify / AskHuman / Answer / Abstain`），才能回答金融 AI 真正的问题：**"我现在已有这些证据；还缺什么？下一步值得查哪里？一个新证据的预期价值是多少？继续检索的价值是否超过成本？"**

### 2.2 分层评分（基于代码验证，2026-08-07）

| 层次 | 文件 1 评分 | 文件 3 评分 | 判断依据 |
|---|---|---|---|
| 研究方向潜力 | 8/10 | **9/10** | 序贯证据获取把 IR + 信息论 + submodular + 风险控制 + 人审经济学统一为一个决策问题；尚无完整组合。 |
| 科研工程与可审计性 | 8.5/10 | **9/10** | leak-free corpus、SHEP 冻结、production/evaluator 物理隔离继续成立；P0-9 追加程序归纳隔离。 |
| 当前实验可信度 | 3/10 | **4/10** | A11 唯一 ANSWER 正确（answer_precision 1.0），REVIEW 指标不再恒真；但 `calculation_program` 读取在新方向下成为新 oracle 依赖（P0-9）。 |
| 当前方法创新 | 2.5/10 | **4/10** | P0-9 增加程序归纳模块（question → executable program）；仍无 learned acquisition policy。 |
| 当前 benchmark 成熟度 | 3/10 | **3/10** | 19 评估案例、单人 provisional labels、6 issuer 未变。这是接下来的瓶颈。 |
| 当前顶会就绪度 | 2-3/10 | **3/10** | 新方向的问题定义配得上顶会讨论，但数据规模/检索/learned 方法仍远未达标。 |
| 优化后潜力 | 7-8.5/10 | **8-9/10** | 见 §8 论文树与 §9 门槛。 |

### 2.3 核心结论

> **文件 2 的方向是"收敛"——把首篇论文收缩到金融单域最小充分证据集。文件 3 是"升级"——把同一个问题放进序贯决策框架，让`继续检索 / 请求人 / 停止`成为一等动作。二者不冲突：文件 3 是文件 2 的自然延伸，文件 2 的收缩策略仍适用于文件 3 的首篇论文。**

---

## 3. P0-9 代码级审计

### 3.1 发现：production verifier 仍读取 `calculation_program`

参考文件 3 的来源审计指出：虽然 production verifier 已经不读取 `gold_answer`，但 `experiments/a11_retrieval/run.py` 的 `_verify` 仍从 sealed case payload 读取 `calculation_program["operation"]` 做数值可执行性验证。

**代码验证**（`submodules/ecoquant/experiments/a11_retrieval/run.py`）：

```python
# run.py:492-502
program = case.get("calculation_program")
numerical = None
if program and program.get("operation"):
    from finvest.retrieval.retrievers import _concepts_for
    texts = tuple(u.text_span or "" for u in items)
    numerical = verify_calculation(
        operation=program["operation"], evidence_texts=texts,
        expected_value=None, tolerance=0.01,
        required_concepts=_concepts_for(case.get("question") or ""),
    )
```

**为什么这是 P0**：`calculation_program` 与 `gold_answer`、`requirement_graph`、`acceptable_evidence_sets`、`minimal_evidence_sets`、`evidence_items` 位于**同一个 sealed benchmark case payload**（`human_review/day1/v0.2-draft/EXTENSION_40_cases.json:135-143`）。虽然问题文字本身确实说了 "operating cash flow minus capital expenditure"，但：

> **如果 `calculation_program` 是 gold annotation / benchmark construction 阶段生成的，而不是 production task specification，那么它仍然属于 oracle assistance。**

生产路径应该自己从问题预测 `operation = SUBTRACT / input concepts = OCF, CAPEX`，而不是从 sealed benchmark target metadata 读取。

**`result` 字段风险（本次审计新增）**：`calculation_program` 里还带着 `result`（如 `99584000000.0`，`EXTENSION_40_cases.json:141`），与 `gold_answer` 相同。虽然当前代码只读 `operation`，但该字段与答案同处一个 dict，任何未来"顺手用一下"都可能成为直接泄漏点。**P0-9 将其整体移出生产路径。**

### 3.2 范围核对：其余字段当前是否被生产路径读取？

按新方向 Gate 0 原则（"凡是测试时真实用户不会提供的东西，都不能成为 inference feature"），逐一核对 sealed case 字段：

| 字段 | 当前生产路径读取？ | 判定 | 备注 |
|---|---|---|---|
| `question` / `issuer_id` / `source_cutoff` / `target_fiscal_year` / `target_period_end` | 是 | **production input**（真实用户会提供） | 保留 |
| `version_relations` | 是（`run.py:476-478`） | **production input**（版本图谱是语料结构元数据，非答案） | 保留；来自版本账本而非 gold |
| `calculation_program` | **是（`run.py:492`）** | **gold（oracle assistance）** | **P0-9 移除** |
| `requirement_graph` | 否 | **gold（应由模型归纳）** | 生产路径用 `_concepts_for(question)` 代替 |
| `answer_type` | 否 | gold（观察即可得） | 保留 gold 侧 |
| `sufficiency_label` / `decision_label` | 否（仅 evaluator 用 human_route） | gold | 保留 gold 侧 |
| `gold_answer` / `evidence_items` / `acceptable/minimal_evidence_sets` | 否（仅 evaluator / S4 oracle） | gold | 保留 gold 侧 |

**结论**：`calculation_program` 是当前生产路径中**唯一**仍被读取的 gold-adjacent 字段。移除它是新方向 Gate 0 的硬性要求。

### 3.3 新增回归测试（P0-9）

| 测试 | 拦截什么 |
|---|---|
| `test_verify_never_reads_calculation_program` | `_verify` 源码不得访问 `calculation_program`（AST 扫描） |
| `test_verify_never_reads_gold_adjacent_fields` | 生产路径不得读取 `requirement_graph / answer_type / sufficiency_label / decision_label` |
| `test_verify_decision_invariant_to_calculation_program_mutation` | **改变 / 删除 case 的 `calculation_program`，production decision 不改变**（新方向 Gate 0 的核心测试） |
| `test_induce_program_subtract_cashflow` | 程序归纳把 "operating cash flow minus capital expenditure" 归纳为 subtract + {OCF, CAPEX} |
| `test_induce_program_extractive_no_op` | 抽取式问题（"What is Assets for FY2022?"）不产生 operation |
| `test_induce_program_gold_free` | 归纳模块签名只接受 question 字符串，不接触 case payload |

---

## 4. P0-9 修复：程序归纳

### 4.1 修复原则

> **production 完全删除 `case["calculation_program"]`。** 改成：
> `question → Requirement / Program Induction → executable symbolic program`
> 这会直接把项目往 AI / neuro-symbolic reasoning 推进一步。

### 4.2 新模块：`finvest/program_induction/induction.py`

输入（仅 question 字符串，gold-free）：

```text
"What is AAPL operating cash flow minus capital expenditure for the fiscal period ending 2023-09-30?"
```

输出：

```json
{
  "entity": "AAPL",
  "period": "FY2023",
  "required_metrics": ["NetCashProvidedByUsedInOperatingActivities",
                       "PaymentsToAcquirePropertyPlantAndEquipment"],
  "operation": "subtract",
  "version_policy": "as-of-cutoff",
  "source": "rule-lexicon"
}
```

实现：
- 复用公开、版本化的 `CONCEPT_DICTIONARY`（`finvest/retrieval/retrievers.py:36-54`）从问题归纳 required metrics；
- 新增 finance-operators 词典把自然语言操作符（`minus / subtract / difference between`、`sum / total / plus`、`average / mean`）映射到可执行 operation（与 `src/ecoquant/research/table_eval/calculate.py:24-27` 的 `FUNCTIONS` 对齐）；
- FCFF 派生规则：`free cash flow` → `subtract(OCF, CAPEX)`（与 `finvest/requirement_graph/parsers.py:79-90` 的 `deterministic_finance_parser` FCFF 派生一致）；
- **不读取任何 case payload 字段。**

### 4.3 `_verify` 改造

`run.py` 的 `_verify` 中，把 `program = case.get("calculation_program")` 替换为：

```python
from finvest.program_induction.induction import induce_program
induced = induce_program(case.get("question") or "")
numerical = None
if induced.operation:
    numerical = verify_calculation(
        operation=induced.operation, evidence_texts=texts,
        expected_value=None, tolerance=0.01,
        required_concepts=set(induced.required_metrics),
    )
```

并在 numerical 输出中记录 `induced_program` 以供审计（operation / required_metrics / source）。`expected_value` 仍为 `None`——可执行性验证，gold 永不进入决策。

### 4.4 行为等价性验证

对 sealed 的 9 个 cashflow case（`EXTENSION_40_cases.json` 中 `operation == "subtract"`），问题文字均含 "minus"，归纳结果与 gold `calculation_program` 语义一致（subtract + {OCF, CAPEX}）；对 30 个非 cashflow case，`induce_program` 不产生 operation（抽取式问题无操作符），`numerical` 保持 `None`，行为与修复前一致。**修复前后 production decision 不变**，但 now 该 decision 的数值验证不再依赖 gold-adjacent 字段。

---

## 5. 新终极方向的形式化定义

### 5.1 核心研究问题

> **Can an AI sequentially acquire the lowest-cost temporally valid, version-consistent, numerically executable and provenance-complete evidence certificate required for a financial decision, while deciding when to answer, retrieve more evidence, seek human review or abstain under controlled risk?**

> **AI 能否用最低成本逐步获取完成一个金融决策所需的时间有效、版本一致、数值可执行、来源完整的证据证书，并在受控风险下自主决定继续检索、请求人工、回答或弃答？**

### 5.2 State

```
s_t = (q, E_t, G_t, V_t, B_t, H_t)
```

- `q`：问题；
- `E_t`：当前已获取 evidence set；
- `G_t`：当前 inferred requirement graph；
- `V_t`：version / temporal state；
- `B_t`：剩余 retrieval/computation budget；
- `H_t`：human-review state。

### 5.3 Actions

```
a_t ∈ { Retrieve, QueryExpand, FindVersion, FindAmendment,
        ReadTable, Calculate, Verify, AskHuman, Answer, Abstain }
```

这比 `retrieve top-5 → answer` 高一个层级：**系统要决策的不是一个检索，而是一个获取策略。**

### 5.4 Evidence Certificate

```
C = (E, Γ, Π, T, V, P)
```

- `E`：evidence set；
- `Γ`：requirement graph；
- `Π`：executable reasoning/calculation proof（**P0-9 保证它是从 question 归纳的，不是从 gold 读的**）；
- `T`：valid/source time constraints；
- `V`：version/amendment lineage；
- `P`：provenance。

约束：

```
Complete(C)=1  ∧  VersionValid(C)=1  ∧  TemporalValid(C)=1
∧  Executable(C)=1  ∧  Traceable(C)=1
```

### 5.5 Minimum Evidence Certificate

```
C* = argmin_C Cost(C)
s.t. S(C, q) = 1
```

```
Cost(C) = c_r·N_retrieval + c_t·N_tokens + c_v·N_verification + c_h·N_human + c_l·Latency
```

这统一了 IR、信息论、submodular optimization、人工复核与经济学。

### 5.6 决策目标

```
max_π  E[ U_correct − C_retrieval − C_compute − C_human − C_abstain − L_unsafe ]
s.t.   R_accepted(π) ≤ α
```

**关键含义**：当前 A11 的 `1 ANSWER / 18 REVIEW` 即使 precision=100%，utility 也可能很低（安全到几乎没用）。新方向必须研究 **Price of Safety / Price of Review**。

---

## 6. 为什么这个方向比 Financial RAG 更能活 5 年以上

### 6.1 容易被 commodity 化的部分（未来 3-5 年越来越便宜）

```text
OCR / generic embeddings / PDF parsing / generic RAG / reranking /
long context / generic agents / basic citation / table extraction
```

**不能把商业壁垒押在这些上面。**

### 6.2 很难消失的问题（无论 GPT-8 / Claude-X / Gemini-X 多强，企业都会问）

```text
这条信息来自哪里？哪个版本？当时是否已公开？后来是否修订？
哪个法律/财务期间适用？哪些证据是必须的？缺什么？
为什么允许 AI 自动决定？风险阈值是什么？谁复核过？能否重放这个决定？
```

这不是模型智商问题，而是 **information governance + decision rights + evidence economics** 问题。

### 6.3 与文件 2 的差异：新增"序贯获取"科学维度

| 维度 | 文件 2（Evidence Entitlement） | 文件 3（Sequential Evidence Acquisition） |
|---|---|---|
| 证据如何获得 | 一次性选择集合（retrieve → select） | **序贯动作**：查哪个 filing、哪个 amendment、是否需要计算 |
| 决策时点 | 一次 `ANSWER/REVIEW/ABSTAIN` | **每步都可决策**：继续查 / 请求人 / 停止 |
| 成本建模 | 证据数量 | **获取成本 + 计算成本 + 人审成本 + 延迟** |
| 理论语言 | 信息瓶颈 / submodular / conformal | **+ Value of Information / 序贯决策 / bandit** |
| 下一步证据价值 | 未建模 | **`E(ΔU|a) − Cost(a)` 显式进入 policy** |

---

## 7. 与参考文件 1/2 的一致性核对

| 文件 1/2 声明 | 文件 3 的关系 | 处理 |
|---|---|---|
| 文件 1 §7 科研定位 `Evidence Entitlement` | 是文件 3 §5 的一个静态特例 | 文件 3 泛化；文件 1 的验证仍有效 |
| 文件 2 §1.1 唯一方向 `Risk-Controlled, Version-Aware Minimum Sufficient Evidence Systems` | 被文件 3 升级为序贯版本 | 不撤销；文件 2 的收缩策略适用于文件 3 首篇论文 |
| 文件 2 §6.14 10 个月 go/no-go 门槛 | 全部保留，追加文件 3 §9 的 Gate 0（程序归纳纯化） | 见 §9 |
| 文件 1 §3 A11 的 `1 ANSWER / 18 REVIEW` | 有效但受 P0-9 影响 | **P0-9 修复前该数字不再可归因于"生产路径自身推断程序"**；修复后已恢复 |
| 文件 1 §5 检索瓶颈（document recall > fact recall） | 文件 3 把它升级为研究问题：**hierarchical semantic resolution（document → statement → table → row → concept → period/version）** | 作为 Paper 2 核心 |
| 文件 2 §3.4 仓库组合战略（4 一线入口） | 不影响 | 保留 |

---

## 8. 五篇论文树与顶会路线

### Paper 1 — Benchmark / Evaluation
**FinVEST: Evaluating Versioned Evidence Acquisition in Financial Documents**
贡献：version conflicts / restatements / stale evidence / minimum evidence certificates / leak-free evaluation / human labels。
目标：**NeurIPS E&D / SIGIR / ACL**。

### Paper 2 — Retrieval / Sequential AI
**Sequential Evidence Acquisition for Long Financial Documents**
核心：requirement induction → hierarchical search → query planning → next-evidence policy。
比较：BM25 / dense / ColBERT / cross encoder / RAPTOR / GraphRAG / agentic retrieval / learned policy。
目标：**SIGIR / WWW / ACL / KDD**。

### Paper 3 — Set / Certificate
**Learning Minimum Sufficient Evidence Certificates**
结合：submodular objective / learned set prediction / information bottleneck / version constraints / numerical executability。
目标：**KDD / ICLR / NeurIPS / UAI**。

### Paper 4 — Risk
**Risk-Controlled Evidence Entitlement**
研究 `ANSWER / RETRIEVE / REVIEW / ABSTAIN`，给 selective risk / finite-sample control / temporal shift / cost-aware review。
目标：**ICML / NeurIPS / AISTATS / UAI**。

### Paper 5 — Human AI
**The Value of Human Review in Financial AI**
实验比较 human alone / AI answer / AI+citations / AI+certificate / AI+calibrated review policy。
目标：**CHI / CSCW / FAccT**。

**路线判断（来自来源审计）**：
- **SIGIR** 最匹配：Sequential Version-Aware Evidence Acquisition for Long Financial Documents（★★★★★）；
- **ACL/EMNLP**：financial language → requirement graph、program induction、conflict/version language（★★★★☆）；
- **KDD 2026**：financial version graph + sequential policy + large-scale experiment（★★★★☆）；
- **NeurIPS E&D**：FinVEST 作为 evaluation science paper（★★★★☆）；
- **ICML/NeurIPS/ICLR main**：需要 theorem/statistical guarantee + decision policy + generalization（★★★☆☆ → ★★★★★，取决于理论突破）。

---

## 9. Go/No-Go 门槛

在文件 2 §6.14 的基础上，追加新方向的硬性门槛：

### Gate 0 — Purity（新增，P0-9）
所有 production outputs 对 `gold_answer / gold evidence / gold program / gold requirement graph / calculation_program` invariant。
**不通过：禁止跑 headline experiments。**（2026-08-07 已修复并通过测试）

### Gate 1 — Retrieval（文件 2 保留）
`Recall@20 ≥ 0.70` + `AllRequiredEvidenceRecall@20` 达到可用水平。
**不通过：verifier 研究暂停。**（当前 Recall@5≈0.08 是最大瓶颈）

### Gate 2 — Annotation（文件 2 保留）
≥ 300 cases / 20 issuers / high-risk 双标 / disagreement adjudication。
**不通过：不称 benchmark V1。**

### Gate 3 — Utility（文件 2 保留）
`Risk ≤ 5%` 时 `Coverage` 明显优于 baseline，且 `ReviewBurden` 显著下降。

### Gate 4 — Generalization（文件 2 保留）
同时通过 issuer holdout / time holdout / version holdout / template holdout。

### Gate 5 — External Domain（文件 2 保留）
至少一个 industrial / trade / legal 文档域。

### Gate 6 — Product（文件 2 保留）
一个真实 workflow pilot 证明 review time 下降、critical error 未恶化、用户愿意复用。

---

## 10. 十五大弱点与自我批评

新方向**不能因为推荐就忽略风险**。来源审计列出十五大弱点，最相关的六条在此登记：

1. **evaluation cases 仍太少（19）**，solo provisional labels，无独立 gold。
2. **held-out issuer generalization 极差**（JNJ/KO/MSFT/UPS Recall@5≈0），document recall > fact recall。
3. **`calculation_program` 潜在 oracle dependency** —— 已修（P0-9）。
4. **当前 18/19 REVIEW，automation utility 极低** —— 必须研究 Price of Safety。
5. **真正 finite-sample selective guarantee 尚未 held-out 验证**。
6. **human review cost 未进入 objective** —— §5.5/§5.6 的 `Cost(C)` 已把它形式化，但尚未实现。

**新方向自身弱点（诚实登记）**：
- **太大**：同时含 retrieval/version/sets/risk/human review/agents/finance。**不要一篇论文全做。**
- **Sequential policy 需要 trajectory data**：现在只有 final evidence labels。第一阶段用 synthetic action environment / oracle trajectories / heuristic policy，产品未来产生 real trajectories。
- **Conformal 假设受 temporal shift 影响**：金融数据非 iid。研究 chronological/rolling/weighted conformal + shift detection。
- **Human review data 贵**：科研做 100-150 expert-reviewed cases；商业靠 reviewer action 自动积累。
- **"Certification" 有监管语义风险**：研究中定义为 **machine-checkable evidence certificate**，不是 regulatory certification。

---

## 11. 90 天执行计划

| 时段 | 动作 | 状态 |
|---|---|---|
| Day 0-3 | **P0-9：程序归纳模块 + `_verify` 改造 + 测试**（本文档 §3/§4） | **已完成（2026-08-07）** |
| Day 0-15 | CFA 重置期；不启动重大科研开发（文件 2 §1.10） | 进行中 |
| Week 3-6 | P1：Retrieval representation 升级（raw XBRL → canonical concept + label + definition + statement + table context + version metadata）+ 严格 ablation | 计划 |
| Week 4-8 | P2：strong retrieval baseline（BM25 / dense bi-encoder / ColBERT / cross-encoder / RRF / RAPTOR / hierarchical / taxonomy-aware）；**Recall@20 < 0.70 不堆 verifier** | 计划 |
| Week 6-10 | P3：Requirement / Program Induction 强化（规则 → 小模型微调） | 计划 |
| Week 8-12 | P4：300 case pilot（20-30 issuers / 15 error families / 20-30% 双标，重点构造 amendments / restatements / unit ambiguity / stale evidence / future evidence / conflicting evidence） | 计划 |

---

## 12. 参考文献与文献信号

### 12.1 来源审计核心结论

> 大部分单组件（RAG / dense / hybrid / GraphRAG / hierarchical / financial QA / multimodal financial RAG / agentic retrieval / evidence sufficiency / abstention / conformal / version-aware）**都已经有人做了。真正的创新空间在它们之间尚未解决的联合决策问题。**

### 12.2 关键信号文献（分类摘录）

**CS/AI（44 篇核心）**：
- RAG 基础已饱和：Lewis et al. (NeurIPS 2020)、Karpukhin et al. (EMNLP 2020)、Asai et al. (Self-RAG, ICLR 2024)、Edge et al. (GraphRAG)、Sarthi et al. (RAPTOR, ICLR 2024)。
- Sufficiency 近邻已出现：Qiu et al. (SURE-RAG 2026)、Zhu et al. (SABER 2026)、RC-RAG (Findings EMNLP 2024)、FinAbstain (2026)。
- 金融 QA 已拥挤：FinQA、TAT-QA、FinanceBench、FinAgentBench、FinDER、HiREC/LOFin、FinRAGBench-V、FinMRAGBench、VersionRAG、DocNavRAG。

**数学/统计/物理/金融经济（27 篇核心）**：
- 信息论：Tishby et al. (Information Bottleneck)、Alemi et al. (Deep VIB)。
- Submodular：Bilmes (Submodularity in ML)。
- 风险控制：Angelopoulos et al. (CRC)、SCoRE、Selective Conformal Risk Control、Joint finite-sample certificate (2026)。
- 稳健优化：Bertsimas & Sim（robustness 不是免费的 → Price of Safety）。
- Value of Information：Guo et al. (human-AI decision framework)。
- 披露处理成本：Blankespoor, deHaan & Marinovic（**FinVEST 商业价值最重要的金融经济学基础**）。
- AI 生产率：Brynjolfsson, Li & Raymond (5,172 客服，+15% 生产率，低经验者收益更大 → 未来 human study 应测 FinVEST 是否尤其帮助 junior analysts)。

### 12.3 最终战略评分（来源审计）

| 维度 | 评分 |
|---|---|
| AI novelty potential | 91/100 |
| AI MSc/PhD alignment | 95/100 |
| 5-year research durability | 91/100 |
| Finance synergy | 94/100 |
| Commercial optionality | 93/100 |
| Long-term infrastructure fit | 95/100 |
| Execution difficulty | 94/100 |
| **Scope risk** | **90/100（风险项，不是优点）** |

> 最大危险不是价值不足，而是**想一次把它全做完。**千万不要。

---

## 附录：2026-08-07 P0-9 修复记录

**变更**（`submodules/ecoquant`，branch `codex/sol4a-final-coordination`）：
- 新增 `finvest/program_induction/induction.py`：`induce_program(question)` → `InducedProgram(operation, required_metrics, entity, period, version_policy, source, confidence)`，仅消费问题字符串。
- `experiments/a11_retrieval/run.py` `_verify`：删除 `case.get("calculation_program")` 读取，改用 `induce_program`。
- 新增测试：`tests/finvest/test_program_induction.py`（含 Gate 0 mutation invariance 测试）+ `tests/finvest/test_verifier_gold_isolation.py` 追加 AST 扫描断言。
- 文档：本文档 + `RESEARCH_DESIGN_AND_PLAN.md` §3.7-3.9 + `RESEARCH_REFERENCE_RECONCILIATION.md` §三。

**验证**：`pytest tests/finvest/ -q` → 249 passed, 3 skipped（全绿）。

**端到端等价性核对（2026-08-07）**：
- 对 sealed 39 个 case，`induce_program` 的 operation 预测与 gold `calculation_program` **0 不一致**（9 个 cashflow → `subtract`，30 个抽取式 → 无 operation）。
- 全量 A11 重跑对比：**所有 19 个 case 的 numerical verification_state 逐 case 一致**（`INVALIDATED_PENDING_PROGRAM_INDUCTION` 无变化）；decision 差异仅来自 temporal verifier 的检索候选漂移。
- **检索漂移根因（环境性，非 P0-9）**：本次重跑环境 `dense_available = False`（`research/cache/models/all-MiniLM-L6-v2` 缺失 + `sentence_transformers` 未安装），而提交的 `a11_two_stage.json`（`1 ANSWER / 18 REVIEW`）是在 dense 可用环境生成的。dense 缺失使 R3/RRF 退化为纯 BM25 排序，改变 top-5 证据 → temporal 判定翻转。corpus_id 与 record_count 两跑完全一致（`af406d47…` / 170,229）。
- **结论**：P0-9 是数值路径等价替换；提交的 A11 工件在 P0-9 下仍然有效（唯一 ANSWER case 无 `calculation_program`，两跑 numerical 均为 None）。工件文件保持 dense-可用版本，未用 dense 缺失环境的结果覆盖。
