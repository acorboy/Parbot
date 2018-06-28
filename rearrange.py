def rearrange(pred_class, schema):
    final_labels = [None]*len(schema)
    for k in range(0, len(pred_class)):
        label = pred_class[k]
        try:
            i = schema.index(label)
            final_labels[i] = label
            schema[i] = None
        except:
            final_labels[k] = None
    return final_labels