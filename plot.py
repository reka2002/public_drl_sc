# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Provided schedule array
# schedule = np.loadtxt("schedule_file_GOD.csv", delimiter=",")
# schedule2 = np.loadtxt("schedule_file_GOD.csv", delimiter=",")

# # Convert the schedule array into a DataFrame with appropriate column names
# df = pd.DataFrame(schedule, columns=[
#     'batch_num', 'gmid', 'production_rate', 'prod_qty', 'prod_time',
#     'prod_start_time', 'prod_end_time', 'cure_time', 'cure_end_time',
#     'booked_inventory', 'action', 'off_grade_production', 'actual_production'
# ])

# # Create a color map for each unique `gmid`
# unique_gmid = df['gmid'].unique()
# color_map = {gmid: plt.cm.tab10(i % 10) for i, gmid in enumerate(unique_gmid)}

# # Initialize plot
# fig, ax = plt.subplots(figsize=(10, 6))

# # Create Gantt bars for each product type based on `prod_start_time` and `prod_time`
# for i, gmid in enumerate(unique_gmid):
#     subset = df[df['gmid'] == gmid]
#     # Each row represents a bar from `prod_start_time` to `prod_end_time`
#     ax.broken_barh([(row['prod_start_time'], row['prod_end_time'] - row['prod_start_time']) for _, row in subset.iterrows()],
#                    (i - 0.4, 0.8),  # Position bars for each product type
#                    facecolors=color_map[gmid],
#                    edgecolor='black')

# # Set labels and title
# ax.set_yticks(np.arange(len(unique_gmid)))
# ax.set_yticklabels([f"Product {int(g)}" for g in unique_gmid])
# ax.set_xlabel("Time (days)")
# ax.set_ylabel("Product Type")
# ax.set_title("Gantt Chart for Product Types by Production Time")
# ax.grid(True)

# # Show plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Assuming schedule_file_GOD.csv includes all the schedules, you may need to load four separate arrays or files for each.
schedule = np.loadtxt("schedule_file_GOD.csv", delimiter=",")
schedule1 = np.loadtxt("schedule_file_GOD.csv", delimiter=",")
schedule2 = np.loadtxt("schedule_file_GOD.csv", delimiter=",")
schedule3 = np.loadtxt("schedule_file_GOD.csv", delimiter=",")

# Function to plot a Gantt chart for a given schedule DataFrame
def plot_gantt(ax, df, title):
    unique_gmid = df['gmid'].unique()
    color_map = {gmid: plt.cm.tab10(i % 10) for i, gmid in enumerate(unique_gmid)}

    for i, gmid in enumerate(unique_gmid):
        subset = df[df['gmid'] == gmid]
        ax.broken_barh(
            [(row['prod_start_time'], row['prod_end_time'] - row['prod_start_time']) for _, row in subset.iterrows()],
            (i - 0.4, 0.8),  # Position bars for each product type
            facecolors=color_map[gmid],
            edgecolor='black'
        )

    ax.set_yticks(np.arange(len(unique_gmid)))
    ax.set_yticklabels([f"Product {int(g)}" for g in unique_gmid])
    ax.set_xlabel("Time (days)")
    ax.set_ylabel("Product Type")
    ax.set_title(title)
    ax.grid(True)

# Convert the schedule arrays into DataFrames with appropriate column names
df_schedule = pd.DataFrame(schedule, columns=[
    'batch_num', 'gmid', 'production_rate', 'prod_qty', 'prod_time',
    'prod_start_time', 'prod_end_time', 'cure_time', 'cure_end_time',
    'booked_inventory', 'action', 'off_grade_production', 'actual_production'
])

df_schedule1 = pd.DataFrame(schedule1, columns=df_schedule.columns)
df_schedule2 = pd.DataFrame(schedule2, columns=df_schedule.columns)
df_schedule3 = pd.DataFrame(schedule3, columns=df_schedule.columns)

# Create a 2x2 grid of subplots
fig, axs = plt.subplots(4, 1, figsize=(12, 10))

# Plot Gantt charts for each schedule on the respective subplot
plot_gantt(axs[0], df_schedule, "Gantt Chart for Schedule")
plot_gantt(axs[1], df_schedule1, "Gantt Chart for Schedule1")
plot_gantt(axs[2], df_schedule2, "Gantt Chart for Schedule2")
plot_gantt(axs[3], df_schedule3, "Gantt Chart for Schedule3")
plt.tight_layout()
plt.show()
