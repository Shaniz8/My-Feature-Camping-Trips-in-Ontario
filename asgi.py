"""
ASGI config for Assignment2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

#  Copyright (c). 2023 - All rights reserved.
#  Created by [Shaniz Shehreen] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Shaniz Shehreen, 400174897 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Assignment2.settings')

application = get_asgi_application()
