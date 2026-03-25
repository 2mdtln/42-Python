# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   stream_processor.py                                 :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/24 14:13:41 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/25 23:22:44 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any, List


def ft_len(data: str) -> int:
    count = 0
    for _ in data:
        count += 1
    return count


def ft_sum(data: Any) -> Any:
    try:
        total = 0
        for x in data:
            total += x
        return total
    except TypeError:
        return None


def ft_split(data: str, delimiter: str) -> list:
    result = []
    current = ""
    i = 0
    while i < ft_len(data):
        if data[i:i+ft_len(delimiter)] == delimiter:
            result += [current]
            current = ""
            i += ft_len(delimiter)
        else:
            current += data[i]
            i += 1
    result += [current]
    return result


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str: ...

    @abstractmethod
    def validate(self, data: Any) -> bool: ...

    def format_output(self, result: str) -> str: return result


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        total = ft_sum(data)
        return (f"Processed {ft_len(data)} numeric values,"
                f" sum={total}, avg={total / ft_len(data)}")

    def validate(self, data: Any) -> bool:
        try:
            ft_sum(data)
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError
        char_count = ft_len(data)
        word_count = ft_len(ft_split(data, " "))
        return f"Processed text: {char_count} characters, {word_count} words"

    def validate(self, data: Any) -> bool:
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError
        if "ERROR" in data:
            level = "ERROR"
            prefix = "[ALERT]"
        else:
            level = "INFO"
            prefix = "[INFO]"
        return f"{prefix} {level} level detected: {ft_split(data, ": ")[1]}"

    def validate(self, data: Any) -> bool:
        try:
            return "ERROR" in data or "INFO" in data
        except AttributeError:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    processors_list: List[tuple] = [
        (NumericProcessor(), [1, 2, 3, 4, 5], "Numeric"),
        (TextProcessor(), "Hello Nexus World", "Text"),
        (LogProcessor(), "ERROR: Connection timeout", "Log")
    ]

    i = 0
    while i < ft_len(processors_list):
        processor, data, name = processors_list[i]
        print(f"\nInitializing {name} Processor...")
        print(f"Processing data: {data}")
        if processor.validate(data):
            print(f"Validation: {name} data verified")
            result = processor.process(data)
            output = processor.format_output(result)
            print(f"Output: {output}")
        i += 1

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")

    processors: List[DataProcessor] = [processors_list[1],
                                       processors_list[2],
                                       processors_list[3]]
    test_data: List[Any] = [[1, 2, 3],
                            "Hello Code",
                            "INFO: System ready"]
    i = 1
    while i <= ft_len(processors):
        processor = processors[i - 1]
        data = test_data[i - 1]
        try:
            if processor.validate(data):
                print(f"Result {i}: {processor.format_output(
                                     processor.process(data))}")
        except ValueError:
            print("Error processing data")
        i += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
