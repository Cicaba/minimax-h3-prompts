# Native Audio Direction and Safety

Use this reference whenever H3 jointly generates dialogue, voiceover, lyrics, ambience, sound effects, music, or audio for clips that will be joined. H3 outputs native 32 kHz stereo audio.

## Bind every vocal event

- Assign `(S1)`, `(S2)`, and later IDs in order of first vocal event.
- At the first vocal event, identify the source by visible subject or narrator role, on-screen/off-screen status, age range, voice pitch, timbre, pace, accent, and delivery when relevant.
- Reuse the same ID for the same source across every shot and independently generated segment.
- Put only the language tag and exact spoken words or lyrics inside `<d>`.
- Keep one speaker at a time for quantized or short-step workflows unless overlap is essential.

```text
年轻女性、清晰柔和的中音声线 (S1) 说道：<d>[Chinese] 我们到站了。</d>
```

For voiceover, explicitly identify it as off-screen. In `official-en`, use `says in an off-screen voiceover`; after the line, state that the related on-screen character's lips remain closed.

Use `<scenetrans>` on both dialogue fragments when one utterance crosses a cut and state that the audio continues across the transition. Use `<cutoff>` only when the video deliberately ends mid-utterance.

## Prevent instruction leakage

Community and local workflows report occasional prompt fragments or gibberish being voiced, especially at the beginning. Reduce the risk as follows:

- Put only intended speech or lyrics inside `<d>[Language] ...</d>`.
- Write surrounding directions as positive, observable states.
- Replace negative production phrasing:
  - `不切镜` -> `单一连续镜头`
  - `不改变服装` -> `服装全程保持一致`
  - `不要增加武器` -> `武器全程保持为单剑`
  - `不说话` or `无对白` -> `角色闭口静默`
  - `避免爆炸` -> `场面保持克制，仅呈现指定能量效果`
- Keep unavoidable restrictions short, late in the description, and away from the first vocal event.
- Do not emit experimental, undocumented emphasis or non-verbal tags by default. Some community tests report that such tags may become gibberish.

Preserve negation when it belongs to user-supplied dialogue, lyrics, or visible text.

## Protect the opening boundary

For local INT8/FP8, short-step, dialogue-heavy, or independently generated clips, reserve `0.80-1.00` seconds for a closed-mouth ambience-only lead-in unless immediate speech is required:

```text
00:00.000-00:00.900，角色闭口静默，只有环境声与衣料轻响；00:00.900后开始对白。
```

This is a conservative community heuristic, not an official H3 syntax requirement. A few workflows still produce a millisecond-scale onset fragment; when it survives prompt revisions, trim or fade the opening in post-production rather than adding more verbal restrictions.

For clips with no intended human voice, explicitly keep visible characters closed-mouth and describe only the wanted ambience and physical sounds. `overall_soundscape: N/A` is reserved for complete silence.

## Match dialogue to time

- Read every line aloud or estimate natural delivery time before placing it.
- Include reaction and breathing space after important lines.
- Finish dialogue before the final transition or continuity pose.
- If the words do not fit, recommend a longer clip, fewer lines, or a separate segment. Never silently delete or compress user-supplied dialogue.
- Avoid overlapping action, loud effects, music peaks, and multiple voices over the same short interval unless the overlap is the intended result.

## Direct all audio layers

- Put timed dialogue, singing, diegetic music, and shot-specific synchronized effects in the main timeline.
- Use `overall_soundscape` for continuous ambience, physical sounds, and non-verbal human sounds.
- Use `non_diegetic_music` only for audience-only score, with instrumentation, tempo/rhythm, and dynamic changes.
- Write `non_diegetic_music: N/A` to request no audience-only score.
- Write `overall_soundscape: N/A` only when the entire target is silent.

## Reference-audio caution

- Follow Ref2VA connection order and use one consistent `<Audio N>` / `<Video N>` mapping throughout the prompt.
- State whether the target copies the signal or only references timbre, delivery, beat, ambience, or music style.
- Do not copy words from a voice-timbre reference unless the user explicitly requests those words.
- Community tests report that combining several standalone audio references with enabled reference-video soundtracks can reduce clarity. Treat this as workflow-dependent: start with the fewest audio conditions, generate ambience from text when feasible, then add references one at a time.

## Continue across independent clips

- Repeat the same concise speaker voice description, ambience, music tempo, instrumentation, loudness, and acoustic-space wording in every segment.
- Give each segment its own opening boundary protection when local audio artifacts are a concern.
- End on sustainable ambience or a music bed suitable for a crossfade.
- A boundary image preserves visual state only; it does not preserve the previous waveform, voice phase, ambience phase, or music phase.
