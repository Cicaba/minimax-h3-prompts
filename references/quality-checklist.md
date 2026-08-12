# H3 Prompt Quality Checklist

Check every item before returning the prompt.

## Structure

- The selected mode matches the actual role of each asset.
- Required fields are present once, in the correct order.
- All labels are defined before use and retain one meaning.
- Every asset citation uses canonical angle brackets, for example `<Picture 1>` rather than `Picture 1`.
- No phantom picture, video, audio, speaker, dialogue, or text asset was invented.

## Timing

- The prompt uses the effective rendered duration when known; otherwise it uses the requested duration.
- `[Shot 1]` has no cut timestamp.
- Later shot times increase, fit inside the duration, and leave enough time for their actions and dialogue.
- For a ComfyUI H3 workflow using the common `17k+5` frame grid at 24 fps, calculate effective duration as `frame_count / 24`; align the final keyframe to that value rather than the rounded UI duration.

## Continuity

- Identity, clothing, props, lighting, screen direction, and geography remain stable unless a change is explicitly animated.
- I2VA begins from the supplied first frame.
- FL2VA describes a continuous path and reaches the supplied last frame.
- L2VA converges to the supplied final frame instead of treating it as an opening.
- Ref2VA distinguishes a source asset from the reusable subject or attribute derived from it.

## Audio and text

- Speaker IDs are stable and assigned only to actual vocal sources.
- Dialogue, lyrics, and visible text preserve the user's exact language and wording.
- Only intended speech or lyrics appear inside `<d>...</d>`.
- Unless immediate speech is required, the first `0.80` seconds keep visible speakers closed-mouth and ambience-only; the first `<d>` event begins afterward.
- Outside exact dialogue, lyrics, and visible text, scan for `不`, `不要`, `不能`, `禁止`, `避免`, `切勿`, and similar negative production language. Rewrite it as positive, observable state wherever possible.
- Image/keyframe continuity is not described as audio continuity. Independently generated clips repeat stable voice and sound-bed descriptors and leave room for post-production crossfades.
- Diegetic events appear in the shot timeline; ambience/physical sounds appear in `overall_soundscape`; audience-only score appears in `non_diegetic_music`.
- An explicit no-music request produces exactly `non_diegetic_music: N/A`.
- Spoken duration is realistic for the clip; shorten staging or recommend a longer clip rather than silently deleting required dialogue.

## Clarity

- Every sentence maps to something observable or audible.
- Camera direction includes a subject or compositional purpose.
- The prompt avoids contradictory motions, duplicate action beats, excessive cuts, and abstract mood-only wording.
- The ending is explicit: final pose, composition, action result, transition, or freeze frame.
- In INT8/FP8 or short-step workflows, the audio plan is simplified and uses a `0.80-1.00` second ambience-only lead-in.
