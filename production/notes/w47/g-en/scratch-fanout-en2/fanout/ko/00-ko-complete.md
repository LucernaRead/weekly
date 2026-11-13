# ko — COMPLETE, self-check zero issues (2026-11-11)

- Edition: `production/2026-w47/2026-w47-en-ko/` (slug `2026-w47-en-ko`)
- Print PDF: `The-Lucerna-VOL4-en-ko.pdf`, 32,386,030 bytes,
  SHA-256 `983ad19cbd400836a465b9592d9a866597d5476b39a0a36a3c8e6ea9e6834c18`
- Web PDF: `The-Lucerna-VOL4-en-ko.web.pdf`, 2,594,367 bytes,
  SHA-256 `e2439e78fc3d551503b7222ed740f2868eba415bddaa960a1fd47d06a126907a`
- Gates: run exit 0, 0 overflow after the P2 fix (all flows within bottom; P8-keys 2205/2560;
  P2-ex 2532/2560); occlusion 0 flags; p8 extract 60/150, compare CLEAN (keydiff 137–140, 150,
  expected); freeze direct sha256 8/8; print/web text diff 0/0; P8 min font 13.5 pt; badges =
  core on all 8 pages; text.md 52,965 bytes, 150/150 keys; 8 cards visually checked after the
  final render, zero issues.
- Fix in this round (→ rebuild + re-render + full re-gate): P2-ex FLOW OVERFLOW (y=2946/2560)
  on the first run — the only overflow in the whole fan-out. Root cause: the W46 TM B bridge
  wrapped to 2 lines; one early extra line cascaded through the 4-column flow packing and
  `match_set`'s keep-together _fit(362) clamped the D block to the page bottom (333pt dead gap).
  Fixed via lit_overrides → 1-line bridge; re-run P2-ex ends 2532/2560 (same as ja).
- Incident: VM restart SIGTERM'd the gates run at ~05:25 (text.md step never ran, /tmp log wiped).
  Recovered the es way: completed steps verified from artifacts; re-ran only direct-sha (8/8),
  print/web diff (0/0), print SHA/size, text.md (RC=0, 150/150).
- Standing lesson for zh-tw: verify every reused TM bridge fits on ONE line — a 1-line excess
  early in a 4-column flow cascades; check the P2-ex flow end on the first run.
- Full record: the edition WEEKLY-KIT.md §5/§10.
