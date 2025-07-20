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
        "claims(death)": [sum(liab.claims(t, 'DEATH')) for t in t_len],
        "claims(lapse)": [sum(liab.claims(t, 'LAPSE')) for t in t_len],
        "claims(maturiry)": [sum(liab.claims(t, 'MATURITY')) for t in t_len],
        "expenses": [sum(liab.expenses(t)) for t in t_len],
        "commissions": [sum(liab.commissions(t)) for t in t_len],
        "liab_cf": [liab.liab_cf(t) for t in t_len]
    }

    return pd.DataFrame(data, index=t_len)


def cash_result(ast_seg_id):

    asset = asset_seg[ast_seg_id]

    t_len = 121

    data = {
        "seg_cash_pre_trade": [asset.seg_cash_pre_trade(t) for t in range(t_len)],
        "seg_trade_amount": [asset.seg_trade_amount(t) for t in range(t_len)],
        "seg_cash_post_trade": [asset.seg_cash_post_trade(t) for t in range(t_len)],
        "seg_asset_cashflows": [asset.seg_asset_cashflows(t) for t in range(t_len)],
        "liab_cashflows": [asset.liab_cashflows(t) for t in range(t_len)]
    }

    return pd.DataFrame(data, index=range(t_len))


def av_movement(liab_id):

    liab = liab_seg[liab_id]
    t_len = range(liab.max_proj_len())

    data = {'av_at(pre_mat)': [sum(liab.av_at(t, "BEF_MAT")) for t in t_len],
            'claims_from_av(maturity)': [sum(liab.claims_from_av(t, 'MATURITY')) for t in t_len],
            'prem_to_av': [sum(liab.prem_to_av(t)) for t in t_len],
            'maint_fee': [sum(liab.maint_fee(t)) for t in t_len],
            'coi': [sum(liab.coi(t)) for t in t_len],
            'inv_income': [sum(liab.inv_income(t)) for t in t_len],
            'claims_from_av(death)': [sum(liab.claims_from_av(t, 'DEATH')) for t in t_len],
            'claims_from_av(lapse)': [sum(liab.claims_from_av(t, 'LAPSE')) for t in t_len],
            }

    return pd.DataFrame(data, index=t_len)


def pols_result(liab_id):

    liab = liab_seg[liab_id]
    t_len = range(liab.max_proj_len())

    data = {'pols_if(pre_mat)': [sum(liab.pols_if_at(t, "BEF_MAT")) for t in t_len],
            'pols_matuirty': [sum(liab.pols_maturity(t)) for t in t_len],
            'pols_new_biz': [sum(liab.pols_new_biz(t)) for t in t_len],
            'pols_lapse': [sum(liab.pols_lapse(t)) for t in t_len],
            'pols_death': [sum(liab.pols_death(t)) for t in t_len]}

    return pd.DataFrame(data, index=t_len)


def asset_result(ast_seg_id):

    asset = asset_seg[ast_seg_id]

    t_len = 121

    data = {
        "seg_face_value": [asset.seg_face_value(t) for t in range(t_len)],
        "seg_market_value": [asset.seg_market_value(t) for t in range(t_len)],
        "seg_mv_return": [asset.seg_mv_return(t) for t in range(t_len)],
    }

    return pd.DataFrame(data, index=range(t_len))


# ---------------------------------------------------------------------------
# References

liab_seg = ("Interface", ("..", "LiabSeg"), "auto")

asset_seg = ("Interface", ("..", "AssetSeg"), "auto")