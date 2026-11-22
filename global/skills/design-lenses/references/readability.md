# Readability

Lenses for seeing what happens: alerts, icons, highlights, the HUD, the minimap, the camera, and the player who
loses track of the battle. Diagnose first, then pick a remedy.

## Diagnose: where the player's loop breaks

- **The interaction loop** (Fullerton ch. 5, Cook's sidebar "Interaction Loops and Arcs"; Sellers ch. 4,
  "Interactive Game Loops"): mental model, decision, action, the rules, feedback, an updated model. Find the step
  that fails: the player didn't know what mattered (model), had too many decisions at once (decision), missed what
  happened (feedback), or lacked an earlier skill the next one builds on (skill chain). Alerts and icons fix
  feedback; a slower opponent fixes decision rate; neither fixes a missing model.
- **Mental model** (Sellers ch. 4, "Internal State"): after seeing it twice, could the player predict it a third
  time? Separate what is hidden on purpose from what is hidden by accident.
- **Information structure** (Fullerton ch. 5, "Information Structure"): fog hides by design and carries
  tension; clutter hides by accident. A readability fix touches only the clutter.
- **Schell #62 Transparency** (ch. 15): does the interface hold up under stress, or do players fumble and miss
  what matters? On which link between player, controls and world does confusion happen?
- **Schell #67 Modes** (ch. 15) with Sid Meier's rule (Schell ch. 12, "Modes"): a player should never stay in a
  sub-game so long they forget the main one. One absorbing fight that hides the rest of the map is this failure.

## Budget: attention runs out

- **The fast drives out the slow** (Sellers ch. 4, "Mental Load and the Interactivity Budget"): reflex demands take
  attention first, then tactics, then strategy. Every alert is a reflex demand; it helps only if it carries
  something the player must act on. Stellaris lets battles run unattended so attention stays on strategy.
- **Cut before adding** (Sellers ch. 8, "Providing Feedback"): in a strategy game, visual overload is a signal to
  cut parts and behaviours, not to add feedback.
- **Micromanagement** (Fullerton ch. 11, "Fun Killers"): merge small decisions into one, set sensible defaults,
  offer optional automation. A third remedy beside alerts and a slower opponent.
- **A small cue at the stuck moment** (Fullerton ch. 11, "Insurmountable Obstacles", the Halo door): a few small
  cues fixed confusion without lowering the challenge.

## Feedback rules

- **Semantic and articulatory distance** (Sellers ch. 4, "Player Behaviors and Cognitive Load"): how hard the
  result is to read, and the order to give. An animation reads faster than an icon, an icon faster than text.
- **Sellers ch. 8, "Providing Feedback"**: every state change worth having gets feedback; full state changes (a
  unit pinned, broken, a soldier dead) are emphatic; feedback lands within 100 to 250 ms or loses its cause after about
  a second; engaged players don't read text; meaningless or inconsistent effects get read as meaning anyway.
- **Schell #63 Feedback** (ch. 15): at each moment, what must the player know, what do they want to know, and what
  should they feel?
- **Schell #61 Virtual Interface** (ch. 15): what does the world fail to show (an attack off-screen, a unit
  breaking, a world event's timer), and when is it needed?
- **Schell #66 Channels and Dimensions** (ch. 15, "Channels of Information"), the four-step method: (1) list the
  information and rank it: needed every moment, at a glance, now and then; (2) list the channels: screen regions,
  the unit itself, the minimap, sound, the screen edge; (3) map information to channels; (4) use each channel's
  dimensions (colour, size, shape, motion) to reinforce one fact, or to carry several at a teaching cost.
- **Schell #67½ Metaphor** (ch. 15, ToyTopia): a visible radio pulse with a sound made a network delay readable.
  In-fiction signals (radio chatter, flares) can carry alerts.

## Strategy-game translations of Rogers' rules

Rogers writes for third-person action games; these carry over once the hero becomes every unit.

- **Never lose a unit** (lvl 6, [«Не позволяйте персонажу пропадать из кадра»]): every unit behind a wall, inside
  a building or off-screen is findable in a second (silhouette, edge arrow, minimap mark).
- **The camera points at the goal** (lvl 6, [«Всегда направляйте камеру на цель»]): something must pull the eye to
  an important event off-screen. Taking camera control away must be obvious; a jump-to key is the gentler form.
- **Reach the fight in time** (lvl 6, [«Прокручивающаяся камера»]): scroll speed lets the player reach a distant
  fight before it is decided.
- **Fade occluders, never pop them** (lvl 6, camera collision): roofs and walls that hide units turn translucent.
- **Don't blind a losing player** (lvl 6, first-person camera): no blur or splash that hides where the damage comes
  from. Watch full-screen weather and status effects.
- **State on the model** (lvl 10, [«Черт побери, Джонс, что у тебя не болит?»]): the player can't watch bars all
  the time; fewer men, a limp, a man lying flat show health and morale on the unit itself.
- **Minimap** (lvl 8, [«Радар/карта»]): a legend, height and layers; extra layers like vision cones become alert and
  fog layers here.
- **Context signs at the unit** (lvl 8, [«Контекстная подсказка»]): "flanked", "suppressed" show where the unit is.
- **Icons** (lvl 8, [«Icon has cheezburger?»]): picture matches the action, colour by family, shape backs colour up,
  a clear outline, no two alike, no text, a tooltip, feedback on every click.
- **Placement** (lvl 8, [«HUD и куда его засунуть»]): keep the centre clear; panels on three sides make a
  letterbox, a "mail slot" view of the battle.

## Cautions

- Rogers' clean-screen, no-HUD advice: he himself puts strategy games on the "lots of interface" side. It never
  argues for removing RTS information, only for hiding what is inactive.
- Rogers' numbers (safe frame, minimum font size, the three-press menu rule) are console-TV rules; keep the
  principle, drop the number.
- Schell #64 Juiciness: extra motion on a busy battlefield is noise; weigh it against #62 and #66.
- Sellers' "every behaviour needs feedback", taken literally, adds the noise a readability fix removes: pair it
  with his cut-parts remedy and emphasis only for full state changes.
- The 100 to 250 ms feedback target is for the local view and input; lockstep input delay is a separate budget.
- Sellers concedes the attention budget can't be measured: whether a player is over it comes from playtests.
