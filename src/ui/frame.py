from settings.settings import UI_WIDTH, UI_HEIGHT
import os

class Frame:
    def __init__(self):
        self.width = UI_WIDTH
        self.height = UI_HEIGHT
        self.frame = self.clear_frame()

    def clear_frame(self) -> list[list[str]]:
        frame = []
        for r in range(self.height):
            row = []
            for c in range(self.width):
                if (r == 0 and c == 0) or \
                    (r == 0 and c == self.width - 1) or \
                    (r == self.height - 1 and c == 0) or \
                    (r == self.height - 1 and c == self.width - 1):
                    row.append("X")
                elif (r == 0 or r == self.height - 1):
                    row.append("-")
                elif (c == 0 or c == self.width - 1):
                    row.append("|")
                else:
                    row.append(" ")
            frame.append(row)
        return frame
    
    def draw_frame(self):
        os.system('clear')
        frame_string = "\r"
        for row in range(self.height):
            for col in range(self.width):
                frame_string += self.frame[row][col]
            if row < self.height:
                frame_string += "\n"
        print(frame_string)

    def insert_drawable(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0, drawable: list[list] = None):
        pass

    def insert_text(self, x: int = 0, y: int = 0, text: str = None):
        for col in range(len(text)):
            self.frame[y][col + x] = text[col]
