"""Assert frozen-French E keys are byte-identical to the core (zh) expl."""
import sys, importlib.util
FROZEN = ["head_budget3","head_zoom","head_chiffres","head_foot","head_sortir",
          "head_opinion","head_comp6","head_3dates","outils_intro","chart_sub",
          "n_futur2","n_futur3","n_futur4","n_neg1","n_gp1","n_gp2","n_e4"]
def load(path):
    spec = importlib.util.spec_from_file_location("expl_" + path.replace("/","_"), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m.E
core = load(sys.argv[1])
bad = []
for p in sys.argv[2:]:
    e = load(p)
    for k in FROZEN:
        if e.get(k) != core.get(k):
            bad.append((p, k, e.get(k)))
print("FROZEN-KEY CHECK:", "PASS" if not bad else f"FAIL {len(bad)}")
for p, k, v in bad:
    print("  ", p.split("/")[-2], k, "=", v)
sys.exit(1 if bad else 0)
