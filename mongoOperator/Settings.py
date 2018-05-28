# Copyright (c) 2018 Chris ter Beke
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import os


STRING_TO_BOOL_DICT = {"True", "true", "yes", "1"}


class Settings:
    
    # Custom resource (CRD) API config.
    CUSTOM_OBJECT_API_NAMESPACE = "operators.ultimaker.com"
    CUSTOM_OBJECT_API_VERSION = "v1"
    CUSTOM_OBJECT_RESOURCE_NAME = "mongo"
    
    # Kubernetes config.
    KUBERNETES_SERVICE_ADDRESS = "{}:{}".format(os.getenv("KUBERNETES_SERVICE_HOST", "http://localhost"),
                                                os.getenv("KUBERNETES_SERVICE_PORT", 8001))
    KUBERNETES_SERVICE_SKIP_TLS = os.getenv("KUBERNETES_SERVICE_SKIP_TLS", "True") in STRING_TO_BOOL_DICT
    KUBERNETES_SERVICE_DEBUG = os.getenv("KUBERNETES_SERVICE_DEBUG", "False") in STRING_TO_BOOL_DICT
    KUBERNETES_NAMESPACE = os.getenv("KUBERNETES_NAMESPACE", "default")

    # Mongo RS config.
    MONGO_RS_POD_LABELS = os.getenv("MONGO_RS_POD_LABELS", "app=mongo")
    MONGO_RS_SERVICE_NAME = os.getenv("KUBERNETES_MONGO_SERVICE_NAME")
    MONGO_RS_SERVICE_PORT = os.getenv("MONGO_RS_SERVICE_PORT", 27017)
    MONGO_RS_USERNAME = os.getenv("MONGO_RS_USERNAME", "")
    MONGO_RS_PASSWORD = os.getenv("MONGO_RS_PASSWORD", "")
    MONGO_RS_DATABASE = os.getenv("MONGO_RS_DATABASE", "local")