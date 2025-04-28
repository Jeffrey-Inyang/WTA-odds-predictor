import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import filedialog, messagebox

class WTAPredictorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WTA Odds Predictor")
        self.root.geometry("500x400")
        self.model = None
        self.df = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="WTA Odds Predictor", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Load CSV", command=self.load_csv, width=20).pack(pady=5)
        tk.Button(self.root, text="Train Model", command=self.train_model, width=20).pack(pady=5)
        tk.Button(self.root, text="Predict New Odd", command=self.predict_new, width=20).pack(pady=5)
        tk.Button(self.root, text="Plot Results", command=self.plot_results, width=20).pack(pady=5)

        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack(pady=10)

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return
        try:
            self.df = pd.read_csv(file_path)
            self.df['Odd_1'] = pd.to_numeric(self.df['Odd_1'], errors='coerce')
            self.df = self.df[['Rank_1', 'Pts_1', 'Odd_1']].dropna()
            self.output_text.insert(tk.END, "CSV loaded successfully!\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV:\n{e}")

    def train_model(self):
        if self.df is None:
            messagebox.showwarning("Warning", "Please load a CSV first.")
            return
        x = self.df[['Rank_1', 'Pts_1']]
        y = self.df['Odd_1']
        self.model = LinearRegression()
        self.model.fit(x, y)
        y_pred = self.model.predict(x)
        mse = mean_squared_error(y, y_pred)

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, f"Model Trained!\n\n")
        self.output_text.insert(tk.END, f"Slope (Rank_1): {self.model.coef_[0]:.4f}\n")
        self.output_text.insert(tk.END, f"Slope (Pts_1): {self.model.coef_[1]:.4f}\n")
        self.output_text.insert(tk.END, f"Bias (Intercept): {self.model.intercept_:.4f}\n")
        self.output_text.insert(tk.END, f"MSE: {mse:.4f}\n")

    def predict_new(self):
        if self.model is None:
            messagebox.showwarning("Warning", "Please train the model first.")
            return
        try:
            rank = float(simple_input("Enter Rank_1:"))
            pts = float(simple_input("Enter Pts_1:"))
            pred = self.model.predict([[rank, pts]])
            messagebox.showinfo("Prediction", f"Predicted Odd_1: {pred[0]:.4f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")

    def plot_results(self):
        if self.model is None:
            messagebox.showwarning("Warning", "Please train the model first.")
            return
        x = self.df[['Rank_1', 'Pts_1']]
        y = self.df['Odd_1']
        y_pred = self.model.predict(x)

        plt.figure(figsize=(8,6))
        plt.scatter(y, y_pred, color='blue', alpha=0.5)
        plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red', linestyle='--')
        plt.title("Actual vs Predicted Odds", fontsize=14)
        plt.xlabel("Actual Odds", fontsize=12)
        plt.ylabel("Predicted Odds", fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.show()

def simple_input(prompt_text):
    popup = tk.Toplevel()
    popup.title("Input")

    tk.Label(popup, text=prompt_text, font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(popup)
    entry.pack(pady=5)
    result = []

    def submit():
        result.append(entry.get())
        popup.destroy()

    tk.Button(popup, text="Submit", command=submit).pack(pady=10)
    popup.grab_set()
    popup.wait_window()
    return result[0] if result else ""

if __name__ == "__main__":
    root = tk.Tk()
    app = WTAPredictorApp(root)
    root.mainloop()
