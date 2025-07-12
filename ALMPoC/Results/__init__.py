from modelx.serialize.jsonvalues import *

_formula = None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def liab_cf(liab_id):

    liab = liab_seg[liab_id]


    t_len = range(liab.max_proj_len())

    data = {
        "premiums": [sum(liab.premiums(t)) for t in t_len],
        "claims": [sum(liab.claims(t)) for t in t_len],
        "expenses": [sum(liab.expenses(t)) for t in t_len],
        "commissions": [sum(liab.commissions(t)) for t in t_len],
        "net cashflows": [sum(liab.net_cf(t)) for t in t_len]
    }

    return pd.DataFrame(data, index=t_len)


# ---------------------------------------------------------------------------
# References

liab_seg = ("Interface", ("..", "LiabSeg"), "auto")