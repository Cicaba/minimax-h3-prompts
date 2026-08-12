# MiniMax H3 Prompts

一个中文优先的 Codex 技能，用于把创意、脚本、对白、关键帧和多模态参考转换为可直接使用的 MiniMax H3 视频提示词。

它不仅组织镜头、动作、对白、环境声与配乐，还针对 H3 原生音频生成中的开场串词问题提供防护规则。

## 功能

- 中文优先输出，保留用户提供的对白、歌词与可见文字原文。
- 支持文生视频、首帧图生视频、首尾帧、尾帧和全参考生成。
- 生成带时间轴、镜头运动、说话人、环境声和配乐的结构化提示词。
- 使用稳定的 `<Picture N>`、`<Video N>`、`<Audio N>` 和 `<Subject N>` 引用标签。
- 自动检查时长、镜头连续性、角色身份、服装、道具和空间关系。
- 将画面约束改写为正向、可观察的描述，降低非对白文字被错误发声的概率。
- 为独立生成的长视频分段安排开场静默和一致的声线、环境声及音乐描述。

## 支持模式

| 模式 | 用途 |
| --- | --- |
| `T2VA` | 纯文本生成完整视听时间线 |
| `I2VA` | 使用一张图片作为精确首帧 |
| `FL2VA` | 使用两张图片锚定首帧和末帧 |
| `L2VA` | 使用一张图片作为精确末帧 |
| `Ref2VA` | 使用图片、视频或音频参考身份、风格、动作、结构或声音 |

## 安装

将仓库克隆到 Codex 的个人技能目录：

```powershell
git clone https://github.com/Cicaba/minimax-h3-prompts.git "$env:USERPROFILE\.codex\skills\minimax-h3-prompts"
```

macOS 或 Linux：

```bash
git clone https://github.com/Cicaba/minimax-h3-prompts.git ~/.codex/skills/minimax-h3-prompts
```

也可以让 Codex 从该 GitHub 仓库安装技能。

## 使用

在 Codex 中调用：

```text
$minimax-h3-prompts

生成一段 10 秒、9:16 的图生视频提示词。
一名身穿白色现代服装的中国女孩在清晨森林里跳舞，镜头环绕人物运动，最后停在她面向镜头的姿势。需要森林环境音和轻柔现代音乐。
```

带对白的分段视频示例：

```text
$minimax-h3-prompts

把这个故事规划成 6 段独立生成、每段约 9.4 秒的连续视频。保持角色外观、声线、环境声和配乐一致；每段对白必须使用我提供的原文。
```

技能会返回一个可复制的 H3 提示词代码块，并根据素材角色自动选择合适的生成模式。

## 原生音频防串词

H3 联合生成画面与声音时，偶尔会把“不切镜”“不要改变”等制作约束误当成对白。该技能采用以下策略降低风险：

- 仅将真正需要说出的内容放入 `<d>[Language] ...</d>`。
- 将“不切镜”改写为“单一连续镜头”等正向描述。
- 默认让角色在开头约 0.8 秒闭口静默，仅保留环境声。
- 对 INT8、FP8 或短步数工作流采用更简单的声音设计和更长的安全开场。
- 明确区分画面连续性与音频连续性；尾帧图片本身不会继承上一段音轨。

详细规则见 [`references/native-audio.md`](references/native-audio.md)。

## 项目结构

```text
minimax-h3-prompts/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── base-modes.md
    ├── native-audio.md
    ├── quality-checklist.md
    └── reference-mode.md
```

## 说明

这是一个独立的社区提示词编写技能，基于公开的 MiniMax H3 接口信息和实际生成经验整理。它不依赖 ComfyUI、特定操作系统、私有 API、TE_MAN 二进制文件或专有提示词增强节点。
