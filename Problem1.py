class DataStream:
    def __init__(self):
        self.last_seen = {}

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        """
        Determines if the given data string should be printed at the provided timestamp.
        """
        if data_string not in self.last_seen or timestamp >= self.last_seen[data_string] + 5:
            self.last_seen[data_string] = timestamp
            return True
        return False

data_stream = DataStream()
output = [
    data_stream.should_output_data_str(timestamp=0, data_string="hello"),
    data_stream.should_output_data_str(timestamp=1, data_string="world"),
    data_stream.should_output_data_str(timestamp=6, data_string="hello"),
    data_stream.should_output_data_str(timestamp=7, data_string="hello"),
    data_stream.should_output_data_str(timestamp=8, data_string="world")
]
print(output)
