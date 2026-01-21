class Frame:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.frame = self.clear_frame()

    def clear_frame(self) -> list[list[str]]:
        frame = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append("")
            frame.append(row)
        return frame