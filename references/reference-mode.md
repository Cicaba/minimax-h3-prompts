# Full-Reference Mode: Ref2VA

Use `Ref2VA` when images, videos, or audio supply reusable identity, appearance, location, style, motion, camera, editing structure, voice, music, or sound. Boundary-frame-only tasks belong to the base modes unless an asset also has a broader reference role. Use the H3-Base-Ref2VA model family.

Read [model-capabilities.md](model-capabilities.md) before writing a Ref2VA prompt and verify all input limits.

## Required output structure

Return exactly these six fields in order:

```text
subject_definitions:
...

summary:
...

retention_analysis:
...

detailed_description:
...

overall_soundscape:
...

non_diegetic_music:
...
```

In `official-en`, write all six sections in English while preserving dialogue, lyrics, and visible text in their original language. In `zh-first`, keep field names, labels, relationship markers, shot markers, speaker IDs, and control tags in canonical English, while writing explanatory prose in Simplified Chinese.

## Label system

- `<Subject N>`: reusable visible content such as a person, creature, object, costume, location, action style, pose, or effect.
- `<Picture N>`: a concrete image used as a first frame, last frame, keyframe, storyboard panel, edited frame, or composition anchor.
- `<Video N>`: a whole-video source used for editing, continuation, camera movement, cuts, rhythm, or temporal structure.
- `<Audio N>`: a standalone audio asset or explicitly enabled video soundtrack used by copying or reference.

Number each label type independently in connection/input order. Keep every label's meaning stable. If an image only supplies a subject's appearance, define the subject and cite the picture in that definition; do not create an unnecessary standalone picture role.

One `<Subject N>` may combine traits from several assets, and one asset may define several separately tracked subjects. State which source supplies each trait. Keep contact sheets or storyboard grids as planning references unless their panel layout is intended to appear in the target.

An ordinary reference video does not automatically create `<Audio N>` merely because the file contains sound. Define an audio label only when that soundtrack is explicitly supplied or enabled as an audio condition.

## Assign one job to every reference

State what each asset controls:

- identity or costume;
- location layout or visual style;
- action, motion, or camera path;
- first frame, last frame, keyframe, or storyboard;
- voice timbre, delivery, dialogue content, ambience, beat, or soundtrack;
- source-video editing or continuation.

When one asset has multiple jobs, state them in one concise definition and distinguish which properties are reused, copied, changed, or ignored. Do not rely on filename semantics.

## `subject_definitions`

Define each referenced unit in one concise line. State the source asset, its job, and the traits that matter. For an audio reference bound to a target speaker, reuse that target speaker's global ID:

```text
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

## `summary`

Begin with one bracketed combination of applicable task relationships:

- `reference generation`
- `keyframe completion`
- `video editing`
- `video continuation`
- `audio reuse`
- `audio reference`

Join multiple relationships with ` + `. Then summarize the target and the main asset roles without introducing new labels.

Use `video editing` only when a source video is directly modified, and `video continuation` only when new content resumes from a source video. A reference video used only for motion, camera, or rhythm normally belongs to `reference generation`.

In `official-en`, a direct editing summary begins with `The target video is an edited version of <Video 1>.` after the task-type prefix.

## `retention_analysis`

Give one line per label. Visible references use one fixed marker:

- `fully_preserved`
- `partially_preserved`
- `attribute_transfer`
- `weak_reference`

Audio references use one fixed marker:

- `fully_copy`
- `partially_copy`
- `reference`
- `weak_reference`

State where the reference applies and what is preserved, changed, transferred, copied, or loosely followed. Do not treat newly requested target actions as losses of reference fidelity.

Keep speaker IDs out of `retention_analysis`; `(Sx)` belongs to actual vocal-source definitions and vocal events.

## `detailed_description`

Write the target timeline in playback order. Establish visual medium and treatment first, then use `[Shot 1]` without a timestamp and later shots with increasing `MM:SS.mmm` cut times.

At a subject's first appearance:

1. cite its label;
2. describe the referenced traits actually visible;
3. establish frame position and current action;
4. state where any motion, camera, style, voice, or audio reference begins to apply.

Reuse the same label later without redefining it. For concrete frame anchors, use natural relationships such as `the shot begins from <Picture 1>`, `the keyframe corresponds to <Picture 2>`, or `the shot ends on <Picture 3>`.

When a referenced subject speaks, keep both identifiers:

```text
<Subject 2> (S1) 说道：<d>[Chinese] 用户提供的原句。</d>
```

If reference audio supplies only timbre or delivery, do not carry its original words into the target. Copy source words only when the user explicitly requests dialogue/lyric reuse or reperformance. Use `[unclear]` for unintelligible spans instead of guessing.

When verbal content exists only inside a directly reused song or complete soundtrack, cite `<Audio N>` as the audible source and do not invent a separate speaker ID. Assign `(Sx)` only when a concrete person, character, narrator, or other independent source produces the voice.

For dialogue or lyrics transcribed from reference audio, preserve the source words and language while normalizing only decorative punctuation, emoji, bullets, and repeated tildes. Preserve user-supplied text verbatim.

Official English generation prompts normally use about 350-500 words for `detailed_description`. In `zh-first`, match the information density rather than the English word count. Dialogue-heavy or simple single-action clips may be shorter when the timeline is already explicit.

## Sound fields

Use `overall_soundscape` for target ambience, physical sounds, non-verbal human sounds, and the corresponding audio copy/reference relationship. Use `non_diegetic_music` for audience-only score and its copy/reference relationship. Keep full dialogue and lyrics only in `detailed_description`.

Write `overall_soundscape: N/A` only for complete silence. Write `non_diegetic_music: N/A` when there is no audience-only score.
