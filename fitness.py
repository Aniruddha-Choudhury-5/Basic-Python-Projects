import tkinter as tk
from tkinter import messagebox

class FitnessTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health and Fitness Tracker")
        self.root.geometry("300x200")

        # Labels and Entry fields
        tk.Label(root, text="Steps taken:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.steps_entry = tk.Entry(root)
        self.steps_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Distance (km):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.distance_entry = tk.Entry(root)
        self.distance_entry.grid(row=1, column=1, padx=10, pady=5)

        # Track Button
        self.track_button = tk.Button(root, text="Track Activity", command=self.track_activity)
        self.track_button.grid(row=2, columnspan=2, pady=10)

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=3, columnspan=2)

    def calculate_calories_burned(self, steps, distance):
        calories_per_step = 0.04
        calories_per_distance = 0.1
        return (steps * calories_per_step) + (distance * calories_per_distance)

    def track_activity(self):
        try:
            steps = int(self.steps_entry.get())
            distance = float(self.distance_entry.get())
            calories = self.calculate_calories_burned(steps, distance)
            self.result_label.config(text=f"Calories Burned: {calories:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTrackerApp(root)
    root.mainloop()
