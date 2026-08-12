# Full-Reference Mode: Ref2VA

Use `Ref2VA` when one or more assets supply reusable identity, appearance, setting, style, motion, editing structure, voice, music, or sound. Boundary-frame-only tasks belong to the base modes unless broader reference roles are also required.

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

## Label system

- `<Subject N>`: reusable visible content such as a person, creature, object, costume, location, action style, pose, or effect.
- `<Picture N>`: a concrete image asset used as a frame, keyframe, storyboard panel, or composition anchor.
- `<Video N>`: a source video used for editing, continuation, shot structure, camera motion, rhythm, or timing.
- `<Audio N>`: an audio signal used by copying or by reference to voice, music, beat, dialogue, or sound texture.

Number each label type independently in input order. Keep every label's meaning unchanged across all sections. If a picture only supplies a subject's appearance, define the subject and cite that picture in the definition; do not create an unnecessary standalone picture role.

Always render asset references with canonical angle-bracket syntax: `<Picture 1>`, `<Video 1>`, and `<Audio 1>`. Never downgrade them to plain phrases such as `Picture 1` when the asset is being cited.

## subject_definitions

Define each referenced unit in one concise line. State the source asset, what it contributes, and the traits that matter. Define assets by role, not merely by filename.

## summary

Begin with a bracketed combination of applicable relationships:

- `reference generation`
- `keyframe completion`
- `video editing`
- `video continuation`
- `audio reuse`
- `audio reference`

Join multiple relationships with ` + `. Then summarize the target video and how its main references are used. Do not introduce new labels.

## retention_analysis

Give one line per label. For visible references, choose one marker:

- `fully_preserved`
- `partially_preserved`
- `attribute_transfer`
- `weak_reference`

For audio, choose one marker:

- `fully_copy`
- `partially_copy`
- `reference`
- `weak_reference`

State where the item appears or applies and what is preserved, changed, transferred, copied, or only loosely followed.

## detailed_description

Write the target timeline in playback order. Establish the overall visual medium and treatment, then use `[Shot 1]` without a timestamp and later shots with increasing `MM:SS.mmm` cut times. At a subject's first appearance, describe its referenced identity, frame position, and current action. Reuse its label without redefining it later.

Combine visual labels and speaker IDs when a referenced subject speaks, for example `<Subject 2> (S1)`. Put exact speech or lyrics inside `<d>[Language] ...</d>`. If a reference audio supplies only timbre or delivery, do not copy its original words. If an audio signal is reused directly, describe the copied signal rather than inventing a new speaker.

Unless immediate speech is required, reserve `0.00-0.80` seconds for closed-mouth ambience before the first `<d>` event. Keep production directions outside `<d>` positive and observable. A picture reference does not preserve audio continuity; only a supplied `<Audio N>` may guide or copy audio according to its declared retention marker.

## Sound fields

Use `overall_soundscape` for target ambience, physical sounds, and any copied/referenced environmental layer. Use `non_diegetic_music` for audience-only score and its copy/reference relationship. Keep full dialogue and lyrics only in `detailed_description`.

When the user requests no background score, write exactly `non_diegetic_music: N/A`.
