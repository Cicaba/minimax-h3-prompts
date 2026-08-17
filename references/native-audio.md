# Native Audio Direction and Safety

Use this reference whenever H3 jointly generates dialogue, voiceover, lyrics, ambience, sound effects, music, or audio for clips that will be joined. H3 outputs native 32 kHz stereo audio.

## Bind every vocal event

- Assign `(S1)`, `(S2)`, and later IDs in order of first vocal event.
- Use a compound ID such as `(S1,S2)` when already-numbered speakers vocalize together.
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
  - `不说话` or `无对白` -> `声音由环境声、动作声与指定音乐构成`
  - `避免爆炸` -> `场面保持克制，仅呈现指定能量效果`
- Keep unavoidable restrictions short, late in the description, and away from the first vocal event.
- Do not emit experimental, undocumented emphasis or non-verbal tags by default. Some community tests report that such tags may become gibberish.

Preserve negation when it belongs to user-supplied dialogue, lyrics, or visible text.

## Preserve the intended opening

- Start action, dialogue, ambience, and music at the times implied or specified by the user.
- Do not insert a mandatory silent interval, ambience-only lead-in, delayed music entrance, or closed-mouth pose.
- When the user explicitly asks to troubleshoot a recurring onset fragment, offer timing padding, a short fade, or post-production trimming as optional tests rather than embedding them in every prompt.
- For clips with no intended human voice, describe the desired ambience, action sounds, and music without prescribing the visible character's mouth state. `overall_soundscape: N/A` is reserved for complete silence.

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
- Represent each audible music layer once. Do not describe the same soundtrack as both native generated score and a separate replacement track.
- Write `non_diegetic_music: N/A` to request no audience-only score.
- Write `overall_soundscape: N/A` only when the entire target is silent.

## Reference-audio caution

- Follow Ref2VA connection order and use one consistent `<Audio N>` / `<Video N>` mapping throughout the prompt.
- State whether the target copies the signal or only references timbre, delivery, beat, ambience, or music style.
- Do not copy words from a voice-timbre reference unless the user explicitly requests those words.
- When words are audible only inside a directly reused song or complete soundtrack, use `<Audio N>` as the source; reserve `(Sx)` for a concrete independent vocal source.
- Community tests report that combining several standalone audio references with enabled reference-video soundtracks can reduce clarity. Treat this as workflow-dependent: start with the fewest audio conditions, generate ambience from text when feasible, then add references one at a time.

## Continue across independent clips

- Repeat the same concise speaker voice description, ambience, music tempo, instrumentation, loudness, and acoustic-space wording in every segment.
- Place dialogue and lyric cut points at pauses, breaths, beats, or other intentional boundaries whenever possible.
- Preserve each segment's intended opening timing; add diagnostic padding only when the user explicitly requests an onset-artifact test.
- End on sustainable ambience or a music bed suitable for a crossfade.
- A boundary image preserves visual state only; it does not preserve the previous waveform, voice phase, ambience phase, or music phase.
