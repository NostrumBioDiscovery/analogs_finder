import pytest
import os
import glob
from analogs_finder import main as an
from analogs_finder.rank_methods import phase as ps

DIR = os.path.dirname(__file__)
RESULT_TRESH=1
RESULT_COMBI_SEARCH=2
RESULT_SIMILAR=4
RESULT_SUBSTRUCTURE=2

MOLECULE = os.path.join(DIR, "data/substructre_1.sdf")
MOLECULES = glob.glob(os.path.join(DIR, "data/substructre_*.sdf"))
DB = os.path.join(DIR, "data/database.sdf")
HYPO = os.path.join(DIR, "data/substructre_1.phypo")

def test_tresh(molecule=MOLECULE, db=DB, result=RESULT_TRESH):
    output = an.query_database(db, molecule, treshold=0.45)
    assert result == output


def test_combi(molecule=MOLECULES, db=DB, result=RESULT_COMBI_SEARCH):
    output = an.query_database(db, molecule, combi_subsearch=True)
    assert result == output

def test_similar(molecule=MOLECULE, db=DB, result=RESULT_SIMILAR):
    output = an.query_database(db, molecule, most_similars=True, n_structs=result)
    assert result == output

def test_substructure(molecule=MOLECULE, db=DB, result=RESULT_SUBSTRUCTURE):
    output = an.query_database(db, molecule, substructure=True)

def test_phase(molecule=MOLECULE, db=DB):
    ps.run_phase_screen(molecule, db)

def test_phase_external_hypo(molecule=MOLECULE, db=DB, hypotesis=HYPO):
    ps.run_phase_screen(molecule, db, hypotesis=HYPO)

def test_phase_no_minimization(molecule=MOLECULE, db=DB, hypotesis=HYPO):
    ps.run_phase_screen(molecule, db, hypotesis=HYPO, minimization=False)
