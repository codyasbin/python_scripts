"""Rate-limited GET loop tester for an authorized private-network lab."""
# python bruteforce.py "http://192.168.18.9:3000/" --delay 0.5 --max-attempts 50 --success-status 999
from __future__ import annotations

import argparse
import ipaddress
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


def private_target(url: str) -> bool:
    """Return True only for loopback or private IP-literal targets."""
    hostname = urlsplit(url).hostname
    if not hostname:
        return False
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        return hostname.lower() == "localhost"
    return address.is_private or address.is_loopback


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Repeatedly GET a URL on an authorized lab host."
    )
    parser.add_argument("url", help="Target URL to request repeatedly")
    parser.add_argument(
        "--success-status", type=int, default=200, help="expected HTTP status (default: 200)"
    )
    parser.add_argument(
        "--contains", help="text that must appear in the successful response body"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0, help="seconds between requests (minimum: 0.2)"
    )
    parser.add_argument(
        "--max-attempts", type=int, default=100, help="request cap (maximum: 1000)"
    )
    parser.add_argument("--timeout", type=float, default=5.0, help="request timeout in seconds")
    parser.add_argument("--dry-run", action="store_true", help="show URL without sending requests")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not private_target(args.url):
        print("error: only localhost or private IP-literal targets are allowed", file=sys.stderr)
        return 2
    if not 1 <= args.max_attempts <= 1000:
        print("error: --max-attempts must be between 1 and 1000", file=sys.stderr)
        return 2
    if args.delay < 0.2:
        print("error: --delay must be at least 0.2 seconds", file=sys.stderr)
        return 2
    if args.timeout <= 0:
        print("error: --timeout must be positive", file=sys.stderr)
        return 2

    for attempt in range(1, args.max_attempts + 1):
        if args.dry_run:
            print(f"[{attempt}] {args.url}")
            continue

        request = Request(args.url, headers={"User-Agent": "Authorized-Lab-GET-Tester/1.0"})
        try:
            with urlopen(request, timeout=args.timeout) as response:
                status = response.status
                body = response.read(1_000_000).decode("utf-8", errors="replace")
        except HTTPError as exc:
            status = exc.code
            body = exc.read(1_000_000).decode("utf-8", errors="replace")
        except URLError as exc:
            print(f"[{attempt}] request failed: {exc.reason}")
            time.sleep(args.delay)
            continue

        status_matches = status == args.success_status
        text_matches = args.contains is None or args.contains in body
        print(f"[{attempt}] status={status}")
        if status_matches and text_matches:
            print(f"MATCH found on attempt {attempt}")
            return 0
        time.sleep(args.delay)

    print("No match found within the attempt cap.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())