# Sources and Evidence Priority

Last verified: 2026-08-16.

Use official sources for syntax, capability limits, model families, and ComfyUI settings. Use community reports only for failure patterns and conservative production heuristics.

## Official

- MiniMax H3 repository and system specifications: <https://github.com/MiniMax-AI/MiniMax-H3>
- Official portable prompt-writing skill: <https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing>
- Official base-mode guide: <https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/base-en.txt>
- Official full-reference guide: <https://github.com/MiniMax-AI/MiniMax-H3/blob/main/skills/h3-prompt-writing/references/ref-en.txt>
- ComfyUI MiniMax H3 workflows and runtime notes: <https://docs.comfy.org/tutorials/video/minimax/minimax-h3>
- ComfyUI official workflow templates: <https://github.com/Comfy-Org/workflow_templates/tree/main/templates>

## Community observations

- Official-format adoption, speaker binding, shot timestamps, pacing, and wrong-speaker/random-cut reports: <https://www.reddit.com/r/StableDiffusion/comments/1vhloyz/walter_white_and_the_minimax_h3_official/>
- Explicit dialogue, room tone, effects, and music improve native-audio direction: <https://www.reddit.com/r/comfyui/comments/1vm5xq5/most_h3_prompts_skip_the_audio_here_are_50_that/>
- Multi-speaker reference-audio experiments, connection-order sensitivity, and onset fragments: <https://www.reddit.com/r/comfyui/comments/1vj8nyp/forcing_minimax_h3_to_generate_multispeaker/>
- Location treated as a referenced subject and reinforced by concrete layout descriptions: <https://www.reddit.com/r/StableDiffusion/comments/1vmul6f/how_to_achieve_location_consistency_in_minimax_h3/>
- Reported wide-shot face degradation, dialogue gibberish, and clipped opening audio: <https://www.reddit.com/r/StableDiffusion/comments/1vg65hr/what_problems_have_you_found_with_minimax_h3/>

## Resolution policy

When sources disagree:

1. follow current official MiniMax documentation for model behavior and prompt syntax;
2. follow current ComfyUI documentation for local node behavior and templates;
3. treat reproducible community observations as optional mitigations;
4. label single-user findings as experimental and avoid converting them into guarantees.
