import tkinter as tk
from tkinter import messagebox
from functools import partial

class ToolTip:
    """
    Create a tooltip for a given widget.
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text:
            return
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)  # Remove window decorations
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, justify="left",
                         background="#ffffe0", relief="solid", borderwidth=1,
                         font=("Helvetica", "10", "normal"))
        label.pack(ipadx=1)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

class DSCRCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DSCR Loan Calculator")
        self.geometry("900x800")
        self.configure(bg="#f0f0f0")
        self.resizable(True, True)

        # Define fonts and colors
        self.font_title = ("Helvetica", 20, "bold")
        self.font_labels = ("Helvetica", 12)
        self.font_results = ("Helvetica", 12, "bold")
        self.bg_color = "#f0f0f0"

        # Initialize variables
        self.loan_type_var = tk.StringVar(value="Amortizing")

        # Setup UI
        self.create_widgets()

    def create_widgets(self):
        # Title
        label_title = tk.Label(self, text="Debt Service Coverage Ratio (DSCR) Calculator",
                               bg=self.bg_color, font=self.font_title, wraplength=880, justify="center")
        label_title.pack(pady=20)

        # Scrollable Frame
        container = tk.Frame(self, bg=self.bg_color)
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg=self.bg_color)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        self.scrollable_frame = tk.Frame(canvas, bg=self.bg_color)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Financial Inputs
        self.create_financial_inputs_section()

        # Loan Details Inputs
        self.create_loan_details_section()

        # Loan Type Selection
        self.create_loan_type_section()

        # Calculate Button
        button_calculate = tk.Button(self.scrollable_frame, text="Calculate",
                                     command=self.calculate_dscr, bg="#4CAF50", fg="white",
                                     font=self.font_labels, width=20, height=2)
        button_calculate.pack(pady=20)

        # Results Display
        self.create_results_section()

    def create_financial_inputs_section(self):
        frame_financials = tk.LabelFrame(self.scrollable_frame, text="Financial Inputs", bg=self.bg_color,
                                         font=self.font_labels, padx=10, pady=10)
        frame_financials.pack(pady=10, padx=20, fill="x")

        inputs = [
            {"label": "Gross Income ($):", "row": 0, "tooltip": "Total income generated from the property before expenses."},
            {"label": "Operational Expenses ($):", "row": 1, "tooltip": "Costs associated with operating the property (e.g., maintenance, utilities)."},
            {"label": "Taxes ($):", "row": 2, "tooltip": "Annual property taxes."},
            {"label": "HOA Fees ($):", "row": 3, "tooltip": "Homeowners Association fees, if applicable."},
            {"label": "Insurance ($):", "row": 4, "tooltip": "Property insurance costs."},
        ]

        self.financial_entries = {}
        for input_field in inputs:
            label = tk.Label(frame_financials, text=input_field["label"],
                             bg=self.bg_color, font=self.font_labels, anchor="w")
            label.grid(row=input_field["row"], column=0, sticky="w", padx=10, pady=5)

            entry = tk.Entry(frame_financials, width=30)
            entry.grid(row=input_field["row"], column=1, padx=10, pady=5)
            ToolTip(entry, input_field["tooltip"])

            self.financial_entries[input_field["label"]] = entry

    def create_loan_details_section(self):
        frame_loan = tk.LabelFrame(self.scrollable_frame, text="Loan Details", bg=self.bg_color,
                                   font=self.font_labels, padx=10, pady=10)
        frame_loan.pack(pady=10, padx=20, fill="x")

        inputs = [
            {"label": "Loan Amount ($):", "row": 0, "tooltip": "Amount borrowed to purchase the property."},
            {"label": "Interest Rate (%):", "row": 1, "tooltip": "Annual interest rate of the loan."},
            {"label": "Loan Term (Years):", "row": 2, "tooltip": "Duration of the loan in years."},
            {"label": "Down Payment Percentage (%):", "row": 3, "tooltip": "Percentage of the total property price paid upfront."},
        ]

        self.loan_entries = {}
        for input_field in inputs:
            label = tk.Label(frame_loan, text=input_field["label"],
                             bg=self.bg_color, font=self.font_labels, anchor="w")
            label.grid(row=input_field["row"], column=0, sticky="w", padx=10, pady=5)

            entry = tk.Entry(frame_loan, width=30)
            entry.grid(row=input_field["row"], column=1, padx=10, pady=5)
            ToolTip(entry, input_field["tooltip"])

            self.loan_entries[input_field["label"]] = entry

    def create_loan_type_section(self):
        frame_loan_type = tk.Frame(self.scrollable_frame, bg=self.bg_color)
        frame_loan_type.pack(pady=10, padx=20, fill="x")

        label_loan_type = tk.Label(frame_loan_type, text="Loan Type:",
                                   bg=self.bg_color, font=self.font_labels, anchor="w")
        label_loan_type.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        radio_interest_only = tk.Radiobutton(frame_loan_type, text="Interest Only",
                                             variable=self.loan_type_var, value="Interest Only",
                                             bg=self.bg_color, font=self.font_labels)
        radio_interest_only.grid(row=0, column=1, sticky="w", padx=10, pady=5)
        ToolTip(radio_interest_only, "Loan payments consist only of interest.")

        radio_amortizing = tk.Radiobutton(frame_loan_type, text="Amortizing",
                                          variable=self.loan_type_var, value="Amortizing",
                                          bg=self.bg_color, font=self.font_labels)
        radio_amortizing.grid(row=0, column=2, sticky="w", padx=10, pady=5)
        ToolTip(radio_amortizing, "Loan payments include both principal and interest.")

    def create_results_section(self):
        frame_results = tk.LabelFrame(self.scrollable_frame, text="Results", bg=self.bg_color,
                                      font=self.font_labels, padx=10, pady=10)
        frame_results.pack(pady=10, padx=20, fill="x")

        results = [
            {"label": "Net Operating Income (NOI):", "row": 0},
            {"label": "Down Payment Amount:", "row": 1},
            {"label": "Total Property Price:", "row": 2},
            {"label": "Monthly Debt Service:", "row": 3},
            {"label": "Annual Debt Service:", "row": 4},
            {"label": "Debt Service Coverage Ratio (DSCR):", "row": 5},
        ]

        self.result_labels = {}
        for res in results:
            label = tk.Label(frame_results, text=res["label"],
                             bg=self.bg_color, font=self.font_labels, anchor="w")
            label.grid(row=res["row"], column=0, sticky="w", padx=10, pady=5)

            value_label = tk.Label(frame_results, text="$0.00",
                                   bg=self.bg_color, font=self.font_results, anchor="w")
            value_label.grid(row=res["row"], column=1, sticky="w", padx=10, pady=5)

            self.result_labels[res["label"]] = value_label

        # DSCR Interpretation
        self.label_interpretation = tk.Label(self.scrollable_frame, text="", bg=self.bg_color,
                                            font=self.font_labels, wraplength=880, justify="center")
        self.label_interpretation.pack(pady=10)

    def validate_inputs(self):
        try:
            # Convert and validate financial inputs
            gross_income = float(self.financial_entries["Gross Income ($):"].get())
            operational_expenses = float(self.financial_entries["Operational Expenses ($):"].get())
            taxes = float(self.financial_entries["Taxes ($):"].get())
            hoa_fees = float(self.financial_entries["HOA Fees ($):"].get())
            insurance = float(self.financial_entries["Insurance ($):"].get())

            # Convert and validate loan details
            loan_amount = float(self.loan_entries["Loan Amount ($):"].get())
            annual_interest_rate = float(self.loan_entries["Interest Rate (%):"].get())
            loan_term_years = int(self.loan_entries["Loan Term (Years):"].get())
            down_payment_percentage = float(self.loan_entries["Down Payment Percentage (%):"].get())

            # Input validation
            if gross_income < 0 or operational_expenses < 0 or taxes < 0 or hoa_fees < 0 or insurance < 0:
                raise ValueError("Income and all expenses must be non-negative.")
            if annual_interest_rate < 0:
                raise ValueError("Interest Rate cannot be negative.")
            if loan_term_years <= 0:
                raise ValueError("Loan Term must be a positive integer.")
            if not (0 <= down_payment_percentage <= 100):
                raise ValueError("Down Payment Percentage must be between 0 and 100.")
            if loan_amount < 0:
                raise ValueError("Loan Amount cannot be negative.")
            if down_payment_percentage == 100 and loan_amount != 0:
                raise ValueError("With a 100% down payment, Loan Amount must be zero.")

            return {
                "gross_income": gross_income,
                "operational_expenses": operational_expenses,
                "taxes": taxes,
                "hoa_fees": hoa_fees,
                "insurance": insurance,
                "loan_amount": loan_amount,
                "annual_interest_rate": annual_interest_rate,
                "loan_term_years": loan_term_years,
                "down_payment_percentage": down_payment_percentage
            }

        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))
            return None

    def calculate_dscr(self):
        inputs = self.validate_inputs()
        if not inputs:
            return  # Invalid inputs; error message already shown

        loan_type = self.loan_type_var.get()

        # Calculate Total Operating Expenses
        total_operating_expenses = inputs["operational_expenses"] + inputs["taxes"] + inputs["hoa_fees"] + inputs["insurance"]
        noi = inputs["gross_income"] - total_operating_expenses

        if noi < 0:
            messagebox.showerror("Calculation Error", "Net Operating Income (NOI) cannot be negative.")
            return

        # Calculate Total Property Price and Down Payment Amount
        if inputs["down_payment_percentage"] == 0:
            total_property_price = inputs["loan_amount"]
            down_payment_amount = 0
        else:
            total_property_price = inputs["loan_amount"] / (1 - inputs["down_payment_percentage"] / 100)
            down_payment_amount = total_property_price * (inputs["down_payment_percentage"] / 100)

        # Calculate Debt Service
        if loan_type == "Interest Only":
            monthly_interest_rate = inputs["annual_interest_rate"] / 100 / 12
            monthly_debt_service = inputs["loan_amount"] * monthly_interest_rate
        else:  # Amortizing
            monthly_interest_rate = inputs["annual_interest_rate"] / 100 / 12
            total_payments = inputs["loan_term_years"] * 12
            monthly_debt_service = self.calculate_pmt(monthly_interest_rate, total_payments, inputs["loan_amount"])

        annual_debt_service = monthly_debt_service * 12

        if annual_debt_service == 0:
            messagebox.showerror("Calculation Error", "Annual Debt Service cannot be zero.")
            return

        dscr = noi / annual_debt_service

        # Update Results
        self.update_results(noi, down_payment_amount, total_property_price,
                            monthly_debt_service, annual_debt_service, dscr)

    def update_results(self, noi, down_payment, property_price,
                       monthly_ds, annual_ds, dscr):
        # Update the result labels
        self.result_labels["Net Operating Income (NOI):"].config(text=f"${noi:,.2f}")
        self.result_labels["Down Payment Amount:"].config(text=f"${down_payment:,.2f}")
        self.result_labels["Total Property Price:"].config(text=f"${property_price:,.2f}")
        self.result_labels["Monthly Debt Service:"].config(text=f"${monthly_ds:,.2f}")
        self.result_labels["Annual Debt Service:"].config(text=f"${annual_ds:,.2f}")
        self.result_labels["Debt Service Coverage Ratio (DSCR):"].config(text=f"{dscr:.2f}")

        # Interpretation
        if dscr < 1:
            interpretation = "DSCR < 1: Income does not cover debt obligations."
            color = "red"
        elif dscr == 1:
            interpretation = "DSCR = 1: Income exactly covers debt obligations."
            color = "orange"
        else:
            interpretation = "DSCR > 1: Income exceeds debt obligations."
            color = "green"

        self.label_interpretation.config(text=interpretation, fg=color)

    def calculate_pmt(self, rate, nper, pv):
        """
        Calculate the monthly payment using the PMT formula.
        """
        if rate == 0:
            return pv / nper
        return pv * (rate * (1 + rate) ** nper) / ((1 + rate) ** nper - 1)

if __name__ == "__main__":
    app = DSCRCalculatorApp()
    app.mainloop()
