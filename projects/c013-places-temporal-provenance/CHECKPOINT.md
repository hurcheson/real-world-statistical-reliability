# C013 Stage 0A durable checkpoint

**Date:** 2026-09-21  
**Branch:** `codex/c013-stage0-provenance`  
**Base main commit:** `712701002bf51d94e49bc15e7c3651382d0f3bb0`

This branch is an intentionally **incomplete remote checkpoint** of the C013 Stage 0A execution. The complete verified working tree is preserved separately as a content-hashed archive because the current execution bridge can write GitHub text files but cannot directly transfer the complete local repository overlay or raw HTTP response bytes.

Verified before this checkpoint:

- Project Sources normalized to canonical filenames and all 24 SHA-256 entries in v0.28.0 `MANIFEST.json` matched byte-for-byte.
- Canonical state: D039 controls; C013 survives to controlled execution design; C011 remains parked under D037; C012 remains killed under D038.
- Frozen C013 protocol SHA-256: `fa87dc628428b9c9b613f20f2fa80769fe16d153e1f749962fc32b2ceb126629`.
- Local C013 Stage 0A suite: 14/14 tests passed on Python 3.13.5.
- Fresh-directory validation rerun produced byte-identical validation output with 16 retrieval-manifest records and 128 preliminary crosswalk records.
- Preliminary crosswalk SHA-256: `81f7b98a9e30392e65a21d5c59a9ca192fdccda9ee66fbfbe751aa985801b98e`.
- Retrieval manifest SHA-256: `5cb27117dcf71c380adf86ff4cb45faffb74e206f7e1dcfbb8d259494ec12621`.
- Complete local overlay archive SHA-256: `3eda10e4587fba8b14245a7f64e507a99e3f64b99f991923c19b67e8aa4fb2e1`.
- Official-source investigation resolved an important mutable-ID distinction: current `cwsq-ngmh` / `swc5-untb` represent 2025 tract/county releases, while `ai6z-tcin` / `fu4u-a9bh` preserve 2024 archive releases.

Known resolvable blockers:

1. Raw official HTTP response bytes could not be persisted from the web-inspection layer; no raw-response hashes are claimed.
2. Complete per-anchor row-count and measure/source-year grouped queries remain to be rerun from a network-enabled execution environment.
3. Direct first-party raw metadata snapshots remain needed for `rja3-32tc`, `ai6z-tcin`, and `fu4u-a9bh`.
4. The full crosswalk and exact-copy diagnostics are Stage 0B work after raw archival is resolved.

Current readiness: **STAGE 0A INCOMPLETE — RESOLVABLE BLOCKERS**.

Do not merge this checkpoint branch and do not draft a manuscript or conference abstract from it.
