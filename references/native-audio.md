# Native Audio Safety

Apply these rules whenever H3 generates audio jointly with video.

## Prevent instruction leakage

- Put only exact spoken words or lyrics inside `<d>[Language] ...</d>`.
- Write non-dialogue directions as positive, observable states. H3 can occasionally vocalize nearby Chinese constraint words, especially at clip onset.
- Outside `<d>...</d>`, replace constructions such as:
  - `不切镜` -> `单一连续镜头`
  - `不改变服装` -> `服装全程保持一致`
  - `不要增加武器` -> `武器全程保持为单剑`
  - `不说话` or `无对白` -> `角色闭口静默`
  - `避免爆炸` -> `场面保持克制，仅呈现指定能量效果`
- Preserve negation when it belongs to user-supplied dialogue, lyrics, or visible text. Never rewrite quoted content merely to satisfy this safeguard.
- If a negative condition cannot be expressed positively, place it late in the visual description, keep it short, and keep it away from the first vocal event.

## Protect the opening

- Unless the user requires immediate speech, reserve `0.00-0.80` seconds for a closed-mouth, ambience-only lead-in.
- Use positive timing language, for example: `00:00.000-00:00.800，角色闭口静默，只有林间风声与衣甲轻响；00:00.800后开始对白。`
- Start the first `<d>` event at or after `00:00.800`. Keep the speaker's mouth closed before that point.
- Do not place dialogue-like prose, quoted sound words, or emphatic Chinese instruction fragments in the opening alignment paragraph.

## Continue across independently generated clips

- Reuse the same concise voice description, ambience, music tempo, instrumentation, loudness, and acoustic-space wording in every clip.
- Give every clip its own ambience-only lead-in; a previous clip's last-frame image does not carry audio context.
- Schedule dialogue after the lead-in and finish it before the final transition beat.
- End on a sustainable ambience or music bed when clips will be joined. Expect post-production crossfades for sample-accurate audio continuity.

## Quantized or short-step workflows

Treat INT8/FP8 models and 4-step or other short trajectories as higher-risk for onset syllables, slurred speech, and instruction leakage. Prefer simpler sentences, fewer simultaneous sound events, a longer `0.80-1.00` second lead-in, and one speaker at a time.
