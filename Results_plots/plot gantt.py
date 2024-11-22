import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

schedule = np.loadtxt("Results_plots/schedule_file_RL_new_new.csv", delimiter=",")
schedule1 = np.loadtxt("Results_plots/schedule_file_MPCRH_new_new.csv", delimiter=",")
#schedule2 = np.loadtxt("Results_plots/schedule_file_MPC.csv", delimiter=",")
schedule2 = np.loadtxt("Results_plots/schedule_file_MPC_new_new.csv", delimiter=",")
schedule3 = np.loadtxt("Results_plots/schedule_file_GOD.csv", delimiter=",")

# # run MPC for 3 forecast
# schedule = np.loadtxt("schedule_file_MPC.csv", delimiter=",")
# schedule1 = np.loadtxt("schedule_file_MPC_STOCHASTIC.csv", delimiter=",")
# # running for so long ??
# schedule2 = np.loadtxt("schedule_file_MPC_DETERMINISTIC.csv", delimiter=",")


# # run MPC RH for 3 forecast
# schedule = np.loadtxt("schedule_file_MPCRH.csv", delimiter=",") # uniform
# schedule1 = np.loadtxt("schedule_file_MPCRH_STOCHASTIC.csv", delimiter=",") # stochastic
# schedule2 = np.loadtxt("schedule_file_MPCRH_DETERMINISTIC.csv", delimiter=",") # deterministic

# # run SMPC for 3 forecast



# # run RL for 3 forecast
# schedule = np.loadtxt("schedule_file_RL_60.csv", delimiter=",")
# schedule1 = np.loadtxt("schedule_file_RL_STOCHASTIC.csv", delimiter=",")
# schedule2 = np.loadtxt("schedule_file_RL_DETERMINISTIC.csv", delimiter=",")




# # run RL and MILP for weekend shipment false, uniform
# schedule1 = np.loadtxt("schedule_file_MPCRH_ws_false.csv", delimiter=",")
# # running so long again 
# schedule2 = np.loadtxt("schedule_file_MPC_ws_false.csv", delimiter=",")


# # run RL for different states
# INV_BALANCE_PRODUCTION
# schedule = np.loadtxt("schedule_file_RL_new_new.csv", delimiter=",")
# schedule1 = np.loadtxt("schedule_file_RL_IO_PRODUCT_new_new.csv", delimiter=",")
#io rTIO



def plot_gantt(ax, df, title):
    unique_gmid = df['gmid'].unique()
    color_map = {gmid: plt.cm.tab10(i % 10) for i, gmid in enumerate(unique_gmid)}

    for i, gmid in enumerate(unique_gmid):
        subset = df[df['gmid'] == gmid]
        ax.broken_barh(
            [(row['prod_start_time'], row['prod_end_time'] - row['prod_start_time']) for _, row in subset.iterrows()],
            (i - 0.4, 0.8), 
            facecolors=color_map[gmid],
            edgecolor='black'
        )

    ax.set_yticks(np.arange(len(unique_gmid)))
    ax.set_yticklabels([f"Product {int(g)}" for g in unique_gmid])
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Product Type")
    ax.set_title(title)
    ax.grid(True)


df_schedule = pd.DataFrame(schedule1, columns=[
    'batch_num', 'gmid', 'production_rate', 'prod_qty', 'prod_time',
    'prod_start_time', 'prod_end_time', 'cure_time', 'cure_end_time',
    'booked_inventory', 'action', 'off_grade_production', 'actual_production'
])

df_schedule1 = pd.DataFrame(schedule1, columns=df_schedule.columns)
df_schedule2 = pd.DataFrame(schedule2, columns=df_schedule.columns)
df_schedule3 = pd.DataFrame(schedule3, columns=df_schedule.columns)


fig, axs = plt.subplots(4, 1, figsize=(12, 10))


plot_gantt(axs[0], df_schedule, "RL")
plot_gantt(axs[1], df_schedule1, "MILP RH UNIFORM")
plot_gantt(axs[2], df_schedule2, "MILP SH DETERMINISTIC")
plot_gantt(axs[3], df_schedule3, "PI MILP")
#plot_gantt(axs[0], df_schedule, "RL")
# plot_gantt(axs[0], df_schedule, "INV_BALANCE_PRODUCTION")
# plot_gantt(axs[1], df_schedule1, "IO_PRODUCT")
# #plot_gantt(axs[2], df_schedule2, "RL DETERMINISTIC")
plt.tight_layout()
plt.show()
