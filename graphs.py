import matplotlib.pyplot as plt

def plot_calories_intake(ax):
    intake = [1700, 1500, 2000, 1800, 2100, 1900, 1600]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.bar(days, intake, color='skyblue')
    ax.set_title('Daily Calories Intake')
    ax.set_ylabel('Calories Intake')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def plot_calories_expense(ax):
    expense = [1800, 1600, 1900, 1700, 2000, 1800, 1500]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.bar(days, expense, color='lightcoral')
    ax.set_title('Daily Calories Expense')
    ax.set_ylabel('Calories Expense')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def plot_challenge_completion(ax):
    challenge = [1, 0, 1, 1, 0, 1, 0]
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    ax.bar(days, challenge, color='lightgreen')
    ax.set_title('Challenge Completion Status')
    ax.set_xlabel('Day of the Week')
    ax.set_ylabel('Completed (0 or 1)')
    ax.set_ylim(-0.5, 1.5)
    ax.grid(axis='y', linestyle='--', alpha=0.7)

def create_weekly_progress_figure():
    fig, axs = plt.subplots(3, 1, figsize=(10, 12))
    fig.suptitle('Weekly Progress Metrics', fontsize=18)
    fig.subplots_adjust(hspace=1)

    plot_calories_intake(axs[0])
    plot_calories_expense(axs[1])
    plot_challenge_completion(axs[2])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    return fig

def export_to_png(fig, filename="weekly_progress.png"):
    fig.savefig(filename, dpi=300, bbox_inches='tight')

def export_to_pdf(fig, filename="weekly_progress.pdf"):
    fig.savefig(filename, bbox_inches='tight')

fig = create_weekly_progress_figure()
export_to_png(fig)
export_to_pdf(fig)
plt.show()
