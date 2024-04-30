import tkinter as tk

class Speedometer(tk.Canvas):
    def _init_(self, master, *args, **kwargs):
        super()._init_(master, *args, **kwargs)
        self.configure(width=200, height=200)
        self.speed_label = tk.Label(master, text="0", font=("Helvetica", 20))
        self.speed_label.pack()
        self.draw_speedometer()

    def draw_speedometer(self):
        center_x = self.winfo_width() / 2
        center_y = self.winfo_height() / 2
        radius = min(center_x, center_y) - 10

        # Draw the speedometer circle
        self.create_oval(center_x - radius, center_y - radius,
                         center_x + radius, center_y + radius,
                         outline="black", width=2)

        # Draw the needle
        self.create_line(center_x, center_y, center_x, center_y - radius,
                         width=3, fill="red", tags="needle")

    def update_speed(self, speed):
        self.speed_label.config(text=str(speed))
        center_x = self.winfo_width() / 2
        center_y = self.winfo_height() / 2
        radius = min(center_x, center_y) - 10

        angle = speed / 100 * 180  # Assuming speed range from 0 to 100

        # Rotate the needle
        self.delete("needle")
        self.create_line(center_x, center_y, center_x + radius * sin(angle),
                         center_y - radius * cos(angle), width=3, fill="red", tags="needle")

# Create the main window
root = tk.Tk()
root.title("Speedometer")

# Create a Speedometer widget
speedometer = Speedometer(root)
speedometer.pack()

# Update the speed (for testing purposes)
speedometer.update_speed(75)

# Start the GUI event loop
root.mainloop()