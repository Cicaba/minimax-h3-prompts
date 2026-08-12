# Base Modes: T2VA, I2VA, FL2VA, L2VA

Use this reference when assets are absent or act as exact boundary frames.

## Required output structure

For `T2VA`, begin directly with these fields:

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

For keyframe modes, add one alignment line before the three fields:

- `I2VA`: state that `<Picture 1>` is fully referenced as the first frame of `[Shot 1]` at `0.00` seconds.
- `FL2VA`: state that `<Picture 1>` anchors `0.00` seconds and `<Picture 2>` anchors the final frame at the effective duration, each mapped to its actual shot.
- `L2VA`: state that `<Picture 1>` anchors the final frame at the effective duration and belongs to the actual final shot.

Format the final duration with two decimals in the alignment line.

## Timeline construction

- Start `[Shot 1]` without a timestamp. Establish medium/style, composition, subjects, environment, lighting, and the initial state.
- Introduce later shots as `[Shot N] At MM:SS.mmm, ...`; timestamps must increase and remain below the final duration.
- Add a cut only when it reveals a new subject, location, state, time, or materially different viewpoint. Use camera motion for smaller framing changes.
- Keep each shot proportional to the action and dialogue it contains.

## Keyframe behavior

### I2VA

Treat Picture 1 as a hard initial condition. Preserve identity, clothing, palette, composition anchors, important objects, and spatial relationships. Develop forward through visible cause and effect.

### FL2VA

Describe the motion path, pose changes, object manipulation, camera evolution, and lighting transition that connect the two frames. Prefer one continuous shot unless the user explicitly requires cuts. End on the supplied last-frame composition.

### L2VA

Infer a plausible earlier state, then progressively reduce differences until subject pose, object state, camera angle, lighting, and composition land on Picture 1 at the final moment.

## Dialogue and visible text

- Assign speakers `(S1)`, `(S2)`, and so on in order of first vocal event; reuse IDs across shots.
- Put only the language tag and exact spoken words inside `<d>`.
- Unless immediate speech is required, keep `0.00-0.80` seconds ambience-only with the visible speaker's mouth closed, then begin the first `<d>` event.
- Express production constraints positively outside `<d>`; prefer `单一连续镜头` and `服装全程保持一致` over Chinese negative imperatives that native audio may vocalize.
- For an off-screen voice, say it is off-screen and keep the corresponding visible character's lips closed when applicable.
- Put literal visible text in double quotes and preserve it exactly.
- If speech crosses a cut, explicitly describe audio continuity. Use `<cutoff>` only when the clip intentionally ends mid-utterance.

## Sound fields

`overall_soundscape` summarizes ambience, movement, impacts, machinery, weather, breathing, laughter, and other physical/non-verbal sounds. Do not repeat dialogue or audience-only music here.

`non_diegetic_music` describes only score unheard by characters. Specify instruments, tempo/rhythm, and dynamic progression. Use `N/A` when there is no audience-only score.

For a sequence of independently generated clips, repeat the same compact voice and sound-bed description in each clip. Do not claim that an I2VA boundary image preserves the preceding audio waveform.
