# 在哦 DEMO - 主动沟通的知识机器人
https://www.bilibili.com/video/BV1eXyHBaEJY/?spm_id_from=333.1387.homepage.video_card.click&vd_source=7b7e42b072c6f1cec64e402f737ceef3
## 项目概述

**在哦 DEMO** 是一个创新的知识机器人，致力于成为一个 **主动沟通的智能体**。它不是传统意义上的智慧体，而是一个新型的对话媒介，通过深层交流帮助用户发现新的问题视角和知识洞见。

### 核心特性

- 🎯 **主动性** - 主动思考、推进话题
- 🔍 **审时度势** - 在因缘际会时推介对应观点
- 💬 **互动反馈** - 平等对话、双向反馈

### 设计哲学

> "一生二、二生三、三生万物"

这个项目遵循以下设计理念：
- 我们编程的是一个逻辑点，希望它们能连接成功能
- 在与用户互动中产生新的可能性
- 作为沟通引擎，强点在于开启新的思维视角
- 是人的见证者和对话伙伴，而非独立思考者

## 使用场景

在哦 DEMO 特别适合以下场景：

- 需要深层次对话的知识探讨
- 寻求新的问题解决视角
- 自我认识和内心对话
- 知识梳理和总结输出

## 快速开始

### 环境要求

- Python 3.10 或更高版本
- pip 或 uv 包管理器

### 安装步骤

1. **克隆或解压项目文件**
   ```bash
   # 保持以下目录结构完整
   # assets/        - 图片资源（娃娃、渐变图等）
   # config/        - 配置文件
   # data/          - 数据文件（对话日志、状态等）
   # core/          - 核心引擎模块
   ```

2. **创建虚拟环境**

   使用 uv（推荐）：
   ```bash
   uv venv
   source .venv/bin/activate  # macOS/Linux
   # 或
   .venv\Scripts\activate     # Windows
   ```

   或使用 pip：
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   ```

3. **安装依赖**
   ```bash
   uv pip install -r requirements.txt
   # 或
   pip install -r requirements.txt
   ```

4. **配置 API KEY**

   程序首次运行会提示输入 API KEY，或点击界面右侧"输入 API KEY"按钮：
   - 目前支持 DeepSeek API
   - 获取方式：https://platform.deepseek.com/
   - API KEY 格式：`sk-` 开头的一串字符

5. **启动程序**
   ```bash
   python main.py
   ```

## 程序运行
<img width="1038" height="613" alt="image" src="https://github.com/user-attachments/assets/13ea27a3-3622-445e-8313-6b598cf4a3a1" />

<img width="1038" height="613" alt="image" src="https://github.com/user-attachments/assets/ba0f6d79-9c1c-4aa2-bf83-bd7b13e04e13" />

### 界面组成

```
┌─────────────────────────────────────────┐
│          📌 在哦 DEMO版                  │
├──────────────┬──────────────┬───────────┤
│              │              │           │
│   娃娃虚拟形象 │  聊天气泡区域 │ 功能按钮栏 │
│   (ON/OFF状态)│  (左粉/右青)  │           │
│              │              │           │
├──────────────┴──────────────┴───────────┤
│  输入框                        发送 按钮 │
└─────────────────────────────────────────┘
```

### 工作流程

1. **初期交互** - 在哦会问一些问题了解你的情况
2. **主题推荐** - 转入观点引擎，推荐新的思考角度
3. **知识总结** - 进入总结引擎，梳理对话内容
4. **持续探索** - 可基于总结继续深层对话

### 交互提示

- 🔴 **娃娃灭灯（OFF）** - 在哦正在思考中，请耐心等待
- 🟢 **娃娃亮灯（ON）** - 在哦已准备好，可以继续交流

### 右侧功能按钮

| 按钮 | 功能描述 |
|-----|--------|
| 输入 API KEY | 配置或更新 DeepSeek API 密钥 |
| 查看人格引擎 | 查看 LLM 调用日志和提示词 |
| 回到初见 | 清空对话记录，重新开始 |
| 在哦理解你 | 查看当前状态快照（情绪、能量、活动等） |
| 观点树 | 查看自动生成的观点树结构 |
| 模拟忙碌 | 测试娃娃状态切换 |
| 时光飞逝下 | 触发时间跳过，让在哦思念你 |

## 项目结构

```
zaio_app_v2/
├── main.py
├── log_view_controller.py
├── run.ipynb
├── 文件结构说明.txt（本文件）
│
├── assets/
│
├── config/
│   ├── api_key.txt          ← 存储你的key
│   └── settings.yaml
│
├── core/
│   ├── __init__.py
│   ├── first_turn.py        ← 第一拍开场引擎
│   └── orchestrator.py      ← 我们刚刚改的数据流总控
│
├── data/
│   ├── current_state_snapshot.json
│   ├── tree_default.json
│   ├── logs/
│   │   └── ...（每天的对话日志，对应 对话_日期.txt）
│   ├── perspective_trees/
│   │   └── ...（观点树 JSON）
│   └── prompt_logs/
│       ├── llm_prompt_log.txt
│       └── llm_trigger_log.txt
│
├── llm/
│   ├── __init__.py
│   └── client.py            ← 所有 LLM 调用入口（role → prompt_map）重要节点
│
├── persona/
│   ├── __init__.py
│   ├── fast_engine.py       ← Q-Engine（快人格）
│   ├── slow_engine.py       ← T-Engine（慢人格）
│   ├── direct_engine.py     ← L-Engine（直答人格）
│   ├── deep_engine.py        ← D-Engine（描绘人格）
│   └── sum_engine.py        ← SUM-Engine（总结人格）
│
├── state/
│   ├── __init__.py
│   ├── history_manager.py   ← 对话历史管理
│   ├── snapshot_manager.py  ← current_state_snapshot 的读写
│   └── user_profile.py      ← 用户长期画像
│
├── thinking/
│   ├── __init__.py
│   ├── behavior_selector.py           ← 现在已经不负责选引擎了，只是历史遗留
│   ├── guess_engine.py
│   ├── perspective_generate_engine.py ← 观点树生成引擎
│   └── perspective_tree.py            ← 运行时观点树结构与操作
│
├── trigger/
│   ├── __init__.py
│   ├── engine_select_trigger.py       ← ✅ 现在真正的 Q/T/L/SUM 选择器
│   ├── perspective_move_trigger.py    ← T 引擎内部，决定怎么看树 / 跳节点
│   ├── state_update_trigger.py        ← 更新 snapshot 的 LLM 触发器
│   ├── talk_trigger.py                ← “要不要说话”的触发器
│   └── timing_engine.py               ← 非 LLM 的节奏/冷却引擎
│
└── ui/
    └── __init__.py    ← DearPyGUI 的 UI 逻辑（chat 窗口、娃娃、按钮等）
```

## 数据文件说明

### 对话日志
- 位置：`data/logs/对话_YYYYMMDD.txt`
- 内容：每日所有对话记录（用户 + AI）
- 格式：`[时间] [角色] 内容`

### LLM 日志
- 位置：`data/prompt_logs/llm_prompt_log.txt`
- 内容：所有 LLM API 调用的提示词和响应
- 用途：调试和优化人格引擎

### 状态快照
- 位置：`data/current_state_snapshot.json`
- 内容：在哦对用户状态的理解
- 字段包括：情绪、能量、活动、位置、需求等

### 观点树
- 位置：`data/perspective_trees/`
- 描述：自动生成的对话观点结构
- 格式：JSON，可通过"观点树"按钮查看

## 常见问题

### Q: 程序卡顿或崩溃？
A: 这是 DEMO 版本的已知问题。建议：
- 避免快速连续点击按钮
- 避免疯狂发送大量消息
- 给在哦充足的思考时间（娃娃灭灯时）

### Q: 如何更改 API 提供商？
A: 目前 DEMO 版默认使用 DeepSeek API。修改需在 `core/` 模块中调整 LLM 客户端配置。

### Q: 如何重新开始？
A: 点击右侧"回到初见"按钮，在哦会：
- 清空所有对话日志
- 清空 LLM 调用日志
- 重置状态快照
- 保留用户长期画像数据

### Q: macOS 显示"无法验证开发者"？
A: 系统设置 → 隐私与安全性 → 允许运行此应用

## 设计特色

### 观点树生成引擎
在哦使用 LLM 控制的观点树生成引擎，能够：
- 实时分析对话主题
- 自动推导相关观点
- 根据上下文调整讨论方向

### 排队系统
为了保证 API 调用的稳定性：
- 所有 LLM 请求按顺序排队
- 每个请求之间间隔 0.2 秒
- 避免高并发导致的 API 超时

### 思考状态反馈
- 娃娃灭灯（OFF）表示正在处理
- 娃娃亮灯（ON）表示已准备好
- 视觉反馈增强用户体验

## 局限性与改进方向

### 已知局限
1. **流程优化空间** - DEMO 版流程可能需进一步调整
2. **观点树稳定性** - LLM 生成的观点有时不够稳定
3. **长对话处理** - 长时间对话可能导致性能下降

### 后续改进方向
- 更强大的观点推导引擎
- 改进对话上下文管理
- 优化用户界面和交互体验
- 支持多 LLM 提供商
- 数据标注和模型训练

## 贡献与反馈

这是一个 VIBE CODING 的独立制作项目。我们期待社区的：
- 意见反馈
- 功能建议
- Bug 报告
- 代码改进

如遇任何问题，请：
1. 检查终端输出的错误信息（红字）
2. 确保项目目录结构完整
3. 验证 API KEY 配置
4. 提供详细的问题描述和截图

## 愿景

> "既然三生了万物，那这个万物里面可能包含有 AGI，这是我们的奢望。"

在哦 DEMO 的目标是作为一个沟通媒介，在生活中存在 5-10 年，通过与用户的交互积累数据，最终探索能否达成真正的 AGI。

这不是一个竞速项目，而是一个对话的见证。

## 许可证

本项目为教育和研究用途。详见项目许可证文件。

---

**感谢使用在哦 DEMO！** 🎉

希望它能成为你的思维伙伴，帮助你在纷乱的世界中找到清晰的问题视角。

*"充分的沟通，解决未见之问题。"*

<img width="300" height="300" alt="微信图片_20240427151732" src="https://github.com/user-attachments/assets/34455983-c567-401c-ac99-e1c69a2c1f7c" />
<img width="300" height="300" alt="9cc53f4294103210ea4117a037fb62fb" src="https://github.com/user-attachments/assets/0190ad25-e4e9-4f0f-87ce-fbac295b2d29" />
<img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/fe9d4ede-c37d-4806-ba50-46c3196c88d1" />



