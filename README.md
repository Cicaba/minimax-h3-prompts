# MiniMax H3 Prompts

一个中文优先、兼容 MiniMax 官方提示词结构的 Codex 技能，用于把创意、脚本、对白、关键帧和图片/视频/音频参考转换为可直接使用的 H3 视频提示词。

本次版本根据 MiniMax 官方 Base/Ref 提示词指南、官方 H3 Skills、ComfyUI 官方工作流文档以及社区实际生成反馈进行了系统更新。

## 主要能力

- 支持 `T2VA`、`I2VA`、`FL2VA`、`L2VA` 和 `Ref2VA`。
- 默认中文叙述，保留官方字段名、引用标签、镜头标记、说话人编号和音频控制标签。
- 可按需切换为官方英文提示词模式。
- 自动校验官方 4–15 秒时长、24fps、参考素材数量及模型模式边界。
- 为动作、打斗、舞蹈和多人场景设置保守的镜头与动作预算。
- 区分“增加细节”和“增加事件”，降低动作拥挤、肢体错乱及镜头失控概率。
- 将抽象风格词转换为可观察的材质、光线、色彩、镜头和运动属性。
- 每个镜头明确起始状态、动作路径、可见结果和连续性移交状态。
- 将联系表、分镜网格、箭头和时间标注留在制作阶段，防止误生成进成片。
- 为对白绑定稳定的 `(S1)`、`(S2)` 说话人，并使用 `<d>[Language] ...</d>` 保存原句。
- 处理画外音、跨镜头对白 `<scenetrans>`、结尾截断 `<cutoff>`、环境声和观众配乐。
- 针对本地量化/短步数工作流提供音频碎片、串词和多声源冲突的可选排查策略。
- 为 ComfyUI 的 `17k+5` 帧网格计算真实有效时长。

## 官方能力边界

| 项目 | 官方规格 |
| --- | --- |
| 输出时长 | 4–15 秒 |
| 帧率 | 24fps |
| 音频 | 原生 32kHz 立体声 |
| 常见画幅 | 21:9、16:9、4:3、1:1、3:4、9:16 |
| Ref2VA 图片 | 最多 9 张 |
| Ref2VA 视频 | 最多 3 段，每段 2–15 秒，总时长最多 15 秒 |
| Ref2VA 音频 | 最多 3 段，每段 2–15 秒，总时长最多 15 秒 |
| 混合参考文件 | 最多 12 个 |

`H3-Base-FL2VA` 用于文生视频和首/尾帧任务；`H3-Base-Ref2VA` 使用另一套模型权重处理多模态参考。技能会阻止两种提示词格式被错误混用。

## 安装

Windows PowerShell：

```powershell
git clone https://github.com/Cicaba/minimax-h3-prompts.git "$env:USERPROFILE\.codex\skills\minimax-h3-prompts"
```

macOS 或 Linux：

```bash
git clone https://github.com/Cicaba/minimax-h3-prompts.git ~/.codex/skills/minimax-h3-prompts
```

## 使用示例

```text
$minimax-h3-prompts

生成一段 10 秒、9:16 的文生视频提示词：成年中国女舞者在霓虹火车站表演火车舞。使用中文优先模式，需要环境声和放克配乐。
```

动作场景：

```text
$minimax-h3-prompts

将这个仙侠战斗创意改写为 9.4 秒提示词。优先保证两名角色的完整动作、武器接触和受力反馈；增加细节，但控制为两个交锋和一个结尾。
```

全参考模式：

```text
$minimax-h3-prompts

<Picture 1> 负责人物身份，<Picture 2> 负责场景布局，<Video 1> 只参考运镜，<Audio 1> 只参考声线。生成 15 秒 Ref2VA 官方英文格式提示词。
```

## ComfyUI 时长换算

ComfyUI 官方 H3 节点将时长吸附到 24fps 的 `17k+5` 帧网格。技能附带确定性计算脚本：

```powershell
python scripts/h3_duration.py 9.4
python scripts/h3_duration.py 15 --json
```

常见结果：

| 输入时长 | 帧数 | 有效时长 |
| --- | ---: | ---: |
| 9.4 秒 | 226 | 9.42 秒 |
| 10 秒 | 243 | 10.13 秒 |
| 15 秒 | 362 | 15.08 秒 |

## 原生音频策略

- 每个对白明确绑定实际说话人。
- 只有真正要发声的内容进入 `<d>`。
- 制作约束尽量改写为正向、可观察的画面状态。
- 开场动作、对白、环境声和音乐严格遵循用户要求，不默认添加闭口、静音或环境声缓冲。
- 同一音乐层只描述一次，防止原生配乐与外部替换配乐重复。
- 多个独立片段分别重述声线、环境声、音乐速度和声学空间。
- 边界图片只延续画面，无法继承上一段音频波形。
- 若开头仍出现毫秒级残音，优先在后期裁切或淡入，而不是继续堆叠文字禁令。

## 项目结构

```text
minimax-h3-prompts/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── scripts/
│   └── h3_duration.py
└── references/
    ├── base-modes.md
    ├── model-capabilities.md
    ├── motion-budget.md
    ├── native-audio.md
    ├── prompt-craft.md
    ├── quality-checklist.md
    ├── reference-mode.md
    └── sources.md
```

## 资料来源

- [MiniMax H3 官方仓库](https://github.com/MiniMax-AI/MiniMax-H3)
- [MiniMax 官方 Base 提示词指南](https://modelscope.cn/models/MiniMax/MiniMax-H3/file/view/master/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md?status=1)
- [MiniMax 官方 Ref 提示词指南](https://modelscope.cn/models/MiniMax/MiniMax-H3/file/view/master/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md?status=1)
- [MiniMax 官方 H3 Skills](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills)
- [MiniMax 官方 H3 Prompt Writing Skill](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing)
- [ComfyUI 官方 MiniMax H3 教程](https://docs.comfy.org/tutorials/video/minimax/minimax-h3)
- 详细官方与社区资料清单见 [`references/sources.md`](references/sources.md)。

## 说明

社区经验在技能内均作为保守启发式，而不是模型保证。该技能独立于 TE_MAN、私有二进制和专有提示词增强节点。
