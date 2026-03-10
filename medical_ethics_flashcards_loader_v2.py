import json
import random
import tkinter as tk
import math
from pathlib import Path

BG = "#07090d"
CARD_BG = "#000000"
CARD_INNER = "#000000"
TEXT = "#ffffff"
MUTED = "#aab4c3"
ACCENT = "#4db6ff"
BORDER = "#000000"
BUTTON = "#141a22"
BUTTON_ACTIVE = "#1d2631"
EASY_COLOR = "#1a3a24"
MEDIUM_COLOR = "#4a3f16"
HARD_COLOR = "#4a2416"

CHAPTER_ORDER = [
    "Foundation",
    "Informed consent",
    "Children and medical decision-making",
    "Human Experimentation",
    "Physician-Assisted Death",
    "Reproductive Ethics and Family Formation",
    "Medical tourism",
    "Psychiatry, Mental illness, and Paternalism",
    "Military Medicine",
    "Pandemic Ethics, Quarantine, and Biosecurity",
    "Genetics, biobanks, and the right not to know",
    "AI and Brain-computer Interfaces",
    "Future-Oriented Medicine",
    "Patients as Art and Diagnostic Observation",
]

ALL_CHAPTERS = "All Chapters"
ALL_DIFFICULTIES = "All"
JSON_FILE = "medical_ethics_1400_cards.json"

def load_flashcards():
    here = Path(__file__).resolve().parent
    path = here / JSON_FILE
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

FLASHCARDS = load_flashcards()

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Ethics Flashcards")
        self.root.geometry("1280x800")
        self.root.minsize(1000, 700)
        self.root.configure(bg=BG)

        self.chapter_var = tk.StringVar(value=CHAPTER_ORDER[0])
        self.difficulty_var = tk.StringVar(value=ALL_DIFFICULTIES)
        self.side_var = tk.StringVar(value="Front")
        self.progress_var = tk.StringVar(value="Card 0 of 0")
        self.status_var = tk.StringVar(value="Choose a chapter and press Start / Restart.")
        self.deck_info_var = tk.StringVar(value="")

        self.cards = []
        self.index = 0
        self.showing_back = False
        self.animating = False
        self.drag_start_x = None
        self.drag_start_y = None
        self.is_dragging = False
        self.drag_threshold = 50

        self.build_ui()

    def make_button(self, parent, text, command, width=14, bg=None):
        return tk.Button(
            parent,
            text=text,
            command=command,
            width=width,
            bg=bg or BUTTON,
            fg=TEXT,
            activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT,
            relief="flat",
            bd=0,
            padx=10,
            pady=10,
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )

    def build_ui(self):
        top = tk.Frame(self.root, bg=BG)
        top.pack(fill="x", padx=16, pady=16)

        left = tk.Frame(top, bg=BG)
        left.pack(side="left", anchor="nw")

        tk.Label(left, text="Chapter", bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(anchor="w", pady=(0, 6))

        options = [ALL_CHAPTERS] + CHAPTER_ORDER
        self.chapter_menu = tk.OptionMenu(left, self.chapter_var, *options)
        self.chapter_menu.config(
            bg=BUTTON, fg=TEXT, activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT, highlightthickness=1,
            highlightbackground=BORDER, font=("Segoe UI", 11), width=42
        )
        self.chapter_menu["menu"].config(
            bg=BUTTON, fg=TEXT, activebackground=BUTTON_ACTIVE,
            activeforeground=TEXT, font=("Segoe UI", 10)
        )
        self.chapter_menu.pack(anchor="w")

        controls = tk.Frame(top, bg=BG)
        controls.pack(side="right", anchor="ne")

        row1 = tk.Frame(controls, bg=BG)
        row1.pack(anchor="e")
        self.make_button(row1, "Start / Restart", self.start_session).pack(side="left", padx=4)
        self.make_button(row1, "Shuffle Again", self.shuffle_again).pack(side="left", padx=4)
        self.make_button(row1, "Random Card", self.random_card).pack(side="left", padx=4)

        row2 = tk.Frame(controls, bg=BG)
        row2.pack(anchor="e", pady=(10, 0))
        self.make_button(row2, "Previous", self.previous_card).pack(side="left", padx=4)
        self.make_button(row2, "Next", self.next_card).pack(side="left", padx=4)

        difficulty_bar = tk.Frame(self.root, bg=BG)
        difficulty_bar.pack(fill="x", padx=16, pady=(0, 10))

        tk.Label(difficulty_bar, text="Difficulty", bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(side="left", padx=(0, 10))
        self.make_button(difficulty_bar, "All", lambda: self.set_difficulty(ALL_DIFFICULTIES), width=8).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Easy", lambda: self.set_difficulty("Easy"), width=8, bg=EASY_COLOR).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Medium", lambda: self.set_difficulty("Medium"), width=8, bg=MEDIUM_COLOR).pack(side="left", padx=4)
        self.make_button(difficulty_bar, "Hard", lambda: self.set_difficulty("Hard"), width=8, bg=HARD_COLOR).pack(side="left", padx=4)

        tk.Label(difficulty_bar, textvariable=self.deck_info_var, bg=BG, fg=MUTED, font=("Segoe UI", 10)).pack(side="right")

        info = tk.Frame(self.root, bg=BG)
        info.pack(fill="x", padx=16, pady=(0, 10))

        tk.Label(info, textvariable=self.side_var, bg=BG, fg=ACCENT, font=("Segoe UI", 11, "bold")).pack(side="left")
        tk.Label(info, text="   ", bg=BG, fg=TEXT).pack(side="left")
        tk.Label(info, textvariable=self.progress_var, bg=BG, fg=TEXT, font=("Segoe UI", 11, "bold")).pack(side="left")
        tk.Label(info, text="   ", bg=BG, fg=TEXT).pack(side="left")
        tk.Label(info, textvariable=self.status_var, bg=BG, fg=MUTED, font=("Segoe UI", 11)).pack(side="left")

        self.canvas = tk.Canvas(self.root, bg=BG, highlightthickness=0, bd=0)
        self.canvas.pack(fill="both", expand=True, padx=16, pady=(0, 16))
        self.canvas.bind("<Configure>", self.on_canvas_resize)
        self.canvas.bind("<Button-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        self.root.bind("<Left>", lambda e: self.previous_card())
        self.root.bind("<Right>", lambda e: self.next_card())
        self.root.bind_all("<space>", lambda e: self.flip_card())
        self.root.bind("<Return>", lambda e: self.flip_card())

        self.card_bounds = None
        self.card_text = None
        self.draw_card(1.0, 0.0, 0)

    def set_difficulty(self, value):
        self.difficulty_var.set(value)
        self.start_session()

    def get_cards_for_selection(self):
        selected_chapter = self.chapter_var.get()
        selected_difficulty = self.difficulty_var.get()

        base_cards = []
        if selected_chapter == ALL_CHAPTERS:
            for chapter in CHAPTER_ORDER:
                for card in FLASHCARDS[chapter]:
                    base_cards.append({
                        "chapter": chapter,
                        "difficulty": card["difficulty"],
                        "question": card["question"],
                        "answer": card["answer"],
                    })
        else:
            for card in FLASHCARDS[selected_chapter]:
                base_cards.append({
                    "chapter": selected_chapter,
                    "difficulty": card["difficulty"],
                    "question": card["question"],
                    "answer": card["answer"],
                })

        if selected_difficulty != ALL_DIFFICULTIES:
            base_cards = [c for c in base_cards if c["difficulty"] == selected_difficulty]

        return base_cards

    def current_card_text(self):
        if not self.cards:
            return "No cards loaded for this chapter/difficulty filter."
        card = self.cards[self.index]
        return card["answer"] if self.showing_back else card["question"]

    def update_labels(self):
        if not self.cards:
            self.side_var.set("Front")
            self.progress_var.set("Card 0 of 0")
            self.status_var.set("No cards in this filter.")
            self.deck_info_var.set("0 cards loaded")
            return

        card = self.cards[self.index]
        chapter = card["chapter"]
        difficulty = card["difficulty"]
        self.progress_var.set(f"Card {self.index + 1} of {len(self.cards)}")
        self.status_var.set(f"Chapter: {chapter} | Difficulty: {difficulty}")

        if self.chapter_var.get() == ALL_CHAPTERS:
            self.deck_info_var.set(f"Using all topics | {len(CHAPTER_ORDER)} chapters | {len(self.cards)} cards")
        else:
            self.deck_info_var.set(f"{len(self.cards)} cards in this selection")

        self.side_var.set("Back" if self.showing_back else "Front")

    def on_canvas_resize(self, event=None):
        self.draw_card(1.0, 0.0, 0)

    def on_mouse_down(self, event):
        if not self.cards or self.animating:
            return
        if self.card_bounds:
            x1, y1, x2, y2 = self.card_bounds
            padding = 10
            if (x1 - padding <= event.x <= x2 + padding and y1 - padding <= event.y <= y2 + padding):
                self.drag_start_x = event.x
                self.drag_start_y = event.y
                self.is_dragging = True

    def on_mouse_drag(self, event):
        if not self.is_dragging or not self.cards or self.animating:
            return
        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y
        if abs(dx) > abs(dy) and abs(dx) > 10:
            max_offset = 200
            x_offset = max(-max_offset, min(max_offset, dx))
            self.draw_card(1.0, 0.0, x_offset)

    def on_mouse_up(self, event):
        if not self.is_dragging:
            if self.card_bounds:
                x1, y1, x2, y2 = self.card_bounds
                padding = 10
                if (x1 - padding <= event.x <= x2 + padding and y1 - padding <= event.y <= y2 + padding):
                    self.flip_card()
            return

        if not self.cards or self.animating:
            self.is_dragging = False
            self.drag_start_x = None
            self.drag_start_y = None
            return

        dx = event.x - self.drag_start_x
        dy = event.y - self.drag_start_y

        if abs(dx) > abs(dy) and abs(dx) > self.drag_threshold:
            if dx > 0:
                self.previous_card()
            else:
                self.next_card()
        else:
            self.draw_card(1.0, 0.0, 0)

        self.is_dragging = False
        self.drag_start_x = None
        self.drag_start_y = None

    def draw_card(self, scale_x=1.0, rotation=0.0, x_offset=0):
        self.canvas.delete("all")
        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()
        if w < 10 or h < 10:
            return

        card_w = int(min(980, w * 0.82))
        card_h = int(min(500, h * 0.78))
        rotation_rad = math.radians(rotation)
        perspective_scale = abs(math.cos(rotation_rad))
        scaled_w = max(12, int(card_w * scale_x * perspective_scale))

        x1 = (w - scaled_w) // 2 + x_offset
        y1 = (h - card_h) // 2
        x2 = x1 + scaled_w
        y2 = y1 + card_h
        self.card_bounds = (x1, y1, x2, y2)

        if rotation < 90.0:
            display_back = self.showing_back
        else:
            display_back = not self.showing_back

        radius = 12
        shadow_offset = 5

        shadow_x1 = x1 + shadow_offset
        shadow_y1 = y1 + shadow_offset
        shadow_x2 = x2 + shadow_offset
        shadow_y2 = y2 + shadow_offset

        self.canvas.create_rectangle(shadow_x1 + radius, shadow_y1, shadow_x2 - radius, shadow_y1 + radius, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_rectangle(shadow_x1, shadow_y1 + radius, shadow_x2, shadow_y2 - radius, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_rectangle(shadow_x1 + radius, shadow_y2 - radius, shadow_x2 - radius, shadow_y2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x1, shadow_y1, shadow_x1 + radius * 2, shadow_y1 + radius * 2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x2 - radius * 2, shadow_y1, shadow_x2, shadow_y1 + radius * 2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x2 - radius * 2, shadow_y2 - radius * 2, shadow_x2, shadow_y2, fill="#0a0a0a", outline="", width=0)
        self.canvas.create_oval(shadow_x1, shadow_y2 - radius * 2, shadow_x1 + radius * 2, shadow_y2, fill="#0a0a0a", outline="", width=0)

        self.canvas.create_rectangle(x1 + radius, y1, x2 - radius, y1 + radius, fill=CARD_BG, outline="", width=0)
        self.canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=CARD_BG, outline="", width=0)
        self.canvas.create_rectangle(x1 + radius, y2 - radius, x2 - radius, y2, fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x1, y1, x1 + radius * 2, y1 + radius * 2, fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x2 - radius * 2, y1, x2, y1 + radius * 2, fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x2 - radius * 2, y2 - radius * 2, x2, y2, fill=CARD_BG, outline="", width=0)
        self.canvas.create_oval(x1, y2 - radius * 2, x1 + radius * 2, y2, fill=CARD_BG, outline="", width=0)

        self.canvas.create_rectangle(x1, y1, x2, y2, fill="", outline="", width=0, tags="card_clickable")
        self.canvas.tag_bind("card_clickable", "<Button-1>", lambda e: self.flip_card())

        text_visible = perspective_scale > 0.25
        text_center_x = w // 2
        text_center_y = h // 2

        if text_visible:
            card_label_x = text_center_x - card_w // 2 + 30
            card_label_y = text_center_y - card_h // 2 + 25

            card_number_text = "Card"
            if self.cards and len(self.cards) > 0:
                card_number_text = f"Card {self.index + 1} of {len(self.cards)}"

            self.canvas.create_text(card_label_x, card_label_y, text=card_number_text, fill=TEXT, font=("Segoe UI", 14, "normal"), anchor="nw")

            self.card_text = tk.Text(
                self.canvas, wrap="word", bg=CARD_BG, fg=TEXT, insertbackground=TEXT,
                relief="flat", bd=0, font=("Segoe UI", 20), padx=30, pady=30
            )
            if display_back:
                card = self.cards[self.index] if self.cards and self.index < len(self.cards) else None
                text_content = card["answer"] if card else "No cards loaded."
            else:
                card = self.cards[self.index] if self.cards and self.index < len(self.cards) else None
                text_content = card["question"] if card else "No cards loaded."

            self.card_text.insert("1.0", text_content)
            self.card_text.config(state="disabled")
            self.card_text.bind("<Button-1>", lambda e: self.flip_card())

            text_w = max(50, card_w - 100)
            text_h = max(50, card_h - 150)

            self.canvas.create_window(text_center_x, text_center_y, window=self.card_text, width=text_w, height=text_h)

            chapter_name = "No Chapter"
            if self.cards and self.index < len(self.cards):
                chapter_name = self.cards[self.index].get("chapter", "No Chapter")

            chapter_x = text_center_x - card_w // 2 + 30
            chapter_y_bottom = text_center_y + card_h // 2

            self.canvas.create_text(chapter_x, chapter_y_bottom - 50, text="Chapter", fill=TEXT, font=("Segoe UI", 11, "normal"), anchor="sw")
            self.canvas.create_text(chapter_x, chapter_y_bottom - 20, text=chapter_name, fill=TEXT, font=("Segoe UI", 14, "bold"), anchor="sw")

            difficulty_text = ""
            if self.cards and self.index < len(self.cards):
                difficulty = self.cards[self.index].get("difficulty", "")
                difficulty_text = difficulty.upper() if difficulty else ""

            difficulty_x = text_center_x + card_w // 2 - 30
            difficulty_y = text_center_y + card_h // 2 - 35
            self.canvas.create_text(difficulty_x, difficulty_y, text=difficulty_text, fill=TEXT, font=("Arial", 18, "bold"), anchor="se")

            side_label = "BACK" if display_back else "FRONT"
            side_x = text_center_x
            side_y = text_center_y + card_h // 2 - 35
            self.canvas.create_text(side_x, side_y, text=side_label, fill=MUTED, font=("Segoe UI", 22, "bold"), anchor="s")

    def refresh_card_without_animation(self):
        self.update_labels()
        self.draw_card(1.0, 0.0, 0)

    def start_session(self):
        self.cards = self.get_cards_for_selection()
        random.shuffle(self.cards)
        self.index = 0
        self.showing_back = False
        self.refresh_card_without_animation()

    def shuffle_again(self):
        if not self.cards:
            self.start_session()
            return
        random.shuffle(self.cards)
        self.index = 0
        self.showing_back = False
        self.refresh_card_without_animation()

    def flip_card(self):
        if not self.cards:
            return
        self.showing_back = not self.showing_back
        self.refresh_card_without_animation()

    def next_card(self):
        if not self.cards or self.animating:
            return
        if self.index < len(self.cards) - 1:
            self.index += 1
            self.showing_back = False
            self.refresh_card_without_animation()

    def previous_card(self):
        if not self.cards or self.animating:
            return
        if self.index > 0:
            self.index -= 1
            self.showing_back = False
            self.refresh_card_without_animation()

    def random_card(self):
        if self.animating:
            return
        if not self.cards:
            self.start_session()
            return
        if len(self.cards) == 1:
            return

        old_index = self.index
        while True:
            new_index = random.randrange(len(self.cards))
            if new_index != old_index:
                break

        self.index = new_index
        self.showing_back = False
        self.refresh_card_without_animation()

def main():
    root = tk.Tk()
    FlashcardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()