#  Copyright (c). 2023 - All rights reserved.
#  Created by [Shaniz Shehreen] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Shaniz Shehreen, 400174897 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

#  Copyright (c). 2023 - All rights reserved.
#  Created by [Shaniz Shehreen] for PROCTECH 4IT3/SEP 6IT3.
#
#  SoA Notice: I Shaniz Shehreen, 400174897 certify that this material is my original work.
#  I certify that no other person's work has been used without due acknowledgement.
#  I have also not made my work available to anyone else without their due acknowledgement.

from django.shortcuts import render


def index(request):
    data = ""
    context = {
        'data': data
    }
    return render(request, 'index.html', context)
