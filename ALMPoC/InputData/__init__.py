from modelx.serialize.jsonvalues import *

_formula = None

_bases = []

_allow_none = None

_spaces = []

# ---------------------------------------------------------------------------
# Cells

def model_point_table():
    return pd.read_excel(_model.path.parent / 'alm_model_point_10K.xlsx', index_col='policy_id')


def model_point_segment(liab_id):
    table = model_point_table()
    return table[table['liab_id'] == liab_id]


def bond_data():
    return pd.read_excel(
        _model.path.parent / 'alm_bond_data.xlsx', 
        sheet_name='inforce_bonds',
        index_col='bond_id')


def newmoney_bond_params():
    return pd.read_excel(
        _model.path.parent / 'alm_bond_data.xlsx',
        sheet_name='bond_template',
        index_col='bond_id')


def is_inforce_bond(bond_id):
    if bond_id in bond_data().index:
        return True
    else:
        return False


def spread(bond_id):
    if is_inforce_bond(bond_id):
        return bond_data().loc[bond_id]['z_spread']
    else:
        return newmoney_bond_params().loc[bond_id]['z_spread']


def coupon_rate(bond_id):
    if is_inforce_bond(bond_id):
        return bond_data().loc[bond_id]['coupon_rate']
    else:
        return newmoney_bond_params().loc[bond_id]['coupon_rate']


def issue_date(bond_id):
    if is_inforce_bond(bond_id):
        d = bond_data().loc[bond_id]['issue_date']
        return ql.Date(d.day, d.month, d.year)
    else:
        offset = newmoney_bond_params().loc[bond_id]['issue_mth_offset']
        return ql.Date(date_init, "%Y-%m-%d") + ql.Period(int(offset), ql.Months)


def maturity_date(bond_id):
    if is_inforce_bond(bond_id):
        d = bond_data().loc[bond_id]['maturity_date']
        return ql.Date(d.day, d.month, d.year)
    else:
        term = newmoney_bond_params().loc[bond_id]['bond_term']
        return issue_date(bond_id) + ql.Period(int(term), ql.Years)


def tenor(bond_id):
    if is_inforce_bond(bond_id):
        tenor = bond_data().loc[bond_id]['tenor']
    else:
        tenor = newmoney_bond_params().loc[bond_id]['tenor']

    return ql.Period(ql.Semiannual if tenor == '6M' else ql.Annual)


# ---------------------------------------------------------------------------
# References

segment_data = ("Pickle", 2223849419936)

segment_map = ("Pickle", 2223849419936)

date_init = "2022-01-01"