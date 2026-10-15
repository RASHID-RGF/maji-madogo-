"""Helpers for the tractor field and trip logging exercises."""


def reverse_list(values=None):
    """Return a reversed copy of the input list."""
    if values is None:
        return []
    try:
        return list(reversed(list(values)))
    except TypeError:
        return []


def tractor_movement_standard(field=None):
    """Traverse the field in standard snake order."""
    if not field:
        return []

    path = []
    for row_index, row in enumerate(field):
        if not row:
            continue
        if row_index % 2 == 0:
            path.extend(row)
        else:
            path.extend(reversed(row))
    return path


def tractor_movement_realistic(field=None, start="right"):
    """Traverse the field in alternating direction from the chosen start side."""
    if not field:
        return []

    start_side = str(start).lower() if start is not None else "right"
    if start_side not in {"left", "right"}:
        start_side = "right"

    path = []
    for row_index, row in enumerate(field):
        if not row:
            continue
        if start_side == "right":
            if row_index % 2 == 0:
                path.extend(row)
            else:
                path.extend(reverse_list(row))
        else:
            if row_index % 2 == 0:
                path.extend(reverse_list(row))
            else:
                path.extend(row)
    return path


def field_summary(field=None):
    """Return (rows, columns, irregular_flag)."""
    if not field:
        return (0, 0, False)

    rows = len(field)
    cols = len(field[0]) if rows else 0
    irregular = any(len(row) != cols for row in field)
    return (rows, cols, irregular)


def total_fuel_used(*amounts):
    """Return the sum of the provided fuel amounts."""
    total = 0.0
    for amount in amounts:
        try:
            total += float(amount)
        except (TypeError, ValueError):
            continue
    return total


def log_trip(trip_id, **details):
    """Create a log line starting with the trip ID."""
    trip_id = str(trip_id)
    if not details:
        return trip_id
    detail_text = ", ".join(f"{key}={value}" for key, value in details.items())
    return f"{trip_id}: {detail_text}"


__all__ = [
    "reverse_list",
    "tractor_movement_standard",
    "tractor_movement_realistic",
    "field_summary",
    "total_fuel_used",
    "log_trip",
]