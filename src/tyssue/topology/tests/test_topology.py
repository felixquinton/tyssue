import pandas as pd
import numpy as np
import json
from scipy import optimize # Usefull to access the docs

from tyssue.core.sheet import Sheet

from tyssue.geometry.sheet_geometry import SheetGeometry as geom

from tyssue.stores import load_datasets
from tyssue.topology.sheet_topology import cell_division, type1_transition


def test_division():

    h5store = 'small_hexagonal.hf5'
    datasets = load_datasets(h5store,
                         data_names=['face', 'vert', 'edge'])
    sheet = Sheet('emin', datasets)
    sheet.set_geom('sheet')
    geom.update_all(sheet)

    Nf, Ne, Nv = sheet.Nf, sheet.Ne, sheet.Nv

    cell_division(sheet, 17, geom)

    assert sheet.Nf - Nf == 1
    assert sheet.Nv - Nv == 2
    assert sheet.Ne - Ne == 6

def test_t1_transition():

    h5store = 'small_hexagonal.hf5'
    datasets = load_datasets(h5store,
                         data_names=['face', 'vert', 'edge'])
    sheet = Sheet('emin', datasets)
    sheet.set_geom('sheet')
    geom.update_all(sheet)
    face = sheet.edge_df.loc[84, 'face']
    type1_transition(sheet, 84)
    assert sheet.edge_df.loc[84, 'face'] != face