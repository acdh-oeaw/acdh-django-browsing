from django import template

register = template.Library()


@register.simple_tag
def windowed_page_range(page_range, current_page, window=1):
    """
    Returns a list representing windowed pagination.
    Includes first page, last page, current page ±window pages,
    and None as a sentinel for ellipsis gaps.
    """
    page_range = list(page_range)
    if not page_range:
        return []

    first = page_range[0]
    last = page_range[-1]

    near_start = set(range(first, first + 1))
    near_end = set(range(last, last + 1))
    near_current = set(
        range(max(first, current_page - window), min(last, current_page + window) + 1)
    )

    pages_to_show = sorted(near_start | near_end | near_current)

    result = []
    prev = None
    for p in pages_to_show:
        if prev is not None and p - prev > 1:
            result.append(None)  # ellipsis sentinel
        result.append(p)
        prev = p

    return result
