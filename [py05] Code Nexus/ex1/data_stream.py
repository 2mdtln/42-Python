# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   data_stream.py                                      :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/25 23:17:42 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/26 13:59:45 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


def ft_len(data: str) -> int:
    count = 0
    for _ in data:
        count += 1
    return count


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


def ft_sum(data: Any) -> Any:
    try:
        total = 0
        for x in data:
            total += x
        return total
    except TypeError:
        return None


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id: str = stream_id
        self.processed_count: int = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str: ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id, "processed": self.processed_count}


class SensorStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Sensor analysis: 0 readings processed"

        self.processed_count += ft_len(data_batch)
        temps = [float(ft_split(str(item), ":")[1])
                 for item in data_batch if "temp" in str(item)]
        avg_temp = ft_sum(temps) / ft_len(temps) if temps else 0
        return (f"Sensor analysis: {ft_len(data_batch)} readings processed, "
                f"avg temp: {avg_temp}°C")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Sensor"
        return stats


class TransactionStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Transaction analysis: 0 operations"
        self.processed_count += ft_len(data_batch)
        buy_total = 0
        sell_total = 0
        for item in data_batch:
            item_str = str(item)
            if "buy" in item_str:
                try:
                    amount = float(ft_split(str(item), ":")[1])
                    buy_total += amount
                except (ValueError, IndexError):
                    pass
            elif "sell" in item_str:
                try:
                    amount = float(ft_split(str(item), ":")[1])
                    sell_total += amount
                except (ValueError, IndexError):
                    pass
        net_flow = buy_total - sell_total
        return (f"Transaction analysis: {ft_len(data_batch)} operations, "
                f"net flow: "
                f"{'+' if net_flow >= 0 else ''}{int(net_flow)} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Transaction"
        return stats


class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            return "Event analysis: 0 events"
        self.processed_count += ft_len(data_batch)
        error_count = 0
        for item in data_batch:
            if "error" in str(item):
                error_count += 1
        return (f"Event analysis: {ft_len(data_batch)} events, "
                f"{error_count} error detected" if error_count == 1 else
                f"Event analysis: {ft_len(data_batch)} events, "
                f"{error_count} errors detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["type"] = "Event"
        return stats


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams += [stream]

    def process_all(self, batches: List[List[Any]]) -> None:
        i = 0
        while i < ft_len(self.streams):
            stream = self.streams[i]
            if i < ft_len(batches):
                batch = batches[i]
                stream.process_batch(batch)
                stream_type = stream.get_stats()['type']
                if stream_type == "Sensor":
                    suffix = "readings processed"
                elif stream_type == "Event":
                    suffix = "events processed"
                else:
                    suffix = "operations processed"
                print(f"- {stream_type} data: {ft_len(batch)} {suffix}")
            i += 1

    def filter_all(self, batches: List[List[Any]], criteria: str) -> None:
        parts = []
        i = 0
        while i < ft_len(self.streams):
            stream = self.streams[i]
            if i < ft_len(batches):
                batch = batches[i]
                filtered = stream.filter_data(batch, criteria)
                if ft_len(filtered) > 0:
                    stream_type = stream.get_stats()['type']
                    if stream_type == "Sensor":
                        parts += [f"{ft_len(filtered)} critical sensor alerts"]
                    elif stream_type == "Transaction":
                        parts += [f"{ft_len(filtered)} large transaction"]
            i += 1
        if parts:
            result = ""
            i = 0
            while i < ft_len(parts):
                result += parts[i]
                if i < ft_len(parts) - 1:
                    result += ", "
                i += 1
            print("Filtered results: " + result)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    sensor_stream = SensorStream("SENSOR_001")
    print(f"Stream ID: {sensor_stream.stream_id}, Type: Environmental Data")
    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_data}")
    result = sensor_stream.process_batch(sensor_data)
    print(result)

    print("\nInitializing Transaction Stream...")
    transaction_stream = TransactionStream("TRANS_001")
    print(f"Stream ID: {transaction_stream.stream_id}, Type: Financial Data")
    trans_data = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {trans_data}")
    result = transaction_stream.process_batch(trans_data)
    print(result)

    print("\nInitializing Event Stream...")
    event_stream = EventStream("EVENT_001")
    print(f"Stream ID: {event_stream.stream_id}, Type: System Events")
    event_data = ["login", "error", "logout"]
    print(f"Processing event batch: {event_data}")
    result = event_stream.process_batch(event_data)
    print(result)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    processor.add_stream(sensor_stream)
    processor.add_stream(transaction_stream)
    processor.add_stream(event_stream)

    print("Batch 1 Results:")
    processor.process_all([["temp:20.1", "humidity:60"],
                           ["buy:50", "sell:75", "buy:25", "sell:100"],
                           ["login", "logout", "error"]])

    print("\nStream filtering active: High-priority data only")
    processor.filter_all([["critical:25.5", "critical:70"],
                          ["buy:500critical", "sell:600"],
                          ["error", "critical"]],
                         "critical")

    print("\nAll streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
