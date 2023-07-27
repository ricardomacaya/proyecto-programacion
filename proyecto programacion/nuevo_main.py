import gi
import pathlib
from ventanagrafico import VentanaGrafico
from nuevo_simulacion import ejecutar
import matplotlib.pyplot as plt

gi.require_version(namespace='Gtk', version='4.0')
gi.require_version(namespace='Adw', version='1')

from gi.repository import Adw, Gtk, Gio, Pango, GObject

Adw.init()

def crear_grafica(s,i,r,m,d):
        fig,ax = plt.subplots()
        x = []
        for a in range(int(d)) :
            x.append(a+1)
        sir = {"s":s,"i":i,"r":r,"m":m}
        ax.set_title("Modelo. S.I.R.m", loc = "left")
        ax.set_xlabel("Dias",fontdict = 
        {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        ax.set_ylabel("Personas",fontdict =
        {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
        ax.plot(x,sir["s"],color= "tab:blue",label ="supseptible")
        ax.plot(x,sir["i"],color= "tab:purple",label ="infectado")
        ax.plot(x,sir["r"],color= "tab:green",label ="recuperados")
        ax.plot(x,sir["m"],color= "tab:red",label ="muertos")
        ax.legend(loc = 'upper right')
        plt.savefig("gra.png")

class ExampleWindow(Gtk.ApplicationWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.set_title(title='Simulador')
        self.set_default_size(width=int(620 / 2), height=int(768 / 2))
       
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)

        menu_button_model = Gio.Menu()
        menu_button_model.append('About', 'app.about')

        menu_button = Gtk.MenuButton.new()
        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)

        self.vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.vbox1.set_homogeneous(homogeneous=True)
        self.set_child(child=self.vbox1)
        #poblacion, dias, tasa de infeccion, tasa recuperacion, tasa de muerte
        self.label = Gtk.Label()
        self.label.set_text("Bienvenidos al simulador")
        self.vbox1.append(self.label)
        self.label0 = Gtk.Label()
        self.label0.set_text(" ")
        self.vbox1.append(self.label0)
        self.label1 = Gtk.Label()
        self.label1.set_text("Población (500 a 5000)")
        self.vbox1.append(self.label1)
        self.poblacion = Gtk.SpinButton.new_with_range(500,5000,1)
        self.vbox1.append(self.poblacion)
        self.label2 = Gtk.Label()
        self.label2.set_text("Días (10 a 100)")
        self.vbox1.append(self.label2)
        self.dias = Gtk.SpinButton.new_with_range(  10,100,1)                                
        self.vbox1.append(self.dias)
        self.label3 = Gtk.Label()
        self.label3.set_text("Probabilidad de infectar (1 a 100)")
        self.vbox1.append(self.label3)
        self.tasa_inf = Gtk.SpinButton.new_with_range(1,100,1)
        self.vbox1.append(self.tasa_inf)
        self.label4 = Gtk.Label()
        self.label4.set_text("Probabilidad de recuperacion (1 a 100)")
        self.vbox1.append(self.label4)
        self.tasa_rec = Gtk.SpinButton.new_with_range(1,100,1)
        self.vbox1.append(self.tasa_rec)
        self.label5 = Gtk.Label()
        self.label5.set_text("""!!Esto afecta a la probabilidad de morir, si de 
recuperacion es 60 por defecto la de morir sera 40!!""")
        self.vbox1.append(self.label5)
        self.button_action = Gtk.Button(label="Simular")
        self.button_action.connect('clicked', self.simular)                          
        self.vbox1.append(self.button_action)

    def simular(self, button):
        p,d = self.poblacion.get_text(),self.dias.get_text()
        ti = self.tasa_inf.get_text()
        tr = self.tasa_rec.get_text()
        p = p.replace(",",".")
        d = d.replace(",",".")
        ti = ti.replace(",",".")
        tr = tr.replace(",",".")
        g_s, g_i, g_r, g_m = ejecutar(int(p),int(d),int(ti),int(tr))
        crear_grafica(g_s,g_i,g_r,g_m,int(d))
        dialog = VentanaGrafico(parent=self.get_root())
        dialog.set_visible(True)
    
class ExampleApplication(Adw.Application):

    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('about', self.on_about_action)

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = ExampleWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def on_about_action(self, action, param):
        self.about=Gtk.AboutDialog.new()
        self.about.set_authors(["Samantha Agurto","Matias Gajardo",
                                "Ricardo Macaya"])
        self.about.set_program_name("<<Simulador de Enfermedad>>")
        self.about.set_copyright("Ing. Civil en Bioinformática")
        self.about.set_visible(True)

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)

if __name__ == '__main__':
    import sys
    app = ExampleApplication()
    app.run(sys.argv)