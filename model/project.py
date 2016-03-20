# -*- coding: utf-8 -*-

# Проект

class Project:

    def __init__(self, name=None, status=None, inherit_global=None, view_status=None, description=None):
        self.name = name
        self.status = status
        self.inherit_global = inherit_global
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return "%s;%s;%s;%s" % (self.name, self.status, self.view_status, self.description)

    def __eq__(self, other):
        return ((self.name == other.name or self.name is None or other.name is None) and
               (self.status == other.status or self.status is None or other.status is None) and
               (self.view_status == other.view_status or self.view_status is None or other.view_status is None) and
               (self.description == other.description or self.description is None or other.description is None))