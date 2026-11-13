# Disk-quota incident (2026-11-10 ~19:30 EST, transient)

- Two muse.edit calls on apply.py failed: "Disk quota exceeded (os error 122)".
- Follow-up patch attempt via exec also failed once with Errno 122.
- df at the time: /home/hatch 45-46G free (70% used); 1KB touch-writes succeeded, 10KB writes failed intermittently, then succeeded again minutes later.
- A concurrent du -sh ~/workspace from another session was running in the same window; cause is likely transient I/O/quota pressure, not a full disk.
- No hammer-retry: work continued only after single-shot 10KB write tests succeeded in both the scratch dir and the edition dir. If a large write fails again, work stops and the incident goes to the coordinator.
- apply.py itself was verified intact after the incident (syntax OK, HAN fix present).
