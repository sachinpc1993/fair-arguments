import pandas as pd
from FairEvalClass import rND, rRD, rKL


if __name__ == '__main__':

    system_ranking = pd.read_csv('input_file.csv')  # Containing all of the rankings from all the systems.

    systems = system_ranking['system_name'].unique()

    unfairness_df = []
    for system in systems:
        system_temp_df = system_ranking[system_ranking['system_name'] == system]

        for i in range(1, 51):
            ranking_temp_df = system_temp_df[system_temp_df['topic'] == i]
            unfairness_rnd = rND.rND_fairness_ranking_calculation(ranking_temp_df)
            unfairness_rrd = rRD.rRD_fairness_ranking_calculation(ranking_temp_df)
            unfairness_rkl = rKL.rKL_fairness_ranking_calculation(ranking_temp_df)
            unfairness_df.append([system, i, unfairness_rnd, unfairness_rkl, unfairness_rrd])

    unfairness = pd.DataFrame(unfairness_df,
                              columns=['system', 'topic', 'rND_unfairness', 'rKL_unfairness', 'rRD_unfairness'])

    unfairness.to_csv('System_Unfairness.csv')