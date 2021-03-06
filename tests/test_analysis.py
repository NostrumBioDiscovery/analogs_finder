import pytest
import os
import glob
from analogs_finder import main as an


DIR = os.path.dirname(__file__)
MOLECULE_CIRCULAR = [os.path.join(DIR, "data/query_circular.sdf"),]
DB_CIRCULAR = os.path.join(DIR, "data/db_circular.sdf")


def test_circular(molecule=MOLECULE_CIRCULAR, db=DB_CIRCULAR, fp_type="circular", result=18):
    if os.path.exists("counts_circular.txt"): os.remove("counts_circular.txt")
    output = an.query_database(db, molecule, treshold=0.4, fp_type=fp_type, analysis_dataset=True, test=True)
    assert (os.path.exists("counts_circular.txt"))
