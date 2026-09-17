from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "outputs/determinism/run1/2016"
OUT = ROOT / "outputs/final"
OUT.mkdir(parents=True, exist_ok=True)
r = pd.read_csv(SRC / "annual_result.csv").iloc[0]

pd.DataFrame([r]).to_csv(OUT / "c011_final_master_results.csv", index=False, lineterminator="\n")
pd.read_csv(SRC / "population_quintiles.csv").to_csv(OUT / "c011_final_population_burden.csv", index=False, lineterminator="\n")
pd.DataFrame([{k: r[k] for k in ["year", "churn", "L1", "L2", "L3", "G1", "G2", "strict_nonlocal",
    "strict_nonlocal_share", "strict_nonlocal_areas", "strict_nonlocal_states"]}]).to_csv(
    OUT / "c011_final_decomposition.csv", index=False, lineterminator="\n")
pd.read_csv(SRC / "precision_purchased.csv").to_csv(OUT / "c011_final_precision_purchased.csv", index=False, lineterminator="\n")
pd.DataFrame([{k: r[k] for k in ["year", "binding_100", "binding_050", "binding_to_nonbinding", "nonbinding_to_binding"]}]).to_csv(
    OUT / "c011_final_cap_transitions.csv", index=False, lineterminator="\n")
pd.DataFrame([{"year": 2016, "official_qct_count": r.official_qct_050,
    "reconstructed_qct_count": r.reconstructed_qct_050, "mismatch_count": r.mismatches_050,
    "qct_set_digest": r.Q050_digest, "mismatch_file": "reconstruction_mismatches.csv"}]).to_csv(
    OUT / "c011_final_reconstruction_validation.csv", index=False, lineterminator="\n")

classification = [
 {"year":2016,"role":"historical","historical_execution_status":"prior_Tier_A",
  "current_reproducibility_status":"counterfactual_identified","manuscript_admissibility":True},
 {"year":2020,"role":"historical","historical_execution_status":"prior_Tier_A",
  "current_reproducibility_status":"unresolved_allocation_and_c100_arithmetic","manuscript_admissibility":False},
 {"year":2021,"role":"historical","historical_execution_status":"prior_Tier_A",
  "current_reproducibility_status":"unresolved_blank_geography_provenance","manuscript_admissibility":False},
 {"year":2022,"role":"historical","historical_execution_status":"prior_Tier_A",
  "current_reproducibility_status":"nonexact_two_record_cap_boundary_swap","manuscript_admissibility":False},
 {"year":2026,"role":"development_anchor","historical_execution_status":"prior_exact_c050",
  "current_reproducibility_status":"c100_not_uniquely_adjudicated","manuscript_admissibility":False},
]
pd.DataFrame(classification).to_csv(OUT / "c011_final_year_classification.csv", index=False, lineterminator="\n")

pd.DataFrame([
 {"year":2016,"raw_sha256":"75ae56ca258aabde75081739c401aa619886f0463a525d7cf786effbe9ba991f","config":"config/rules/2016.yml","provenance":"docs/rule_provenance/2016.md"},
 {"year":2020,"raw_sha256":"8bab36cb40569a6d79c7bf592eebf0099b631b384c48581244916d48935de0e1","config":"config/rules/2020.yml","provenance":"C011_FINAL_REPRODUCIBILITY_ADJUDICATION.md"},
 {"year":2021,"raw_sha256":"bb63235d8c9b103d3a9dddd9b4b3f97949ed6bc8c7b006d9c895c924abba8b16","config":"config/rules/2021.yml","provenance":"docs/rule_provenance/2021.md"},
 {"year":2022,"raw_sha256":"d613b576695f9f01c800616775bc06aa72a514d350fa3c9a11df9ef8d205f3e0","config":"config/rules/2022.yml","provenance":"docs/rule_provenance/2022.md"},
 {"year":2026,"raw_sha256":"aa1a076b63ca839402558fd1b57f017d1b934857851ebf5726876455dffc8e29","config":"config/rules/2026.yml","provenance":"C011_FINAL_REPRODUCIBILITY_ADJUDICATION.md"},
]).to_csv(OUT / "c011_final_provenance.csv", index=False, lineterminator="\n")

pd.DataFrame([
 {"year":2016,"metric":"BRD","historical_value":"0.1223915232729","current_value":str(r.BRD),"disposition":"minor numerical correction; E/Q sets unchanged"},
 {"year":2016,"metric":"Q100","historical_value":"14057","current_value":str(int(r.Q100)),"disposition":"confirmed"},
 {"year":2020,"metric":"counterfactual","historical_value":"CHR about 3.771%; strict nonlocal 166","current_value":"not admitted","disposition":"current durable provenance incomplete"},
 {"year":2021,"metric":"counterfactual","historical_value":"prior Tier A","current_value":"not admitted","disposition":"blank-geography operational rule undocumented"},
 {"year":2022,"metric":"counterfactual","historical_value":"prior Tier A","current_value":"not admitted","disposition":"two-record boundary swap"},
 {"year":2026,"metric":"Q100","historical_value":"15797","current_value":"not uniquely adjudicated (candidate 15798)","disposition":"15797 not confirmed"},
]).to_csv(OUT / "c011_historical_vs_current_results.csv", index=False, lineterminator="\n")
