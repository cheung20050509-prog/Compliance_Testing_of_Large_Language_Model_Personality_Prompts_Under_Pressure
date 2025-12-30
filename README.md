# 压力下大语言模型人格提示词的合规性测试

## 项目概述

本项目又名 **Islanders（荒岛求生）**，是一个用于测试大语言模型（LLMs）在压力下的合规性和人格一致性的模拟环境。它模拟了"荒岛生存"场景，AI 驱动的 NPC 角色在其中互动、收集资源并努力生存。

该模拟基于 Python 和 Pygame 构建，NPC 由阿里云百炼（DashScope）API 驱动。

## 功能特性

- **AI 驱动的 NPC**：三个具有独特人格和记忆系统的角色（凯、伊拉拉、贾克斯）。
- **生存模拟**：NPC 管理能量水平，收集资源（水、鱼、果实），并受库存限制约束。
- **社交互动**：NPC 可以进行对话、分享信息并建立关系。
- **记忆系统**： 
  - 个体 NPC 记忆流。
  - 全局"编年史"记录重大事件。
- **可视化界面**：使用 Pygame 实时可视化岛屿、NPC 移动和状态。

## 项目结构

```text
.
├── Islanders-main/          # 主要源代码目录
│   ├── main.py              # 应用程序入口
│   ├── game.py              # 主游戏循环和逻辑
│   ├── npc.py               # NPC 类和行为定义
│   ├── ai_client.py         # 阿里云百炼 API 客户端
│   ├── world.py             # 世界生成和管理
│   ├── ui.py                # 用户界面渲染
│   ├── memory_system.py     # 记忆和编年史管理
│   ├── dialog_system.py     # 对话管理
│   └── config.py            # 配置设置
├── data/                    # 记忆和日志数据存储
├── LICENSE
└── README.md
```

## 前置要求

- Python 3.8+
- 阿里云百炼 API 密钥（DashScope）

## 安装

1. 克隆仓库：
   ```bash
   git clone https://github.com/cheung20050509-prog/Compliance_Testing_of_Large_Language_Model_Personality_Prompts_Under_Pressure.git
   ```

2. 安装所需的 Python 包：
   ```bash
   pip install pygame dashscope
   ```

## 使用方法

1. **配置 API 密钥**：
   打开 `Islanders-main/main.py`（或 `ai_client.py`）并确保正确配置了你的阿里云百炼 API 密钥。
   *注意：当前代码库可能包含硬编码的占位符，建议使用环境变量以提高安全性。*

2. **运行模拟**：
   导航到项目根目录并运行：
   ```bash
   python Islanders-main/main.py
   ```

3. **控制说明**：
   - 模拟会自动运行。
   - 你可以通过 UI 观察 NPC 的互动和状态。

## 研究背景

本工具旨在研究基于 LLM 的智能体在面临生存压力（资源稀缺、竞争）时如何维持其被赋予的人格特征。它分析：
- **合规性**：它们是否遵守角色指令？
- **社交动态**：它们如何合作或竞争？
- **记忆使用**：过去的事件如何影响当前决策？

## 许可证

详见 [LICENSE](LICENSE) 文件。
