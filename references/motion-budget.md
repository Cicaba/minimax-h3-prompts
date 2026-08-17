# Motion and Complexity Budget

Use this reference for fights, dances, sports, chases, transformations, multiple interacting subjects, or prompts that ask for "more detail." These are conservative production heuristics derived from community results and local testing, not official hard limits.

## Budget by duration

| Duration | Conservative shot budget | Major action beats |
| --- | ---: | ---: |
| 4-6 s | 1 shot | 1-2 |
| 7-10 s | 1-2 shots | 2-3 |
| 11-15 s | 2-3 shots | 3-4 |

For INT8/FP8, four-step, or other short-trajectory workflows, remove one major beat or one cut from the upper end of the budget.

One major beat is a complete readable unit such as:

```text
setup -> committed movement -> contact or transition -> visible consequence
```

Examples include one attack-and-response exchange, one dance phrase, one vehicle maneuver, one transformation, or one dialogue reaction. Several strikes inside a single choreographed combination may remain one beat when their order and result are clear.

## Add detail without adding events

When the user asks for more detail, enrich the current beat with:

- body mechanics: weight shift, foot placement, recoil, balance recovery;
- material response: cloth drag, hair motion, armor flex, debris, water, dust;
- lighting response: reflections, energy spill, exposure change;
- spatial causality: where each subject starts, travels, and lands;
- synchronized sound: approach, contact, resonance, decay.

Do not add another opponent, transformation, weapon, camera reversal, or explosion merely to make the prompt more detailed.

## Complexity risks

Count one risk for each condition:

- three or more interacting foreground subjects;
- more than one simultaneous large effect;
- identity-critical faces held in a wide shot;
- a rapid camera move during fine hand or weapon choreography;
- costume, body, creature, or vehicle transformation;
- overlapping dialogue during action;
- more than one reference role assigned to the same asset without explanation.

At three or more risks, simplify the shot, split the work into clips, or use a first-frame/reference workflow. State the trade-off briefly when it materially changes the user's request.

## Action-scene construction

1. Establish geography in a medium-wide or wide composition: subject positions, facing directions, distance, weapons, and the escape or impact space.
2. Give the initiator one clear attack or movement direction.
3. Give the responder one readable defense, dodge, or counter.
4. Show contact and consequence before starting the next beat.
5. End in a sustainable pose or composition that can serve as the next clip's first frame.

Use one dominant camera behavior per shot. Tracking, arcing, or pulling back can evolve within a shot; stacking several unrelated camera commands usually weakens choreography.

## Framing trade-offs

- Use medium-wide framing for full-body choreography, interaction, and weapon paths.
- Use medium or medium-close framing for identity, facial acting, and dialogue.
- Use a dedicated close shot for fine facial detail rather than demanding sharp faces from a distant battle tableau.
- If both face fidelity and large-scale action matter, allocate separate shots instead of requiring both at the same instant.

## Dance and group movement

- Define the lead dancer, formation, spacing, and travel direction before choreography.
- Treat one eight-count phrase as one major beat.
- Describe the lead motion first, then state how the group follows or ripples through the formation.
- Change formation only after the previous formation becomes readable.
- Keep hands, feet, and partner contact observable; use full-body or medium-wide framing.

## Continuity locks

Repeat only the traits that are at risk in the current shot: identity, costume, weapon count, vehicle shape, screen direction, or location anchors. Avoid repeating the entire character description at every timestamp.

For a sequence of independent clips, preserve:

- the actual final frame as the next visual boundary when using I2VA;
- pose, facing direction, screen position, subject spacing, prop count/state, and stable environmental landmarks;
- camera height, movement direction, action momentum, light direction, and color treatment;
- separately restated audio bed, speaker voice, music tempo, acoustic space, and current audio phase.

For a hard cut, keep the global identity/style lock and use a readable transition relationship such as matched movement direction, shared shape, object occlusion, impact, or beat cut.
