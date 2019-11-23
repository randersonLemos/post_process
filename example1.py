# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 13:49:04 2019

@author: randerson
"""


if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

    import pathlib
    from scripts import utils

    from config.scripts import settings as sett

    sim_folder = 'sim_016'
    path_to_rep_file = sett.REP_ROOT / sim_folder / sett.REP_NAME
    ref = utils.get_tables(path_to_rep_file)

    from inputt.scripts import resume
    for well in resume.inje_lst:

       ref.add(ref.join(well.name, *well.nickname_lst))

    #from post_process.scripts import sector_graph
    #sGraph = sector_graph.Sector_Graph(ref)

    #from inputt.scripts.infos import prods_lst
    #from post_process.scripts import producer_graph
    #pGraph = producer_graph.Producer_Graph(prods_lst, ref)

    #from post_process.scripts import special_graph
    #spGraph = special_graph.Special_Graph(prods_lst, ref)

    #from inputt.scripts.infos import injes_lst
    #from post_process.scripts import injector_graph

    #iGraph = injector_graph.Injector_Graph(injes_lst, ref)