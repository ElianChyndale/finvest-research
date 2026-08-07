# FinVEST 科研核心参考文件 2 — 战略决策与文献综合

> **FinVEST Research Core Reference #2 — Strategic Decision & Literature Synthesis**
>
> 本文档是 FinVEST 研究纲领的**战略决策参考文件**：确定唯一终极方向、评估备选方向、完成 103-source 文献综合、GitHub 组合审计、候选方向锦标赛、正式科研程序定义、顶会匹配与 go/no-go 门槛。
>
> **与参考文件 1 的关系**：文件 1（`FINVEST_RESEARCH_REFERENCE.md`）是**代码级验证的现状审计 + 修复路线**；文件 2 是**战略选择 + 方向收敛 + 文献定位**。两者配套使用。冲突点与已过时声明见 `RESEARCH_REFERENCE_RECONCILIATION.md`。
>
> **输入说明**：本文件由用户提供的战略文档转录（截至 §7.1 与 §7.2 开头；原始输入在 §7.2 处被系统截断，§7.2 之后内容不可用）。
>
> **验证基准**：转录于 2026-08-07。其中"当前 GitHub 状态"（§2.2/§3.3）基于 P0 修复前的状态；P0-1..N-8 修复后 A11 已是 `1 ANSWER / 18 REVIEW / 0 ABSTAIN`，Integration CI 已转绿——详见 reconciliation 文件。

---

## 目录

1. [最终决策](#section-1--final-decision)
2. [决策证据](#section-2--decision-evidence)
3. [GitHub 审计](#section-3--github-audit)
4. [文献综合](#section-4--literature-synthesis)
5. [候选方向锦标赛](#section-5--candidate-direction-tournament)
6. [科研程序](#section-6--research-programme)
7. [顶会匹配](#section-7--top-venue-review)

---

# SECTION 1 — Final Decision

你给出的研究对象是你本人的科研、技术、GitHub、商业资源、金融能力、爱尔兰升学路径与未来10—20年方向；GitHub、Consensus和Web Search只是取证工具，不是研究主题。

## 1.1 唯一终极方向

### **Risk-Controlled, Version-Aware Minimum Sufficient Evidence Systems**

### **风险受控、版本感知的最小充分证据系统**

**一句话Thesis：**

> 对不断修订、存在冲突、跨页且包含数值关系的金融与工业文档，系统不应仅检索"相关内容"，而应选择一个**版本正确、最小但充分、数值可执行、来源可追溯**的证据集合，并在错误风险与人工复核成本约束下决定 `ANSWER / REVIEW / ABSTAIN`。

**[Recommendation]** 这是未来三年的科研主线，也是最适合连接Document AI、金融、工业文档、人工审查、商业工作流和长期资本基础设施的统一方向。

**首篇论文应进一步收缩为：**

> **When Is Evidence Enough? Version-Aware Minimum Evidence Sets and Risk-Controlled Abstention for Long Financial Documents**

首篇论文只做金融文档。工业文档应作为后续external validity或商业产品数据，不应为了"跨域"而把第一篇论文写散。

## 1.2 两个备选方向

### 备选一：Evaluation Science and AI Assurance for Complex Document Agents

**复杂文档智能体的评价科学与AI审计**

当真实标注、工业数据或检索性能无法达到论文门槛时，转向：

* Benchmark有效性；
* gold leakage；
* evaluation artifacts；
* evidence judge可靠性；
* agent轨迹审计；
* counterfactual evidence swaps；
* 可复现与声明治理。

该方向的学术抽象性更强，但商业数据优势弱于主方向。

### 备选二：Cross-Border Industrial Evidence Intelligence

**跨境工业证据智能**

聚焦：

* 产品规格书；
* 证书与声明；
* 检验报告；
* 供应商技术文档；
* 修订版本；
* 适用产品范围；
* 有效期、签字与责任主体；
* 中英双语证据包。

该方向近期更容易收费和形成专有数据，但若没有新的评价问题或算法贡献，主要是企业软件，而非顶会研究。

## 1.3 Scenario A：彻底推翻当前方向

**最优转向：Evaluation Science and AI Assurance for Complex Document Agents。**

**[Source-Supported Interpretation]** "Financial RAG + multimodal parsing + verifier + abstention"已经高度拥挤：金融数值QA、跨表推理、多模态金融检索、视觉引用、证据充分性、风险控制和版本化RAG均已有直接近邻。[1]–[14]

因此，若必须推翻Document AI主线，最值得保留的是你已经形成的：

* 泄漏审计；
* artifact manifests；
* claim-evidence governance；
* counterfactual tests；
* reproducibility；
* failure-state reporting；
* selective decision机制。

这些可以升级为通用Document Agent Evaluation。

**Scenario A的弱点：**

* 无法充分利用家庭外贸与工业文档资源；
* 容易成为"评价别人的系统"，缺乏独有应用数据；
* 短期收费能力较弱；
* 与长期贸易、供应链金融的连接更间接。

## 1.4 Scenario B+D：保留基础并彻底升级

保留：

* PDF与Document AI工程；
* 金融和工业文档；
* 时间、版本、数值验证；
* selective prediction；
* 长期金融基础设施optionality。

但必须放弃以下主张：

* "RAG + Verifier"本身是创新；
* "拒答更安全"本身是创新；
* 普通多模态金融QA是新问题；
* 只要加入GraphRAG、Agent或知识图谱就能达到顶会；
* 工程模块数量等于科研贡献。

将核心问题升级为：

> **在检索可能失败、证据可能陈旧或互相冲突、人工复核成本有限时，如何联合优化证据集合、风险、覆盖率与人工审查？**

这不是把更多模块接在一起，而是定义一个新的**受约束决策问题**。

## 1.5 最终胜者

# **Scenario B+D胜出**

战略评分模型中，主方向得分 **83.3/100**，高于：

* Cross-Border Industrial Evidence Intelligence：81.4；
* Human Review Allocation under Selective Risk：81.3；
* Trade & Supply-Chain Finance Evidence AI：80.9；
* Document Agent Evaluation Science：79.0；
* 当前Verifier-Guided Multimodal RAG：66.5。

在对权重进行20,000次扰动的内部敏感性分析中，主方向约有92%的情景保持第一。该数字是战略模型结果，不是科学实验证据。

## 1.6 未来10个月最强论文项目

### **When Is Evidence Enough? Version-Aware Minimum Evidence Sets and Risk-Controlled Abstention for Long Financial Documents**

目标：

* 36—50家发行人；
* 2019—2026年SEC文件；
* 约600个人工审查case；
* 100—150个双人标注case；
* issuer、time、version、template四种holdout；
* 独立检索语料；
* minimum evidence-set gold；
* version/temporal/numerical consistency；
* risk–coverage与review burden联合评价。

最低可发表贡献不是"系统比GPT强"，而是以下三项中的至少两项：

1. 新Benchmark和严格的版本化评价协议；
2. 最小充分证据集合选择方法；
3. 在固定风险下提高ANSWER coverage并减少人工复核。

## 1.7 未来10个月最强收费产品

# **Evidence Revision Dossier**

# **工业与供应商文档修订证据包**

面向中小型出口商、工业制造企业和技术贸易团队：

* 上传证书、规格书、声明、检验报告和技术PDF；
* 自动识别版本、适用产品、发行方、有效期和签字；
* 对比新旧版本；
* 标出修改、冲突、过期和缺失项；
* 每个结论链接到页码和文档区域；
* 人工确认关键字段；
* 输出可发送给客户、审计方或内部质量部门的证据包。

不得承诺自动法律合规，也不得输出无人负责的"合规通过"。

## 1.8 三年壁垒

三年内只建设一条壁垒：

> **经授权的版本化工业—金融证据图谱 + 人工审查决策数据 + 客户工作流。**

真正的壁垒不来自：

* 公共SEC文件；
* 普通OCR；
* 通用LLM；
* 一个聊天界面；
* RAG框架；
* 独立的Verifier代码。

壁垒来自：

* 文档版本历史；
* 文档—产品—供应商—证书—要求之间的关系；
* 客户自己的规则；
* reviewer接受、修改和驳回记录；
* 错误与争议案例；
* 可追溯的证据输出；
* 嵌入日常工作流后的切换成本。

## 1.9 10—20年终局

### **AI-Native Industrial Evidence and Capital Intelligence Infrastructure**

这条路线只能按以下顺序成立：

```
Research → Evidence Product → Workflow Adoption → Proprietary Evidence → Risk Models → Decision Support → Regulated Services → Capital Allocation
```

**[Speculation]** 未来可以连接：

* 供应商风险；
* 贸易融资；
* 项目融资；
* 保险与保单审查；
* 工业资产尽调；
* 基础设施投资；
* 工业资本配置。

目前不能声称已经在建设"金融基础设施"。当前只是最前端的证据与决策支持层。

## 1.10 未来30天第一行动

由于CFA考试临近，未来15天不应启动重大科研开发。该约束来自你提供的背景。

**今天：**

* 建立一个GitHub issue：`POST-CFA RESEARCH RESET`；
* 记录本报告中的go/no-go门槛；
* 不新增研究功能；
* 不重新设计架构；
* 不进行大规模标注；
* 只允许修复阻止已有CI运行的极小问题；
* 主要精力用于CFA。

**考试结束后的第一周：**

1. 修复integration CI；
2. 冻结论文RQ和数据schema；
3. 删除所有paper-ineligible headline；
4. 确定第二标注者；
5. 构造50个高质量版本冲突pilot；
6. 先解决Recall@20，再开发Verifier。

---

# SECTION 2 — Decision Evidence

## 2.1 个人资源匹配

你目前具备的组合并不是"金融RAG研究者"的标准组合，而是：

* Document AI与PDF工程；
* OCR、翻译、渲染与QA；
* evidence、manifest、immutable runs和release governance；
* CFA基础学习；
* 工业与外贸文档接触渠道；
* 投资和尽调讨论资源；
* 爱尔兰AI/CS升学目标；
* 16GB RAM、8GB VRAM的有限算力；
* 短期论文、收入与产品目标。

**[Inference]** 最有价值的交叉点不是预测股价，也不是直接设计金融市场协议，而是：

> 将非结构化、版本化和可争议的文件转化为可审查的证据与决策输入。

这同时服务于：

* 科研：检索、证据集合、风险控制、评价科学；
* 产品：文档审查、revision intelligence、evidence dossier；
* 金融：尽调、风险、贸易和项目融资；
* 工业：供应商、产品与项目文档；
* 申请：清晰的研究问题和可复现项目。

## 2.2 GitHub当前真实状态

### 已经成立

**[Verified Fact]**

`finvest-research`已经成为13个项目的研究协调hub，明确将研究实现放在submodules中，并定义了SEC数据、检索、证据选择、验证、选择性决策与公开声明之间的证据链。

当前仓库材料记录：

* 170,229条SEC CompanyFacts记录；
* 6家发行人；
* 20条solo-provisional标注；
* 60个冻结证据包；
* A11最终评价19例；
* 0 `ANSWER`；
* 18 `REVIEW`；
* 1 `ABSTAIN`；
* coverage = 0；
* BM25、dense、RRF和concept-temporal Recall@5均很低。

仓库也明确规定：

* corpus builder不得读取gold；
* production verifier不得收到gold answer；
* gold只进入离线evaluator；
* 所有公开声明必须携带证据状态。

### 尚未成立

**[Verified Fact]**

* 没有experimentally-supported论文级结果；
* 标注仍是单人provisional；
* 低Recall意味着Verifier经常无法接触正确证据；
* coverage为0意味着当前系统没有自动化效用；
* 原AUROC 0.923因gold-feature leakage被判定失效；
* 0.719只是小样本pilot；
* human study尚未完成。

**[Source-Supported Interpretation]**

当前真正成立的是一套**诚实且较完整的研究工程骨架**，不是一个已经证明有效的金融AI系统。

> **⚠ 已过时（2026-08-07 P0 修复后）**：上表"0 ANSWER / coverage=0 / integration CI failed"已改变。修复后真实 A11 = `1 ANSWER / 18 REVIEW / 0 ABSTAIN`，`answer_precision 1.0`，`unsafe_answer_rate 0.0`，Integration CI 转绿。详见 `RESEARCH_REFERENCE_RECONCILIATION.md`。

## 2.3 文献竞争密度

金融文档QA并非空白领域：

* FinQA已有专家问题和gold reasoning programs。[1]
* TAT-QA研究表格与文本联合数值推理。[2]
* MultiHiertt覆盖多层级、多表和复杂推理。[3]
* FinanceBench提供开放式金融QA和evidence strings。[4]
* MultiFinRAG已经组合文本、表格、图像和分层fallback。[5]
* FinRAGBench-V已经研究视觉检索和visual citation。[6]

Evidence sufficiency与risk control同样已有直接近邻：

* SURE-RAG将充分性视为set-level property，并输出support/refute/insufficient。[7]
* MultiHop-RAG证明多跳检索仍然是核心瓶颈。[8]
* C-RAG研究RAG generation risk的conformal控制。[9]
* RC-RAG将retrieval quality和evidence use纳入拒答风险。[10]
* RGB分别评价noise robustness、negative rejection、information integration和counterfactual robustness。[11]

版本和冲突也已进入研究前沿：

* VersionRAG显式建模技术文档版本。[12]
* conflicting-evidence RAG研究歧义、错误信息和噪声。[13]
* temporal-conflict QA研究过时和相互冲突的事实版本。[14]

**[Conclusion]**

> "金融RAG + Verifier + Abstention"已经不够新。
> "版本感知 + 最小充分证据集合 + 检索失败传播 + 风险受控人工分配"的联合问题仍有空间。

## 2.4 商业竞争密度

供应商证书、产品合规、文档抽取、证据映射和贸易文档检查已经有大量产品。公开市场中可见的相邻产品包括supplier compliance packages、product-compliance evidence、certificate/document extraction、per-SKU dossier和LC discrepancy checking。

Rossum等document automation平台已经覆盖交易文档、人工review和audit workflow；其2026年的并购也说明通用文档自动化已经成为成熟企业软件赛道。厂商性能数字只能视为vendor claims。

因此，产品不能只说：

> "AI读取供应商PDF并判断合规。"

必须形成更窄的wedge：

* cross-version；
* exact evidence regions；
* 产品适用范围；
* 双语；
* reviewer sign-off；
* change impact；
* 客户自定义control packs；
* 可导出的证据链。

## 2.5 爱尔兰匹配

University of Galway的MSc AI是90 ECTS、包含较大的研究capstone，并覆盖NLP、information retrieval、ML、deep learning、ethics和agent/RL等内容，与你的研究主线匹配度最高。

UCD Computer Science Negotiated Learning更灵活，适合组合IR、data science、software engineering和研究项目，但学费更高。

Research Ireland的centre体系包含ADAPT、Insight、Lero、I-Form和MaREI等网络；2026年的Rinn centres投资进一步强化了AI、制造和产业研究资源。

---

# SECTION 3 — GitHub Audit

## 3.1 Repository Portfolio Map

| Repository                                   | 真实角色                          | 证据状态                                      | 决策                       |
| -------------------------------------------- | ----------------------------- | ----------------------------------------- | ------------------------ |
| `finvest-research`                           | Research coordination hub     | IMPLEMENTED                               | 保留为唯一总入口                 |
| `EcoQuant-Financial-Intelligence`            | 主研究实现                         | TEST-VALIDATED / PILOT / SOLO-PROVISIONAL | 保留，收缩为论文core             |
| `green-finance-bench`                        | 合成Benchmark与metric regression | SYNTHETIC-ONLY                            | 保留为测试套件，不作真实结果           |
| `pdf-manager`                                | Document engineering与商业基础     | IMPLEMENTED                               | 保留为独立产品基础                |
| `financial-ai-contracts`                     | 跨项目数据contracts                | TEST-VALIDATED                            | 作为内部package或support repo |
| `financial-systems-verification-kit`         | 独立数值与协议验证                     | SYNTHETIC-ONLY / TEST-VALIDATED           | 保留为verification package  |
| `paper-reproduction-lab`                     | 可复现研究模板                       | SYNTHETIC-ONLY                            | 合并入research tooling      |
| `project-evidence-dossiers`                  | 声明与证据治理                       | SUPPORTING INFRASTRUCTURE                 | 合并入governance monorepo   |
| `Green-Bond-Market-Infrastructure`           | 金融基础设施原型                      | PROTOTYPE-ONLY                            | 冻结；从当前论文叙事移除             |
| `Auralynq`                                   | CFA学习产品                       | COMMERCIAL PRODUCT / PROTOTYPE            | 独立发展，不与FinVEST混合         |
| `research-defence-lab`                       | 答辩与面试训练                       | SUPPORTING                                | 合并入application/tooling   |
| `academic-application-generator`             | 申请材料生成                        | SUPPORTING                                | 合并入application/tooling   |
| `chen-ai-systems-portfolio`                  | 展示层                           | PORTFOLIO SURFACE                         | 保留一个部署，不作研究项目            |
| `repo-reconciliation-toolkit`                | 仓库治理                          | SUPPORTING                                | 合并入developer tooling     |
| `ai-research-engineering-lab`                | ML/IR学习实验                     | SYNTHETIC EDUCATIONAL                     | 冻结为学习档案                  |
| `EcoQuant-Pro-AI-Driven-Green-RWA-`          | 早期Green RWA原型                 | DUPLICATE / OUTDATED CLAIM SURFACE        | 归档                       |
| `open-exam`                                  | 与Auralynq高度重合                 | DUPLICATE                                 | 合并后归档                    |
| `Research-Ireland`                           | workspace snapshot            | DUPLICATE SNAPSHOT                        | 私有备份或归档                  |
| `elian-financial-intelligence`               | 内容无法完整核验                      | INSUFFICIENT-EVIDENCE                     | 暂停公开主叙事                  |
| `Green-Bond-Lending1` / `green-bond-lending` | 旧版/重复原型                       | DUPLICATE                                 | 归档                       |
| `deepseek-ocr-screenshot-captor`             | OCR小工具                        | UTILITY                                   | 合并到PDF Manager或归档        |
| `PDF-to-Word-Converter`                      | PDF工具                         | UTILITY / DUPLICATE                       | 合并到PDF Manager           |
| `CFA_learning`                               | 私人学习材料                        | PERSONAL                                  | 不进入科研叙事                  |
| `disk-organizer`                             | 通用工具                          | IRRELEVANT                                | 移出portfolio              |
| `frontend-optimiser`                         | 通用工具                          | IRRELEVANT                                | 移出portfolio              |
| `clearview`、`Praxis`、`self`                  | 未形成核心证据                       | INSUFFICIENT-EVIDENCE                     | 默认归档候选                   |

`pdf-manager`具有OCR、布局保持翻译、公式与表格、Typst渲染、Rust API和Python pipeline等明确工程能力，应作为商业和Document AI基础，而不是论文创新。

`financial-ai-contracts`明确只证明结构一致性，不证明金融正确性、监管合规或production fitness。

`verification-kit`和`paper-reproduction-lab`均使用合成fixture，并明确限制研究声明边界。

Green Bond Market Infrastructure拥有较完整的原型与测试，但现金轨、oracle和市场行为均是模拟，未获得监管批准，也没有生产部署。

Auralynq是独立的CFA学习系统，拥有event stream、knowledge memory、review scheduling和ResourceOS；它适合独立产品线，不应进入FinVEST论文。

## 3.2 Research Dependency Graph

```text
                              ┌──────────────────────────┐
                              │      finvest-research    │
                              │ narrative + governance   │
                              └──────────┬───────────────┘
                                         │
                    ┌────────────────────┼─────────────────────┐
                    │                    │                     │
       ┌────────────▼──────────┐ ┌──────▼───────┐ ┌──────────▼─────────┐
       │ EcoQuant / FinVEST    │ │ Governance   │ │ Document Product   │
       │ research core         │ │ contracts/   │ │ PDF Manager        │
       │                       │ │ repro        │ │                    │
       └──────┬────────────────┘ └──────────────┘ └──────────┬─────────┘
              │                                              │
     ┌────────┼─────────┐                          ┌──────────▼──────────┐
     │        │         │                          │ Evidence Revision   │
 corpus  retrieval  verification                   │ Dossier commercial  │
     │        │         │                          │ workflow            │
     └────────┴────┬────┘                          └─────────────────────┘
                  decision
        ANSWER / REVIEW / ABSTAIN

Separate product:
Auralynq → CFA learning workflow

Frozen optionality:
Green-Bond-Market-Infrastructure → future regulated-market research only
```

## 3.3 Claim-to-Code-to-Artifact Matrix

| Claim                    | Code/Artifact                               | 当前状态                   | 允许表述                                     | 禁止表述                                 |
| ------------------------ | ------------------------------------------- | ---------------------- | ---------------------------------------- | ------------------------------------ |
| Gold-blind corpus        | corpus builder、manifest、guard tests         | TEST-VALIDATED         | "Builder被测试为不依赖gold文件"                   | "已由外部独立复现"                           |
| 170,229 facts            | corpus manifest                             | PILOT ARTIFACT         | "Pilot corpus contains 170,229 records"  | "高质量公开Benchmark"                     |
| 20 annotations           | solo JSONL                                  | SOLO-PROVISIONAL       | "20 single-annotator provisional labels" | "human-validated gold"               |
| 60 evidence packages     | package manifest                            | IMPLEMENTED            | "Packages frozen and hashed"             | "annotation reliability established" |
| A11 Recall@5             | A11 result JSON                             | PILOT                  | 报告低Recall                                | 宣称SOTA                               |
| Verifier gold-free       | production signature tests                  | TEST-VALIDATED         | "gold not passed to production verifier" | "system cannot leak by any route"    |
| 0 unsafe answers         | A11 with 0 ANSWER                           | NON-INFORMATIVE SAFETY | 同时报告coverage=0                           | 宣称系统安全有效                             |
| E5 AUROC 0.923           | leakage audit                               | INVALIDATED            | 仅作失败案例                                   | 重复为成果                                |
| GreenFinanceBench 1.0    | synthetic fixtures                          | SYNTHETIC-ONLY         | metric regression                        | 真实金融性能                               |
| Integration adapters     | local report + failed remote integration CI | PARTIAL                | "implemented locally"                    | "CI-validated integration"           |
| Reduced analyst workload | 无完成human study                              | PLANNED                | 未来假设                                     | 已降低工作量                               |
| Financial infrastructure | prototype contracts                         | PROTOTYPE-ONLY         | 长期optionality                            | 生产基础设施                               |

> **⚠ 已过时（P0 修复后）**：上表"0 unsafe answers (0 ANSWER)"与"Integration adapters PARTIAL (failed CI)"已改变——修复后 A11 有 1 个正确答案且 `unsafe_answer_rate 0.0`（真实），Integration CI 转绿。

## 3.4 最大瓶颈

### 最大科研瓶颈：Retrieval validity

当前Recall@5约为个位数至10%左右，说明正确证据通常无法进入候选集。此时优化Verifier，相当于检查一份经常缺少正确材料的卷宗。

### 最大工程瓶颈：真实数据与CI的分裂

* 本地缓存和远程CI条件不同；
* 某些heavy tests依赖cache或模型；
* integration CI尚未形成可靠release gate；
* 多repo版本固定与同步成本过高。

### 最大商业瓶颈：尚未验证payer与重复工作流

有技术产品，不等于有人付费。当前没有：

* 真实付费pilot；
* measurable time saved；
* recurring document cycle；
* reviewer error reduction；
* liability acceptance；
* customer retention数据。

## 3.5 GitHub目标架构

三个月后公开portfolio最多保留四个一线入口：

1. **finvest-research**
   论文、Benchmark、实验、治理和复现总入口。

2. **finvest-core**
   由EcoQuant研究核心、GreenFinanceBench和关键contracts整合而成。

3. **pdf-manager**
   文档产品与工业证据工作流。

4. **auralynq**
   独立学习产品。

内部工具合并成：

```text
finvest-tooling/
  governance/
  contracts/
  verification/
  reproduction/
  dossiers/
  application/
  repo-audit/
```

---

# SECTION 4 — Literature Synthesis

## 4.1 搜索协议与配额审计

本次建立了一个紧凑的 **103-source evidence matrix**：

| 类别                                        |      数量 |
| ----------------------------------------- | ------: |
| AI / CS                                   |      50 |
| Finance / Economics                       |      13 |
| Mathematics / Statistics / Optimisation   |      13 |
| Physics / Complex Systems / Energy        |       6 |
| Industrial / Supply Chain / Operations    |       9 |
| Policy / Regulation / Official Programmes |      12 |
| **总计**                                    | **103** |

质量审计：

* 约69项为正式同行评审论文；
* 约62项发表于2022—2026；
* 预印本低于30%；
* 政策、学校与监管信息使用官方来源；
* 同一来源只计入一个主类别；
* 最关键17项完成了更深度核验。

## 4.2 核心研究发现

### 发现一：Financial Document QA仍然困难，但Benchmark很多

FinQA、TAT-QA和MultiHiertt已经覆盖：文本与表格、gold reasoning programs、算术运算、多表与层级结构、supporting facts。[1]–[3]

FinanceBench进一步表明，即使是相对清晰的open-book金融问题，检索增强系统也会大量错误或拒答。[4]

因此，建立另一个普通金融QA dataset并不足以形成贡献。新Benchmark必须突出：version、amendment、cutoff、stale evidence、conflicting evidence、insufficient evidence、minimal evidence set、selective risk。

### 发现二：Multimodal Financial RAG已明显拥挤

MultiFinRAG已经进行模态感知抽取和fallback。[5] FinRAGBench-V已经覆盖大规模视觉页面、双语、visual citation和自动引用评价。[6]

因此，以下内容不再构成强创新：把表格截图送给VLM；图像转文字后embedding；text/table/image三路检索；普通hybrid retrieval；生成答案附页码。

### 发现三：Evidence sufficiency已有直接近邻

SURE-RAG明确提出：relevance不等于sufficiency；sufficiency是集合级属性；support/refute/insufficient；selective answer；calibrated risk。[7]

因此，你不能把"三分类Verifier"或"集合充分性"单独列为创新。

真正可区分之处应是：

1. 证据单位具有版本与有效期；
2. sufficiency以金融计算或审计requirements定义；
3. 正确证据可能根本未被retrieval找到；
4. 证据选择与review allocation联合优化；
5. benchmark按issuer/time/version拆分；
6. 评价人工复核成本，而不仅是Macro-F1。

### 发现四：Risk-controlled refusal已有方法学基础

C-RAG已经研究generation risk上界；RC-RAG研究retrieval quality和evidence use对拒答风险的影响。[9][10]

因此，研究贡献不能只是"我们使用conformal prediction选择阈值"。必须展示：risk定义与金融错误成本的关系；calibration数据与test distribution隔离；under-shift表现；coverage；review cost；failure-aware calibration；small-sample不确定性。

### 发现五：Version-aware retrieval是新兴但不再空白

VersionRAG已经将版本序列、content boundaries和change tracking纳入技术文档QA。[12] Temporal-conflict和conflicting-evidence研究也已证明，模型会被旧版本和冲突材料误导。[13][14]

因此，你的gap不能写成"现有RAG没有考虑文档版本"。

更准确的gap是：

> 现有工作尚未充分研究，在金融和工业文档中，版本约束、最小证据集合、数值可执行性、检索遗漏和人工复核成本如何被统一到一个风险受控决策问题中。

### 发现六：Human review本身可以成为方法贡献

Targeted Automation研究表明，自动化比例、人工改进和未来学习数据之间存在权衡。[15]

这启发你的系统不应只输出"是否拒答"，而应判断：哪些case值得人工审查；审查哪一个证据缺口；人工补充哪一项信息价值最高；如何避免自动化后失去训练反馈；如何控制review capacity。

### 发现七：工业域不是简单替换数据集

供应链风险KG和digital thread文献已经覆盖企业、产品、认证、能力和生命周期数据。[16][17]

工业域有合理共同结构：文档不断更新；多主体；证据存在有效期；规则依赖产品范围；决策需要审计；错误成本不对称。

但要证明跨域合理，必须建立结构映射，而不是仅同时测试"SEC PDF"和"工业PDF"。

## 4.3 Literature Evidence Matrix

### AI / CS — S001–S050

| ID   | Source                                                   | 年份/类别                      | 证据角色                                       |
| ---- | -------------------------------------------------------- | -------------------------- | ------------------------------------------ |
| S001 | FinQA                                                    | 2021, peer-reviewed        | 金融数值QA与gold programs                       |
| S002 | TAT-QA                                                   | 2021, peer-reviewed        | 表格—文本联合推理                                  |
| S003 | ConvFinQA                                                | 2022, peer-reviewed        | 对话式金融推理链                                   |
| S004 | MultiHiertt                                              | 2022, peer-reviewed        | 多层级、多表推理                                   |
| S005 | FinanceBench                                             | 2023, preprint             | 真实金融open-book QA                           |
| S006 | SEC-QA                                                   | 2024, preprint/workshop    | 持续更新、多文档SEC QA                             |
| S007 | Evaluating LLMs' Mathematical Reasoning in Financial DQA | 2024, preprint             | 多步算术失败                                     |
| S008 | FinQAPT                                                  | 2024, peer-reviewed        | end-to-end financial QA pipeline           |
| S009 | MultiFinRAG                                              | 2025, peer-reviewed        | 多模态金融RAG                                   |
| S010 | FinRAGBench-V                                            | 2025, peer-reviewed record | 视觉检索与引用                                    |
| S011 | Multimodal RAG for Financial Documents                   | 2025, peer-reviewed        | 图表和表格image-centric QA                      |
| S012 | FinMMDocR                                                | 2025, preprint             | 长文档、跨页、多步金融推理                              |
| S013 | FinLongDocQA                                             | 2026, preprint             | 多表与长上下文                                    |
| S014 | FinCARDS                                                 | 2026, preprint             | 金融schema约束reranking                        |
| S015 | HierFinRAG                                               | 2026, peer-reviewed        | 层级表文融合与symbolic routing                    |
| S016 | ChartQA                                                  | 2022, peer-reviewed        | 图表视觉与逻辑推理                                  |
| S017 | PlotQA                                                   | 2020, peer-reviewed        | 科学图表数值QA                                   |
| S018 | DocVQA                                                   | 2021, peer-reviewed        | 文档图像VQA                                    |
| S019 | InfographicVQA                                           | 2022, peer-reviewed        | 视觉布局与信息图                                   |
| S020 | LayoutLM                                                 | 2020, peer-reviewed        | 文本与布局联合表示                                  |
| S021 | LayoutLMv2                                               | 2021, peer-reviewed        | 视觉—文本预训练                                   |
| S022 | LayoutLMv3                                               | 2022, peer-reviewed        | unified document pretraining               |
| S023 | Donut                                                    | 2022, peer-reviewed        | OCR-free document understanding            |
| S024 | Nougat                                                   | 2023, peer-reviewed        | academic PDF parsing                       |
| S025 | Retrieval-Augmented Generation                           | 2020, peer-reviewed        | RAG基础                                      |
| S026 | Dense Passage Retrieval                                  | 2020, peer-reviewed        | dense retrieval基础                          |
| S027 | ColBERT                                                  | 2020, peer-reviewed        | late interaction                           |
| S028 | SPLADE v2                                                | 2021, peer-reviewed        | learned sparse retrieval                   |
| S029 | BEIR                                                     | 2021, peer-reviewed        | heterogeneous retrieval evaluation         |
| S030 | Contriever                                               | 2022, peer-reviewed        | unsupervised dense retrieval               |
| S031 | IRCoT                                                    | 2023, peer-reviewed        | retrieval与chain-of-thought交替               |
| S032 | MultiHop-RAG                                             | 2024, preprint             | 多跳RAG Benchmark                            |
| S033 | RGB                                                      | 2023/24, peer-reviewed     | noise、rejection、integration、counterfactual |
| S034 | ALCE                                                     | 2023, peer-reviewed        | 引用式长文本生成                                   |
| S035 | FActScore                                                | 2023, peer-reviewed        | atomic factuality                          |
| S036 | QAFactEval                                               | 2022, peer-reviewed        | QA-based factual consistency               |
| S037 | SelfCheckGPT                                             | 2023, peer-reviewed        | black-box hallucination detection          |
| S038 | SURE-RAG                                                 | 2026, preprint             | set-level sufficiency                      |
| S039 | C-RAG                                                    | 2024, peer-reviewed        | conformal generation risk                  |
| S040 | RC-RAG Counterfactual Risk Control                       | 2024, preprint             | risk-aware refusal                         |
| S041 | VersionRAG                                               | 2025, preprint             | evolving document versions                 |
| S042 | RAG with Conflicting Evidence                            | 2025, preprint             | ambiguity、misinformation、noise             |
| S043 | QA under Temporal Conflict                               | 2025, preprint             | evolving and stale facts                   |
| S044 | ChronoQA                                                 | 2025, peer-reviewed        | temporal-sensitive RAG                     |
| S045 | FRESCO                                                   | 2026, preprint             | evolving semantic conflict reranking       |
| S046 | S2G-RAG                                                  | 2026, peer-reviewed record | sufficiency与gap judging                    |
| S047 | ScienceAgentBench                                        | 2024, preprint             | 科研agent严谨评价                                |
| S048 | Benchmarking Benchmark Leakage in LLMs                   | 2024, preprint             | 数据污染                                       |
| S049 | SWE-Bench+                                               | 2024, preprint             | 弱测试和solution leakage                       |
| S050 | MME                                                      | 2023, benchmark paper      | 多模态模型综合评价                                  |

### Finance / Economics — S051–S063

| ID   | Source                                                                                        | 用途                     |
| ---- | --------------------------------------------------------------------------------------------- | ---------------------- |
| S051 | Akerlof, The Market for "Lemons"                                                              | 信息不对称                  |
| S052 | Grossman & Stiglitz, On the Impossibility of Informationally Efficient Markets              | 信息生产价值                 |
| S053 | Stiglitz & Weiss, Credit Rationing in Markets with Imperfect Information                    | 信贷信息不对称                |
| S054 | Diamond, Financial Intermediation and Delegated Monitoring                                  | 受托监督                   |
| S055 | Leland & Pyle, Informational Asymmetries, Financial Structure, and Financial Intermediation | 信号与金融结构                |
| S056 | Jensen & Meckling, Theory of the Firm                                                       | agency与monitoring cost |
| S057 | Healy & Palepu, Information Asymmetry, Corporate Disclosure, and Capital Markets            | 公司披露                   |
| S058 | Bushman & Smith, Financial Accounting Information and Corporate Governance                  | 会计信息与治理                |
| S059 | Feng Li, The Information Content of Forward-Looking Statements                              | 年报文本信息                 |
| S060 | Loughran & McDonald, When Is a Liability Not a Liability?                                   | 金融文本领域词典               |
| S061 | Berg et al., On the Rise of FinTechs—Credit Scoring Using Digital Footprints                | alternative data       |
| S062 | Bartlett et al., Consumer-Lending Discrimination in the FinTech Era                         | 算法与公平                  |
| S063 | Fuster et al., Predictably Unequal?                                                         | ML信贷分配影响               |

### Mathematics / Statistics / Optimisation — S064–S076

| ID   | Source                                                | 用途                           |
| ---- | ----------------------------------------------------- | ---------------------------- |
| S064 | El-Yaniv, Foundations of Selective Classification     | 拒答理论                         |
| S065 | Geifman & El-Yaniv, Selective Classification for DNNs | risk–coverage                |
| S066 | Learn then Test                                       | 风险校准                         |
| S067 | Conformal Risk Control                                | 有限样本risk control             |
| S068 | Nemhauser–Wolsey–Fisher                               | submodular greedy            |
| S069 | Sviridenko, Submodular Knapsack                       | 预算化选择                        |
| S070 | Golovin & Krause, Adaptive Submodularity              | 序贯信息获取                       |
| S071 | Bertsimas & Sim, Robust Discrete Optimization         | 不确定性与鲁棒约束                    |
| S072 | Lewis & Gale, Sequential Text Classification          | active learning              |
| S073 | Targeted Automation and Sustaining Human–AI Learning  | review allocation            |
| S074 | When Should Humans Step In?                           | costly human dispatch        |
| S075 | Learning Conformal Abstention Policies                | 动态拒答阈值                       |
| S076 | COIN                                                  | selective QA risk guarantees |

### Physics / Complex Systems / Energy — S077–S082

| ID   | Source                                                           | 用途             |
| ---- | ---------------------------------------------------------------- | -------------- |
| S077 | Albert–Jeong–Barabási, Error and Attack Tolerance                | 网络脆弱性          |
| S078 | Buldyrev et al., Catastrophic Cascade of Failures                | 相互依赖网络         |
| S079 | Gao et al., Universal Resilience Patterns                        | 系统韧性           |
| S080 | Brummitt et al., Suppressing Cascades in Interdependent Networks | cascading risk |
| S081 | Ouyang, Interdependent Critical Infrastructure Review            | 基础设施依赖         |
| S082 | Panteli & Mancarella, Power-System Resilience Framework          | 能源基础设施韧性       |

### Industrial / Supply Chain / Operations — S083–S091

| ID   | Source                                                  | 用途                    |
| ---- | ------------------------------------------------------- | --------------------- |
| S083 | Kosasih et al., KG Reasoning for Supply-Chain Risk      | 供应商图谱与隐性风险            |
| S084 | Abdel-Aty & Negri, Digital Thread Review                | 生命周期证据                |
| S085 | Kwon et al., Standards-Based Digital Thread             | 设计—检测数据连接             |
| S086 | Buchgeher et al., KGs in Manufacturing                  | 制造KG综述                |
| S087 | Yahya et al., Semantic Web and KGs for Industry 4.0     | 工业语义                  |
| S088 | Ivanov & Dolgui, Digital Supply-Chain Twin              | disruption management |
| S089 | Christopher & Peck, Building the Resilient Supply Chain | 韧性管理                  |
| S090 | Tang, Robust Strategies for Supply-Chain Disruptions    | 风险策略                  |
| S091 | Cognitive Digital Twin in Manufacturing                 | 人机协作与工业知识             |

### Policy / Regulation / Official Sources — S092–S103

| ID   | Source                                          | 用途                       |
| ---- | ----------------------------------------------- | ------------------------ |
| S092 | EU AI Act                                       | AI治理与高风险要求               |
| S093 | DORA                                            | 金融ICT与第三方风险              |
| S094 | EBA Risk Assessment 2026                        | 金融AI风险                   |
| S095 | Central Bank of Ireland Regulatory Outlook 2026 | 监管重点                     |
| S096 | IOSCO AI Supervisory Toolkit 2026               | 证券监管与监督                  |
| S097 | NIST AI RMF 1.0                                 | AI风险框架                   |
| S098 | Research Ireland Centres                        | 爱尔兰研究网络                  |
| S099 | Rinn Centres Investment 2026                    | AI与产业研究资源                |
| S100 | University of Galway MSc AI                     | 课程与capstone              |
| S101 | UCD Negotiated Learning                         | 灵活课程与入学要求                |
| S102 | UL Official Module Catalogue                    | AI、risk与research modules |
| S103 | EU ESPR / Digital Product Passport              | 产品证据与生命周期数据              |

## 4.4 关键论文正式记录

[1] FinQA — Wenhu Chen et al., 2021, EMNLP, 750 citations.
[2] TAT-QA — Fengbin Zhu et al., 2021, ACL-IJCNLP, 568 citations.
[3] MultiHiertt — Yilun Zhao et al., 2022, ACL/arXiv, 189 citations.
[4] FinanceBench — Pranab Islam et al., 2023, arXiv, 258 citations.
[5] MultiFinRAG — Chinmay Gondhalekar, Urjitkumar Patel, Fang-Chun Yeh, 2025, IEEE BigData, 13 citations.
[6] FinRAGBench-V — Suifeng Zhao et al., 2025, proceedings record, 12 citations.
[7] SURE-RAG — Jing Qiu, Zeyu Han, Chengen Huang, 2026, arXiv, 0 citations.
[8] MultiHop-RAG — Yixuan Tang, Yi Yang, 2024, arXiv, 308 citations.
[9] C-RAG — Mintong Kang et al., 2024, proceedings record, 35 citations.
[10] RC-RAG — Luyao Chen et al., 2024, arXiv, 14 citations.
[11] RGB — Jiawei Chen et al., 2023, proceedings record, 602 citations.
[12] VersionRAG — Daniel Huwiler, Kurt Stockinger, Jonathan Fürst, 2025, arXiv, 5 citations.
[13] RAG with Conflicting Evidence — Han Wang et al., 2025, arXiv, 65 citations.
[14] QA under Temporal Conflict — Atahan Özer, Çagatay Yildiz, 2025, arXiv, 3 citations.
[15] Targeted Automation and Sustaining Human-AI Learning — Christina Imdahl, William Schmidt, Kai Hoberg, 2025, Production and Operations Management, 1 citation.
[16] KG Reasoning for Supply Chain Risk Management — E. Kosasih et al., 2022, IJPR, 130 citations.
[17] Digital Thread for Smart Manufacturing — T. A. Abdel-Aty, Elisa Negri, 2024, JIM, 47 citations.

---

# SECTION 5 — Candidate Direction Tournament

## 5.1 初始八个方向

| 方向                                             | 初判                 |
| ---------------------------------------------- | ------------------ |
| Risk-Controlled Version-Aware Evidence Systems | 决赛                 |
| Minimum Sufficient Evidence Set Selection      | 并入终极方向             |
| Evaluation Science for Complex Document Agents | 决赛                 |
| Cross-Border Industrial Evidence Intelligence  | 决赛                 |
| Human Review Allocation under Selective Risk   | 决赛                 |
| Temporal and Version-Aware Financial QA        | 被终极方向覆盖            |
| Trade and Supply-Chain Finance Evidence AI     | 决赛                 |
| Current Verifier-Guided Multimodal RAG         | 淘汰为主论文，保留为baseline |

## 5.2 100分评分

| 方向                                            |       总分 | 关键优势             | 关键缺陷            |
| --------------------------------------------- | -------: | ------------------ | --------------- |
| Version-Aware Minimum Evidence + Risk Control | **83.3** | 统一科研、产品和长期路径     | 必须获得高质量标注       |
| Industrial Evidence Intelligence              |     81.4 | 商业/data moat强    | 学术方法可能不足        |
| Human Review Allocation                       |     81.3 | 数学与实际成本强         | 需要真实review data |
| Trade & Supply-Chain Finance Evidence AI      |     80.9 | 金融optionalities强 | 数据和监管门槛         |
| Document Agent Evaluation Science             |     79.0 | 新颖性和顶会fit        | 商业闭环弱           |
| Industrial Digital Thread/Evidence Graph      |     78.4 | 三年基础设施潜力         | 单人十个月过大         |
| Temporal Financial QA                         |     77.5 | 清晰、可执行           | VersionRAG等近邻强  |
| 当前Multimodal RAG + Verifier                   |     66.5 | 工程资产充足           | 新颖性低、Recall低    |

## 5.3 Pareto Frontier

进入Pareto frontier：Version-aware minimum evidence；industrial evidence；human review allocation；trade-finance evidence；evaluation science。

被严格或近似支配：单独temporal QA；普通multimodal financial RAG。

## 5.4 Sensitivity Analysis

主方向失去第一名的主要条件：

1. **商业权重极高、学术权重极低**：Industrial Evidence Intelligence可能成为第一。
2. **无法获得第二标注者或真实版本数据**：Evaluation Science可能成为第一。
3. **检索Recall长期无法提升**：应转向Benchmark/retrieval failure，而不是继续Verifier。
4. **工业客户愿意提供高价值文档和付费pilot**：工业产品可提前成为执行重点，但论文仍保持金融单域。

---

# SECTION 6 — Research Programme

## 6.1 符号

设：D（文档集合）、d∈D（单一文档）、v∈V(d)（文档版本）、p（页）、r（页内证据区域）、q（问题）、t_q（问题要求的时间或cutoff）、e（EvidenceUnit）、C_q（检索候选集合）、S_q⊆C_q（选择的证据集合）、y（候选答案）、a∈{ANSWER,REVIEW,ABSTAIN}、G_q（问题requirement graph）、R(a)（选择性错误风险）、c_r（人工复核成本）、c_a（拒答成本）、c_e（证据处理成本）。

定义EvidenceUnit：

```
e=(d,v,p,r,t_s,t_v,z,u,h,m)
```

其中：t_s（source/publication time）、t_v（validity interval）、z（版本、amendment或supersession状态）、u（单位与scale）、h（hash/provenance）、m（modality与metadata）。

## 6.2 Problem Statement

给定问题 q 和版本化文档库，系统必须：

1. 检索可能相关的EvidenceUnits；
2. 选择最小但充分的证据集合；
3. 产生或验证答案；
4. 检测版本、时间、数值和来源冲突；
5. 在风险约束下决定自动回答、人工复核或拒答。

## 6.3 Objective

```
max_{S,y,a}  B_c·P(correct|S,y) − C_err·P(error|S,y) − c_e·|S| − c_r·1[a=REVIEW] − c_a·1[a=ABSTAIN]
```

约束：

```
P(error|a=ANSWER) ≤ α
Coverage(S,G_q) ≥ τ
VersionConsistent(S,t_q) = 1
NumericallyExecutable(S,y) = 1
```

## 6.4 Evidence Sufficiency

S 充分，当且仅当：

1. G_q 中所有required nodes均被证据覆盖；
2. required edges或计算关系可执行；
3. 没有未解决的高严重度冲突；
4. 证据在cutoff前有效；
5. superseded evidence未被错误使用；
6. 所有关键claim都有provenance；
7. 删除任一必要evidence会导致至少一个requirement不再满足（minimality）。

## 6.5 Evidence Selection

可定义：

```
F(S) = Σ_{j∈G_q} w_j·min(1, Σ_{e∈S} c_ej) + λ·D(S) − μ·R_d(S) − ν·V_c(S) − ξ·|S|
```

其中：c_ej（证据对requirement j的覆盖）、D(S)（证据多样性）、R_d(S)（冗余）、V_c(S)（版本冲突）、|S|（集合大小）。

求解方法：greedy cover；beam search；small-case ILP oracle；learned reranker/selector；adaptive retrieval when gaps remain。

Set cover一般是NP-hard，因此不能声称全局最优。对于满足单调submodular假设的理想化子问题，greedy具有经典近似性质；真实版本和冲突惩罚可能破坏这些假设。

## 6.6 Review Allocation

定义人工复核的Value of Information：

```
VOI(i) = E[ΔL_i | review] / c_r(i)
```

当 max_i VOI(i) > 0，系统选择 REVIEW，并将最有价值的缺口交给人，而不是简单展示全部top-k。

例如：确认哪一个amended filing有效；判断两个XBRL概念是否语义等价；核验表中单位；判断证书是否覆盖目标产品型号；确认缺失证据是否确实不存在。

## 6.7 Toy Example

问题：截至2024年11月1日，公司FY2024自由现金流是多少？

候选材料包含：2024原始10-K中的operating cash flow；2024原始10-K中的capital expenditure；2025 10-K中重新列示的2024比较数字；一个季度表；一个错误单位的摘要。

系统必须：识别cutoff；优先选择cutoff前可获得的原始filing；选择OCF和CapEx两个证据单位；检查period、单位和sign；执行公式；若2024和2025版本存在material restatement，则在cutoff语义下使用原始版本并说明后续restatement；若问题要求"最新已知FY2024值"，则使用最新有效版本；无法确定问题语义时转 REVIEW。

## 6.8 Dataset

| 维度                                | 设计                        |
| --------------------------------- | ------------------------- |
| Issuers                           | 36—50                     |
| 时间                                | 2019—2026                 |
| 文件                                | 10-K、10-Q、8-K、10-K/A      |
| Base cases                        | 360                       |
| Multi-evidence cases              | 120                       |
| Conflict/insufficient/adversarial | 120                       |
| 总计                                | 约600                      |
| 双人标注                              | 100—150                   |
| 完整adjudication                    | disagreement + 50随机一致case |
| 工业transfer                        | 60—80，可选且需授权              |

Question types：direct extraction；numerical derivation；cross-table；cross-page；version-sensitive；point-in-time；amended filing；conflicting evidence；insufficient evidence；minimal-set comparison；review-needed。

## 6.9 Annotation Protocol

标注者分别回答：

1. 问题是否answerable？
2. cutoff和版本语义是什么？
3. 所需证据有哪些？
4. 哪些是必要证据？
5. 哪些是冗余证据？
6. 是否存在冲突？
7. 是否需要计算？
8. gold calculation program是什么？
9. 理想动作是ANSWER、REVIEW还是ABSTAIN？
10. 信心与争议原因。

质量控制：候选答案在初次判断前隐藏；标注证据包冻结；source hash记录；机器校验在人工判断后执行；第二标注者独立；disagreement adjudication；记录原始判断，不仅保留最终gold。

IAA：categorical labels用Cohen's κ或Krippendorff's α；evidence set用Jaccard、set-F1；numerical answer用exact/tolerance agreement；route用weighted κ。

## 6.10 Splits与Leakage Controls

必须同时报告：issuer holdout；chronological holdout；amendment/version holdout；document-template holdout；question-family holdout。

泄漏控制：corpus builder不读取case或annotation；production pipeline不接收gold；query generation模板不得包含答案字符串；同一filing的比较版本不得跨train/test错误共享；feature只能来自inference-time information；oracle selectors只能作upper bound；frozen manifests；model、prompt、commit、seed和API version记录；benchmark contamination card。

## 6.11 Baselines

Retrieval：BM25；small dense embedding；SPLADE或等效learned sparse；ColBERT-style late interaction；RRF；metadata/time filter；finance-aware concept matching；version-aware filtering。

Selection：top-k；MMR；greedy set cover；beam；learned selector；ILP oracle。

Verification：no verifier；pairwise support classifier；concatenated cross-encoder；SURE-RAG-like set verifier；numerical program execution；version-only；joint version+numerical。

Routing：always answer；always review；confidence threshold；temperature/Platt；split conformal；cost-aware review policy。

## 6.12 Metrics

Retrieval：Recall@1/5/20；MRR；nDCG；document recall；stale evidence rate；version-correct recall。

Evidence set：all-required-evidence recall；set precision；set-F1；exact set match；minimality violation；redundancy；average tokens。

Answer：exact match；numeric tolerance；program execution accuracy；citation entailment；temporal/version accuracy。

Selective system：risk–coverage curve；AURC；coverage at 1%、5%、10% risk；unsafe answer rate；review precision；false-review rate；abstention precision；calibration ECE、Brier、NLL。

Operational：reviewer minutes；cases per reviewer-hour；latency；API cost；error cost avoided；review burden reduction。

## 6.13 Statistical Analysis

issuer-stratified bootstrap 10,000次；95% confidence intervals；paired permutation tests；binary outcomes用McNemar；Holm correction；effect sizes；多seed报告；per-question-family与per-issuer结果；不报告只有一个聚合平均数。

## 6.14 Go/No-Go Gates

| 时间       | 门槛                             | 未达成动作                    |
| -------- | ------------------------------ | ------------------------ |
| Month 2  | 至少50个可复核case                   | 停止算法开发，修Benchmark        |
| Month 3  | 第二标注者确定                        | 无第二标注者则降级为pilot          |
| Month 4  | IAA ≥ 0.70                     | 重写定义和界面                  |
| Month 5  | Recall@20 ≥ 0.70               | 论文转向retrieval            |
| Month 6  | all-required set recall ≥ 0.55 | 停止calibration主张          |
| Month 7  | coverage ≥ 20% at ≤5% risk     | 不得宣称自动化效用                |
| Month 8  | version holdout gain成立         | 否则移除version novelty      |
| Month 9  | 至少一项显著且有实质效应                   | 转Benchmark/failure paper |
| Month 10 | 可独立复现                          | 不投稿主会                    |

---

# SECTION 7 — Top-Venue Review

## 7.1 Venue匹配

### SIGIR

最匹配：retrieval；reranking；set selection；temporal/version-aware ranking；reproducibility；Benchmark。

SIGIR的reproducibility方向欢迎通过重复、泛化或审计产生的新发现。

### ACL / EMNLP / NAACL

最匹配：financial/document QA；evidence sufficiency；temporal reasoning；numerical reasoning；multilingual industrial transfer；resource/Benchmark；negative findings。

ACL明确允许资源、复现和negative findings，但要求原创贡献、limitations和ethics。

### ICDAR

最匹配：document layout；tables/formulas；visual evidence；provenance；complex-document Benchmark；industrial documents。

ICDAR的scope直接覆盖document retrieval、表格、公式、provenance和Benchmark。

### FAccT / AIES

只有当论文真正研究：谁应复核；错误成本；人机责任；auditability；automation bias；review allocation；evidence transparency。

FAccT强调evaluation practices、audits、metrics与风险。

### NeurIPS / ICML / ICLR

当前不建议作为首要目标。除非出现：新的selective-risk理论；一般化的set-selection方法；明确的有限样本保证；多域大规模实验；对现有方法有稳定、显著的提升。

## 7.2 当

*[输入在此处被截断——§7.2 及之后的内容不可用。]*

---

*本文档由用户提供的战略文档转录（截至输入可读范围）。关键数字与门槛保持原文。已过时声明已在相关位置标注 ⚠。*
