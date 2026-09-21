# Stage 0A side findings

- **Mutable catalog identity is itself a provenance risk.** The current live 2025 IDs are different from the archive IDs used to preserve 2024. Downstream code must never bind a nominal release only to a human-readable title or a stale bookmark.
- **Source-year is measure-specific.** Release year is not a temporal observation time; alternating BRFSS measures require record-level source-year mapping.
- **A same-source-year declaration is not sufficient for exact carry-forward.** Exact/revised classification remains empirical and must use the frozen 100%/99.5% rules.
- **The 2023 CI-method transition and 2024 tract-vintage/poststratification transition are separate comparability axes.** They should not be collapsed into one generic “method changed” flag.
