#!/usr/bin/env python3
# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   ft_data_stream.py                                   :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/03/06 18:17:47 by mtaheri            #+#    #+#             #
#   Updated: 2026/03/08 11:00:42 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

from typing import Generator
# import time


players = ["mtaheri", "ybarut", "aldinc", "miskirik", "root"]
projects = ["libft", "printf", "get_next_line", "push_sawap"]


def event_stream(num_events: int) -> Generator[dict, None, None]:
    for index in range(num_events):
        player = players[index % len(players)]
        level = (index * 7) % 20 + 1
        event_type = (
            "leveled up"
            if (index + 1) % 10 == 0
            else projects[index % len(projects)]
        )
        yield {
            "event_id": index + 1,
            "player": player,
            "level": level,
            "event_type": event_type,
        }


def fibonacci_generator(count: int) -> Generator[int, None, None]:
    first = 0
    second = 1
    for _ in range(count):
        yield first
        first, second = second, first + second


def prime_generator(count: int) -> Generator[int, None, None]:
    found = 0
    candidate = 2
    while found < count:
        if is_prime(candidate):
            yield candidate
            found += 1
        candidate += 1


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def generator_to_comma(values: Generator[int, None, None]) -> str:
    result = ""
    for value in values:
        if result:
            result += ", "
        result += f"{value}"
    return result


def main() -> None:
    print("=== Game Data Stream Processor ===")
    num_events = 1000
    print(f"\nProcessing {num_events} 42 events...\n")
#    start_time = time.time()

    total_events = 0
    high_level_count = 0
    levelup_count = 0

    for event in event_stream(num_events):
        total_events += 1
        if total_events <= 3:
            print(
                f"Event {event['event_id']}: Player {event['player']} "
                f"(level {event['level']}) done {event['event_type']}"
            )
        if event["level"] >= 10:
            high_level_count += 1
        if event["event_type"] == "leveled up":
            levelup_count += 1

    print("...\n")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Level-up events: {levelup_count}")
    print("\nMemory usage: Constant (streaming)")
#    processing_time = time.time() - start_time
#    print(f"Processing time: {processing_time:.3f} seconds")

    print("\n=== Generator Demonstration ===")
    fibonacci_values = generator_to_comma(fibonacci_generator(10))
    print(f"Fibonacci sequence (first 10): {fibonacci_values}")
    prime_values = generator_to_comma(prime_generator(5))
    print(f"Prime numbers (first 5): {prime_values}")

    print("\n=== Memory Efficiency Comparison ===")
    print("Method 1: store everything (list)")
#    list_start = time.time()
    all_events = list(event_stream(num_events))
#    list_time = time.time() - list_start
    print(f"- Events kept in RAM: {len(all_events)}")
#    print(f"- Time: {list_time:.6f} seconds")
    print("- Memory pattern: grows with data size")

    print("\nMethod 2: stream everything (generator)")
#    stream_start = time.time()
    stream = event_stream(num_events)
    first_event = next(stream)
    stream_count = 1
    for _ in stream:
        stream_count += 1
#    stream_time = time.time() - stream_start
    print(f"- Events processed: {stream_count}")
#    print(f"- Time: {stream_time:.6f} seconds")
    print("- Events kept in RAM at once: 1")
    print(f"- First streamed event id (via next): {first_event['event_id']}")


if __name__ == "__main__":
    main()
