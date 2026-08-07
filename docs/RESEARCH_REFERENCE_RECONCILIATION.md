# 参考文件 1 vs 参考文件 2 — 差异、协调与新发现

> **Reconciliation of FINVEST_RESEARCH_REFERENCE.md (#1) and FINVEST_RESEARCH_REFERENCE_2.md (#2)**
>
> 本文件回答两个问题：
> 1. 两份核心参考文件有什么**本质不同**？
> 2. 文件 2 带来了哪些**新发现**，如何据此**优化一切**？
>
> 日期：2026-08-07。

---

## 一、两份文件的本质差异

| 维度 | 文件 1 `FINVEST_RESEARCH_REFERENCE.md` | 文件 2 `FINVEST_RESEARCH_REFERENCE_2.md` |
|---|---|---|
| **本质** | 代码级**现状审计 + 修复路线** | 战略**方向决策 + 文献综合 + 科研程序** |
| **回答的问题** | "我现在的科研状态真实如何？哪些 claim 不可信？" | "我未来 3-10 年唯一方向是什么？顶会 gap 在哪？" |
| **方法** | 逐行验证代码、跑测试、核对产物 | 20,000 次敏感性分析、103-source 证据矩阵、候选方向锦标赛 |
| **输出** | 状态重分类表 + P0/N 修复 + 4 篇论文拆分 | 唯一终极方向 + go/no-go 门槛 + 正式问题定义 + 仓库组合审计 |
| **范围** | 聚焦 ecoquant 科研实现 | 全 GitHub 组合（29 repo）+ 商业 + 升学 + 终局 |
| **时间视角** | 现在（2026-08） | 未来 10 个月 → 3 年 → 10-20 年 |
| **参考文件关系** | 配套（文件 2 的定位细化文件 1 的论文 2） | 配套（文件 1 的验证是文件 2 战略的现状基础） |

**一句话**：文件 1 回答"**你现在是什么**"，文件 2 回答"**你应该成为什么**"。

---

## 二、两份文件已过时/冲突的点（2026-08-07 P0 修复后）

> 文件 2 的 §2.2、§3.3 基于 **P0 修复前**的状态。P0-1..N-8 修复后，以下声明已改变：

| 文件 2 声明（过时） | 现在的真实状态（P0 修复后） | 影响 |
|---|---|---|
| "A11 最终评价 19 例；0 ANSWER；18 REVIEW；1 ABSTAIN；coverage=0" | **1 ANSWER（正确）/ 18 REVIEW / 0 ABSTAIN**；coverage **0.0526**；answer_precision **1.0** | 系统现在有真实的（虽小）自动化效用 |
| "coverage=0 意味着当前系统没有自动化效用" | coverage 0.0526（1/19）——仍有实际效用，但极低 | 效用真实但微弱 |
| "0 unsafe answers 是 NON-INFORMATIVE SAFETY（因为 0 ANSWER）" | unsafe_answer_rate 0.0 是**真实**的（唯一 ANSWER 正确） | 安全性声明现在有意义 |
| "Integration adapters：failed remote integration CI / PARTIAL" | **Integration CI 已转绿**（`#egg=` 修复） | 集成层现在是 CI-validated |
| "低 Recall 意味着 Verifier 经常无法接触正确证据" | 仍真（Recall@5 ≈ 0.08），但 N-6 后 R4 到 0.08、S2 有 size=1 | 检索仍是最大瓶颈（文件 2 §3.4 判断正确） |
| "10 个月最强论文 = 36-50 issuers / 600 cases" | 与文件 1 的 FinVEST-V1（2,000-5,000）有规模差异 | 文件 2 更现实（600 人工复核），优先采用 |
| "先解决 Recall@20，再开发 Verifier" | 与文件 1 Phase 1 一致（检索基线先行） | 确认检索优先 |

**协调结论**：文件 2 的核心战略判断（检索是最大瓶颈、方向需收缩、文献拥挤）**全部正确**；只有少数"当前状态"数字需要更新为 P0 修复后的值。

---

## 三、文件 2 带来的核心新发现（相对文件 1）

### 新发现 1：方向收缩 — 首篇论文变窄
文件 1 的四篇论文拆分中，Paper 2 是 `VISTA-Fin` 方法。文件 2 建议首篇论文更聚焦：

> **When Is Evidence Enough? Version-Aware Minimum Evidence Sets and Risk-Controlled Abstention for Long Financial Documents**

只做金融文档，不做跨域。这是对文件 1 Paper 1+2 的**合并与收缩**。

### 新发现 2：文献竞争比文件 1 认知的更拥挤
文件 1 提到 FinanceBench/FinAgentBench/FinDER/HiREC/SURE-RAG/FinReflectKG。文件 2 增加：
- **多模态金融 RAG 已拥挤**：MultiFinRAG、FinRAGBench-V、FinMMDocR
- **sufficiency 近邻**：SURE-RAG、S2G-RAG
- **风险控制近邻**：C-RAG、RC-RAG、COIN、Learn then Test
- **版本近邻**：VersionRAG、conflicting-evidence RAG、temporal-conflict QA、ChronoQA、FRESCO

**影响**：文件 1 的 novelty 表述"首次提出 set-level sufficiency"必须撤销。文件 2 给出的正确 gap：

> 版本约束、最小证据集合、数值可执行性、检索遗漏和人工复核成本**统一到一个风险受控决策问题**中——尚无人完整组合。

### 新发现 3：检索失败传播 + Review Allocation 联合优化
文件 2 §4.2 发现六 + §6.6：系统不应只输出"是否拒答"，而应**判断审查哪一个证据缺口、人工补充哪项信息价值最高**（VOI）。这比文件 1 的"ANSWER/REVIEW/ABSTAIN"更具体。

### 新发现 4：正式问题形式化（文件 1 缺）
文件 2 §6 给出完整符号系统：EvidenceUnit `e=(d,v,p,r,t_s,t_v,z,u,h,m)`、目标函数（收益−错误成本−证据成本−复核成本−拒答成本）、充分性定义、VOI 复核分配。文件 1 只有叙述性定位。

### 新发现 5：go/no-go 门槛（可执行验收）
文件 2 §6.14：Month 5 Recall@20≥0.70、Month 7 coverage≥20%@≤5% risk、Month 8 version holdout gain 等。文件 1 只有 90 天计划，无量化门槛。

### 新发现 6：数据漂移 / 双 checkout 教训被战略化
文件 2 §3.4 指出"真实数据与 CI 的分裂"是最大工程瓶颈——正是我们在 P0-6 和 UPS 漂移中遇到的。文件 2 把它提升为**战略级风险**。

### 新发现 7：仓库组合战略（29 repo → 4 一线入口）
文件 2 §3.5：三个月后只保留 4 个一线入口（finvest-research / finvest-core / pdf-manager / auralynq），内部工具合并为 `finvest-tooling/`。文件 1 未涉及仓库级战略。

---

## 四、如何据此优化一切（行动项）

### A. 科研方向（立即）
1. **首篇论文标题**采用文件 2 的 `When Is Evidence Enough?`（收缩、金融单域）。
2. **撤销**"首次提出 set-level sufficiency"表述；用文件 2 的统一风险受控决策 gap。
3. **检索优先**：先解决 Recall@20（文件 2 §1.10 第 6 条），再开发 Verifier。当前 Recall@5≈0.08 是最大瓶颈。

### B. 计划（90 天计划叠加 go/no-go）
4. 把文件 2 §6.14 的 10 个月门槛映射到我们的 90 天计划（Phase 0 已完成 P0 修复 → Phase 1 检索基线 → Month 5 Recall@20≥0.70）。
5. 增加 **50 个版本冲突 pilot**（文件 2 §1.10）作为 Phase 1 的挑战集核心——现有 challenge cases 已有 6 类 mutation，需扩展到版本冲突场景。
6. Dataset 目标采用文件 2 的 600 cases / 100-150 双标 / 36-50 issuers（比文件 1 的 2,000-5,000 更现实，优先执行）。

### C. 工程治理（进行中）
7. 文件 2 §3.4 的"真实数据与 CI 分裂"——我们已修 P0-6（Integration CI）并记录 UPS 漂移。继续：把 `research/cache` 与 manifest 的关系固化为 CI 检查。
8. 仓库合并战略（4 一线入口）作为**三个月后**目标，当前不打断 P0/Phase 1。

### D. CFA 重置（纪律约束）
9. 文件 2 §1.10：未来 15 天**不启动重大科研开发**，专注 CFA。今天只建 `POST-CFA RESEARCH RESET` issue 记录 go/no-go 门槛。已完成的 P0 修复恰好在重置窗口内（CI 已绿，符合"只允许修复阻止 CI 运行的极小问题"）。

---

## 五、最终协调立场

两份文件**不冲突**，是互补的：
- **文件 1 证明我们现在能做什么**（真实、无泄漏、可复现的骨架）。
- **文件 2 决定我们要成为什么**（风险受控、版本感知的最小充分证据系统）。

> 执行优先级：文件 2 的战略方向 → 文件 1 的工程验证 → 两者的 go/no-go 门槛把关。

下一步（CFA 后）按文件 2 §1.10 执行：冻结 RQ/schema → 删除 paper-ineligible headline → 确定第二标注者 → 50 版本冲突 pilot → 解决 Recall@20。
