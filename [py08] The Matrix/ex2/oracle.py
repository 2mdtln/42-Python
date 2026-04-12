# *************************************************************************** #
#                                                                             #
#                                                         :::      ::::::::   #
#   oracle.py                                           :+:      :+:    :+:   #
#                                                     +:+ +:+         +:+     #
#   By: mtaheri <mtaheri@student.42istanbul.com.tr> +#+  +:+       +#+        #
#                                                 +#+#+#+#+#+   +#+           #
#   Created: 2026/04/12 13:16:43 by mtaheri            #+#    #+#             #
#   Updated: 2026/04/12 13:46:14 by mtaheri           ###   ########.fr       #
#                                                                             #
# *************************************************************************** #

import os
import sys
from dotenv import load_dotenv


def load_config() -> tuple[dict, bool]:
    load = load_dotenv()
    return {
        "MODE":         os.getenv("MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", ""),
        "API_KEY":      os.getenv("API_KEY", ""),
        "LOG_LEVEL":    os.getenv("LOG_LEVEL", "DEBUG"),
        "ENDPOINT":     os.getenv("ENDPOINT", ""),
    }, load


def display_config(config: dict) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config["MODE"]}")

    if config["DATABASE_URL"]:
        label = ("Connected to local instance"
                 if config["MODE"] == "development"
                 else "Connected to production cluster")
        print(f"Database: {label}")
    else:
        print("Database: [WARNING] DATABASE_URL not set")

    if config["API_KEY"]:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] API_KEY not set")

    print(f"Log Level: {config['LOG_LEVEL']}")

    if config["ENDPOINT"]:
        print("Network: Online")
    else:
        print("Network: [WARNING] ENDPOINT not set")

    if config["MODE"] == "production":
        missing = [k for k in ["DATABASE_URL", "API_KEY", "ENDPOINT"]
                   if not config[k]]
        if missing:
            print(f"\n[ERROR] Production requires: {', '.join(missing)}",
                  file=sys.stderr)
            sys.exit(1)


def main() -> None:
    config, env_loaded = load_config()
    if not env_loaded:
        print("[WARNING] No .env file found... cp .env.example .env")
        sys.exit(1)
    display_config(config)


if __name__ == "__main__":
    main()
