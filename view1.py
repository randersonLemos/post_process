# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 16:16:55 2020

@author: randerson
"""

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from post_process.scripts import utils
    from config.scripts import settings as sett
    from post_process.scripts import graph

    sim_group_folder = 'REFERENCE'
    sim_folder  = 'sim_001'
    path_to_rep_file = sett.REP_ROOT / sett.SIMS_FOLDER / sim_group_folder / sim_folder / sett.REP_NAME
    tables = utils.get_tables(path_to_rep_file)

    from inputt import loader

    for well in loader.inje_lst: tables.add(tables.join(well.name, *well.alias_lst)) # Join XXXXXX-W and XXXXXX-G to XXXXXX

    from inputt.scripts import utils as inputt_utils
    from post_process.scripts.sector_graph import Sector_Graph
    sg = Sector_Graph(tables)

    from post_process.scripts.well_graph import Well_Graph
    pg = Well_Graph(inputt_utils.gather_wells_names(loader.prod_lst), tables)
    ig = Well_Graph(inputt_utils.gather_wells_names(loader.inje_lst), tables)

    from post_process.scripts.special_graph import Special_Graph
    spg = Special_Graph(inputt_utils.gather_wells_names(loader.prod_lst), tables)
    sig = Special_Graph(inputt_utils.gather_wells_names(loader.inje_lst), tables)

    pg.essential_prod(); ig.essential_inje()
    for well_name in inputt_utils.gather_wells_names(loader.prod_lst): spg.essential_prod(well_lst=[well_name])
    for well_name in inputt_utils.gather_wells_names(loader.inje_lst): sig.essential_inje(well_lst=[well_name])
    graph.Graph.show()