# window.py
#
# Copyright 2020 ceo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk

from ..utils.dialogs import warning_dialog
from ..utils.plots import Plots


@Gtk.Template(resource_path='/org/example/App/ui/plot_window.ui')
class PlotWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'PlotWindow'

    limsupEntry = Gtk.Template.Child()
    liminfEntry = Gtk.Template.Child()
    colorButton1 = Gtk.Template.Child()
    colorButton2 = Gtk.Template.Child()

    def __init__(self, f1, f2, **kwargs):
        super().__init__(**kwargs)

        self.f1 = f1
        self.f2 = f2


    @Gtk.Template.Callback()
    def plot(self, widget):

        try:
            limsup = float(self.limsupEntry.get_text())
            liminf = float(self.liminfEntry.get_text())
        except ValueError:
            warning_dialog(self, 'O intervalo deve ser numérico')
            return


        color1 = self.colorButton1.get_rgba()
        color2 = self.colorButton2.get_rgba()

        color1 = (color1.red, color1.green, color1.blue)
        color2 = (color2.red, color2.green, color2.blue)

        Plots.n_subplots('Expressão Original e Resultado',
                            (liminf, limsup),
                            (self.f1, self.f2),
                            ('Original', 'Resultado'),
                            (color1, color2))
        self.close()

    @Gtk.Template.Callback()
    def cancel_plot(self, widget):
        self.close()
