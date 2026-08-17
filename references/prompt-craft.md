# Prompt Craft from Official H3 Workflows

Use this reference for stylized, under-specified, brand/product, music-led, multi-clip, or continuity-critical requests. It adapts reusable prompt-writing practices from the official MiniMax H3 guides and bundled style skills without inheriting their Hub-only tooling or approval workflow.

## Lock the production facts

- Fix duration, aspect ratio, visual medium, intended audio, dialogue/lyrics, visible text, and ending before adding detail.
- Separate user facts from creative fill. Preserve exact identity cues, product facts, brand copy, lyrics, dialogue, and asset provenance; invent only details that are compatible with the request.
- Assign each reference a narrow primary job such as identity, costume, scene, style, motion, camera, keyframe, voice, beat, or soundtrack. If one asset has several jobs, state each role explicitly.
- Prefer separate identity, scene, product, and typography anchors. Treat a contact sheet, storyboard grid, arrows, labels, or timing marks as production material rather than target imagery unless the user wants that layout visible.

## Build an executable shot

Write each shot in playback order:

```text
composition and geography -> subject identity and position -> initial state -> action path -> visible or audible consequence -> camera response -> end state or handoff
```

- Establish screen direction, spacing, important objects, light direction, and the available movement path before complex action.
- Use one primary action beat, one dominant camera path, and one main visual effect per short shot. Secondary details should support the same beat.
- Describe body mechanics, object state changes, material response, and causal timing. Replace “the scene becomes exciting” with the visible action that creates the change.
- End on a readable result, reaction, pose, object state, composition, or transition anchor.
- Keep the render prompt free of storyboard-only panel names, arrows, approval notes, timing marks, and production commentary.

## Translate style into observable properties

- Name the medium or rendering treatment, then specify material texture, light source and direction, palette, contrast, depth of field, lens behavior, grain, and motion character when relevant.
- Use broad words such as `cinematic`, `beautiful`, `premium`, or `dreamlike` only when nearby details show what they mean on screen.
- Lock a small set of high-value style traits and repeat only those at risk. Large adjective stacks consume attention without improving motion clarity.

## Map timing and rhythm

- Allocate enough time for setup, committed movement, consequence, and recovery. Add per-second directives only when exact choreography, dialogue, lyrics, UI events, or beat synchronization matters.
- Map dialogue and lyrics to natural delivery time. Place cuts at phrase boundaries, breaths, beats, impacts, or intentional match points.
- For music-led clips, define one master tempo or audio window and align visual peaks to its beat structure. Do not describe the same soundtrack as both native score and a separate replacement track.

## Hand off continuity between clips

For a continuing scene, carry forward:

- the actual tail frame when an image boundary is available;
- subject identity, wardrobe, pose, facing direction, screen position, and spacing;
- prop count and state, environmental landmarks, light direction, and color treatment;
- camera height, movement direction, action momentum, and audio phase.

For a deliberate hard cut, preserve the global identity and style lock while using an explicit transition logic such as matched movement direction, shared shape, object occlusion, impact, or beat cut. A visual boundary preserves image state only; restate the required audio bed separately.

## Final craft check

- Every sentence produces an observable image, motion, sound, or reference relationship.
- The event count fits the duration and model path.
- References have explicit roles and no production layout is accidentally treated as target content.
- The opening follows the user's request, and the ending lands on a clear state.
- Literal dialogue, lyrics, visible text, product facts, and brand claims remain exact and sourced.
