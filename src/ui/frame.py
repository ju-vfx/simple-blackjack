from settings.settings import UI_WIDTH, UI_HEIGHT
import os

class Frame:
    def __init__(self):
        self.width = UI_WIDTH
        self.height = UI_HEIGHT
        self.frame = None
        self.clear_frame()
        self.prev_frame = self.frame

    def clear_frame(self):
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
        self.frame = frame
    
    def store_frame(self):
        self.prev_frame = self.frame

    def restore_frame(self):
        self.frame = self.prev_frame
    
    def draw_frame(self):
        os.system('clear')
        frame_string = "\r"
        for row in range(self.height):
            for col in range(self.width):
                frame_string += self.frame[row][col]
            if row < self.height:
                frame_string += "\n"
        print(frame_string)


    def insert_element(self, x: int = 0, y: int = 0, text: str = None):
        lines = text.splitlines()
        if lines[0] == "":
            del lines[0]
        width = max([len(line) for line in lines])
        height = len(lines)
        lines = [f"{line: <{width}}" for line in lines]

        for row in range(height):
            for col in range(width):
                if row + y >= self.height or row + y < 0 or col + x >= self.width or col + x < 0:
                    continue
                self.frame[row + y][col + x] = lines[row][col]
