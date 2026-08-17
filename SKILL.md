---
name: minimax-h3-prompts
description: Write production-ready MiniMax H3 prompts from video ideas, scripts, dialogue, keyframes, and image/video/audio references. Use for T2VA, I2VA, FL2VA, L2VA, and Ref2VA requests that need official H3 field structure, Chinese-first or official-English directions, feasible shot/action timing, reference-role mapping, camera control, exact dialogue, native stereo audio, ComfyUI duration snapping, or continuity across independently generated clips.
---

# MiniMax H3 Prompt Writing

Produce H3 prompt text only. Do not require ComfyUI, an API, a specific operating system, or a proprietary node.

## Workflow

1. Infer or collect:
   - target duration from 4 to 15 seconds and aspect ratio;
   - visual medium, subjects, setting, action, camera, and ending;
   - exact dialogue, lyrics, and visible text;
   - every image, video, and audio asset plus its intended role;
   - generation path: official API/app, local H3-Base, or ComfyUI when known;
   - priority among identity, choreography, camera, dialogue, and visual detail.
2. Read [model-capabilities.md](references/model-capabilities.md) when duration, resolution, references, local inference, ComfyUI, or model variants matter. Reject or revise requests outside verified limits.
3. Select one mode:
   - `T2VA`: text only;
   - `I2VA`: one image is the exact first frame;
   - `FL2VA`: two images are the exact first and last frames;
   - `L2VA`: one image is the exact last frame;
   - `Ref2VA`: images, videos, or audio guide reusable identity, setting, style, motion, camera, voice, or editing relationships.
4. Read [base-modes.md](references/base-modes.md) for `T2VA`, `I2VA`, `FL2VA`, or `L2VA`. Read [reference-mode.md](references/reference-mode.md) for `Ref2VA`.
5. Read [motion-budget.md](references/motion-budget.md) for action scenes, dances, multiple interacting subjects, complex camera work, 10-15 second clips, or quantized/short-step local workflows.
6. Read [native-audio.md](references/native-audio.md) whenever H3 generates dialogue, voiceover, lyrics, ambience, sound effects, music, or multiple clips that will be joined.
7. Draft three private planning artifacts before the final prompt:
   - an asset-role map;
   - a shot-and-action budget with observable cause and effect;
   - an audio timeline with stable speakers and enough time for every line.
8. Apply [quality-checklist.md](references/quality-checklist.md), then return the prompt.

## Language Strategy

- Default to `zh-first`: write production directions in Simplified Chinese while preserving official English field names, asset labels, shot markers, speaker IDs, language tags, and control tags.
- Use `official-en` when the user requests the official format, maximum guide compatibility, or an English prompt. Preserve dialogue, lyrics, and visible text in their original language.
- Keep one production language throughout a prompt. Do not mix Chinese and English prose except for canonical syntax and user-supplied content.

## Output Contract

- Return one copy-ready prompt in a fenced `text` block.
- Keep the required field names and order for the selected mode.
- Put unavoidable assumptions or recommended workflow settings in at most three short bullets before the prompt.
- Put only intended speech or lyrics inside `<d>[Language] ...</d>`. Preserve user-supplied words and punctuation verbatim.
- Define every reference label before use and keep its meaning stable.
- Never invent an unavailable asset, reference label, quoted line, lyric, brand copy, or visible text.
- If the request exceeds the model's verified duration or reference limits, explain the smallest feasible correction instead of silently truncating it.

## Direction Rules

- Describe visible and audible events, not plot summaries or adjective stacks.
- Establish identity, clothing, props, geography, lighting, and initial pose before complex motion.
- Treat detail density and event count separately. Add material, lighting, body mechanics, reactions, and sound to an existing action beat; do not turn “more detail” into more simultaneous actions.
- Give each major action a readable setup, contact or transition, and result.
- Express camera motion as a natural action tied to composition. Use one dominant camera path per shot.
- Prefer a coherent sequence over maximum cut count. Every explicit cut must reveal new subject, space, state, time, or viewpoint information.
- Separate diegetic ambience and physical sounds from audience-only score.
- Treat visual continuity and audio continuity independently across separately generated clips.
- Preserve the user's intended opening. Do not add a closed-mouth state, silent interval, ambience-only lead-in, or delayed music by default; use any of these only when the user explicitly requests them.

## Evidence Policy

- Treat the official MiniMax H3 repository, official prompt guides, and ComfyUI documentation as authoritative for syntax and capability limits.
- Treat community findings as conservative heuristics, not guaranteed model behavior. Do not promise identity fidelity, exact lip sync, perfect text, or artifact-free audio.
- Read [sources.md](references/sources.md) when verifying a version-sensitive claim or updating this skill.

## Independence

This skill is an independent Chinese-first adaptation of public MiniMax H3 documentation and community observations. It does not load, execute, reproduce, or depend on TE_MAN binaries or proprietary prompt-enhancement nodes.
