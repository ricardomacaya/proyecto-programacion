# Import general
import sys
import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio, GObject

# Esta clase es de tipo dialogo, por lo que funciona parecido, no igual a la de
#window, suando sus propios metodos
class VentanaGrafico(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(title="Simulación", transient_for=parent)
        self.set_default_size(width=int(1366 / 2), height=int(768 / 2))

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.box.set_homogeneous(homogeneous=True)
        self.set_child(child=self.box)

        image = Gtk.Image.new_from_file('gra.png')
        self.set_child(image)


        
