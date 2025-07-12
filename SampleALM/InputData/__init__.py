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
    return pd.read_excel(_model.path.parent / 'alm_bond_data.xlsx', index_col='bond_id')


# ---------------------------------------------------------------------------
# References

model_point_10000 = ("Pickle", 2344556816160)

segment_data = ("Pickle", 2344556818752)

segment_map = ("Pickle", 2344556818752)