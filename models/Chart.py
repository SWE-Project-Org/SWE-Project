import matplotlib.pyplot as plt  

class Chart:
    def __init__(self):
        dpi = 100
        self.fig, axs = plt.subplots(3, 1, figsize=(3.11, 6.31), dpi=dpi)
        self.fig.suptitle('Weekly Progress Metrics', fontsize=18)
        self.fig.subplots_adjust(hspace=1)
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        intake = [1700, 1500, 2000, 1800, 2100, 1900, 1600]
        axs[0].bar(days, intake, color='skyblue')
        axs[0].set_title('Daily Calories Intake')
        axs[0].set_ylabel('Calories Intake')
        axs[0].grid(axis='y', linestyle='--', alpha=0.7)
        expense = [1800, 1600, 1900, 1700, 2000, 1800, 1500]
        axs[1].bar(days, expense, color='lightcoral')
        axs[1].set_title('Daily Calories Expense')
        axs[1].set_ylabel('Calories Expense')
        axs[1].grid(axis='y', linestyle='--', alpha=0.7)
        challenge = [1, 0, 1, 1, 0, 1, 0]
        axs[2].bar(days, challenge, color='lightgreen')
        axs[2].set_title('Challenge Completion Status')
        axs[2].set_xlabel('Day of the Week')
        axs[2].set_ylabel('Completed (0 or 1)')
        axs[2].set_ylim(-0.5, 1.5)
        axs[2].grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])