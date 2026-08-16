# MiniMax H3 Capabilities and Local Runtime Notes

Use this reference for duration, resolution, aspect ratio, reference limits, model selection, or ComfyUI settings. Official limits take precedence over local heuristics.

## Official H3 limits

- Output duration: 4-15 seconds.
- Output frame rate: 24 FPS.
- Output audio: native 32 kHz stereo.
- Aspect ratios include 21:9, 16:9, 4:3, 1:1, 3:4, and 9:16.
- H3-Base normally generates at a 768-pixel short edge. Official H3-Regenerate-2K can regenerate the base result at up to 2K.
- Stable dialogue-language support covers Arabic, Chinese, English, French, German, Italian, Japanese, Korean, Portuguese, Russian, and Spanish. Other languages have variable support.

## Model families

- `H3-Base-FL2VA`: text-to-audio-video plus optional first frame, last frame, or both. Use this family for T2VA, I2VA, FL2VA, and L2VA.
- `H3-Base-Ref2VA`: multimodal reference-to-audio-video. Use this family when images, videos, or audio guide reusable identity, style, motion, camera, voice, editing, or continuation relationships.
- The FL2VA and Ref2VA families use different diffusion weights. Do not write a Ref2VA prompt for an FL2VA workflow or vice versa.

## Ref2VA input limits

- Images: at most 9.
- Videos: at most 3; each clip is 2-15 seconds and their total duration is at most 15 seconds.
- Standalone audio clips: at most 3; each clip is 2-15 seconds and their total duration is at most 15 seconds.
- Mixed inputs: at most 12 files across all input types.
- Assign every reference one explicit job such as identity, location, style, motion, camera, voice, soundtrack, keyframe, editing source, or continuation source.

## ComfyUI official workflow notes

- Use ComfyUI 0.30.0 or later for native H3 workflows.
- Keep generated width and height on a multiple-of-32 grid.
- The native canvas uses a 768-pixel short edge and is capped around 768x1344 before official 2K regeneration.
- The official templates use pruned INT8 diffusion weights and an NVFP4/AWQ text encoder. Treat these as supported local defaults, while BF16 remains the released base-checkpoint precision.
- `ref_image_size=match` favors speed by scaling references to generation size. `ref_image_size=max` retains up to a 2048-pixel short edge for stronger reference detail at higher cost.

## ComfyUI duration grid

ComfyUI snaps local duration to a `17k+5` frame grid at 24 FPS:

```text
frames = 17 * k + 5
effective_seconds = frames / 24
```

Use the effective duration for last-frame alignment and final timestamps. Run `scripts/h3_duration.py <requested-seconds>` when the user supplies a rounded duration.

Common values:

| Requested | Frames | Effective |
| --- | ---: | ---: |
| 9.4 s | 226 | 9.42 s |
| 10 s | 243 | 10.13 s |
| 15 s | 362 | 15.08 s |

The local snapped value may slightly exceed the rounded official duration label. Treat it as a workflow-specific effective timeline, not a new platform limit.

## Resolution and duration trade-off

Longer duration and larger pixel count increase memory and generation time together. Prompt rewriting cannot remove this runtime cost. For constrained local hardware, prioritize in this order:

1. preserve the intended aspect ratio;
2. reduce megapixels for motion tests;
3. validate choreography and audio at preview resolution;
4. raise resolution only after the timeline works;
5. use official 2K regeneration or post-production upscaling when available.
