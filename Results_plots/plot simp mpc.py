import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

schedule = np.loadtxt("schedule_file_SIMP_MPC.csv", delimiter=",")


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

df_schedule = pd.DataFrame(schedule, columns=[
    'batch_num', 'gmid', 'production_rate', 'prod_qty', 'prod_time',
    'prod_start_time', 'prod_end_time', 'cure_time', 'cure_end_time',
    'booked_inventory', 'action', 'off_grade_production', 'actual_production'
])




fig, axs = plt.subplots(1, 1, figsize=(12, 10))

# Plot Gantt charts for each schedule on the respective subplot
# plot_gantt(axs[0], df_schedule, "RL")
# plot_gantt(axs[1], df_schedule1, "MILP RH UNIFORM")
# plot_gantt(axs[2], df_schedule2, "MILP SH UNIFORM")
#plot_gantt(axs[3], df_schedule3, "PI MILP")
#plot_gantt(axs[0], df_schedule, "RL")
plot_gantt(axs, df_schedule, "RL UNIFORM")
plt.tight_layout()
plt.show()
