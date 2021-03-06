from datetime import datetime
import json as _json
from flask import current_app

__all__ = (
    "json",
    "render_bool",
    "render_datetime",
    "render_date",
    "render_time",
    "length",
    "dt_from_epoch",
)


def json(obj):
    """Format obj as json string."""
    return _json.dumps(obj, default=str)


def length(obj):
    """Template filter wrapper for len"""
    return len(obj)


def render_bool(val):
    """Render a boolean as checkmark or cross icon."""
    return f"<i class=\"fas {'fa-check-circle text-success' if val else 'fa-times-circle text-danger'}\"></i>"


def render_datetime(dt):
    """Render a datetime to a standardized format."""
    return f"{render_date(dt)} {render_time(dt)}"


def render_time(dt):
    return dt.strftime(current_app.config["TIME_FORMAT"]) if dt is not None else "-"


def render_date(dt):
    return dt.strftime(current_app.config["DATE_FORMAT"]) if dt is not None else "-"


def dt_from_epoch(epoch):
    if not isinstance(epoch, datetime):
        return datetime.fromtimestamp(int(epoch))
    else:
        return epoch
