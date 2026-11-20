CLEARSKY TOWER — ADDITIVE EXPANSION
===================================
QUICK START
1. Extract the entire ZIP into a folder.
2. Windows: double-click START_WINDOWS.bat (Python 3 required).
   macOS/Linux: run python3 launch.py from the extracted folder.
   Or open index.html directly for basic play. Localhost is recommended for camera/mic.
3. Choose your airport, job and staffing, then START SHIFT.
4. The top-left dock opens Expansion, Tactical radar and Flight board.

The launcher serves only this extracted folder at 127.0.0.1, opens your browser,
and stops with Ctrl+C. No packages are required. If Windows does not have the
Python launcher, install Python 3 or open index.html directly.

WHAT WAS ADDED
Gameplay:
- Optional medical, fuel and simulated engine-priority arrivals.
- Five-minute advisory response timers. Timers never crash/delete aircraft.
- Optional incidents approximately every three real simulation minutes.
- One-click additional arrivals and parked departures, using original capacity rules.
- Coastal International: 2 runways / 12 stands, waterfront scenery.
- Cargo Gateway: 3 runways / 24 stands, extra freight buildings.
  These are layout variants on the original proven taxi/service road network,
  not completely redesigned taxiway networks.

Visuals:
- Clear, overcast, rain, fog and storm presets with visibility/wind advisory readout.
- Optional navigation/strobe lights and weather overlays.
- Regional/narrowbody/heavy size variants of the existing aircraft model.
- Extra hangars, cargo containers and perimeter scenery.

Controls/interface:
- Click/tap tactical radar with recent tracks, estimated 60-second vectors,
  range controls, surface view and selected-aircraft route.
- Searchable, filterable flight board; priority/conflict sorting; suggested commands.
- Eight-step guided introduction.
- Optional touch movement pad alongside the original drag/radio/role controls.
- Individual expansion switches and a reset-options button.

PRESERVATION / BACKUP
The original HTML is included unchanged in backup/original-index.html.
The updated index.html preserves the original source and inserts an additive
expansion immediately before the original startup sequence. Existing tower,
ground office, shuttle, NPC roster, routes, commands, head tracking, live camera,
reports and core flight handling were not replaced. The original three airport
profiles and controls remain available. To revert, copy the backup HTML over
index.html. The SHA-256 manifest can verify the original backup.

IMPORTANT LIMITATIONS
- Weather is visual/advisory, not wind drift, braking or engine-failure physics.
- Aircraft classes are size/label variants, not separate aerodynamic models.
- Priority timers are advisory and do not add crash mechanics.
- Radar vectors are straight-line estimates, not guaranteed conflict predictions.
- Original simplified flight handling, role permissions and safety checks apply.
- Added emergency traffic can increase separation alerts: it uses original spawn logic.
- Tutorial/side panels do not pause operations. Use the original Pause button.
- Existing camera tracking may download its external library/model when enabled.
  Camera/mic permissions and webcam hardware were not tested here.
- Expansion controls reset to defaults on reload; this is not a save-system upgrade.
- No software can be guaranteed bug-free. See TEST_RESULTS.txt for actual checks.
- Fictional game only; not for navigation or operational training.
