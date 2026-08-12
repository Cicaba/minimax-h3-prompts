---
name: minimax-h3-prompts
description: Convert video ideas, scripts, dialogue, keyframes, and multimodal references into production-ready, Chinese-first MiniMax H3 prompts with native-audio leakage safeguards. Use for MiniMax H3 text-to-video (T2VA), first-frame image-to-video (I2VA), first-and-last-frame video (FL2VA), last-frame video (L2VA), or full-reference generation/editing (Ref2VA), including shot timing, camera motion, exact dialogue, sound, music, audiovisual continuity, and stable image/video/audio reference labels.
---

# Write MiniMax H3 Prompts

Produce H3 prompt text only; do not require ComfyUI, a specific operating system, an API, or a custom node.

## Workflow

1. Collect or infer:
   - target duration and aspect ratio;
   - story, subjects, setting, visual style, and ending;
   - dialogue or lyrics that must remain exact;
   - each reference asset and its intended role;
   - required camera, sound, music, preservation, and change constraints.
2. Select one mode:
   - `T2VA`: no media reference; create the complete audiovisual timeline from text.
   - `I2VA`: one image is the exact first frame.
   - `FL2VA`: two images are the exact first and last frames.
   - `L2VA`: one image is the exact last frame.
   - `Ref2VA`: images, video, or audio guide identity, style, motion, structure, voice, or reusable content rather than serving only as boundary frames.
3. If the mode is ambiguous and different choices materially change the result, ask one concise question. Otherwise infer the mode from asset roles and state any important assumption briefly.
4. Read [base-modes.md](references/base-modes.md) for `T2VA`, `I2VA`, `FL2VA`, or `L2VA`. Read [reference-mode.md](references/reference-mode.md) for `Ref2VA`.
5. Read [native-audio.md](references/native-audio.md) whenever the target includes generated sound, dialogue, lyrics, or multiple independently generated clips.
6. Draft a duration-feasible shot and audio plan before writing the final prompt. Use fewer shots when continuity, identity, keyframe interpolation, or voice stability matters more than coverage.
7. Apply [quality-checklist.md](references/quality-checklist.md) before returning the result.

## Output Contract

- Return one copy-ready prompt in a fenced `text` block.
- Keep required field names and their order exactly as defined by the selected mode reference.
- Default narrative instructions to Simplified Chinese. Keep required field names, canonical asset labels, shot markers, speaker IDs, and language-tag syntax unchanged. Preserve dialogue, lyrics, and visible text in their original language. Follow an explicit user request for another narrative language.
- Do not add explanations inside the prompt. Put unavoidable assumptions in at most three short bullets before the prompt.
- Preserve user-supplied dialogue verbatim inside `<d>[Language] ...</d>`.
- Keep all intended speech inside `<d>...</d>`. Write surrounding production directions as positive, observable states so native audio does not vocalize instruction fragments.
- Never invent missing reference assets, reference labels, quoted dialogue, lyrics, brand copy, or visible text.

## Creative Rules

- Describe observable audiovisual events, not abstract intentions or plot summaries.
- Establish subject identity, wardrobe, important props, environment, lighting, and spatial relationships before complex action.
- Express camera movement as part of the action and composition. Avoid stacks of disconnected cinematography keywords.
- Keep actions physically continuous between adjacent moments and compatible with supplied keyframes.
- Separate diegetic sound from audience-only score.
- Use stable speaker IDs and reference labels throughout the prompt.
- Prefer a coherent, achievable sequence over excessive shot count or simultaneous actions.
- For independently generated clips, treat image continuity and audio continuity separately. A boundary image preserves appearance, not the preceding waveform, voice phase, ambience, or music phase.

## Independence and Attribution

This skill is an independent prompt-writing workflow derived from publicly documented MiniMax H3 interfaces and observed model input/output conventions. Do not load, execute, reproduce, or depend on TE_MAN binaries or proprietary prompt-enhancement nodes.
