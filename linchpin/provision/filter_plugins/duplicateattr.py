#!/usr/bin/env python


def duplicateattr(output, attr, dattr):
    new_output = []
    for group in output:
        if attr in group:
            new_group = group
            new_group[dattr] = group[attr]
            new_output.append(new_group)
    return output


class FilterModule(object):
    ''' A filter to fix network format '''
    def filters(self):
        return {
            'duplicateattr': duplicateattr
        }
