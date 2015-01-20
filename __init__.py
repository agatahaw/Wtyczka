# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Wtyczka
                                 A QGIS plugin
 This is my wtyczka
                             -------------------
        begin                : 2015-01-15
        copyright            : (C) 2015 by Agata
        email                : a.g.a.t.a1@interia.pl
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Wtyczka class from file Wtyczka.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from wtyczka import Wtyczka
    return Wtyczka(iface)
