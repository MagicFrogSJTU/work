# 评测方案

## 整体需求

benchmark由3部分组成:
- 公开资料：模型商报告 / 第三方报告
- 有限复现：公开benchmark
- 重点自测：智船benchmark

测试对象：
- 知名、最新 大模型

产出：
- 频率：一般每月定期产出。有重要影响力的新模型的时候，可以加急发一版。
- 交付物
  - 评测报告
  - 评测网站：包含分数看板，错误数据可视化

### 当前先不做的

- 开源模型特有：在线API/内网部署对比

## benchmark

重点关注：
- 纯文本
- 图像理解
- agent能力（上下文长度、工具调用能力、指令遵从性）

benchmark 拆成三部分，分别承担不同作用：
- 公开资料：快速筛选候选模型，成本最低，不直接作为最终结论
- 有限复现：用统一口径复现少量公开benchmark，验证官方说法是否可信
- 重点自测：围绕真实业务场景构建智船benchmark，作为最终选型依据

### benchmark文档索引

- [公开资料](./public_material.md)：整理模型商报告、第三方报告及公开资料摘录模板
- [公开benchmark](./public_benchmark.md)：定义有限复现的范围、选型原则、建议清单与输出模板
- [智船benchmark](./zhichuan_benchmark.md)：保留业务场景框架，后续单独补全

### 相关模板

- [月度评测报告模板](./monthly_report_template.md)：用于汇总公开资料、公开benchmark和智船benchmark结果

### 使用原则

- 公开资料用于市场扫描，不做最终判断
- 公开benchmark用于统一口径比较，不追求覆盖大全
- 智船benchmark用于业务验证，权重最高

### 推荐权重

- 公开资料：20%
- 公开benchmark：30%
- 智船benchmark：50%

## Model

- openai gpt
- google gemini
- anthropic claude
- ali qwen
- bytedance seed
- deepseek
