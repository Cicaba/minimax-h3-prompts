# Base Modes: T2VA, I2VA, FL2VA, L2VA

Use this reference when assets are absent or act only as exact boundary frames. These modes use the H3-Base-FL2VA family.

## Required output structure

For `T2VA`, begin directly with:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

For keyframe modes, place the applicable official alignment instruction first, followed by one blank line:

### I2VA

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

### FL2VA

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.
```

### L2VA

```text
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.
```

Keep these alignment instructions in English in both `zh-first` and `official-en` modes. Replace `N` with the actual final shot and `S.SS` with the effective duration to exactly two decimals. The FL2VA instruction is an official template exception to the normal angle-bracket label rule.

## Timeline construction

- Start `[Shot 1]` without a timestamp. Establish visual medium, initial composition, subjects, environment, lighting, and current state.
- Start later shots with `[Shot N] At MM:SS.mmm, ...`. Cut times must increase and remain below the effective duration.
- Add a cut only for new subject, space, state, time, or materially different viewpoint information. Use camera movement for smaller framing changes.
- Match description volume, action count, and dialogue to the time available.
- End with an explicit pose, composition, result, transition, or frame landing.

## Camera direction

Write camera movement as part of the visible action. When useful, specify:

```text
motion type + amplitude + speed + compositional purpose
```

Canonical motion types include push in, pull out, pan, truck, tilt, pedestal, arc shot, tracking shot, static shot, shake, POV, zoom, and roll. Use amplitude and speed only when they change the result. Prefer one dominant camera path per shot.

## Keyframe behavior

### I2VA

Treat `<Picture 1>` as the exact first frame. Preserve its identity, clothing, colors, composition anchors, objects, lighting, and spatial relationships, then develop through visible cause and effect.

Recommended path:

```text
first-frame anchor -> action onset -> continuous development -> readable result
```

### FL2VA

Connect the supplied frames through pose changes, object manipulation, camera evolution, spatial movement, and lighting changes. Prefer one continuous shot unless the user explicitly asks for cuts. Land on the supplied last frame at the effective duration.

Recommended path:

```text
first-frame state -> observable intermediate changes -> narrowing differences -> last-frame state
```

### L2VA

Infer a compatible opening, then progressively converge to the supplied final frame. The reference belongs to the actual final shot, not automatically to Shot 1.

Recommended path:

```text
plausible preceding state -> explicit transition path -> gradual convergence -> final-frame landing
```

## Speakers, dialogue, and visible text

- Assign `(S1)`, `(S2)`, and later IDs in order of first vocal event. Reuse each ID across all shots.
- On first vocal appearance, identify the speaker by visible identity plus relevant voice traits such as age range, pitch, timbre, delivery, pace, accent, and on-screen/off-screen status.
- Put only the language tag and exact spoken words inside `<d>`:

```text
角色描述 (S1) 说道：<d>[Chinese] 用户提供的原句。</d>
```

- For voiceover in `official-en`, use `says in an off-screen voiceover`; after the `<d>` block, state that the corresponding on-screen character's lips remain closed. In `zh-first`, state the same relationship explicitly in Chinese.
- Use `<scenetrans>` at both connecting dialogue fragments when one line crosses a cut, and state that the audio continues across the transition.
- Use `<cutoff>` only when the clip intentionally ends mid-utterance.
- Put literal visible text in English double quotation marks and preserve it exactly.

## Sound fields

`overall_soundscape` uses one compact paragraph for ambience, physical action sounds, and non-verbal human sounds. Keep dialogue, singing, and shot-specific diegetic events in `integrated_multimodal_description`. Write `overall_soundscape: N/A` only when the user requests complete silence.

`non_diegetic_music` describes only audience-only score: instrumentation, tempo or rhythm, and dynamic development. Diegetic music belongs in the timeline. Write exactly `non_diegetic_music: N/A` when there is no audience-only score.
