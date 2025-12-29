
"""Simple Tic Tac Toe game built with Tkinter.

Features
- 3x3 grid of buttons
- Two players: X and O
- Winner/draw announced via message box
- Buttons disable after a move
- Restart button to reset the board
"""

import tkinter as tk
from tkinter import messagebox


class TicTacToe:
	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.root.title("Tic Tac Toe")

		self.current_player = "X"
		self.buttons: list[tk.Button] = []

		self.status_var = tk.StringVar()
		self.status_var.set("Player X's turn")

		self._build_ui()

	def _build_ui(self) -> None:
		"""Create grid buttons and controls."""
		board_frame = tk.Frame(self.root, padx=10, pady=10)
		board_frame.pack()

		for row in range(3):
			for col in range(3):
				index = row * 3 + col
				btn = tk.Button(
					board_frame,
					text="",
					font=("Helvetica", 20, "bold"),
					width=5,
					height=2,
					command=lambda idx=index: self.handle_move(idx),
				)
				btn.grid(row=row, column=col, padx=5, pady=5)
				self.buttons.append(btn)

		control_frame = tk.Frame(self.root, padx=10, pady=5)
		control_frame.pack(fill="x")

		status_label = tk.Label(control_frame, textvariable=self.status_var, anchor="w")
		status_label.pack(side="left", expand=True, fill="x")

		restart_btn = tk.Button(control_frame, text="Restart", command=self.reset_game)
		restart_btn.pack(side="right")

	def handle_move(self, index: int) -> None:
		"""Handle a player's move at the given button index."""
		button = self.buttons[index]
		if button["text"]:  # Already clicked
			return

		button.config(text=self.current_player, state="disabled")

		if self._check_winner():
			self._finish_game(f"Player {self.current_player} wins!")
			return

		if self._is_draw():
			self._finish_game("It's a draw!")
			return

		# Switch players
		self.current_player = "O" if self.current_player == "X" else "X"
		self.status_var.set(f"Player {self.current_player}'s turn")

	def _check_winner(self) -> bool:
		"""Return True if the current player has a winning combination."""
		combos = [
			(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
			(0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
			(0, 4, 8), (2, 4, 6),             # Diagonals
		]

		for a, b, c in combos:
			if (
				self.buttons[a]["text"] == self.current_player
				and self.buttons[b]["text"] == self.current_player
				and self.buttons[c]["text"] == self.current_player
			):
				return True
		return False

	def _is_draw(self) -> bool:
		"""Return True if all buttons are filled and no winner."""
		return all(button["text"] for button in self.buttons)

	def _finish_game(self, message: str) -> None:
		"""Show result, disable board, and update status."""
		for button in self.buttons:
			button.config(state="disabled")

		self.status_var.set(message)
		messagebox.showinfo("Game Over", message)

	def reset_game(self) -> None:
		"""Reset the board for a new game."""
		self.current_player = "X"
		self.status_var.set("Player X's turn")
		for button in self.buttons:
			button.config(text="", state="normal")


if __name__ == "__main__":
	root = tk.Tk()
	app = TicTacToe(root)
	root.mainloop()

