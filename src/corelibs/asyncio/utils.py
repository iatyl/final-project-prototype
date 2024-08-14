def sync_all_of(model, **filter_conditions):
    q = model.objects
    for k, v in filter_conditions.items():
        q = q.filter(**{k: v})
    return list(q.all())
