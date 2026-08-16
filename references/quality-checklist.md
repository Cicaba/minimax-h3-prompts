# H3 Prompt Quality Checklist

Check every item before returning a prompt.

## Capability and mode

- Requested duration is 4-15 seconds, or a longer story is split into feasible clips.
- The selected mode matches the actual role of every asset.
- FL2VA-family prompts and Ref2VA prompts are not mixed into the wrong model workflow.
- Ref2VA inputs stay within 9 images, 3 videos, 3 audio clips, and 12 mixed files; video/audio duration limits are respected.
- For local ComfyUI, the effective `17k+5` frame-grid duration is used when final-frame timing matters.
- Width and height use the workflow's supported multiple-of-32 grid when settings are included.

## Structure and language

- The selected mode's required fields appear once and in the correct order.
- The output consistently uses `zh-first` or `official-en` production prose.
- Canonical field names, `[Shot N]`, `(Sx)`, `<d>`, `<scenetrans>`, `<cutoff>`, and reference markers remain unchanged.
- Every label is defined before use and keeps one meaning.
- Asset citations use `<Picture N>`, `<Video N>`, `<Audio N>`, and `<Subject N>` except inside the exact official FL2VA alignment template.
- No unavailable asset, speaker, dialogue, lyric, or visible text was invented.

## Timing and action budget

- `[Shot 1]` has no timestamp.
- Later shot times increase, remain below the effective duration, and leave enough time for their content.
- Major action count and cut count fit the conservative duration budget.
- Every major action has setup, contact or transition, and visible consequence.
- "More detail" enriches body mechanics, materials, lighting, space, and sound instead of adding simultaneous events.
- One dominant camera path serves each shot's composition.
- The ending is explicit and sustainable: final pose, composition, result, transition, or exact frame landing.

## Continuity and references

- Identity, clothing, props, weapon count, lighting, screen direction, and geography remain stable unless an explicit transition changes them.
- I2VA develops forward from the supplied first frame.
- FL2VA describes a continuous path and reaches the supplied last frame.
- L2VA converges to the supplied final frame rather than treating it as an opening.
- Ref2VA assigns every reference an explicit job and distinguishes subject identity from whole-asset editing/continuation roles.
- Wide shots are used for geography and choreography; identity-critical facial detail receives an appropriate closer shot.

## Dialogue, text, and audio

- Speaker IDs are assigned in order of first vocal event and reused consistently.
- Every line names or labels its actual speaker and fits natural delivery time.
- Dialogue, lyrics, and visible text preserve user-supplied language and wording.
- Only intended speech or lyrics appear inside `<d>...</d>`.
- Voiceover is explicitly off-screen and the related visible character's lips remain closed.
- Dialogue crossing a cut uses `<scenetrans>` and explicit audio continuity; intentional truncation uses `<cutoff>`.
- Production prose is scanned for `不`, `不要`, `不能`, `禁止`, `避免`, `切勿`, and similar negative instructions; these are rewritten positively where possible.
- Experimental undocumented vocal/emphasis tags are absent unless the user explicitly requests a test.
- Diegetic events stay in the timeline, ambience/physical sounds stay in `overall_soundscape`, and audience-only score stays in `non_diegetic_music`.
- `overall_soundscape: N/A` means complete silence; `non_diegetic_music: N/A` means no audience-only score.
- Independent clips repeat voice and sound-bed descriptors and do not claim image-based audio continuity.

## Final clarity

- Every sentence maps to an observable or audible result.
- The prompt contains no plot-summary filler, contradictory camera commands, duplicate beats, or unresolved labels.
- Community heuristics are presented as best effort rather than guaranteed behavior.
