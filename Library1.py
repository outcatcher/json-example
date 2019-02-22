# -*- coding=utf-8 -*-
import os

from jinja2 import Environment, FileSystemLoader

ROBOT_LIBRARY_SCOPE = "TEST SUITE"

ENV = Environment(loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates"))


def json_template1(name, token, client_id, client_secret, group_id, sku_list=()):
    """Generate file from template"""
    template = ENV.get_template("sample.json")
    json = template.render(name=name, token=token, client_id=client_id,
                           client_secret=client_secret,
                           group_id=group_id, skus=sku_list)
    return json


def get_skus(*skus):
    """Get SKU as list"""
    return [sku.split(":") for sku in skus]
